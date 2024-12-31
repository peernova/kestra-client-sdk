#!/bin/sh

VERSION=$1

BASE_PKG=io.kestra.api.sdk

# Generate Java SDK
docker run --rm   -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/kestra-ee.yml -g java -o /local/java-sdk --skip-validate-spec \
    --library apache-httpclient --global-property=apiTests=false,modelTests=false \
    --invoker-package $BASE_PKG.internal --model-package $BASE_PKG.model --api-package $BASE_PKG.api \
    --group-id io.kestra --artifact-id kestra-api-client --artifact-version $VERSION
