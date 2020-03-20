#!/bin/bash
set -e

ARGO_VERSION=$(cat version.txt)

# remove tmp files
if [[ -f tmp ]]; then
  echo "empty tmp/ folder"
  rm -r tmp
fi

# create required folders
mkdir -p tmp
mkdir -p argo/models

# download swagger
./download-swagger.sh

# remove project prefix
echo "removing argo project prefix from openapi spec"
sed s/io.argoproj.workflow.//g openapi-spec/argo-$ARGO_VERSION.json > tmp/swagger.json

# generate python openapi models
echo "starting openapi generator (docker)"
# docker run --rm -ti \
#   -v $PWD/tmp/swagger.json:/tmp/swagger.json \
#   -v $PWD/tmp/argo:/tmp/argo:rw \
#   openapitools/openapi-generator-cli \
#     generate \
#         -i /tmp/swagger.json \
#         -g python \
#         -o /tmp/argo \
#         --package-name=argo
openapi-generator \
    generate \
        -i tmp/swagger.json \
        -g python \
        -o tmp/py \
        --package-name=argo

# delete existing models
echo "removing old model objects"
rm -r argo/models

# copy generated models
echo "updating with new model objects"
cp -r tmp/py/argo/models argo/models
cp tmp/py/argo/configuration.py argo/

# rename k8s dependencies
# echo "renaming k8s objects in argo objects"
# docker run --rm -ti \
#     -v $PWD/argo/models:/models:rw \
#     bash:latest \
#     find models/ -type f -exec sed -i s/IoK8sApiCore/kubernetes.client.models./g {} \;

# point k8s models to kubernetes.client.models instead of openapi generated
find argo/models/ -type f -exec sed -i s/IoK8sApiCore/kubernetes.client.models./g {} \;
# some more clean up. Remove k8s models.
python remove-k8s.py
