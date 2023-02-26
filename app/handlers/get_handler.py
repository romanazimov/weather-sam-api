import json

def get_handler(event):
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
        

def response(message):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
        })
    }
