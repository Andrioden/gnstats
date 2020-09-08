$ngrok_path = "C:\bin\ngrok.exe"

"Starting tunnel using $ngrok_path"
& $ngrok_path http 8080 -host-header="localhost:8080"

Read-Host -Prompt "Tunnel stopped - press enter to exit"