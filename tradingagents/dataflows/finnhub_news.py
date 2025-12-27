from datetime import datetime
import json
import logging
from .finnhub_common import get_client, _make_api_request

logger = logging.getLogger(__name__)

def get_news(
    ticker: str,
    start_date: str,
    end_date: str
) -> str:
    """
    Retrieve company news.
    """
    logger.info(f"Fetching news for {ticker} from {start_date} to {end_date}")
    client = get_client()
    start_date_ts = datetime.strptime(start_date, "%Y-%m-%d").timestamp()
    end_date_ts = datetime.strptime(end_date, "%Y-%m-%d").timestamp()
    response = _make_api_request(client.company_news, ticker, _from=start_date_ts, to=end_date_ts)
    
    # Format as string
    if not response:
        logger.info(f"No news found for {ticker}")
        return ""
        
    logger.info(f"Found {len(response)} news items for {ticker}")
    result_str = ""
    for item in response:
        date_str = datetime.fromtimestamp(item['datetime']).strftime('%Y-%m-%d')
        result_str += f"### {item['headline']} ({date_str})\n{item['summary']}\nSource: {item['source']}\nURL: {item['url']}\n\n"
        
    return f"## {ticker} News from {start_date} to {end_date}:\n\n{result_str}"

def get_insider_sentiment(
    ticker: str,
    curr_date: str = None
) -> str:
    """
    Retrieve insider sentiment.
    """
    logger.info(f"Fetching insider sentiment for {ticker}")
    client = get_client()
    # Finnhub stock_insider_sentiment requires 'from' and 'to' dates.
    # We'll default to last 3 months if curr_date is provided, or just generic range.
    # If curr_date is provided, we look back.
    
    if curr_date:
        end_date = curr_date
        # Look back 90 days
        end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
        # approximate 3 months
        # ... actually let's just use a fixed range or rely on default if API allows (it requires dates)
        start_date = "2020-01-01" # Default fallback? 
        # Better:
        from dateutil.relativedelta import relativedelta
        start_dt = end_dt - relativedelta(months=3)
        start_date = start_dt.strftime("%Y-%m-%d")
    else:
        start_date = "2024-01-01"
        end_date = datetime.now().strftime("%Y-%m-%d")
        
    response = _make_api_request(client.stock_insider_sentiment, ticker, _from=start_date, to=end_date)
    return json.dumps(response, indent=2)

def get_insider_transactions(
    symbol: str,
    curr_date: str = None
) -> str:
    """
    Retrieve insider transactions.
    """
    logger.info(f"Fetching insider transactions for {symbol}")
    client = get_client()
    # Finnhub stock_insider_transactions
    # This endpoint doesn't take date range in python client usually, it just returns recent transactions?
    # Let's check docs or assume standard call.
    # The library docs say: stock_insider_transactions(symbol, _from=None, to=None)
    
    kwargs = {'symbol': symbol}
    if curr_date:
        kwargs['to'] = curr_date
        # Look back 3 months
        end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
        from dateutil.relativedelta import relativedelta
        start_dt = end_dt - relativedelta(months=3)
        kwargs['_from'] = start_dt.strftime("%Y-%m-%d")
        
    response = _make_api_request(client.stock_insider_transactions, **kwargs)
    
    # Format nicely
    if not response or 'data' not in response:
        logger.info(f"No insider transactions found for {symbol}")
        return ""
        
    logger.info(f"Found {len(response['data'])} insider transactions for {symbol}")
    result_str = ""
    for item in response['data']:
        result_str += f"### {item['name']} ({item['transactionDate']})\n"
        result_str += f"Type: {item['transactionCode']}\n"
        result_str += f"Shares: {item['share']}\n"
        result_str += f"Price: {item['transactionPrice']}\n"
        result_str += f"Change: {item['change']}\n\n"
        
    return f"## {symbol} Insider Transactions:\n\n{result_str}"
