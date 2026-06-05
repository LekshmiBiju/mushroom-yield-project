import pandas as pd

df = pd.read_parquet("data/processed/02_cleaned.parquet")

print("Total Rows:", len(df))

print("\nDate Range:")
print("Start:", df["timestamp"].min())
print("End:", df["timestamp"].max())

print("\nSummary Statistics:")
print(df[["temperature", "humidity", "CO2", "yield"]].describe())

humidity_valid = ((df["humidity"] >= 0) & (df["humidity"] <= 100)).sum()
co2_valid = (df["CO2"] > 0).sum()

print("\nHumidity Rule Pass %:", humidity_valid / len(df) * 100)
print("CO2 Rule Pass %:", co2_valid / len(df) * 100)