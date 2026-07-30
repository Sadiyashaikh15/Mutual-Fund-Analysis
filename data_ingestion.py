import os
import pandas as pd

DATA_FOLDER = "data/raw"

csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

print("=" * 60)
print(f"Total CSV Files Found: {len(csv_files)}")
print("=" * 60)

for file in csv_files:

    file_path = os.path.join(DATA_FOLDER, file)

    print(f"\nReading: {file}")

    try:
        df = pd.read_csv(file_path)

        print("Shape:", df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except pd.errors.EmptyDataError:
        print("This CSV file is empty.")

    except Exception as e:
        print("Error:", e)

    print("-" * 60)