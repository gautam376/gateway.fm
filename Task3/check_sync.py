import requests
import json

# RPC endpoint of the Ethereum node
url = "http://localhost:8545"

# RPC request payload for eth_syncing
payload = {
    "jsonrpc": "2.0",
    "method": "eth_syncing",
    "params": [],
    "id": 1
}

try:
    # Send the HTTP POST request to the JSON-RPC endpoint
    response = requests.post(url, json=payload)

    # Parse the response JSON
    result = response.json()

    # Print the output (and write to file)
    print("RPC Response:")
    print(json.dumps(result, indent=4))

    # Save to output.txt for submission
    with open("output.txt", "w") as f:
        json.dump(result, f, indent=4)

except Exception as e:
    print("Error occurred while calling RPC:", str(e))
