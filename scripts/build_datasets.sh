#! /bin/bash

pulumi login gs://intrepid-memory-321513-state
pulumi stack select dev -c --secrets-provider=test
pulumi config set gcp:project intrepid-memory-321513
pulumi config set gcp:region northamerica-northeast1
pulumi version
export PULUMI_CONFIG_PASSPHRASE=test
pulumi up --yes
