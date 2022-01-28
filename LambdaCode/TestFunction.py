import json

def lambda_handler(event, context):
    response = "Sam - Lambda function called !"
    return {"statusCode": 200, "body": json.dumps(response)}