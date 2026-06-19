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