import sys
from .client import IPAPIClient

def main():
    client = IPAPIClient()
    if len(sys.argv) > 1:
        ip = sys.argv[1]
        print(client.query_ip(ip))
    else:
        print("Fetching your public IP address...")
        print(client.query_own_ip())

if __name__ == "__main__":
    main()
