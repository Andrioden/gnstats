docker run `
    --name datastore-admin `
    --rm `
    -p 8002:8080 `
    ghcr.io/remko/dsadmin:latest `
        --project=gnstats-dev `
        --datastore-emulator-host=host.docker.internal:8001