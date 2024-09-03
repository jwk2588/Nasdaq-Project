import nasdaqdatalink
from config import API_KEY

# Set the API key
nasdaqdatalink.ApiConfig.api_key = API_KEY

try:
    # Attempt to fetch a simple, publicly accessible dataset to test your API key
    data = nasdaqdatalink.get("WIKI/AAPL", rows=1)  # Fetch one row of Apple stock data as a test
    print("API Key is working correctly. Data fetched successfully:")
    print(data)
except nasdaqdatalink.errors.DataLinkError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
