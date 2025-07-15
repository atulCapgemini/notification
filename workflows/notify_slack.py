import os
import json
import requests
from datetime import datetime, timedelta

# Load Slack webhook URL from environment
webhook_url = os.getenv("SLACK_WEBHOOK_URL")

# Read last deployment date
with open("last_deployment.txt", "r") as f:
    last_deployment_str = f.read().strip()
    last_deployment = datetime.strptime(last_deployment_str, "%Y-%m-%d")

# Check if 90 days have passed
if datetime.now() - last_deployment >= timedelta(days=90):
    message = {
        "text": f":warning: *90 days since last deployment!* Last deployment was on *{last_deployment.strftime('%Y-%m-%d')}*. Please review deployment schedule."
    }

    response = requests.post(
        webhook_url,
        data=json.dumps(message),
        headers={"Content-Type": "application/json"}
    )

    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned error {response.status_code}, response: {response.text}")
