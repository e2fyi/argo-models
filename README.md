# argo-models

[![Build Status](https://travis-ci.org/e2fyi/argo-models.svg?branch=master)](https://travis-ci.org/e2fyi/argo-models)
[![PyPI version](https://badge.fury.io/py/argo-models.svg)](https://badge.fury.io/py/argo-models)
[![Downloads](https://pepy.tech/badge/argo-models/month)](https://pepy.tech/project/argo-models/month)

`argo-models` is a `argo` namespaced package with the `argo.models` subpackage
which contains the generated OpenAPI models from [Argo](https://github.com/argoproj/argo).

Documentations can be found at https://argo-models.readthedocs.io/en/latest/

```bash
pip install argo-models
```

```py
from argo.models import V1alpha1ArtifactLocation, V1alpha1S3Artifact
from kubernetes.client.models import V1SecretKeySelector

# create aws cred
access_key_secret = V1SecretKeySelector(name="s3_secret", key="accesskey")
secret_key_secret = V1SecretKeySelector(name="s3_secret", key="secretkey")

# create artifact config for s3
s3_artifact = V1alpha1S3Artifact(
    bucket="foobar",
    endpoint="s3.amazonaws.com"
    insecure=False,
    access_key_secret=access_key_secret,
    secret_key_secret=secret_key_secret,
    key=""
)

# create artifact location
artifact_location = V1alpha1ArtifactLocation(s3=s3_artifact)

```

## Developer notes

To generate the latest models, update `version.txt` with the desired argo release
(e.g. `2.3.0-rc3`) and then run `./generate-api.sh`.

To release new version to pypi, create a release with the corresponding version tag (e.g. `v2.2.1`). Travis will automatically publish the package.

> NOTE:
>
> `version.txt` should hold the current/latest argo version to be generated, as it
> is also used by `setup.py` as the `argo-models` package version.
>
> Please install [@openapitools/openapi-generator-cli](https://www.npmjs.com/package/@openapitools/openapi-generator-cli) to
> generate the openapi specs.

## License

This package is licensed under [Apache-2.0](./LICENSE) and is a derivative of the [Argo project](https://github.com/argoproj/argo) using [OpenAPI generator](https://github.com/OpenAPITools/openapi-generator).
