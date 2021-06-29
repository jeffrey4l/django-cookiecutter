#!/usr/bin/env bash

set -xe

workspace=$1

echo $workspace
rm -rf $workspace/project_a
cookiecutter . project_slug=project_a project_name="Project A" author_name="MyName" --no-input -o $workspace

pushd $workspace/project_a
echo $(pwd)

tox -epep8 -vvv
tox -edocs
