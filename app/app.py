import os, json, logging
from datetime import datetime, timezone
import boto3
from botocore.exceptions import ClientError
from flask import Flask, jsonify

logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "info").upper(),
    format="%(asctime)s %(levelname)s %(message)s",
)
log = logging.getLogger("cloudproject")

REGION = os.environ.get("AWS_REGION", "us-east-1")
BUCKET = os.environ["S3_BUCKET"]
KEY = "visits.json"

s3 = boto3.client("s3", region_name=REGION)
ssm = boto3.client("ssm", region_name=REGION)
app = Flask(__name__)

@app.route("/api/status")
def status():
    # Secret is fetched to prove access works, but is never returned or logged
    ssm.get_parameter(Name="/cloudproject/prod/api-key", WithDecryption=True)
    log.info("Secret retrieved from SSM")

    try:
        body = s3.get_object(Bucket=BUCKET, Key=KEY)["Body"].read()
        visits = json.loads(body)["visits"]
    except ClientError as e:
        log.warning("Could not read counter: %s", e.response["Error"]["Code"])
        visits = 0

    visits += 1
    s3.put_object(Bucket=BUCKET, Key=KEY, Body=json.dumps({"visits": visits}))
    log.info("Visit counter updated to %s", visits)

    return jsonify(
        app=os.environ.get("APP_NAME"),
        environment=os.environ.get("APP_ENV"),
        secret_loaded=True,
        visits=visits,
        time=datetime.now(timezone.utc).isoformat(),
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
