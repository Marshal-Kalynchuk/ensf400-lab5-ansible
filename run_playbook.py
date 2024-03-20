import ansible_runner

# Run the hello.yml playbook
import os

hello_yml_path = os.path.join(os.path.dirname(__file__), 'hello.yml')
host_yml_path = os.path.join(os.path.dirname(__file__), 'hosts.yml')
result = ansible_runner.run(playbook=hello_yml_path, inventory=host_yml_path)

# Print the results
print("Playbook Results:")
for host, res in result.stats.items():
    print(f"{host}: {res}")

import ansible_runner

# Read and verify the response of the NodeJS servers
print("\nVerifying NodeJS server responses:")
for port in [3000, 3001, 3002]:
    response = ansible_runner.run(
        inventory=host_yml_path,
        module='uri',
        module_args=f"url=http://localhost:{port} return_content=yes",
        host_pattern='localhost'
    )
    # Find the event with the 'runner_on_ok' event type and extract the content
    content = 'No response'
    for event in response.events:
        if event['event'] == 'runner_on_ok':
            content = event['event_data']['res'].get('content', 'No response')
            break
    print(f"Response from server on port {port}: {content}")
