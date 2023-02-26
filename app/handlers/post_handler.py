import json

def post_handler(event):
    return response("POST REQEUST")


def response(message):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
        })
    }
