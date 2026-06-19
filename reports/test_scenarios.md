# Test Scenarios

| Scenario | Temperature | Humidity | CO₂ | Expected Result |
|----------|-------------|----------|-----|----------------|
| Optimal Conditions | 22 | 88 | 920 | Normal yield prediction |
| Low Humidity | 22 | 60 | 920 | Lower yield |
| High Humidity | 22 | 98 | 920 | Different yield |
| High Temperature | 35 | 88 | 920 | Yield changes |
| High CO₂ | 22 | 88 | 1800 | Yield changes |
| Extreme Values | 10 | 50 | 400 | Boundary prediction |