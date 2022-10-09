import json
import os

from google.cloud.secretmanager import SecretManagerServiceClient


def load_gcloud_secrets_into_env() -> None:
    sec = os.environ["SECRET_ENV"]
    secret_client = SecretManagerServiceClient()
    secret_payload: str = secret_client.access_secret_version(name=sec).payload.data.decode("UTF-8")
    for key, val in json.loads(secret_payload).items():
        os.environ[key] = val
