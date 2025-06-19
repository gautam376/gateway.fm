1. How do you list all running processes that contain the word "ethereum"? 
ans : ps aux | grep ethereum

2. Write a command to fetch the contents of http://localhost:8545 using curl. 
Ans : curl http://localhost:8545

3. Change permissions of a file node.sh to make it executable by everyone.
Ans : chmod +x node.sh

4. How do you change ownership of ethereum.log file to the user ethuser?
Ans : chown ethuser ethereum.log 

5. Show how to filter logs containing "error" from systemd logs using journalctl.
Ans : journalctl | grep -i error