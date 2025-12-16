import os

def export_to_csv(df, filename="output/startup_signal_output.csv"):
    os.makedirs("output", exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"CSV exported to {filename}")
