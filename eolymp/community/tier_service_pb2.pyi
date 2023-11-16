from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import tier_pb2 as _tier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeTierInput(_message.Message):
    __slots__ = ["pricing_country", "tier_id"]
    PRICING_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    TIER_ID_FIELD_NUMBER: _ClassVar[int]
    pricing_country: str
    tier_id: str
    def __init__(self, tier_id: _Optional[str] = ..., pricing_country: _Optional[str] = ...) -> None: ...

class DescribeTierOutput(_message.Message):
    __slots__ = ["tier"]
    TIER_FIELD_NUMBER: _ClassVar[int]
    tier: _tier_pb2.Tier
    def __init__(self, tier: _Optional[_Union[_tier_pb2.Tier, _Mapping]] = ...) -> None: ...

class ListTiersInput(_message.Message):
    __slots__ = ["offset", "pricing_country", "size"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PRICING_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    pricing_country: str
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., pricing_country: _Optional[str] = ...) -> None: ...

class ListTiersOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_tier_pb2.Tier]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_tier_pb2.Tier, _Mapping]]] = ...) -> None: ...
