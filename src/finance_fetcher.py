# finance_fetcher.py

import yfinance as yf

# Define the ticker symbol for General Motors
ticker_symbol = "GM"


# Fetch the ticker object from Yahoo Finance using yfinance
ticker = yf.Ticker(ticker_symbol)

# Fetch the last 5 years of financial statements (income statement, balance sheet, and cash flow)

# The income statement provides details of the company's revenue, expenses, and profit over a period of time.
income_statement = ticker.financials  # Annual income statement
# The balance sheet provides a snapshot of the company's financial position, showing its assets, liabilities, and shareholders' equity.
balance_sheet = ticker.balance_sheet  # Annual balance sheet
# The cash flow statement tracks the cash inflows and outflows, highlighting how the company generates and spends cash.
cash_flow = ticker.cashflow  # Annual cash flow statement

# Display the fetched data
print("Income Statement:")
print(income_statement)

print("\nBalance Sheet:")
print(balance_sheet)

print("\nCash Flow Statement:")
print(cash_flow)
