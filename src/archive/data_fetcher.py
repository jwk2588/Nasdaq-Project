# data_fetcher.py

import pandas as pd
import nasdaqdatalink
from config import API_KEY

# Set the API key
nasdaqdatalink.ApiConfig.api_key = API_KEY

def fetch_data(ticker, data_type):
    """
    Fetches data from Nasdaq Data Link API.

    Args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL').
        data_type (str): The financial data type (e.g., 'IS_MRY' for income statement).

    Returns:
        pd.DataFrame or None: The fetched data as a pandas DataFrame, or None if an error occurs.
    """
    try:
        # Attempt to fetch data from the API
        data = nasdaqdatalink.get(f"SF1/{ticker}_{data_type}")
        print(f"Data for {ticker} {data_type} fetched successfully.")
        return data
    except nasdaqdatalink.errors.DataLinkError as api_error:
        # Handles specific API errors, such as missing data or invalid API key
        print(f"API Error: Unable to fetch data for {ticker} - {api_error}")
    except Exception as e:
        # Handles any other exceptions that may occur
        print(f"Unexpected error fetching data for {ticker}: {e}")
    return None

def save_to_excel(data, file_name, sheet_name):
    """
    Saves the DataFrame to an Excel file using ExcelWriter.

    Args:
        data (pd.DataFrame): The data to be saved.
        file_name (str): The name of the Excel file (e.g., 'financial_data.xlsx').
        sheet_name (str): The name of the sheet in Excel.

    Returns:
        bool: True if the data was saved successfully, False otherwise.
    """
    try:
        # Attempt to save the data to an Excel file
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            data.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"Data successfully saved to '{file_name}' in sheet '{sheet_name}'.")
        return True
    except PermissionError:
        # Handles file permission errors, such as trying to write to a file that is open
        print(f"Permission Error: Unable to save the file '{file_name}'. Please close it if it's open and try again.")
    except FileNotFoundError:
        # Handles cases where the path to save the file is invalid
        print(f"File Not Found Error: The path specified for '{file_name}' does not exist.")
    except Exception as e:
        # Handles any other exceptions that may occur
        print(f"Unexpected error saving to Excel: {e}")
    return False

# Example usage
if __name__ == "__main__":
    ticker = 'AAPL'  # Example ticker
    data_type = 'IS_MRY'  # Example data type
    data = fetch_data(ticker, data_type)
    
    # Check if data was fetched successfully
    if data is not None:
        # Attempt to save the fetched data to an Excel file
        save_path = f'data/{ticker}_{data_type}.xlsx'
        saved = save_to_excel(data, save_path, 'Income Statement')
        
        if not saved:
            print("Failed to save the data.")
    else:
        print("No data fetched. Please check the ticker symbol and data type.")
