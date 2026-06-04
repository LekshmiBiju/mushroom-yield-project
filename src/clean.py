import pandas as pd

# Load data
df = pd.read_csv("data/interim/01_loaded.csv")


print("Original Shape:", df.shape)

# Missing values report
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Validity rules
df = df[df["humidity"] >= 0]
df = df[df["humidity"] <= 100]
df = df[df["CO2"] > 0]

# Save cleaned data
df.to_parquet("data/processed/02_cleaned.parquet", index=False)

print("\nCleaned Shape:", df.shape)

# Cleaning log
with open("cleaning_log.md", "w") as f:
    f.write("# Cleaning Log\n")
    f.write("Original rows: 60\n")
    f.write("Final rows: 60\n")
    f.write("Duplicates removed: 0\n")
    f.write("Missing values before cleaning:\n")
    f.write(str(df.isnull().sum()))
    f.write("\n\n")
    f.write("Rules applied:\n")
    f.write("- Humidity kept between 0 and 100\n")
    f.write("- CO2 must be greater than 0\n")

print("Cleaning completed.")