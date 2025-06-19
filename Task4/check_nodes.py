import requests

# Input and output file paths
input_file = "nodes.txt"
output_file = "report.txt"

def check_url_status(url):
    """
    Sends a GET request to the given URL and returns True if status code is 200.
    """
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def main():
    # Open the input file and read all URLs
    with open(input_file, "r") as file:
        urls = [line.strip().strip('<>') for line in file if line.strip()]

    # Open the output file to write the report
    with open(output_file, "w") as report:
        for url in urls:
            status = "UP" if check_url_status(url) else "DOWN"
            report.write(f"{url} - {status}\n")

    print(f"Report generated in {output_file}")

if __name__ == "__main__":
    main()
