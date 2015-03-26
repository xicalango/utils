#!/bin/bash

set -e

function print_usage() {
  echo Usage:
  echo "$0 project_directory [additional_directories]"
}


PROJECT_DIRS=(documents code misc)

PROJECT_ROOT="$1"

shift

ADDITIONAL_DIRS="$*"

if [[ -z ${PROJECT_ROOT} ]]; then
  print_usage
  exit 1
fi

if [[ -a ${PROJECT_ROOT} ]]; then
  echo Directory already exists: ${PROJECT_ROOT}
  exit 1
fi

echo Creating ${PROJECT_ROOT}
mkdir ${PROJECT_ROOT}

for dir in ${PROJECT_DIRS[@]}; do
  NEW_DIR=${PROJECT_ROOT}/${dir}
  echo Creating ${NEW_DIR}
  mkdir -p "${NEW_DIR}"
done


for dir in ${ADDITIONAL_DIRS}; do
  NEW_DIR=${PROJECT_ROOT}/${dir}
  echo Creating ${NEW_DIR}
  mkdir -p "${NEW_DIR}"
done

cd ${PROJECT_ROOT}
echo ${PROJECT_ROOT} > README.md
echo "==============" >> README.md

git init
git add README.md
git commit -m"Initial commit for ${PROJECT_ROOT}"

echo Project structure in ${PROJECT_ROOT} created.

