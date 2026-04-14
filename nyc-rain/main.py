# Visit https://open-meteo.com/ to see the starter code.



import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry

# Manually added to convert time to readable format
from datetime import datetime
import pytz



print("[SYSTEM]: Initialized")
# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)


# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 40.7128,
	"longitude": 74.006,
	"current": "rain",
	"timezone": "America/New_York",
}
responses = openmeteo.weather_api(url, params=params)


# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone: {response.Timezone()}{response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")


# Process current data. The order of variables needs to be the same as requested.
current = response.Current()
current_rain = current.Variables(0).Value()

# Manually added to convert time to readable format
timestamp = current.Time()
timezone = pytz.timezone(params["timezone"])
current_time = datetime.fromtimestamp(timestamp, timezone)

print(f"\nCurrent time: {current.Time()}")
print(f"\nCurrent time: {current_time}")
print(f"Current rain: {current_rain}")
print("[SYSTEM]: Success")

# current_rain is in milimeters (mm)
with open("rain.csv", "a") as f:
    if current_rain > 0:
        f.write(f"{current_time},{current_rain}\n")
