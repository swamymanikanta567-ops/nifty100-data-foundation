import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
    company_name,
    book_value,
    roe_percentage,
    roce_percentage
FROM companies
ORDER BY roe_percentage DESC
LIMIT 10
"""

df = pd.read_sql(query, conn)

print(df)

df.to_csv(
    "output/top10_roe_companies.csv",
    index=False
)

print("KPI Report Saved")

conn.close()