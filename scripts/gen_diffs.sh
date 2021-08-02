#! /bin/bash

set -e

git rev-parse HEAD >> commit.txt
git rev-parse --short HEAD >> short_commit.txt

commit=$(cat commit.txt)

echo "Commit:   $commit"
echo "Base:     ${BASE_BRANCH}"
if [[ ! -z "$PR_NUMBER" ]]; then
  echo "Pull Request: #${PR_NUMBER}"
fi

git config user.email "<>"
git config user.name "git"
git remote add origin ${BASE_REPO_PULL}
git remove -vv

