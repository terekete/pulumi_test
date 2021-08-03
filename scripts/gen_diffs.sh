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

git fetch origin "${BASE_BRANCH}":base-branch
git checkout base-branch
git diff --name-only feature...base-branch > POTENTIAL_CONFLICTS.txt
git merge --no-ff feature
git status


#! /bin/bash
BUILD_DIFF_FILE="build-diff-file.txt"
DIFF=$(git diff --name-only origin/"${BASE_BRANCH}"...HEAD)

DIFF_TEAMS=""


for file in $DIFF
do
  if [[ "$file" =~ ^teams/[^/]*/[^/]*/ ]]
  then
    echo "REMATCH[0]: ${BASH_REMATCH[0]}"
    echo "REMATCH[1]: ${BASH_REMATCH[1]}" 
    DIFF_TEAMS+="${BASH_REMATCH[0]}\n"
  fi
done

printf "${DIFF_TEAMS}" | sort | uniq > DIFF_TEAMS.txt

cat DIFF_TEAMS.txt > DIFF_TOTAL.txt

touch CONFLICTS.txt
cat POTENTIAL_CONFLICTS.txt | while read file
do
  cat DIFF_TOTAL.txt | while read diff_path
  do
    if [[ $file =~ $diff_path ]]; then
      echo $file >> CONFLICTS.txt
    fi
  done
done

if [[ -s DIFF_TEAMS.txt ]]; then
  printf "\n*** Change occured on team definition ***\n"
  cat DIFF_TEAMS.txt
fi

if [[ -s CONFLICTS.txt ]]; then
  echo ""
  echo "Warning - there are conflicting changes in the base branch."
  echo "The following files have been changed in the base:"
  cat CONFLICTS.txt
fi
