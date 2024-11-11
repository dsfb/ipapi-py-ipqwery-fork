from pydantic import BaseModel, Field
from typing import Optional

class ISPInfo(BaseModel):
    asn: Optional[str] = None
    org: Optional[str] = None
    isp: Optional[str] = None

class LocationInfo(BaseModel):
    country: Optional[str] = None
    country_code: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipcode: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    timezone: Optional[str] = None
    localtime: Optional[str] = None

class RiskInfo(BaseModel):
    is_mobile: Optional[bool] = None
    is_vpn: Optional[bool] = None
    is_tor: Optional[bool] = None
    is_proxy: Optional[bool] = None
    is_datacenter: Optional[bool] = None
    risk_score: Optional[int] = None

class IPInfo(BaseModel):
    ip: str
    isp: Optional[ISPInfo] = None
    location: Optional[LocationInfo] = None
    risk: Optional[RiskInfo] = None
