import os

# Needed for local datastore
os.environ["DATASTORE_DATASET"] = "gnstats-dev"
os.environ["DATASTORE_EMULATOR_HOST"] = "localhost:8001"
