import json

# import requests


def lambda_handler(event, context):

    # /weather
    if event['httpMethod'] == 'GET':
        return response("GET REQEUST")
    
    # /weather
    if event['httpMethod'] == 'POST':
        return response("POST REQEUST")
    
    # /weather/{id}
    if event['httpMethod'] == 'PUT':
        return response("PUT REQEUST")

    # /weather/{id}
    if event['httpMethod'] == 'DELETE':
        return response("DELETE REQEUST")
    

def response(message):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
        })
    }
