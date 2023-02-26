import json

def lambda_handler(event, context):
    
    if event['httpMethod'] == 'GET':
        if event.get('pathParameters') is None:
            # Return list of items
            return response("GET LIST REQUEST")
        else:
            # Return specific item
            item_id = event['pathParameters']['id']
            if item_id.isnumeric():
                return response(item_id)
            else:
                return response("Invalid item ID")
    

    # /weather
    if event['httpMethod'] == 'POST':
        return response("POST REQEUST")
    

    # /weather/{id}
    if event['httpMethod'] == 'PUT':
        item_id = event['pathParameters']['id']
        if not item_id.isnumeric():
            return response("Invalid item ID")
        
        request_body = json.loads(event['body'])
        if 'description' in request_body:
            description = request_body['description']
            return response(f"Description: {description} and ID: {item_id}")
        else:
            return response("Key 'description' not found in request body")


    # /weather/{id}
    if event['httpMethod'] == 'DELETE':
        item_id = event['pathParameters']['id']
        if item_id.isnumeric():
            return response(item_id + " DELETE REQUEST")
        else:                
            return response("Invalid item ID")


def response(message):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
        })
    }
