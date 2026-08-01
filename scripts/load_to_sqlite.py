import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

print("=" * 50)
print("LOADING DATA INTO SQLITE")
print("=" * 50)

# Project root folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Database path
db_path = BASE_DIR / "bluestock_mf.db"

# SQLite connection
engine = create_engine(f"sqlite:///{db_path}")

# Load datasets
fund_df = pd.read_csv(BASE_DIR / "data/raw/01_fund_master.csv")
nav_df = pd.read_csv(BASE_DIR / "data/processed/nav_history_cleaned.csv")
trans_df = pd.read_csv(BASE_DIR / "data/processed/investor_transactions_cleaned.csv")
perf_df = pd.read_csv(BASE_DIR / "data/processed/scheme_performance_cleaned.csv")

# Save tables
fund_df.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)
trans_df.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf_df.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("✅ All tables loaded successfully!")
print(f"Database Location: {db_path}")