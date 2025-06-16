# JavaScript SDK

## Steps to generate the SDK



## Step to use

The openapi generator will generate 1 Api per controller, so we create a custom Kestra Client that need to be instantiated once for every API.
Use the `import {KestraClient} from "kestra_api";` manually written that gather everything in one client.

Then you can instantiate the client with the following code:

```javascript
const kestraClient = new KestraClient(host, token, username, password);
 ```

Then simply use the client to call the API:

```javascript
kestraClient.flowsApi.searchFlows()
```

Each method of the API will expect a callback with the following signature:

```javascript
callback (error, data, response)
```