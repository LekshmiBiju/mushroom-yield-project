# Monitoring Plan

## Deployment
Platform: Streamlit Community Cloud

App URL:
https://mushroom-yield-project-7nxbbbjsufc83coh3l6vz3.streamlit.app

Main File:
app.py

## Sample Prediction Log

| Temperature | Humidity | CO2 | Predicted Yield |
|------------|----------|-----|----------------|
| 22.0 | 88.0 | 920 | 16.98 kg |

## Monitoring Strategy

- Monitor prediction outputs weekly.
- Check for invalid sensor inputs.
- Verify prediction consistency.

## Retraining Triggers

Retrain the model when:
- More than 100 new records are collected.
- Prediction quality decreases.
- Environmental conditions change significantly.

## Prediction Logging

Log:

- Temperature
- Humidity
- CO2
- Predicted Yield
- Timestamp

## Drift Monitoring

Watch for:

- Sensor calibration changes
- Sudden humidity shifts
- Seasonal environmental changes

## Retraining Triggers

Retrain when:

1. New data is available
2. Prediction accuracy drops
3. Sensor behaviour changes
4. Monthly review is reached

## Thresholds

- Temperature: 10–35 °C
- Humidity: 70–100 %
- CO2: 400–2000 ppm