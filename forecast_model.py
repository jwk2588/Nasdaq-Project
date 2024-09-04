import yfinance as yf
import pandas as pd

# Define the ticker symbol for General Motors (GM)
ticker = yf.Ticker("GM")

# Fetch financial data (last 4 years)
income_statement = ticker.financials.T.head(4)  # Transpose and get the last 4 years
balance_sheet = ticker.balance_sheet.T.head(4)
cash_flow = ticker.cashflow.T.head(4)

# Display the fetched data for review
print("Income Statement:\n")
print(income_statement)
print("\nBalance Sheet:\n")
print(balance_sheet)
print("\nCash Flow Statement:\n")
print(cash_flow)

# Forecasting assumptions (adjust these assumptions as per analysis)
revenue_growth_rate = 0.05  # 5% annual growth rate
cogs_percentage_of_revenue = 0.7  # Assume COGS is 70% of Revenue

# Set up historical data points
historical_revenue = income_statement['Total Revenue'].iloc[-1]  # Last year's revenue
forecasted_revenue = historical_revenue * (1 + revenue_growth_rate)

# Create Forecast DataFrame
forecast_years = [2024, 2025, 2026]
forecast_data = {
    "Year": forecast_years,
    "Revenue": [forecasted_revenue * (1 + revenue_growth_rate) ** i for i in range(len(forecast_years))],
    "COGS": [(forecasted_revenue * (1 + revenue_growth_rate) ** i) * cogs_percentage_of_revenue for i in range(len(forecast_years))]
}

# Build Forecast DataFrame
forecast_df = pd.DataFrame(forecast_data)
forecast_df['Gross Profit'] = forecast_df['Revenue'] - forecast_df['COGS']

print("\nForecast Data:\n")
print(forecast_df)
