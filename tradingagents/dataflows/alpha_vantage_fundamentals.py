from .alpha_vantage_common import _make_api_request
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def get_fundamentals(ticker: str, curr_date: str = None) -> str:
  """
  Retrieve comprehensive fundamental data for a given ticker symbol using Alpha Vantage.

  Args:
      ticker (str): Ticker symbol of the company
      curr_date (str): Current date you are trading at, yyyy-mm-dd (not used for Alpha Vantage)

  Returns:
      str: Company overview data including financial ratios and key metrics
  """
  try:
    logger.info(f"📊 [Alpha Vantage] 获取基本面数据: {ticker}")

    # 构建请求参数
    params = {
        "symbol": ticker.upper(),
    }

    # 发起 API 请求
    data = _make_api_request("OVERVIEW", params)

    # 格式化响应
    if isinstance(data, dict) and data:
      # 提取关键指标
      result = f"# Company Overview: {ticker.upper()}\n"
      result += f"# Retrieved on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

      # 基本信息
      result += "## Basic Information\n"
      result += f"**Name**: {data.get('Name', 'N/A')}\n"
      result += f"**Symbol**: {data.get('Symbol', 'N/A')}\n"
      result += f"**Exchange**: {data.get('Exchange', 'N/A')}\n"
      result += f"**Currency**: {data.get('Currency', 'N/A')}\n"
      result += f"**Country**: {data.get('Country', 'N/A')}\n"
      result += f"**Sector**: {data.get('Sector', 'N/A')}\n"
      result += f"**Industry**: {data.get('Industry', 'N/A')}\n\n"

      # 公司描述
      description = data.get('Description', 'N/A')
      if len(description) > 500:
        description = description[:500] + "..."
      result += f"**Description**: {description}\n\n"

      # 估值指标
      result += "## Valuation Metrics\n"
      result += f"**Market Cap**: ${data.get('MarketCapitalization', 'N/A')}\n"
      result += f"**PE Ratio**: {data.get('PERatio', 'N/A')}\n"
      result += f"**PEG Ratio**: {data.get('PEGRatio', 'N/A')}\n"
      result += f"**Price to Book**: {data.get('PriceToBookRatio', 'N/A')}\n"
      result += f"**Price to Sales**: {data.get('PriceToSalesRatioTTM', 'N/A')}\n"
      result += f"**EV to Revenue**: {data.get('EVToRevenue', 'N/A')}\n"
      result += f"**EV to EBITDA**: {data.get('EVToEBITDA', 'N/A')}\n\n"

      # 财务指标
      result += "## Financial Metrics\n"
      result += f"**Revenue TTM**: ${data.get('RevenueTTM', 'N/A')}\n"
      result += f"**Gross Profit TTM**: ${data.get('GrossProfitTTM', 'N/A')}\n"
      result += f"**EBITDA**: ${data.get('EBITDA', 'N/A')}\n"
      result += f"**Net Income TTM**: ${data.get('NetIncomeTTM', 'N/A')}\n"
      result += f"**EPS**: ${data.get('EPS', 'N/A')}\n"
      result += f"**Diluted EPS TTM**: ${data.get('DilutedEPSTTM', 'N/A')}\n\n"

      # 盈利能力
      result += "## Profitability\n"
      result += f"**Profit Margin**: {data.get('ProfitMargin', 'N/A')}\n"
      result += f"**Operating Margin TTM**: {data.get('OperatingMarginTTM', 'N/A')}\n"
      result += f"**Return on Assets TTM**: {data.get('ReturnOnAssetsTTM', 'N/A')}\n"
      result += f"**Return on Equity TTM**: {data.get('ReturnOnEquityTTM', 'N/A')}\n\n"

      # 股息信息
      result += "## Dividend Information\n"
      result += f"**Dividend Per Share**: ${data.get('DividendPerShare', 'N/A')}\n"
      result += f"**Dividend Yield**: {data.get('DividendYield', 'N/A')}\n"
      result += f"**Dividend Date**: {data.get('DividendDate', 'N/A')}\n"
      result += f"**Ex-Dividend Date**: {data.get('ExDividendDate', 'N/A')}\n\n"

      # 股票信息
      result += "## Stock Information\n"
      result += f"**52 Week High**: ${data.get('52WeekHigh', 'N/A')}\n"
      result += f"**52 Week Low**: ${data.get('52WeekLow', 'N/A')}\n"
      result += f"**50 Day MA**: ${data.get('50DayMovingAverage', 'N/A')}\n"
      result += f"**200 Day MA**: ${data.get('200DayMovingAverage', 'N/A')}\n"
      result += f"**Shares Outstanding**: {data.get('SharesOutstanding', 'N/A')}\n"
      result += f"**Beta**: {data.get('Beta', 'N/A')}\n\n"

      # 财务健康
      result += "## Financial Health\n"
      result += f"**Book Value**: ${data.get('BookValue', 'N/A')}\n"
      result += f"**Debt to Equity**: {data.get('DebtToEquity', 'N/A')}\n"
      result += f"**Current Ratio**: {data.get('CurrentRatio', 'N/A')}\n"
      result += f"**Quick Ratio**: {data.get('QuickRatio', 'N/A')}\n\n"

      # 分析师目标价
      result += "## Analyst Targets\n"
      result += f"**Analyst Target Price**: ${data.get('AnalystTargetPrice', 'N/A')}\n"
      result += f"**Analyst Rating Strong Buy**: {data.get('AnalystRatingStrongBuy', 'N/A')}\n"
      result += f"**Analyst Rating Buy**: {data.get('AnalystRatingBuy', 'N/A')}\n"
      result += f"**Analyst Rating Hold**: {data.get('AnalystRatingHold', 'N/A')}\n"
      result += f"**Analyst Rating Sell**: {data.get('AnalystRatingSell', 'N/A')}\n"
      result += f"**Analyst Rating Strong Sell**: {data.get('AnalystRatingStrongSell', 'N/A')}\n\n"

      logger.info(f"✅ [Alpha Vantage] 成功获取基本面数据: {ticker}")
      return result
    else:
      return data

  except Exception as e:
    logger.error(f"❌ [Alpha Vantage] 获取基本面数据失败 {ticker}: {e}")
    return f"Error retrieving fundamentals for {ticker}: {str(e)}"


def get_balance_sheet(ticker: str, freq: str = "quarterly",
    curr_date: str = None) -> str:
  """
  Retrieve balance sheet data for a given ticker symbol using Alpha Vantage.

  Args:
      ticker (str): Ticker symbol of the company
      freq (str): Reporting frequency: annual/quarterly (default quarterly) - not used for Alpha Vantage
      curr_date (str): Current date you are trading at, yyyy-mm-dd (not used for Alpha Vantage)

  Returns:
      str: Balance sheet data with normalized fields
  """
  params = {
      "symbol": ticker,
  }

  return _make_api_request("BALANCE_SHEET", params)


def get_cashflow(ticker: str, freq: str = "quarterly",
    curr_date: str = None) -> str:
  """
  Retrieve cash flow statement data for a given ticker symbol using Alpha Vantage.

  Args:
      ticker (str): Ticker symbol of the company
      freq (str): Reporting frequency: annual/quarterly (default quarterly) - not used for Alpha Vantage
      curr_date (str): Current date you are trading at, yyyy-mm-dd (not used for Alpha Vantage)

  Returns:
      str: Cash flow statement data with normalized fields
  """
  params = {
      "symbol": ticker,
  }

  return _make_api_request("CASH_FLOW", params)


def get_income_statement(ticker: str, freq: str = "quarterly",
    curr_date: str = None) -> str:
  """
  Retrieve income statement data for a given ticker symbol using Alpha Vantage.

  Args:
      ticker (str): Ticker symbol of the company
      freq (str): Reporting frequency: annual/quarterly (default quarterly) - not used for Alpha Vantage
      curr_date (str): Current date you are trading at, yyyy-mm-dd (not used for Alpha Vantage)

  Returns:
      str: Income statement data with normalized fields
  """
  params = {
      "symbol": ticker,
  }

  return _make_api_request("INCOME_STATEMENT", params)
