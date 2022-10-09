from utils.secrets import load_gcloud_secrets_into_env

# Load secrets from google cloud secret manager
load_gcloud_secrets_into_env()

# Then expose app to the outside
from api.app import app  # noqa
