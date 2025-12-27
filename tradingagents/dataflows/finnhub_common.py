import os
import time
import finnhub
import logging
from .config import get_config

logger = logging.getLogger(__name__)

class FinnhubRateLimitError(Exception):
    """Exception raised when Finnhub API rate limit is exceeded."""
    pass

def get_api_key():
    """Retrieve Finnhub API key from config or environment."""
    config = get_config()
    # Check config first
    api_key = config.get("api_keys", {}).get("finnhub")
    if not api_key:
        # Fallback to environment variable
        api_key = os.environ.get("FINNHUB_API_KEY")
    
    if not api_key:
        raise ValueError("Finnhub API key not found in config or environment variables.")
    return api_key

def get_client():
    """Initialize and return a Finnhub client."""
    api_key = get_api_key()
    return finnhub.Client(api_key=api_key)

def _make_api_request(func, *args, **kwargs):
    """
    Wrapper for Finnhub API requests with error handling and rate limit management.
    """
    try:
        # logger.debug(f"Making Finnhub API request: {func.__name__}") # Optional: verbose logging
        return func(*args, **kwargs)
    except finnhub.FinnhubAPIException as e:
        if "API limit reached" in str(e):
            logger.warning(f"Finnhub rate limit exceeded: {e}")
            raise FinnhubRateLimitError(f"Finnhub rate limit exceeded: {e}")
        logger.error(f"Finnhub API exception: {e}")
        raise e
    except Exception as e:
        logger.error(f"Finnhub API request failed: {e}")
        raise RuntimeError(f"Finnhub API request failed: {e}")
