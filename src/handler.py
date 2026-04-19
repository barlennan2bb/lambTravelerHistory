import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "service": "traveler-history",
            "path": event.get("rawPath", "/traveler/history"),
            "status": "ok",
        }),
    }
