import requests
import json
import time
import os
import logging
from datetime import datetime, timedelta

# ----------------------------
# Configuration
# ----------------------------

BASE_URL = "https://api.open-meteo.com/v1/forecast"
OUTPUT_FILE = "eu_weather_data.json"
CACHE_DURATION = timedelta(minutes=30)  # Avoid redundant calls
RATE_LIMIT_DELAY = 0.7
MAX_RETRIES = 3

# ----------------------------
# Logging Setup
# ----------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("weather_collector.log"),
        logging.StreamHandler()
    ]
)

# ----------------------------
# EU Capitals
# ----------------------------

eu_capitals = [
    {"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
    {"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
    {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
    {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
    # (Include full EU list here for submission)
]

# ----------------------------
# Weather Code Mapping
# ----------------------------

weather_code_map = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    51: "Light drizzle",
    61: "Light rain",
    71: "Light snow",
    80: "Rain showers"
}

# ----------------------------
# Cache Handling
# ----------------------------

def is_cache_valid():
    if not os.path.exists(OUTPUT_FILE):
        return False

    file_time = datetime.fromtimestamp(os.path.getmtime(OUTPUT_FILE))
    return datetime.now() - file_time < CACHE_DURATION

# ----------------------------
# API Fetch Logic with Retry
# ----------------------------

def fetch_weather(capital):
    params = {
        "latitude": capital["lat"],
        "longitude": capital["lon"],
        "current_weather": True,
        "hourly": "temperature_2m,precipitation_probability,weathercode",
        "forecast_days": 1,
        "timezone": "auto"
    }

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            logging.warning(
                f"Retry {attempt+1}/{MAX_RETRIES} failed for {capital['city']}: {e}"
            )
            time.sleep(2 ** attempt)  # exponential backoff

    logging.error(f"Failed to retrieve data for {capital['city']} after retries.")
    return None

# ----------------------------
# Data Transformation
# ----------------------------

def transform_weather_data(capital, raw_data):
    try:
        current = raw_data["current_weather"]
        hourly = raw_data["hourly"]

        hourly_data = []
        for i in range(len(hourly["time"])):
            hourly_data.append({
                "time": hourly["time"][i],
                "temperature": hourly["temperature_2m"][i],
                "precipitation_probability": hourly["precipitation_probability"][i],
                "weathercode": hourly["weathercode"][i]
            })

        return {
            "country": capital["country"],
            "coordinates": {
                "latitude": capital["lat"],
                "longitude": capital["lon"]
            },
            "current_weather": {
                "temperature": current["temperature"],
                "windspeed": current["windspeed"],
                "weathercode": current["weathercode"],
                "condition": weather_code_map.get(current["weathercode"], "Unknown"),
                "time": current["time"]
            },
            "hourly_forecast": hourly_data
        }

    except KeyError as e:
        logging.error(f"Malformed data for {capital['city']}: Missing {e}")
        return None

# ----------------------------
# Main Execution Logic
# ----------------------------

def main():
    logging.info("Starting EU Capitals Weather Collection")

    if is_cache_valid():
        logging.info("Using cached data (recent file exists).")
        return

    eu_weather_data = {}

    for capital in eu_capitals:
        logging.info(f"Fetching weather for {capital['city']}")

        raw_data = fetch_weather(capital)
        if raw_data:
            structured = transform_weather_data(capital, raw_data)
            if structured:
                eu_weather_data[capital["city"]] = structured

        time.sleep(RATE_LIMIT_DELAY)

    # Save JSON output
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(eu_weather_data, f, indent=4)

    logging.info("Weather data collection complete.")
    logging.info(f"Output saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()