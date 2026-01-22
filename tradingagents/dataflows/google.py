from typing import Annotated
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .googlenews_utils import getNewsData
import logging

logger = logging.getLogger("google_news")


def get_google_news(
    query: Annotated[str, "Query to search with"],
    # curr_date: Annotated[str, "Curr date in yyyy-mm-dd format"],
    # look_back_days: Annotated[int, "how many days to look back"] = 7,
    start_date: str,
    end_date: str
) -> str:
  query = query.replace(" ", "+")

  # start_date = datetime.strptime(curr_date, "%Y-%m-%d")
  # before = start_date - relativedelta(days=look_back_days)
  # before = before.strftime("%Y-%m-%d")
  # before = datetime.strptime(start_date, "%Y-%m-%d")
  # curr_date = datetime.strptime(end_date, "%Y-%m-%d")

  print(
      f"[Google新闻] 开始获取新闻，查询: {query}, 时间范围: {start_date} 至 {end_date}")

  news_results = getNewsData(query, start_date, end_date)

  news_str = ""

  for news in news_results:
    news_str += (
        f"### {news['title']} (source: {news['source']}) \n\n{news['snippet']}\n\n"
    )

  if len(news_results) == 0:
    logger.warning(f"[Google新闻] 未找到相关新闻，查询: {query}")
    return ""

  print(f"[Google新闻] 成功获取 {len(news_results)} 条新闻，查询: {query}")
  return f"## {query.replace('+', ' ')} Google News, from {start_date} to {end_date}:\n\n{news_str}"


def get_global_news(
    curr_date: Annotated[str, "Curr date in yyyy-mm-dd format"],
    look_back_days: Annotated[int, "how many days to look back"] = 7,
    limit: Annotated[int, "how many articles to return"] = 10,
) -> str:
  query = "global macroeconomics"
  start_date = datetime.strptime(curr_date, "%Y-%m-%d")
  before = start_date - relativedelta(days=look_back_days)
  before = before.strftime("%Y-%m-%d")
  print(
      f"[Google新闻] 开始获取新闻，查询: {query}, 时间范围: {before} 至 {curr_date}")

  news_results = getNewsData(query, before, curr_date, max_results=limit)

  news_str = ""

  for news in news_results:
    news_str += (
        f"### {news['title']} (source: {news['source']}) \n\n{news['snippet']}\n\n"
    )

  if len(news_results) == 0:
    logger.warning(f"[Google新闻] 未找到相关新闻，查询: {query}")
    return ""

  print(f"[Google新闻] 成功获取 {len(news_results)} 条新闻，查询: {query}")
  return f"## {query.replace('+', ' ')} Google News, from {before} to {curr_date}:\n\n{news_str}"
