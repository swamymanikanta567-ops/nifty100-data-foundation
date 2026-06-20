import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql(
    """
    SELECT
        company_name,
        book_value,
        roe_percentage,
        roce_percentage
    FROM companies
    """,
    conn
)

print(df.head())

print("\nSummary Statistics:\n")
print(df.describe())

conn.close()

print("\nHighest ROE Company:\n")

top_roe = df.sort_values(
    by="roe_percentage",
    ascending=False
)

print(
    top_roe[
        ["company_name", "roe_percentage"]
    ].head(10)
)

top_roe.to_csv(
    "output/top10_roe_eda.csv",
    index=False
)

print("EDA Report Saved")