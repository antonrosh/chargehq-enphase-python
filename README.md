# Charge HQ and Enphase Integration Script

This Python script enables efficient communication between your Enphase Solar Energy system and the [Charge HQ](https://chargehq.net) application. Charge HQ is an excellent tool for optimizing the use of solar energy, particularly for charging electric vehicles (EVs) like Tesla. Since Charge HQ does not offer direct integration with Enphase systems, this script provides the necessary functionality to bridge the gap.

---

## Why Use This Script?

As a Charge HQ user with an Enphase solar setup, this solution helps you:
- Leverage your surplus solar energy for EV charging.
- Seamlessly upload solar production and consumption data to Charge HQ.
- Overcome the lack of direct integration between Charge HQ and Enphase devices.

---

## What Makes This Script Different?

Initially, I tried using [this solution](https://github.com/khandelwalpiyush/chargehq-enphase). While functional, it had several limitations:
- **Compatibility Issues:** It relied on older methods for generating JWT tokens, which caused authentication failures with my firmware version (D8.2.4345).
- **Stability Concerns:** The shell script occasionally failed to renew tokens or handle network interruptions gracefully.
- **Limited Debugging:** Logs provided insufficient information for troubleshooting errors.

This Python-based solution addresses these issues with:
- Support for firmware `D8.2.4345` and similar versions.
- Robust error handling and automatic recovery from network issues.
- Detailed logging for easier troubleshooting.

---

## Key Features

- **Firmware Compatibility:** Tested on Enphase firmware `D8.2.4345`.
- **Automated Data Upload:** Sends solar production and consumption data to Charge HQ every 30 seconds.
- **Enhanced Error Handling:** Automatically retries failed requests and logs detailed error messages.
- **Easy Setup:** Minimal configuration required for operation.

---

## Prerequisites

To use this script, you will need:
- An Enphase Solar Energy system with local network access.
- A Charge HQ account.
- Python 3.7 or newer installed on your system.
- Access token for your Envoy device. You can get it [here](https://entrez.enphaseenergy.com/)

---

## How to Use This Script

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/chargehq-enphase-python.git
cd chargehq-enphase-python
```

### 2. Configure the Script
Edit the `chargehq_enphase.py` file and update the following variables with your details:
```python
API_KEY = "your-chargehq-api-key"      # Your Charge HQ Push API key
ENVOY_LOCAL_IP = "192.168.x.x"         # Local IP address of your Envoy device
ACCESS_TOKEN = "your-envoy-access-token"  # Access token for the Envoy
LOG_FILE_PATH = "/path/to/chargehq.log"  # Location of the log file
```

### 3. Install Required Libraries
No additional libraries are needed, as the script uses Python’s standard modules.

### 4. Run the Script
Execute the script manually to verify it works:
```bash
python3 chargehq_enphase.py
```
Monitor the log file for output:
```bash
tail -f /path/to/chargehq.log
```

### 5. Automate the Script

#### Linux (Using Cron)
Set up the script to run automatically on system startup:
```bash
crontab -e
```
Add this line:
```bash
@reboot /usr/bin/python3 /path/to/chargehq_enphase.py >> /path/to/cron_startup.log 2>&1 &
```

#### Windows (Using Task Scheduler)
Refer to this [guide](https://o365reports.com/2019/08/02/schedule-powershell-script-task-scheduler/) to schedule the script on system boot.

---

## Example JSON Payload

Here is an example of the data sent to Charge HQ:
```json
{
  "apiKey": "your-chargehq-api-key",
  "siteMeters": {
    "production_kw": 6.845,
    "consumption_kw": 6.719,
    "net_import_kw": -0.125,
    "imported_kwh": 0,
    "exported_kwh": 0.125
  }
}
```

---

## Troubleshooting

- **Network Errors:** 
  - If you see "Network is unreachable," ensure your Envoy device is powered on and reachable.
  - Add a delay before the script starts to allow network initialization.

- **Empty or Inaccurate Logs:** 
  - Check the log file location and permissions. Make sure the script has write access.

- **Token Expiry:** 
  - The script should handle token renewals automatically. If issues persist, verify the token manually.

---

## Useful Links

- [Charge HQ Official Site](https://chargehq.net)
- [Charge HQ Push API Documentation](https://chargehq.net/kb/push-api)
- [Enphase Energy Official Site](https://enphase.com/en-au)
- [Python Documentation](https://docs.python.org/3/)

---

## Contributing

If you encounter any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

---


This script provides a more robust and reliable integration for Charge HQ users with Enphase systems. Feel free to reach out if you have any questions or need further assistance!

--- 

Let me know if you need any further adjustments! 🚀

<!-- 
Charge HQ, Enphase, Solar Data Integration, Python Script, EV Charging Optimization
Charge HQ Enphase integration script
Python script for Charge HQ Push API
Solar energy data upload to Charge HQ
Enphase firmware D8.x Charge HQ compatibility
Optimizing EV charging with Charge HQ and Enphase
-->
