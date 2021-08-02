#! /bin/bash

set -e

git rev-parse HEAD >> commit.txt
git rev-parse --short HEAD >> short_commit.txt

cat commit.txt
