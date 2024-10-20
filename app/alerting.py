from config.config import TEMP_THRESHOLD, ALERT_CONSECUTIVE_UPDATES

alert_counter = {}

def check_thresholds(df):
    alerts = []
    for index, row in df.iterrows():
        if row['temp'] > TEMP_THRESHOLD:
            if alert_counter.get(row['city'], 0) >= ALERT_CONSECUTIVE_UPDATES:
                alerts.append(f"Alert! {row['city']} temperature exceeded {TEMP_THRESHOLD}°C")
            else:
                alert_counter[row['city']] = alert_counter.get(row['city'], 0) + 1
        else:
            alert_counter[row['city']] = 0
    return alerts
