import json

def lambda_handler(event, context):
    response = "Sam - Lambda function - lambda_handler called !"
    return {"statusCode": 200, "body": json.dumps(response)}

def Show_handler(event, context):
    response = "Sam - Lambda function - Show_handler called !"
    return {"statusCode": 200, "body": json.dumps(response)}    