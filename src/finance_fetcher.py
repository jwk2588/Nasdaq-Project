# finance_fetcher.py

import yfinance as yf

# Define the ticker symbol for General Motors
ticker_symbol = "GM"

# Fetch the ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch the last 5 years of financial statements (income statement, balance sheet, and cash flow)
income_statement = ticker.financials  # Annual income statement
balance_sheet = ticker.balance_sheet  # Annual balance sheet
cash_flow = ticker.cashflow  # Annual cash flow statement

# Display the fetched data
print("Income Statement:")
print(income_statement)

print("\nBalance Sheet:")
print(balance_sheet)

print("\nCash Flow Statement:")
print(cash_flow)
