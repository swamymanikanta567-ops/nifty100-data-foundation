import pandas as pd

df = pd.read_excel("data/raw/companies.xlsx", header=1)

df.to_csv(
    "data/processed/companies_clean.csv",
    index=False
)

print("Companies CSV Saved")