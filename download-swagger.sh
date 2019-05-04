#!/bin/bash
set -e

ARGO_VERSION=$(cat version.txt)

echo "Downloading openapi spec for Argo($ARGO_VERSION)."

# download and untar
wget -qO- https://github.com/argoproj/argo/archive/v$ARGO_VERSION.tar.gz | tar xz

# get openapi spec
mkdir -p openapi-spec
cp argo-$ARGO_VERSION/api/openapi-spec/swagger.json openapi-spec/argo-$ARGO_VERSION.json

# remove directory
rm -r argo-$ARGO_VERSION

echo "Downloaded: openapi-spec/argo-$ARGO_VERSION.json"