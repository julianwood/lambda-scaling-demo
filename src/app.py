import json
import time

def lambda_handler(event, context):
    ret =  {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
    time.sleep(10)
    return ret;

