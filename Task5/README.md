# Bonus Task: Ansible-Based Ethereum Node Deployment

This playbook sets up a Nethermind Ethereum execution node connected to the **Hoodi testnet** on a remote Ubuntu server using Docker Compose.

## Remote Server Details
- IP: 192.168.56.101
- OS: Ubuntu 22.04 LTS
- Access: SSH using key at ~/.ssh/id_rsa

## Requirements
- Ansible installed locally (`sudo apt install ansible`)
- SSH access to the server
- Docker and Docker Compose will be installed automatically

## How to Run

```bash
ansible-playbook -i inventory.ini playbook.yml
