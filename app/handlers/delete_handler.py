import json

def delete_handler(event):
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
