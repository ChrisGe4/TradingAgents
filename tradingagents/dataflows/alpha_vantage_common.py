import os
import requests
import pandas as pd
import json
from datetime import datetime
from io import StringIO
from typing import Dict, Any, Optional

API_BASE_URL = "https://www.alphavantage.co/query"


def get_api_key() -> str:
  """Retrieve the API key for Alpha Vantage from environment variables."""
  api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
  if not api_key:
    raise ValueError("ALPHA_VANTAGE_API_KEY environment variable is not set.")
  return api_key


def format_datetime_for_api(date_input) -> str:
  """Convert various date formats to YYYYMMDDTHHMM format required by Alpha Vantage API."""
  if isinstance(date_input, str):
    # If already in correct format, return as-is
    if len(date_input) == 13 and 'T' in date_input:
      return date_input
    # Try to parse common date formats
    try:
      dt = datetime.strptime(date_input, "%Y-%m-%d")
      return dt.strftime("%Y%m%dT0000")
    except ValueError:
      try:
        dt = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
        return dt.strftime("%Y%m%dT%H%M")
      except ValueError:
        raise ValueError(f"Unsupported date format: {date_input}")
  elif isinstance(date_input, datetime):
    return date_input.strftime("%Y%m%dT%H%M")
  else:
    raise ValueError(
        f"Date must be string or datetime object, got {type(date_input)}")


class AlphaVantageRateLimitError(Exception):
  """Exception raised when Alpha Vantage API rate limit is exceeded."""
  pass


def _make_api_request(
    function: str,
    params: Dict[str, Any],
    max_retries: int = 3,
    retry_delay: int = 2
) -> Dict[str, Any] | str:
  """
  发起 Alpha Vantage API 请求

  Args:
      function: API 函数名（如 NEWS_SENTIMENT, OVERVIEW 等）
      params: 请求参数字典
      max_retries: 最大重试次数
      retry_delay: 重试延迟（秒）

  Returns:
      API 响应的 JSON 数据或错误信息字符串

  Raises:
      AlphaVantageRateLimitError: 速率限制错误
      AlphaVantageAPIError: API 错误
  """
  # Create a copy of params to avoid modifying the original
  api_params = params.copy()
  api_params.update({
      "function": function_name,
      "apikey": get_api_key(),
      "source": "trading_agents",
  })

  # Handle entitlement parameter if present in params or global variable
  current_entitlement = globals().get('_current_entitlement')
  entitlement = api_params.get("entitlement") or current_entitlement

  if entitlement:
    api_params["entitlement"] = entitlement
  elif "entitlement" in api_params:
    # Remove entitlement if it's None or empty
    api_params.pop("entitlement", None)

  logger.debug(f"📡 [Alpha Vantage] 请求 {function}: {params}")

  for attempt in range(max_retries):
    try:
      # 发起请求
      response = requests.get(API_BASE_URL, params=api_params, timeout=30)
      response.raise_for_status()

      # 解析响应
      data = response.json()

      # 检查错误信息
      if "Error Message" in data:
        error_msg = data["Error Message"]
        logger.error(f"❌ [Alpha Vantage] API 错误: {error_msg}")
        raise AlphaVantageAPIError(f"Alpha Vantage API Error: {error_msg}")

      # 检查速率限制
      if "Note" in data and "API call frequency" in data["Note"]:
        logger.warning(f"⚠️ [Alpha Vantage] 速率限制: {data['Note']}")

        if attempt < max_retries - 1:
          wait_time = retry_delay * (attempt + 1)
          logger.info(f"⏳ 等待 {wait_time} 秒后重试...")
          time.sleep(wait_time)
          continue
        else:
          raise AlphaVantageRateLimitError(
              "Alpha Vantage API rate limit exceeded. "
              "Please wait a moment and try again, or upgrade your API plan."
          )

      # 检查信息字段（可能包含限制提示）
      if "Information" in data:
        info_msg = data["Information"]
        logger.warning(f"⚠️ [Alpha Vantage] 信息: {info_msg}")

        # 如果是速率限制信息
        if "premium" in info_msg.lower() or "limit" in info_msg.lower():
          if attempt < max_retries - 1:
            wait_time = retry_delay * (attempt + 1)
            logger.info(f"⏳ 等待 {wait_time} 秒后重试...")
            time.sleep(wait_time)
            continue
          else:
            raise AlphaVantageRateLimitError(
                f"Alpha Vantage API limit: {info_msg}"
            )

      # 成功获取数据
      logger.debug(f"✅ [Alpha Vantage] 请求成功: {function}")
      return data

    except requests.exceptions.Timeout:
      logger.warning(
          f"⚠️ [Alpha Vantage] 请求超时 (尝试 {attempt + 1}/{max_retries})")
      if attempt < max_retries - 1:
        time.sleep(retry_delay)
        continue
      else:
        raise AlphaVantageAPIError("Alpha Vantage API request timeout")

    except requests.exceptions.RequestException as e:
      logger.error(f"❌ [Alpha Vantage] 请求失败: {e}")
      if attempt < max_retries - 1:
        time.sleep(retry_delay)
        continue
      else:
        raise AlphaVantageAPIError(f"Alpha Vantage API request failed: {e}")

    except json.JSONDecodeError as e:
      # logger.error(f"❌ [Alpha Vantage] JSON 解析失败: {e}")
      # raise AlphaVantageAPIError(f"Failed to parse Alpha Vantage API response: {e}")

      # Response is not JSON (likely CSV data), which is normal
      return response.text

  # 所有重试都失败
  raise AlphaVantageAPIError(
      f"Failed to get data from Alpha Vantage after {max_retries} attempts")


def _filter_csv_by_date_range(csv_data: str, start_date: str,
    end_date: str) -> str:
  """
  Filter CSV data to include only rows within the specified date range.

  Args:
      csv_data: CSV string from Alpha Vantage API
      start_date: Start date in yyyy-mm-dd format
      end_date: End date in yyyy-mm-dd format

  Returns:
      Filtered CSV string
  """
  if not csv_data or csv_data.strip() == "":
    return csv_data

  try:
    # Parse CSV data
    df = pd.read_csv(StringIO(csv_data))

    # Assume the first column is the date column (timestamp)
    date_col = df.columns[0]
    df[date_col] = pd.to_datetime(df[date_col])

    # Filter by date range
    start_dt = pd.to_datetime(start_date)
    end_dt = pd.to_datetime(end_date)

    filtered_df = df[(df[date_col] >= start_dt) & (df[date_col] <= end_dt)]

    # Convert back to CSV string
    return filtered_df.to_csv(index=False)

  except Exception as e:
    # If filtering fails, return original data with a warning
    print(f"Warning: Failed to filter CSV data by date range: {e}")
    return csv_data
