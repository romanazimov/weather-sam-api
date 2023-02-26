import json
# from db.connector import connector

def delete_handler(event):
    lookup_id = event['pathParameters']['id']
    if lookup_id.isnumeric():
        # query = f"DELETE FROM lookups WHERE id={lookup_id}"
        # result = connector(query)
        return response(lookup_id + " has been deleted.")
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
