import pandas as pd
from datetime import datetime
import logging
from .finnhub_common import get_client, _make_api_request

logger = logging.getLogger(__name__)

from dateutil.relativedelta import relativedelta

def get_indicator(
    symbol: str,
    indicator: str,
    curr_date: str,
    look_back_days: int,
    interval: str = "daily",
    time_period: int = 14,
    series_type: str = "close"
) -> str:
    """
    Retrieve technical indicator data from Finnhub.
    Matches Alpha Vantage signature and supports specific indicator keys.
    """
    client = get_client()
    
    # Calculate start and end dates based on look_back_days
    end_dt = datetime.strptime(curr_date, "%Y-%m-%d")
    start_dt = end_dt - relativedelta(days=look_back_days)
    
    start_ts = int(start_dt.timestamp())
    end_ts = int(end_dt.timestamp())
    
    # Supported indicators mapping
    # Key: (Finnhub indicator name, default params)
    supported_indicators = {
        "close_50_sma": ("sma", {"timeperiod": 50, "seriestype": "close"}),
        "close_200_sma": ("sma", {"timeperiod": 200, "seriestype": "close"}),
        "close_10_ema": ("ema", {"timeperiod": 10, "seriestype": "close"}),
        "macd": ("macd", {"seriestype": "close"}),
        "macds": ("macd", {"seriestype": "close"}), # Signal line usually part of MACD response
        "macdh": ("macd", {"seriestype": "close"}), # Histogram usually part of MACD response
        "rsi": ("rsi", {"timeperiod": 14, "seriestype": "close"}),
        "boll": ("bbands", {"timeperiod": 20, "seriestype": "close"}),
        "boll_ub": ("bbands", {"timeperiod": 20, "seriestype": "close"}),
        "boll_lb": ("bbands", {"timeperiod": 20, "seriestype": "close"}),
        "atr": ("atr", {"timeperiod": 14}),
        # Add more as needed
    }
    
    if indicator not in supported_indicators:
        # Fallback for direct indicator names if they match Finnhub's expected names
        # But for safety/consistency, we might want to restrict or just try it.
        # Let's try to use it directly if not in our map, assuming user knows what they are doing
        # or just fail if strict. Given the request for specificity, let's try to map generic ones too.
        finnhub_indicator = indicator.lower()
        default_params = {}
        if time_period:
            default_params['timeperiod'] = time_period
        if series_type:
            default_params['seriestype'] = series_type
    else:
        finnhub_indicator, default_params = supported_indicators[indicator]
        # Override defaults if specific params are passed and not just defaults?
        # Usually specific keys like 'close_50_sma' imply fixed params.
        # But 'rsi' might allow custom time_period.
        if indicator == 'rsi' and time_period != 14:
             default_params['timeperiod'] = time_period
    
    indicator_fields = default_params.copy()
    
    logger.info(f"Fetching indicator {indicator} (mapped to {finnhub_indicator}) for {symbol}")
    
    response = _make_api_request(
        client.technical_indicator, 
        symbol=symbol, 
        resolution='D', 
        _from=start_ts, 
        to=end_ts, 
        indicator=finnhub_indicator, 
        indicator_fields=indicator_fields
    )
    
    if not response:
        logger.warning(f"No response for indicator {indicator} on {symbol}")
        return ""
        
    if 't' not in response:
        logger.warning(f"Unexpected response format for {indicator}: {response}")
        return str(response)
        
    data = {
        'date': [datetime.fromtimestamp(t).strftime('%Y-%m-%d') for t in response['t']]
    }
    
    # Extract relevant columns based on the requested indicator
    # Finnhub returns keys like 'sma', 'ema', 'macd', 'macdsignal', 'macdhist', 'rsi', etc.
    
    # Mapping for specific output columns if we want to filter/rename
    # e.g. for 'macds', we might only want the signal line?
    # Alpha Vantage implementation returns everything usually or specific column.
    # Let's return all relevant fields for now to be safe, or filter if strictly needed.
    
    for key, value in response.items():
        if key not in ['t', 's'] and isinstance(value, list):
            data[key] = value
            
    df = pd.DataFrame(data)
    
    # Filter by date range
    # Note: Finnhub might return data outside exact range due to indicator warmup, so we filter.
    df = df[(df['date'] >= datetime.strftime(start_dt, "%Y-%m-%d")) & (df['date'] <= curr_date)]
    
    logger.info(f"Retrieved {len(df)} rows of indicator data for {indicator} on {symbol}")
    return df.to_csv(index=False)
