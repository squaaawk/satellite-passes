import os
import sys

import requests
from datetime import datetime
import pytz

from dotenv import load_dotenv
load_dotenv()


def utc_to_datetime(time: int):
  tz = pytz.timezone("America/Detroit")
  dt = datetime.fromtimestamp(time, tz=tz).replace(tzinfo=None)
  return dt

def query_n2yo(id: str, api_key: str, observer_lat: float, observer_lng: float, observer_alt: float):
  min_elevation = 70.0 # degrees
  days = 10            # days

  url = f"https://api.n2yo.com/rest/v1/satellite/radiopasses/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{days}/{min_elevation}"
  params = { "apiKey": api_key }

  return requests.get(url, params)


# Environment variables
api_key = os.getenv("api_key")
observer_lat = os.getenv("observer_lat")
observer_lng = os.getenv("observer_lng")
observer_alt = os.getenv("observer_alt")

assert api_key is not None
assert observer_lat is not None
assert observer_lng is not None
assert observer_alt is not None


# A list of NORAD Catalog numbers for the spacecraft of interest
ids = [
  "28654",  # NOAA-18
  "33591",  # NOAA-19
  "38771",  # MetOp-B
  "40069",  # Meteor M2
]

for id in ids:
  response = query_n2yo(id, api_key, observer_lat, observer_lng, observer_alt).json()

  id = response["info"]["satid"]
  name = response["info"]["satname"]
  passes = response["passes"]

  print(f"Satellite: {name} ({id})")

  for p in passes:
    elevation = p["maxEl"]
    start = utc_to_datetime(p["startUTC"])
    end = utc_to_datetime(p["endUTC"])
    print(f"  elevation: {elevation:4.1f}°  start: {start}  end: {end}")

  print()
