## Getting started
1. Setup python env
   1. Install python 3.9.X
   2. `pip install pipenv`
   3. `pipenv install --dev`
2. Run local db
   1. Install Docker Desktop med WSL2
   2. Run db `.\scripts\run_db.ps1`
3. (Optional) Run local db admin
   1. Run db admin `.\scripts\run_db_admin.ps1`
   2. [Open db admin](http://localhost:8002)
4. Add secrets 
   1. Copy and rename`.\scripts\secrets_example.ps1` to `secrets.ps1`
   2. Set values
5. Run `.\scripts\run_dev.ps1`
6. (Verify) [Open page](http://localhost:8000/)
7. (Verify) [Open api](http://localhost:8000/docs)
8. (Verify) Run tests `pytest .`


## Using prod data
1. As logged in admin run `[PROD_URL]/api/actions/admin/dataimportpythonscript/`
2. Copy paste data into `api/actions_admin.py > RunImportPythonScriptHandler`
3. As admin run `[LOCAL_URL]/api/actions/admin/runimportpythonscript/`
4. To verify delete an existing Person entity and reverify in the menu


## Relevant links
- Backend
  - [Google OAuth Credentials](https://console.cloud.google.com/apis/credentials?project=game-night-stats)
  - Web framework: https://fastapi.tiangolo.com/
  - Database framework: https://googleapis.dev/python/python-ndb/latest/index.html
- Frontend
  - Framework: https://angularjs.org/
  - UI components: https://material.angularjs.org/latest/
  - Icons: http://google.github.io/material-design-icons/
