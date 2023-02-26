import json
from handlers.get_handler import get_handler
from handlers.post_handler import post_handler
from handlers.put_handler import put_handler
from handlers.delete_handler import delete_handler

def lambda_handler(event, context):
    
    if event['httpMethod'] == 'GET':
        return get_handler(event)
    

    if event['httpMethod'] == 'POST':
        return post_handler(event)
    

    if event['httpMethod'] == 'PUT':
        return put_handler(event)


    if event['httpMethod'] == 'DELETE':
        return delete_handler(event)
