import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    user = event.get("user", "unknown")
    action = event.get("action", "read")

    logger.info(f"User {user} performed {action}")

    return {
        "statusCode": 200,
        "body": f"{user} performed {action}"
    }