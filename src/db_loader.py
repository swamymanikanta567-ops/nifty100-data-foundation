import pandas as pd
import sqlite3

# Read cleaned companies dataset
df = pd.read_csv("data/processed/companies_clean.csv")

# Create SQLite database
conn = sqlite3.connect("db/nifty100.db")

# Load data into database table
df.to_sql(
    "companies",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database Created Successfully")