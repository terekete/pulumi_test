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
git remote | xargs -n1 git remote remove
git remote add origin ${BASE_REPO_URL}
git remote -vv

{
  git branch -D base-branch
} || {
  echo "continuing ..."
}
{
  git branch -D feature
} || {
  echo "continuing ..."
}

if [[ ! -z "${PR_NUMBER}" ]]; then
  git fetch origin "pull/${PR_NUMBER}/head":feature
  git fetch --unshallow
else
  git branch -m feature
fi

ls -la /root/.ssh/config/
git fetch origin "${BASE_BRANCH}":base-branch
# git checkout base-branch
# git diff --name-only feature...base-branch > POTENTIAL_CONFLICTS.txt

# echo "Potential conflicts: "
# cat POTENTIAL_CONFLICTS.txt