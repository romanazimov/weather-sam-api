import os
import requests

API_KEY = os.environ.get('geocodeApiKey')

def get_geocode_coords(address):
    latitude, longitude = None, None
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address}&key={API_KEY}"
    results = requests.get(endpoint)
    latitude = results['geometry']['location']['lat']
    longitude = results['geometry']['location']['lng']
    return latitude, longitude
