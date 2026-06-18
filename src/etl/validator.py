import pandas as pd

def check_pk_uniqueness(df):
    return df.duplicated().sum()

def check_company_year_pk(df):
    if "company_id" in df.columns and "year" in df.columns:
        return df.duplicated(subset=["company_id", "year"]).sum()
    return 0

print("Validator Ready")

df = pd.read_csv("data/sample_data.csv")

print("Duplicate Rows:", check_pk_uniqueness(df))
print("Company-Year Duplicates:", check_company_year_pk(df))
def check_fk_integrity(child_df, parent_df, fk_column):
    invalid_rows = child_df[
        ~child_df[fk_column].isin(parent_df[fk_column])
    ]
    return len(invalid_rows)

def check_positive_sales(df):
    invalid_rows = df[df["sales"] <= 0]
    return len(invalid_rows)

companies_df = pd.read_csv("data/companies.csv")

fk_errors = check_fk_integrity(
    df,
    companies_df,
    "company_id"
)

print("Foreign Key Errors:", fk_errors)

sales_errors = check_positive_sales(df)

print("Positive Sales Errors:", sales_errors)

import pandas as pd

results = {
    "Rule": [
        "DQ-01 PK Uniqueness",
        "DQ-02 Company-Year PK",
        "DQ-03 FK Integrity",
        "DQ-06 Positive Sales"
    ],
    "Errors": [
        check_pk_uniqueness(df),
        check_company_year_pk(df),
        fk_errors,
        check_positive_sales(df)
    ]
}

report_df = pd.DataFrame(results)

report_df.to_csv(
    "output/validation_failures.csv",
    index=False
)

print("Validation Report Saved")
