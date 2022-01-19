
import json

def lambda_handler(event, context):
    response = "Lambda Function 2 - new  !"
    return {"statusCode": 200, "body": json.dumps(response)}
