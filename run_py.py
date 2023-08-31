#!/bin/python
import subprocess

playbook_path = "/home/admin/ansible/facts.yml"

try:
    subprocess.run(["ansible-playbook", playbook_path], check=True)
    print(f"Ansible playbook '{playbook_path}' executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error running Ansible playbook: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

