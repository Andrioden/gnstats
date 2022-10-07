$env:DATASTORE_DATASET='gnstats-dev'
$env:DATASTORE_EMULATOR_HOST='localhost:8001'

./scripts/secrets.ps1

uvicorn main_dev:app --reload