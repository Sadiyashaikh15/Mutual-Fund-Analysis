import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("=" * 60)
print("SCHEME PERFORMANCE CLEANING")
print("=" * 60)

# -------------------------
# Check duplicates
# -------------------------
duplicates = df.duplicated().sum()
print(f"Duplicate Rows: {duplicates}")

# -------------------------
# Validate expense ratio
# -------------------------
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print(f"Invalid Expense Ratio Records: {len(invalid_expense)}")

# -------------------------
# Check numeric columns
# -------------------------
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

print("\nNumeric Column Validation")

for col in numeric_cols:
    print(f"{col}: {pd.api.types.is_numeric_dtype(df[col])}")

# -------------------------
# Missing values
# -------------------------
print("\nMissing Values")
print(df.isnull().sum())

# -------------------------
# Save cleaned dataset
# -------------------------
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("\n✅ Scheme Performance cleaned successfully!")