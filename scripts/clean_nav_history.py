import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 50)
print("Original Dataset")
print("=" * 50)

print(df.head())
print(df.info())

# -----------------------------
# Convert date column
# -----------------------------
df["date"] = pd.to_datetime(
    df["date"],
    format="%d-%m-%Y"
)

# -----------------------------
# Sort values
# -----------------------------
df = df.sort_values(by=["amfi_code", "date"])

# -----------------------------
# Remove duplicate rows
# -----------------------------
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows Found: {duplicates}")

df = df.drop_duplicates()

# -----------------------------
# Validate NAV
# -----------------------------
invalid_nav = df[df["nav"] <= 0]

print(f"Invalid NAV Records: {len(invalid_nav)}")

# -----------------------------
# Missing values
# -----------------------------
print("\nMissing Values")
print(df.isnull().sum())

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("\n✅ Cleaned dataset saved successfully!")