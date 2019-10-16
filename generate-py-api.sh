#!/bin/bash
set -e

if [ "$#" -gt 0 ]; then
  ARGO_VERSION=$1
else
  ARGO_VERSION=$(cat version.txt)
fi

# remove tmp files
if [[ -f tmp ]]; then
  echo "empty tmp/ folder"
  rm -r tmp
fi

# create required folders
mkdir -p tmp
mkdir -p argo/models

# download swagger
./download-swagger.sh $ARGO_VERSION

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
rm -r python/argo/models

# copy generated models 
echo "updating with new model objects"
cp -r tmp/py/argo/models python/argo/models

# rename k8s dependencies
echo "renaming k8s objects in argo objects"
docker run --rm -ti \
    -v $PWD/python/argo/models:/models:rw \
    bash:latest \
    find models/ -type f -exec sed -i s/IoK8sApiCore/kubernetes.client.models./g {} \; 