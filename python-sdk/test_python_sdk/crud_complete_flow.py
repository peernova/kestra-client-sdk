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
flow_id = 'getting_started'
namespace = 'company.team'
body = f"""
id: {flow_id}
namespace: {namespace}

description: Let's `write` some **markdown**

labels:
  team: data
  owner: kestrel
  project: falco
  environment: dev
  country: US

inputs:
  - id: user
    type: STRING
    required: false
    defaults: Kestrel
    description: This is an optional input — if not set at runtime, it will use the default value Kestrel

  - id: run_task
    type: BOOL
    defaults: true

  - id: pokemon
    type: MULTISELECT
    displayName: Choose your favorite Pokemon
    description: You can pick more than one!
    values:
      - Pikachu
      - Charizard
      - Bulbasaur
      - Psyduck
      - Squirtle
      - Mewtwo
      - Snorlax
    dependsOn:
      inputs:
        - run_task
      condition: "{{ inputs.run_task }}"

  - id: bird
    type: SELECT
    displayName: Choose your favorite Falco bird
    values:
      - Kestrel
      - Merlin
      - Peregrine Falcon
      - American Kestrel
    dependsOn:
      inputs:
        - user
      condition: "{{ inputs.user == 'Kestrel' }}"

variables:
  first: 1
  second: "{{ vars.first }} < 2"

tasks:
  - id: hello
    type: io.kestra.plugin.core.log.Log
    description: this is a *task* documentation
    message: |
      The variables we used are {{ vars.first }} and {{ render(vars.second) }}.
      The input is {{ inputs.user }} and the task was started at {{ taskrun.startDate }} from flow {{ flow.id }}.

  - id: run_if_true
    type: io.kestra.plugin.core.debug.Return
    format: Hello World!
    runIf: "{{ inputs.run_task }}"

  - id: fallback
    type: io.kestra.plugin.core.debug.Return
    format: fallback output

finally:
  - id: finally_log
    type: io.kestra.plugin.core.log.Log
    message: "This task runs after all the tasks are run, irrespective of whether the tasks ran successfully or failed. Execution {{ execution.state }}" # Execution RUNNING

afterExecution:
  - id: afterExecution_log
    type: io.kestra.plugin.core.log.Log
    message: "This task runs after the flow execution is complete. Execution {{ execution.state }}" # Execution FAILED / SUCCESS

outputs:
  - id: flow_output
    type: STRING
    value: "{{ tasks.run_if_true.state != 'SKIPPED' ? outputs.run_if_true.value : outputs.fallback.value }}"

pluginDefaults:
  - type: io.kestra.plugin.core.log.Log
    values:
      level: TRACE

triggers:
  - id: monthly
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "0 9 1 * *" # 1st of each month at 9am
"""

api_response = api_client.flows.create_flow(
    tenant,
    body
)
print(api_response)

api_response = api_client.flows.get_flow(
    id=flow_id,
    namespace=namespace,
    tenant=tenant,
    allow_deleted=False,
    source=False
)

print(api_response)


api_response = api_client.flows.delete_flow(
    id=flow_id,
    namespace=namespace,
    tenant=tenant,
)

print(api_response)

