$ngrok_path = "C:\bin\ngrok.exe"

"Starting tunnel using $ngrok_path"
& $ngrok_path http 11080 -host-header="localhost:11080"

Read-Host -Prompt "Tunnel stopped - press enter to exit"