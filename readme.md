# FastAPI SNS Subscription Endpoint

This project sets up a FastAPI application to handle HTTP/HTTPS Amazon SNS subscriptions, capable of managing high request rates with Uvicorn.

## Features

- **SNS Subscription Confirmation**: Confirms subscription requests from SNS.
- **SNS Notification Handling**: Processes messages sent from SNS to the endpoint.
- **Optimized for High Throughput**: Configured to handle up to 1000 requests per second with Uvicorn and async capabilities.

## Prerequisites

- Python 3.7+
- AWS SDK for Python (Boto3)
- FastAPI
- Uvicorn

## Setup

1. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn boto3

## How to run
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 --loop asyncio --access-log

