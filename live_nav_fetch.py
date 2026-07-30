import requests
import pandas as pd
import os

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# AMFI Scheme Codes
schemes = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"Downloading {scheme_name}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"data/raw/{scheme_name}.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"Saved -> {file_name}")

    else:

        print(f"Failed for {scheme_name}")