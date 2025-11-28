from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LookupAddressInput(_message.Message):
    __slots__ = ("ip_address", "secret")
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    ip_address: str
    secret: str
    def __init__(self, ip_address: _Optional[str] = ..., secret: _Optional[str] = ...) -> None: ...

class LookupAddressOutput(_message.Message):
    __slots__ = ("latitude", "longitude", "country", "timezone", "postcode", "city", "region")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    POSTCODE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    country: str
    timezone: str
    postcode: str
    city: str
    region: str
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., country: _Optional[str] = ..., timezone: _Optional[str] = ..., postcode: _Optional[str] = ..., city: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...
