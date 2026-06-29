from src.analytics.cagr import cagr

print("Revenue CAGR:", cagr(100, 200, 5))
print("PAT CAGR:", cagr(50, 100, 3))
print("EPS CAGR:", cagr(10, 20, 2))
print("Zero Base:", cagr(0, 100, 5))