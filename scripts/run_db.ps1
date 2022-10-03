docker run `
    --name datastore-db `
    --rm `
    -p 8001:8001 `
    google/cloud-sdk:emulators gcloud `
        --project=gnstats-dev beta emulators datastore start `
        --host-port 0.0.0.0:8001 `
        --no-store-on-disk