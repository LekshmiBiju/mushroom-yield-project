import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_parquet("data/processed/02_cleaned.parquet")

# Create figures folder automatically
import os
os.makedirs("reports/figures", exist_ok=True)

# Correlation Heatmap
corr = df[["temperature", "humidity", "CO2", "yield"]].corr()

plt.figure(figsize=(6,5))
plt.imshow(corr, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("reports/figures/correlation_heatmap.png")
plt.close()

# Humidity vs Yield
plt.figure()
plt.scatter(df["humidity"], df["yield"])
plt.xlabel("Humidity (%)")
plt.ylabel("Yield (kg)")
plt.title("Humidity vs Yield")
plt.savefig("reports/figures/humidity_vs_yield.png")
plt.close()

# Temperature vs Yield
plt.figure()
plt.scatter(df["temperature"], df["yield"])
plt.xlabel("Temperature (°C)")
plt.ylabel("Yield (kg)")
plt.title("Temperature vs Yield")
plt.savefig("reports/figures/temperature_vs_yield.png")
plt.close()

# CO2 vs Yield
plt.figure()
plt.scatter(df["CO2"], df["yield"])
plt.xlabel("CO2")
plt.ylabel("Yield (kg)")
plt.title("CO2 vs Yield")
plt.savefig("reports/figures/co2_vs_yield.png")
plt.close()

print("EDA figures generated successfully.")