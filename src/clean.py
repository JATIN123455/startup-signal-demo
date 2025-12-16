import pandas as pd

def clean_data(df):
    df.columns = [c.lower().strip() for c in df.columns]
    df = df.drop_duplicates(subset=["company", "round"])
    return df
