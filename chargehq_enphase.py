import requests
import json
import time
from datetime import datetime
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
API_KEY = "your-chargehq-api-key"  # Replace with your Charge HQ Push API key
ENVOY_LOCAL_IP = "192.168.x.x"  # Replace with your Envoy local IP
ACCESS_TOKEN = "your-envoy-access-token"  # Replace with your Envoy access token
LOG_FILE_PATH = "/path/to/chargehq.log"  # Replace with your log file path
CHARGEHQ_URI = "https://api.chargehq.net/api/public/push-solar-data"

def fetch_envoy_data():
    """Fetch data from the Envoy device."""
    try:
        headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
        response = requests.get(f"https://{ENVOY_LOCAL_IP}/production.json?details=1", headers=headers, verify=False, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        log_message(f"Error fetching data from Envoy: {e}")
        return None

def calculate_values(data):
    """Calculate required values from the fetched data."""
    try:
        production_kw = max(data["production"][1]["wNow"] / 1000, 0)
        consumption_kw = data["consumption"][0]["wNow"] / 1000
        net_import_kw = consumption_kw - production_kw

        if net_import_kw < 0:
            imported_kwh = 0
            exported_kwh = abs(net_import_kw)
        else:
            imported_kwh = net_import_kw
            exported_kwh = 0

        return {
            "production_kw": round(production_kw, 3),
            "consumption_kw": round(consumption_kw, 3),
            "net_import_kw": round(net_import_kw, 3),
            "imported_kwh": round(imported_kwh, 3),
            "exported_kwh": round(exported_kwh, 3),
        }
    except (KeyError, TypeError) as e:
        log_message(f"Error calculating values: {e}")
        return None

def push_to_chargehq(values):
    """Send calculated values to ChargeHQ."""
    payload = {
        "apiKey": API_KEY,
        "siteMeters": values
    }
    try:
        response = requests.post(CHARGEHQ_URI, json=payload, timeout=10)
        if response.status_code == 200:
            log_message(f"Successfully pushed to Charge HQ: {payload}")
        else:
            log_message(f"Error pushing data to Charge HQ: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        log_message(f"Error pushing data to Charge HQ: {e}")

def log_message(message):
    """Log a message to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(f"{timestamp} {message}\n")
    print(f"{timestamp} {message}")

def main():
    while True:
        log_message("Starting new iteration.")
        envoy_data = fetch_envoy_data()
        if envoy_data:
            calculated_values = calculate_values(envoy_data)
            if calculated_values:
                push_to_chargehq(calculated_values)
        time.sleep(30)  # Wait 30 seconds before the next iteration

if __name__ == "__main__":
    main()
