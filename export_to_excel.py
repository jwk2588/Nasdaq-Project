# Export DataFrames to Excel
from forecast_model import income_statement, balance_sheet, cash_flow, forecast_df
import pandas as pd

# Assuming income_statement, balance_sheet, and cash_flow are your DataFrames
with pd.ExcelWriter('financial_data.xlsx') as writer:
    income_statement.to_excel(writer, sheet_name='Income Statement')
    balance_sheet.to_excel(writer, sheet_name='Balance Sheet')
    cash_flow.to_excel(writer, sheet_name='Cash Flow Statement')
    forecast_df.to_excel(writer, sheet_name='Forecast Data')
