import json
import logging
from .finnhub_common import get_client, _make_api_request

logger = logging.getLogger(__name__)

def get_fundamentals(ticker: str, curr_date: str = None) -> str:
    """
    Retrieve company basic financials (metrics) from Finnhub.
    """
    logger.info(f"Fetching basic financials for {ticker}")
    client = get_client()
    response = _make_api_request(client.company_basic_financials, ticker, 'all')
    return json.dumps(response, indent=2)

def get_balance_sheet(ticker: str, freq: str = "quarterly", curr_date: str = None) -> str:
    """
    Retrieve balance sheet data.
    """
    logger.info(f"Fetching balance sheet for {ticker} (freq: {freq})")
    client = get_client()
    # Finnhub 'financials_reported' returns raw SEC filings data which includes BS, CF, IS
    # Or 'financials' endpoint for standardized data.
    # We'll use 'financials_reported' for detailed data or 'financials' for standardized.
    # Let's use 'financials' (standardized) as it's easier to parse usually.
    # freq: 'annual' or 'quarterly'
    
    response = _make_api_request(client.financials_reported, symbol=ticker, freq=freq)
    
    # Filter for balance sheet if possible, but this endpoint returns full report
    # We can just return the full JSON or try to extract BS.
    # For simplicity and richness, return the JSON.
    return json.dumps(response, indent=2)

def get_cashflow(ticker: str, freq: str = "quarterly", curr_date: str = None) -> str:
    """
    Retrieve cash flow data.
    """
    # Same endpoint as balance sheet for reported financials
    return get_balance_sheet(ticker, freq, curr_date)

def get_income_statement(ticker: str, freq: str = "quarterly", curr_date: str = None) -> str:
    """
    Retrieve income statement data.
    """
    # Same endpoint as balance sheet for reported financials
    return get_balance_sheet(ticker, freq, curr_date)
