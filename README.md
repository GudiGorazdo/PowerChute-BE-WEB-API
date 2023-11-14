# PowerChute Class Documentation

## Class Overview

The `PowerChute` class is designed to interact with the PowerCute Business Edition v10.0.5 web interface. It provides functionalities for authenticating with the server, retrieving data from specified pages, and parsing HTML content to extract valuable information.

## Class Initialization

```python
def __init__(self, server_ip, port, username, password, pages):
```

Initializes a new instance of the PowerChute class.
Parameters:
    - server_ip (str): The IP address of the PowerCute server.
    - port (str): The port number for the server connection.
    - username (str): The username for authentication.
    - password (str): The password for authentication.
    - pages (list of str): An array of page addresses from which to retrieve data.

## Customizing Page Addresses****
- Users can pass an array of page addresses in the pages parameter during the initialization of the PowerChute class. This allows for flexibility in selecting which pages to retrieve data from.
- The provided page addresses should be valid and accessible through the authenticated session.
- Example of specifying pages:

```python
pages_to_fetch = ['status', 'batterymanagement', 'diagnostics']
myups = PowerChute(server_ip="localhost", port="6547", username="username", password="password", pages=pages_to_fetch)
```

## Retrieving Data as JSON
- The get_all_fields_values_as_json method retrieves the data from the specified pages and returns it in JSON format.
- This method iterates through each page specified in the pages array, extracts the required field values, and compiles them into a JSON object.
- The returned JSON object contains the field IDs as keys and their corresponding values for each specified page.

```python
json_data = myups.get_all_fields_values_as_json()
print(json_data)
```
Result example:
```json
{
    "status": {
        "value_DeviceStatus": "On Battery",
        "value_RealPowerPct": "45.3",
        "value_RuntimeRemaining": "75",
        "value_InternalTemp": "28.3°C / 82.9°F",
        "value_ApparentPowerPct": "46.5",
        "value_LoadCurrent": "6.2",
        "value_InputVoltage": "210.4",
        "value_OutputVoltage": "210.4",
        "value_InputFrequency": "49.7",
        "value_OutputFrequency": "49.7",
        "value_BatteryCharge": "95.0",
        "value_VoltageDC": "26.8"
    },
    "batterymanagement": {
        "value_BatteryStatus": "Replace Soon",
        "value_BatteryCharge": "60.0",
        "value_VoltageDC": "26.1",
        "value_RuntimeRemaining": "45"
    },
    "diagnostics": {
        "SelfTestDate": "August 15, 2023 at 3:20:10 PM UTC",
        "LastReplaceBatteryTestStatus": "Failed",
        "RuntimeCalibDate": "September 5, 2023 at 11:02:30 AM UTC",
        "LastRunTimeCalibrationStatus": "Failed"
    }
}
```
