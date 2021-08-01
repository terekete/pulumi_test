#! /bin/bash

ls -la
pwd
docker build -t pulumi:latest /workspace/builder/
docker push --tag gcr.io/intrepid-memory-321513/pulumi:latest
