import yaml
import ansible_runner
import os

host_yml_path = os.path.join(os.path.dirname(__file__), 'hosts.yml')
# Load the inventory file
with open(host_yml_path, 'r') as file:
    inventory = yaml.safe_load(file)

# Print the names, IP addresses, and group names of all hosts
for group, group_data in inventory.items():
    if 'hosts' in group_data:
        for host, host_data in group_data['hosts'].items():
            ip = host_data.get('ansible_host', 'N/A')
            print(f"Name: {host}, IP: {ip}, Groups: {group}")

            # Ping the host
            response = ansible_runner.run(
                inventory=host_yml_path,
                host_pattern=host,
                module='ping'
            )
            # Output the ping results
            if response.status == 'successful':
                print(f"{host} ping: SUCCESS")
            else:
                print(f"{host} ping: FAILED")
