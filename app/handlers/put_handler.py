import json
# from db.connector import connector

def put_handler(event):
    lookup_id = event['pathParameters']['id']
    if not lookup_id.isnumeric():
        return response("Invalid item ID")
        
    request_body = json.loads(event['body'])
    if 'new_description' in request_body:
        # new_description = request_body['new_description']
        # query = f"UPDATE lookups SET description={new_description} WHERE id={lookup_id}"
        # result = connector(query)
        
        return response(f"The description has been updated for id:{lookup_id}")
    else:
        return response("Key 'new_description' not found in request body")
            

def response(message):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            # "message": result
        })
    }
