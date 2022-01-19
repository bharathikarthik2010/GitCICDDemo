
import json

def lambda_handler(event, context):
    response = "Lambda Function 1 !"
    return {"statusCode": 200, "body": json.dumps(response)}
