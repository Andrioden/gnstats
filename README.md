## Getting started

1. Setup python env
   1. Install python 3.9.X
   2. `pip install pipenv`
   3. `pipenv install --dev`
2. Run local db
   1. Install Docker Desktop with WSL2
   2. Run db `.\scripts\run_db.ps1`
3. (Optional) Run local db admin
   1. Run db admin `.\scripts\run_db_admin.ps1`
   2. [Open db admin](http://localhost:8080)
4. Add secrets 
   1. Copy and rename`.\scripts\env_secrets_example.ps1` to `env_secrets.ps1`
   2. Get values from André and set them in the file
5. Run `.\scripts\run_web.ps1`
6. (Verify) [Open page](http://localhost:8000/)
7. (Verify) [Open api](http://localhost:8000/docs)
8. (Verify) Run tests `pytest .`
    - Take note tests may randomly fail, probably because of the local datastore returning stale values in integration tests, or because of a bug in the db context yielding
9. (Optional) Setup pre-commit: `cp pre-commit.sh .git/hooks/pre-commit`


## Import prod data to local db

1. Run `.\scripts\populate.ps1`


## Relevant links

- Backend
  - [Gcloud OAuth Credentials](https://console.cloud.google.com/apis/credentials?project=game-night-stats)
  - [Gcloud db backup job](https://console.cloud.google.com/cloudscheduler?referrer=search&hl=NO&project=game-night-stats)
  - Web framework: https://fastapi.tiangolo.com/
  - Database framework: https://googleapis.dev/python/python-ndb/latest/index.html
  - Datastore admin: https://github.com/remko/dsadmin
- Frontend
  - Framework: https://angularjs.org/
  - UI components: https://material.angularjs.org/latest/
  - Icons: http://google.github.io/material-design-icons/
