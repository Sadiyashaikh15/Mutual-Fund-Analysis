import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("=" * 50)
print("Transaction Types")
print(df["transaction_type"].unique())

print("\n" + "=" * 50)
print("KYC Status")
print(df["kyc_status"].unique())

print("\n" + "=" * 50)
print("Payment Modes")
print(df["payment_mode"].unique())

print("\n" + "=" * 50)
print("City Tiers")
print(df["city_tier"].unique())