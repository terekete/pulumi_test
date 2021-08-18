#! /bin/bash

export PULUMI_CONFIG_PASSPHRASE=test

pulumi login gs://intrepid-memory-321513-state
pulumi stack select default -c --secrets-provider=test
pulumi config set gcp:project intrepid-memory-321513
pulumi config set gcp:region northamerica-northeast1
pulumi version
pulumi refresh --yes --skip-preview --suppress-outputs
pulumi up --yes --skip-preview --suppress-outputs
