#! /bin/bash

pulumi login gs://intrepid-memory-321513-state
pulumi config set gcp:project intrepid-memory-321513
pulumi config set gcp:region northamerica-northeast1
pulumi version
