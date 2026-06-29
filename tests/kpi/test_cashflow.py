from src.analytics.cashflow_kpis import *

fcf = free_cash_flow(500, -150)

print("Free Cash Flow:", fcf)
print("CapEx Intensity:", capex_intensity(-150, 1000))
print("FCF Conversion:", fcf_conversion(fcf, 400))