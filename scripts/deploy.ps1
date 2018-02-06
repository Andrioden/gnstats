"Deploying to google cloud"
& gcloud app deploy ../app.yaml --project game-night-stats --quiet

Read-Host -Prompt "Finished deployment - press enter to exit"