from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.commerce import price_pb2 as _price_pb2
from eolymp.community import tier_pb2 as _tier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeTierInput(_message.Message):
    __slots__ = ["locale", "render", "tier_id"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    TIER_ID_FIELD_NUMBER: _ClassVar[int]
    locale: str
    render: bool
    tier_id: str
    def __init__(self, tier_id: _Optional[str] = ..., render: bool = ..., locale: _Optional[str] = ...) -> None: ...

class DescribeTierOutput(_message.Message):
    __slots__ = ["tier"]
    TIER_FIELD_NUMBER: _ClassVar[int]
    tier: _tier_pb2.Tier
    def __init__(self, tier: _Optional[_Union[_tier_pb2.Tier, _Mapping]] = ...) -> None: ...

class ListTierPricesInput(_message.Message):
    __slots__ = ["currency", "tier_id"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TIER_ID_FIELD_NUMBER: _ClassVar[int]
    currency: str
    tier_id: str
    def __init__(self, tier_id: _Optional[str] = ..., currency: _Optional[str] = ...) -> None: ...

class ListTierPricesOutput(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    def __init__(self, items: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]] = ...) -> None: ...

class ListTiersInput(_message.Message):
    __slots__ = ["locale", "offset", "render", "size"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    locale: str
    offset: int
    render: bool
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., render: bool = ..., locale: _Optional[str] = ...) -> None: ...

class ListTiersOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_tier_pb2.Tier]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_tier_pb2.Tier, _Mapping]]] = ...) -> None: ...
