import os

# Needed for local datastore
os.environ["DATASTORE_DATASET"] = "gnstats-dev"
os.environ["DATASTORE_EMULATOR_HOST"] = "localhost:8001"

# Needed to avoid that app init crash
os.environ["SECRET_KEY"] = "not-set"
