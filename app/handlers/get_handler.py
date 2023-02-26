import json
# from db.connector import connector

def get_handler(event):
    if event.get('pathParameters') is None:
        # query = "SELECT * FROM lookups"
        # result = connector(query)
        return response("GET LIST REQUEST")
    else:
        item_id = event['pathParameters']['id']
        if item_id.isnumeric():
            # query = f"SELECT * FROM users JOIN lookups ON users.id = lookups.uid WHERE users.id = {id}"
            # result = connector(query)
            return response(item_id)
        else:
            return response("Invalid item ID")
        

def response(message):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            # "message": result
        })
    }
