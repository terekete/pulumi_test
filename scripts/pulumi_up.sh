#! /bin/bash

pulumi login gs://intrepid-memory-321513-state

export PULUMI_CONFIG_PASSPHRASE=test

# pulumi stack select dev -c --secrets-provider=test
# pulumi config set gcp:project intrepid-memory-321513
# pulumi config set gcp:region northamerica-northeast1
# pulumi version
# pulumi refresh --yes
# pulumi up --yes

python3 /workspace/__main__.py