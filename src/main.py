import pandas as pd
from clean import clean_data
from signals import hiring_signal, funding_tier
from sheets import export_to_sheets

SHEET_ID = "PASTE_YOUR_GOOGLE_SHEET_ID"

def main():
    df = pd.read_csv("data/startups.csv")
    df = clean_data(df)

    df["hiring"] = df["careers_url"].apply(hiring_signal)
    df["funding_tier"] = df["funding_amount"].apply(funding_tier)

    export_to_sheets(df, SHEET_ID)
    print("Pipeline completed. Google Sheet updated.")

if __name__ == "__main__":
    main()
