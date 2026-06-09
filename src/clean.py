# src/clean.py

import pandas as pd

df = pd.read_parquet("data/interim/01_loaded.parquet")

print("Columns:")
print(df.columns.tolist())

# Missing values report
print("\nMissing Values:")
print(df.isna().sum())

# Valid ranges for mushroom polyhouse
valid = (
    df["humidity_pct"].between(50, 100)
    & df["temperature_c"].between(10, 35)
    & df["co2_ppm"].between(400, 2000)
    & df["yield_kg"].notna()
)

df = df[valid].copy()

# Forward fill sensor columns
sensor_cols = ["temperature_c", "humidity_pct", "co2_ppm"]
df[sensor_cols] = df[sensor_cols].ffill(limit=2)

# Remove rows with missing target
df = df.dropna(subset=["yield_kg"])

# Remove duplicate timestamps
df = df.drop_duplicates(subset=["timestamp"], keep="last")

# Save cleaned dataset
df.to_parquet("data/interim/02_cleaned.parquet", index=False)

print(f"\nClean rows: {len(df)}")
print("Saved: data/interim/02_cleaned.parquet")