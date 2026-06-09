# src/eda.py

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_parquet("data/interim/02_cleaned.parquet")

print("Columns:")
print(df.columns.tolist())

# Correct column names
features = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "yield_kg"
]

# Create output folders
Path("reports").mkdir(exist_ok=True)
Path("reports/figures").mkdir(parents=True, exist_ok=True)

# ===================================
# Correlation Matrix
# ===================================

corr_matrix = df[features].corr()

print("\nCorrelation Matrix:")
print(corr_matrix)

corr_matrix.to_csv(
    "reports/correlation_matrix.csv"
)

with open(
    "reports/correlation_matrix.md",
    "w",
    encoding="utf-8"
) as f:
    f.write("# Correlation Matrix\n\n")
    f.write(corr_matrix.to_string())

# ===================================
# Correlation Heatmap
# ===================================

fig, ax = plt.subplots(figsize=(6, 5))

im = ax.imshow(
    corr_matrix,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

ax.set_xticks(range(len(features)))
ax.set_xticklabels(
    features,
    rotation=45,
    ha="right"
)

ax.set_yticks(range(len(features)))
ax.set_yticklabels(features)

fig.colorbar(
    im,
    ax=ax,
    label="Pearson r"
)

ax.set_title(
    "Sensor & Yield Correlations"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/correlation_heatmap.png",
    dpi=150
)

# ===================================
# Scatter Plots
# ===================================

fig, axes = plt.subplots(
    1,
    3,
    figsize=(12, 4)
)

# Humidity vs Yield
axes[0].scatter(
    df["humidity_pct"],
    df["yield_kg"],
    alpha=0.5,
    s=15
)
axes[0].set_xlabel("Humidity (%)")
axes[0].set_ylabel("Yield (kg)")
axes[0].set_title("Humidity vs Yield")

# Temperature vs Yield
axes[1].scatter(
    df["temperature_c"],
    df["yield_kg"],
    alpha=0.5,
    s=15
)
axes[1].set_xlabel("Temperature (°C)")
axes[1].set_ylabel("Yield (kg)")
axes[1].set_title("Temperature vs Yield")

# CO2 vs Yield
axes[2].scatter(
    df["co2_ppm"],
    df["yield_kg"],
    alpha=0.5,
    s=15
)
axes[2].set_xlabel("CO₂ (ppm)")
axes[2].set_ylabel("Yield (kg)")
axes[2].set_title("CO₂ vs Yield")

plt.tight_layout()

plt.savefig(
    "reports/figures/scatter_yield.png",
    dpi=150
)

plt.show()

print("\nEDA completed successfully.")
print("Files saved in reports/")