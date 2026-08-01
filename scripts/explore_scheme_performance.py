import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("=" * 60)
print("SCHEME PERFORMANCE")
print("=" * 60)

print(df.head())

print("\n")
print(df.info())

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())