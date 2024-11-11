import httpx
from .models import IPInfo
from typing import List

BASE_URL = "https://api.ipquery.io/"

class IPAPIClient:
    def __init__(self):
        self.client = httpx.Client(base_url=BASE_URL)

    def query_ip(self, ip: str) -> IPInfo:
        """Fetch information for a specific IP address."""
        response = self.client.get(ip)
        response.raise_for_status()
        return IPInfo.parse_raw(response.text)

    def query_bulk(self, ips: List[str]) -> List[IPInfo]:
        """Fetch information for multiple IP addresses."""
        ip_list = ",".join(ips)
        response = self.client.get(ip_list)
        response.raise_for_status()
        return [IPInfo.parse_obj(item) for item in response.json()]

    def query_own_ip(self) -> str:
        """Fetch the public IP address of the current machine."""
        response = self.client.get("/")
        response.raise_for_status()
        return response.text
