
import json

def lambda_handler(event, context):
    response = "Code Pipeline Demo - Test 1 !"
    return {"statusCode": 200, "body": json.dumps(response)}
