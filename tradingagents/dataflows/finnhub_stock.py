import pandas as pd
from datetime import datetime
import logging
from .finnhub_common import get_client, _make_api_request

logger = logging.getLogger(__name__)

def get_stock(
    symbol: str,
    start_date: str,
    end_date: str
) -> str:
    """
    Returns raw daily OHLCV values filtered to the specified date range.

    Args:
        symbol: The ticker symbol.
        start_date: Start date in yyyy-mm-dd format.
        end_date: End date in yyyy-mm-dd format.

    Returns:
        CSV string containing the daily time series data.
    """
    client = get_client()
    
    # Convert dates to unix timestamp
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")
    
    start_ts = int(start_dt.timestamp())
    end_ts = int(end_dt.timestamp())
    
    logger.info(f"Fetching stock data for {symbol} from {start_date} to {end_date}")
    
    # Finnhub stock_candles resolution 'D' for daily
    response = _make_api_request(client.stock_candles, symbol, 'D', start_ts, end_ts)
    
    if response['s'] == 'no_data':
        logger.warning(f"No data returned for {symbol} in range {start_date} to {end_date}")
        return ""
        
    # Convert to DataFrame
    data = {
        'date': [datetime.fromtimestamp(t).strftime('%Y-%m-%d') for t in response['t']],
        'open': response['o'],
        'high': response['h'],
        'low': response['l'],
        'close': response['c'],
        'volume': response['v']
    }
    
    df = pd.DataFrame(data)
    
    # Filter by date range (API might return slightly more)
    df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    
    logger.info(f"Retrieved {len(df)} rows of stock data for {symbol}")
    return df.to_csv(index=False)
