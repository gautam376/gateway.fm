# Gateway.fm – Technical Assignment (Junior Node Operator)

Thank you for reviewing my submission for the Junior Node Operator role. This repository contains solutions to all tasks outlined in the technical assignment. The work demonstrates hands-on experience with Ethereum infrastructure, scripting, containerization, monitoring, and automation.

---



##  Task Summary

### 1.  Basic Linux Knowledge
- File: `Task1-BasicLinux/answers.md`
- Includes Linux commands for:
  - Listing Ethereum processes
  - Curling RPC endpoint
  - File permission change
  - File ownership change
  - Filtering error logs from systemd

---

### 2.  Ethereum Node on Hoodi Testnet
- Directory: `Task2-HoodiNode/`
- Includes:
  - `docker-compose.yml`
  - Instructions to run and verify the setup (`instructions.md`)
  - Node logs and screenshot (`nethermind.log`, `screenshot.png`)
  - Example data directory structure

---

### 3. Calling JSON-RPC Endpoint
- File: `Task3-RPCCall/check_sync.py`
- Description: Python script to call `eth_syncing` RPC method
- Output saved to: `Task3-RPCCall/output.txt`

---

### 4.  Node Health Checker
- File: `Task4-NodeChecker/check_nodes.py`
- Reads URLs from `nodes.txt` and checks for HTTP 200
- Output written to `report.txt`

---

### 5.  Bonus: Ansible Automation
- Directory: `BonusTask-Ansible/`
- Automates deployment of Ethereum node to remote server using Ansible
- Includes:
  - `inventory.ini`
  - `playbook.yml`
  - Role-based structure with Docker Compose deployment
  - `README.md` with usage instructions

---

##  Requirements

- Python 3.x
- Docker & Docker Compose
- Ansible (for Bonus Task)
- Ubuntu server with SSH access (for Bonus Task testing)

---

##  How to Use

Clone the repo and navigate into each task's folder.  
Follow the `README.md` or instructions provided per task.











### 1.  Screenshots of the Tasks





Result of Task -2 
![WhatsApp Image 2025-06-19 at 18 01 46_c88c361c](https://github.com/user-attachments/assets/483e1f2a-c4be-49a2-b2df-59a04073c5be)









Result of Task -3
![WhatsApp Image 2025-06-19 at 17 58 28_0b905bc4](https://github.com/user-attachments/assets/f00eeb71-4f30-4f4b-a383-bfcc024c902c)
 



















Result of Task -4

![WhatsApp Image 2025-06-19 at 17 45 25_cc0acc24](https://github.com/user-attachments/assets/c2821e09-bff1-4881-b63b-ca5ae413208b)

