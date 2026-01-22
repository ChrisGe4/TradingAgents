import logging
from datetime import datetime
from gnews import GNews

logger = logging.getLogger("tools.google_news")


def getNewsData(query, start_date, end_date, max_results=100):
  """
  Scrape Google News search results for a given query and date range.
  query: str - search query
  start_date: str - start date in the format yyyy-mm-dd or mm/dd/yyyy
  end_date: str - end date in the format yyyy-mm-dd or mm/dd/yyyy
  """
  # Parse dates to tuple (Year, Month, Day) for GNews
  try:
    if "-" in start_date:
      sd = datetime.strptime(start_date, "%Y-%m-%d")
    else:
      sd = datetime.strptime(start_date, "%m/%d/%Y")
    
    if "-" in end_date:
      ed = datetime.strptime(end_date, "%Y-%m-%d")
    else:
      ed = datetime.strptime(end_date, "%m/%d/%Y")

    start_date_tuple = (sd.year, sd.month, sd.day)
    end_date_tuple = (ed.year, ed.month, ed.day)
  except ValueError as e:
    logger.error(f"Error parsing dates: {e}")
    return []

  google_news = GNews(
      start_date=start_date_tuple, end_date=end_date_tuple,
      max_results=max_results
  )

  try:
    results = google_news.get_news(query)
  except Exception as e:
    logger.error(f"Error fetching news from GNews: {e}")
    return []

  news_results = []
  for item in results:
    # Map GNews result to expected format
    # GNews returns: {'title': ..., 'description': ..., 'published date': ..., 'url': ..., 'publisher': {'href': ..., 'title': ...}}
    # We need: {'link': ..., 'title': ..., 'snippet': ..., 'date': ..., 'source': ...}

    try:
      source = item.get("publisher", {}).get("title", "")
      if not source and "publisher" in item and isinstance(item["publisher"],
                                                           str):
        source = item["publisher"]

      news_results.append({
          "link": item.get("url", ""),
          "title": item.get("title", ""),
          "snippet": item.get("description", ""),
          "date": item.get("published date", ""),
          "source": source,
      })
    except Exception as e:
      logger.error(f"Error processing GNews result item: {e}")
      continue

  return news_results
