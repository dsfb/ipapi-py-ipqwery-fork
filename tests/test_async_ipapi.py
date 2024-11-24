import pytest
from ipapi.client import AsyncIPAPIClient

@pytest.fixture
def async_client():
    return AsyncIPAPIClient()

async def test_async_query_ip(async_client: AsyncIPAPIClient):
    ip_info = await async_client.query_ip("8.8.8.8")
    assert ip_info.ip == "8.8.8.8"
    assert ip_info.location is not None

async def test_async_query_own_ip(async_client: AsyncIPAPIClient):
    ip = await async_client.query_own_ip()
    assert isinstance(ip, str)
    assert len(ip) > 0

async def test_async_query_bulk(async_client: AsyncIPAPIClient):
    ips = ["8.8.8.8", "1.1.1.1"]
    ip_infos = await async_client.query_bulk(ips)
    assert len(ip_infos) == 2
    assert ip_infos[0].ip == "8.8.8.8"
