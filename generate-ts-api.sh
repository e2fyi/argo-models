#!/bin/bash
set -e

if [ "$#" -gt 0 ]; then
  ARGO_VERSION=$1
else
  ARGO_VERSION=$(cat version.txt)
fi

if ! [ -x "$(command -v openapi-generator)" ]; then
  echo "installing openapi-generator-cli"
  npm install @openapitools/openapi-generator-cli -g
fi

# remove tmp files
if [[ -f tmp ]]; then
  echo "empty tmp/ folder"
  rm -r tmp
fi

# create required folders
mkdir -p tmp
mkdir -p ts/argo/models

# download swagger
./download-swagger.sh $ARGO_VERSION

# remove project prefix
echo "removing argo project prefix from openapi spec"
sed s/io.argoproj.workflow.//g openapi-spec/argo-$ARGO_VERSION.json > tmp/swagger.json

# generate python openapi models
echo "starting openapi generator (docker)"
# docker run --rm -ti \
#   -v $PWD/tmp/swagger.json:/tmp/swagger.json \
#   -v $PWD/tmp/ts/argo:/tmp/argo:rw \
#   openapitools/openapi-generator-cli \
#     generate \
#         -i /tmp/swagger.json \
#         -g typescript-node \
#         -o /tmp/argo \
#         --package-name=argo
openapi-generator \
    generate \
        -i tmp/swagger.json \
        -g typescript-node \
        -o tmp/ts/argo \
        --package-name=argo

# delete existing models
echo "removing old model objects"
rm -r typescript/argo/model

# copy generated models 
echo "updating with new model objects"
cp -r tmp/ts/argo/model typescript/argo/model

# rename k8s dependencies
echo "renaming k8s objects in argo objects"
# docker run --rm -ti \
#    -v $PWD/argo/models:/models:rw \
#    bash:latest \
#    find models/ -type f -exec sed -i s/IoK8sApiCore/kubernetes.client.models./g {} \; 