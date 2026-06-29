import sqlite3

conn = sqlite3.connect("nifty100.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS financial_ratios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    year INTEGER,
    net_profit_margin REAL,
    roe REAL,
    roa REAL,
    roce REAL,
    debt_to_equity REAL
)
""")

conn.commit()
conn.close()

print("financial_ratios table created successfully.")