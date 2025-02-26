# Satellite Passes

A simple script to log out satellite passes of interest at a given location on Earth within the next ten days. If no NORAD catalog numbers are given, defaults to NOAA-18, NOAA-19, MetOp-B, and Meteor M2.

The script expects the following environment variables:

+ `api_key`, a key from n2yo.com
+ `observer_lat`, latitude in degrees
+ `observer_lng`, longitude in degrees
+ `observer_alt`, altitude in meters

Usage: `python3 main.py [ID]...`
