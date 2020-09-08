$DevAppserverPath = "C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\dev_appserver.py"

& python $DevAppserverPath --host=0.0.0.0 --enable_host_checking=false --enable_console=true "..\app.yaml"

Read-Host -Prompt "Finished run - press any key to exit"