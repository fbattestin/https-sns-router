from fastapi import FastAPI, Request
import boto3

app = FastAPI()
sns_client = boto3.client("sns", region_name="us-east-1")

@app.post("/sns/endpoint")
async def sns_endpoint(request: Request):
    headers = request.headers
    message_type = headers.get("x-amz-sns-message-type")
    message = await request.json()

    if message_type == "SubscriptionConfirmation":
        sns_client.confirm_subscription(
            TopicArn=message["TopicArn"], Token=message["Token"]
        )
        return {"message": "Subscription confirmed"}

    elif message_type == "Notification":
        notification_message = message["Message"]
        # Handle notification here
        return {"message": "Notification received"}

    return {"message": "No action taken"}
