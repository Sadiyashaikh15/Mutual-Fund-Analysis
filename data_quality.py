import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 50)
print("FUND MASTER EXPLORATION")
print("=" * 50)

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub-Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

print("\nTotal Fund Houses:", fund_master["fund_house"].nunique())
print("Total Categories:", fund_master["category"].nunique())
print("Total Sub-Categories:", fund_master["sub_category"].nunique())
print("Total Risk Categories:", fund_master["risk_category"].nunique())

print("\n" + "=" * 50)
print("AMFI CODE VALIDATION")
print("=" * 50)

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print(f"Total AMFI Codes in fund_master : {len(master_codes)}")
print(f"Total Unique AMFI Codes in nav_history : {len(nav_codes)}")

if len(missing_codes) == 0:
    print("\n✅ All AMFI Codes are present in nav_history.")
else:
    print("\n❌ Missing AMFI Codes:")
    print(missing_codes)

print("\n" + "=" * 50)
print("DATA QUALITY SUMMARY")
print("=" * 50)

print(f"Fund Master Rows : {len(fund_master)}")
print(f"NAV History Rows : {len(nav_history)}")
print(f"Missing Values in Fund Master : {fund_master.isnull().sum().sum()}")
print(f"Missing Values in NAV History : {nav_history.isnull().sum().sum()}")
print(f"Duplicate Rows in Fund Master : {fund_master.duplicated().sum()}")
print(f"Duplicate Rows in NAV History : {nav_history.duplicated().sum()}")

if len(missing_codes) == 0:
    print("\nData Quality Status: PASS ✅")
else:
    print("\nData Quality Status: FAIL ❌")