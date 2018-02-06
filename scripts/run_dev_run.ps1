$DevAppserverPath = "C:\Users\andre\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\dev_appserver.py"

& python $DevAppserverPath --host=0.0.0.0 --enable_host_checking=false "..\app.yaml"