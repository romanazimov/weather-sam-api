import json
# from api.GoogleGeocode import get_geocode_coords
# from api.OpenWeatherMap import get_weather_data
# from db.connector import connector

def post_handler(event):
    if 'body' not in event or not event['body']:
        return response("Request body is empty. It needs 'address' and 'description' keys.")

    request_body = json.loads(event['body'])
    if 'address' and 'description' in request_body:
        address = request_body['address']
        description = request_body['description']

        # latitude, longitude = get_geocode_coords(f"{address}")
        # data = get_weather_data(latitude, longitude)
        # query = f"INSERT INTO lookups (latitude, longitude, temp, feels_like, temp_min, temp_max, pressure, humidity, note)" + 
        #         f"VALUES ({data['latitude']}, {data['longtitude']}, {data['temp']}, {data['feels_like'], {data['temp_min']}," +
        #         f"{data['temp_max']}, {data['pressure']}, {data['humidity]']}, {data['note']}})"
        # result = connector(query)
        
        return response(f"Address: {address}, Description: {description}")
    else:
        return response("Key 'address' and/or 'description' not found in request body")


def response(message):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            # "message": result
        })
    }
