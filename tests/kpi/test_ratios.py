from src.analytics.ratios import *

print("Net Profit Margin:", net_profit_margin(100, 500))
print("Operating Profit Margin:", operating_profit_margin(150, 500))
print("ROE:", return_on_equity(120, 300, 200))
print("ROA:", return_on_assets(100, 1000))
print("ROCE:", return_on_capital_employed(150, 300, 200, 100))

# Edge cases
print(net_profit_margin(100, 0))
print(return_on_equity(100, -50, 20))
print(return_on_assets(100, 0))

print("Debt to Equity:", debt_to_equity(200, 300, 200))
print("Interest Coverage:", interest_coverage(150, 50, 20))
print("Net Debt:", net_debt(500, 150))
print("Asset Turnover:", asset_turnover(1000, 500))