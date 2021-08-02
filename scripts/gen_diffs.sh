#! /bin/bash

set -e

git rev-parse HEAD >> commit.txt
git rev-parse --short HEAD >> short_commit.txt

commit=$(cat commit.txt)

echo "Commit:   $commit"
echo "Base:     ${BASE_BRANCH}"

