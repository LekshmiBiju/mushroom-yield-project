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

## Random Forest Results

Random Forest model was trained and compared with the baseline Linear Regression model.

Outputs:
- models/random_forest.joblib
- reports/random_forest_report.md
- reports/cv_results.md
- reports/figures/rf_importance.png

# comparison

RF CV MAE: 0.47404833333333257 +/- 0.05711333157026999
Linear CV MAE: 0.4405590208164414 +/- 0.03375818091090288

# Model Comparison

       Model	       Test MAE    Test R²
Linear Regression	    1.8        0.55
Random Forest (Default)	1.4	       0.68
Random Forest (Tuned)	1.2     	0.74

The Tuned Random Forest achieved the lowest MAE and highest R² score, indicating superior predictive performance.

Generated Files

outputs
- models/rf_tuned.joblib
- models/champion.joblib
- models/rf_best_params.json
- reports/grid_search_results.md
- reports/model_comparison.md
- src/grid_search.py
- src/model_comparison.py

## Run Inference

Predict mushroom yield:

```bash
python src/predict.py
Predicted Yield: 16.98 kg

## Streamlit App

Run:

streamlit run app.py

The app allows users to enter sensor values and predict mushroom yield.

Screenshot saved in reports/streamlit_app.png.

## Streamlit Application

Run the App

Activate the virtual environment and run:

streamlit run app.py

Features

- Predict mushroom yield using Temperature, Humidity, and CO₂ sensor readings.
- Interactive sliders for sensor inputs.
- Predicted yield displayed in kilograms.
- Humidity sensitivity analysis chart.
- Model information panel.
- Out-of-range input warnings.

Screenshot

See "reports/streamlit_app.png" for the application interface.

## Run Tests

pytest tests/

## Live Demo

Deployment URL:https://mushroom-yield-project-7nxbbbjsufc83coh3l6vz3.streamlit.app/

## Author
Lekshmi Biju