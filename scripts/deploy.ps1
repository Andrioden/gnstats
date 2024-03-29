Read-Host -Prompt "You are about to deploy - press any key to continue"

"Generate requirements.txt"
pipenv requirements | Out-File -Encoding UTF8 requirements.txt

"Deploying to google cloud"
& gcloud app deploy app.yaml --project game-night-stats --quiet

Read-Host -Prompt "Finished deployment - press any key to exit"