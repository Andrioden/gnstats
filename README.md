## Getting started
1. Setup python env
   1. Install python 3.9.X
   2. `pip install pipenv`
   3. `pipenv install --dev`
2. Run local db
   1. Install Docker Desktop med WSL2
   2. Run db `docker run --name datastore-db --rm -p 8001:8001 google/cloud-sdk:emulators gcloud --project=gnstats-dev beta emulators datastore start --host-port 0.0.0.0:8001 --no-store-on-disk`
3. (Optional) Run local db admin
   1. Run db admin `docker run --name datastore-admin -p 8002:8080 ghcr.io/remko/dsadmin:latest --project=gnstats-dev --datastore-emulator-host=host.docker.internal:8001`
   2. [Open db admin](http://localhost:8002)
4. Copy and rename config_hidden_example.py to config_hidden.py
5. Run `.\scripts\run_dev.ps1`
6. (Verify) [Open page](http://127.0.0.1:8000/static/index.html)
7. (Verify) [Open api](http://127.0.0.1:8000/docs)
8. (Verify) Run tests `pytest .`


## Using prod data
1. As logged in admin run `[PROD_URL]/api/actions/admin/dataimportpythonscript/`
2. Copy paste data into `api/actions_admin.py > RunImportPythonScriptHandler`
3. As admin run `[LOCAL_URL]/api/actions/admin/runimportpythonscript/`
4. To verify delete an existing Person entity and reverify in the menu


## Libs
- Backend
  - Web framework: https://fastapi.tiangolo.com/
  - Database framework: https://googleapis.dev/python/python-ndb/latest/index.html
- Frontend
  - Framework: https://angularjs.org/
  - UI components: https://material.angularjs.org/latest/
  - Icons: http://google.github.io/material-design-icons/
