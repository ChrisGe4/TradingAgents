import sys
import os
import logging

# Add project root to path
sys.path.append(os.getcwd())

from tradingagents.dataflows.googlenews_utils import getNewsData

# Configure logging
logging.basicConfig(level=logging.INFO)


def test_get_news_data():
  query = "Google AI"
  start_date = "2023-01-01"
  end_date = "2023-01-31"

  print(f"Fetching news for '{query}' from {start_date} to {end_date}...")
  results = getNewsData(query, start_date, end_date)

  print(f"Found {len(results)} results.")

  if results:
    print("First result:")
    print(results[0])

    # Verify fields
    required_fields = ["link", "title", "snippet", "date", "source"]
    for field in required_fields:
      if field not in results[0]:
        print(f"ERROR: Missing field '{field}' in result")
      else:
        print(f"Field '{field}' is present.")
  else:
    print(
      "No results found. This might be expected if the query/date is too old or specific, or it might indicate an issue.")


if __name__ == "__main__":
  test_get_news_data()
