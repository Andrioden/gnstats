import os

os.environ["DATASTORE_DATASET"] = "gnstats-dev"
os.environ["DATASTORE_EMULATOR_HOST"] = "localhost:8001"

# $env:DATASTORE_DATASET='gnstats-dev'
# $env:DATASTORE_EMULATOR_HOST='localhost:8001'

# print("lol")
# for i, j in os.environ.items():
#     if "DATASTORE" in i:
#         print(i, j)