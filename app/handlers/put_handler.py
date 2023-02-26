import json

def put_handler(event):
    item_id = event['pathParameters']['id']
    if not item_id.isnumeric():
        return response("Invalid item ID")
        
    request_body = json.loads(event['body'])
    if 'description' in request_body:
        description = request_body['description']
        return response(f"Description: {description} and ID: {item_id}")
    else:
        return response("Key 'description' not found in request body")
            

def response(message):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
        })
    }
