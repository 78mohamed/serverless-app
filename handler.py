import json

def hello(event, context):
    """
    A simple Lambda function that responds with a JSON greeting.
    """
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello, World!",
            "input": event
        })
    }
