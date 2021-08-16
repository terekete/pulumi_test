#! /bin/bash

export PULUMI_CONFIG_PASSPHRASE=test

cat /workspace/DIFF_LIST.txt

pulumi login gs://intrepid-memory-321513-state
pulumi stack select dev -c --secrets-provider=test
pulumi config set gcp:project intrepid-memory-321513
pulumi config set gcp:region northamerica-northeast1
pulumi version
pulumi refresh --yes
pulumi up --yes
