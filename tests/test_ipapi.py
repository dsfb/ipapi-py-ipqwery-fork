import pytest
from ipapi.client import IPAPIClient

@pytest.fixture
def client():
    return IPAPIClient()

def test_query_ip(client):
    ip_info = client.query_ip("8.8.8.8")
    assert ip_info.ip == "8.8.8.8"
    assert ip_info.location is not None

def test_query_own_ip(client):
    ip = client.query_own_ip()
    assert isinstance(ip, str)
    assert len(ip) > 0

def test_query_bulk(client):
    ips = ["8.8.8.8", "1.1.1.1"]
    ip_infos = client.query_bulk(ips)
    assert len(ip_infos) == 2
    assert ip_infos[0].ip == "8.8.8.8"
