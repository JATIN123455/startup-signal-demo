from export_csv import export_to_csv

def main():
    df = pd.read_csv("data/startups.csv")
    df = clean_data(df)

    df["hiring"] = df["careers_url"].apply(hiring_signal)
    df["funding_tier"] = df["funding_amount"].apply(funding_tier)

    export_to_csv(df)
