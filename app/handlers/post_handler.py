import json
# from api.GoogleGeocode import get_geocode_coords
# from api.OpenWeatherMap import get_weather_data

def post_handler(event):
    request_body = json.loads(event['body'])
    if 'address' and 'description' in request_body:
        address = request_body['address']
        description = request_body['description']
        # query = f"INSERT INTO lookups (temp, feels_like, temp_min, temp_max, pressure, humidity, note)" + 
        #         f"VALUES ({data['temp']}, {data['feels_like'], {data['temp_min']}, {data['temp_max']}, {data['pressure']}, {data['humidity]']}, {data['note']}})"

        # latitude, longitude = get_geocode_coords(f"{address}")
        # data = get_weather_data(latitude, longitude)
        # result = connector(query)
        return response(f"Address: {address}, Note: {description}")
    else:
        return response("Key 'address' and/or 'description' not found in request body")


def response(message):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            # "message": results
        })
    }
