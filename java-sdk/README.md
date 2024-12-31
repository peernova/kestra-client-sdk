# kestra-api-client

The class [KestraClient](src/main/java/io/kestra/api/sdk/KestraClient.java) is the entry point of the SDK and the only class that is not generated.

After generation, it can happen that some classes didn't compile anymore due to a wrong `Schema` import.
In this case, the import should be replaced by `io.kestra.api.sdk.model.Schema` manually.

Version is incremented manually.

Gradle is used to package this client:

```shell
# Build
gradle jar

# Publish locally
gradle publishToMavenLocal
```
