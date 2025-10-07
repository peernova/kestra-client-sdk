from kestrapy import KestraClient, Configuration
import json

from kestrapy.exceptions import UnprocessableEntityException


def kestra_client():
    configuration = Configuration()
    configuration.host = "http://localhost:8080"
    configuration.username = "root@root.com"
    configuration.password = "Root!1234"

    return KestraClient(configuration)


api_client = kestra_client()


tenant = 'main'
flow_id = 'sdk-flow-with-label'
namespace = 'demo'
body = f"""
id: {flow_id}
namespace: {namespace}

tasks:
  - id: hello
    type: io.kestra.plugin.core.log.Log
    message: Hello from the SDK! 👋
"""

api_response = api_client.flows.create_flow(
    tenant,
    body
)
print(api_response)

api_response = api_client.executions.create_execution(
    namespace=namespace,
    id=flow_id,
    wait=False,
    tenant=tenant
)

print(api_response)
