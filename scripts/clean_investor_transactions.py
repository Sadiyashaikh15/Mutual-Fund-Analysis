import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("=" * 60)
print("Original Dataset")
print("=" * 60)

print(df.info())

# -----------------------------
# Convert date
# -----------------------------
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# -----------------------------
# Remove duplicates
# -----------------------------
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

df = df.drop_duplicates()

# -----------------------------
# Amount validation
# -----------------------------
invalid_amount = df[df["amount_inr"] <= 0]

print(f"Invalid Amount Records: {len(invalid_amount)}")

# -----------------------------
# Missing values
# -----------------------------
print("\nMissing Values")
print(df.isnull().sum())

# -----------------------------
# Validate KYC
# -----------------------------
valid_kyc = ["Verified", "Pending"]

invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]

print(f"\nInvalid KYC Records: {len(invalid_kyc)}")

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("\n✅ Investor Transactions cleaned successfully!")