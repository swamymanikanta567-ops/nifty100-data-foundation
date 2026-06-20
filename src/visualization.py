import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Database Connection
conn = sqlite3.connect("db/nifty100.db")

# Data Load
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

# ---------------------------
# TOP 10 ROE COMPANIES
# ---------------------------

top_roe = df.sort_values(
    by="roe_percentage",
    ascending=False
).head(10)

plt.figure(figsize=(10, 5))

plt.bar(
    top_roe["company_name"],
    top_roe["roe_percentage"]
)

plt.title("Top 10 Companies by ROE")
plt.xlabel("Company")
plt.ylabel("ROE Percentage")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "output/top10_roe_chart.png"
)

plt.show()

# ---------------------------
# TOP 10 ROCE COMPANIES
# ---------------------------
print(df.columns.tolist())
top_roce = df.sort_values(
    by="roce_percentage",
    ascending=False
).head(10)

plt.figure(figsize=(10, 5))

plt.bar(
    top_roce["company_name"],
    top_roce["roce_percentage"]
)

plt.title("Top 10 Companies by ROCE")
plt.xlabel("Company")
plt.ylabel("ROCE Percentage")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "output/top10_roce_chart.png"
)

plt.show()

conn.close()

print("Charts Generated Successfully")