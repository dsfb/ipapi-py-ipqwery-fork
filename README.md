# ipquery

A Python library to query IP addresses using the [ipquery.io](https://ipquery.io) API. This library allows you to easily retrieve detailed information about IP addresses, including ISP data, geolocation details, and risk analysis.

## Features

- Query detailed information for a specific IP address.
- Fetch your own public IP address.
- Perform bulk queries for multiple IP addresses.
- Includes Pydantic models for easy data validation and parsing.

## Installation

Install the package using pip:

```bash
pip install ipcore
```

## Usage

### Importing the Package

```python
from ipapi.client import IPAPIClient
```

### Query a Specific IP Address

Fetch information about a specific IP address:

#### Synchronously

```python
from ipapi.client import IPAPIClient

client = IPAPIClient()
ip_info = client.query_ip("8.8.8.8")
print(ip_info)
```

#### Asychronously

```python
from ipapi.client import AsyncIPAPIClient

async def main():
    client = AsyncIPAPIClient()
    ip_info = await client.query_ip("8.8.8.8")
    print(ip_info)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

#### Example Output:
```
IPInfo(ip='8.8.8.8', isp=ISPInfo(asn='AS15169', org='Google LLC', isp='Google LLC'),
location=LocationInfo(country='United States', country_code='US', city='Mountain View',
state='California', zipcode='94035', latitude=37.386, longitude=-122.0838, timezone='America/Los_Angeles', localtime='2024-11-09T12:45:32'),
risk=RiskInfo(is_mobile=False, is_vpn=False, is_tor=False, is_proxy=False, is_datacenter=True, risk_score=0))
```

### Fetch Your Own Public IP Address

Retrieve your machine's public IP address:

```python
ip = client.query_own_ip()
print(f"Your IP: {ip}")
```

#### Example Output:
```
Your IP: 203.0.113.45
```

### Bulk Query Multiple IP Addresses

Fetch details for multiple IP addresses in a single request:

```python
ips = ["8.8.8.8", "1.1.1.1"]
results = client.query_bulk(ips)
for ip_info in results:
    print(ip_info)
```

#### Example Output:
```
IPInfo(ip='8.8.8.8', ...)
IPInfo(ip='1.1.1.1', ...)
```

## Running Tests

If you want to run tests to verify functionality:

```bash
pytest tests/
```

## Requirements

- Python 3.7+
- Pydantic 2.x
- httpx

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Links

- [GitHub Repository](https://github.com/ipqwery/ipapi-py)
- [PyPI Project Page](https://pypi.org/project/ipcore/)
