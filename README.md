# Day 1 Smoke Test

This project is my first Python setup test.

## Problem Statement

This project aims to predict mushroom yield using environmental sensor data such as temperature, humidity, and CO2 levels. The goal is to build a machine learning pipeline that helps improve mushroom production and monitoring in agriculture.

## Environment Setup
- Installed Python 3.10
- Created and activated a virtual environment (venv)
- Installed pandas, numpy, matplotlib, scikit-learn, and jupyter
- Created project folders:data/raw,notebooks,src, and models
- Created the smoke test script:src/smoke_test.py
- Ran the smoke test successfully

## Output
- Sample Sensor Data
- Temperature: 25.6°C
- Humidity: 68%
- CO2: 220ppm

## Dataset Columns

- timestamp: Date and time of sensor reading
- temperature: Temperature inside the polyhouse (°C)
- humidity: Relative humidity (%)
- CO2: Carbon dioxide concentration (ppm)
- yield: Mushroom yield harvested

## Git Setup

- Git repository initialized
- Connected to GitHub
- Project pushed to main branch

##Feature Definitions

temperature_c:
Temperature sensor reading in °C

humidity_pct:
Humidity sensor reading in %

co2_ppm:
CO₂ concentration in ppm

temp_humid_interaction:
temperature_c × humidity_pct / 100

##Train/Test Split

Dataset sorted by timestamp.
80% used for training.
20% used for testing.

Training data was used to fit MinMaxScaler.
Testing data was transformed using the same scaler to avoid data leakage.

### Split Summary

Train Rows: 292

Test Rows: 73

Train Dates:
2024-01-01 to 2024-10-19

Test Dates:
2024-10-20 to 2024-12-31

## Linear Regression Interpretation

Temperature coefficient:
Positive value means higher temperature increases yield.

Humidity coefficient:
Positive value means higher humidity increases yield.

CO2 coefficient:
Negative value means higher CO2 decreases yield.

## Residual Analysis

Diagnostic plots generated:

- residual_vs_predicted.png
- residual_vs_humidity.png

Observations:

- Residuals are centered around zero.
- No strong systematic pattern observed.
- Linear Regression is acceptable as a baseline model.

## Author
Lekshmi