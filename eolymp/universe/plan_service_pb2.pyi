from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.universe import plan_pb2 as _plan_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribePlanInput(_message.Message):
    __slots__ = ["currency", "extra", "locale", "plan_id"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    currency: str
    extra: _containers.RepeatedScalarFieldContainer[_plan_pb2.Plan.Extra]
    locale: str
    plan_id: str
    def __init__(self, plan_id: _Optional[str] = ..., locale: _Optional[str] = ..., currency: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_plan_pb2.Plan.Extra, str]]] = ...) -> None: ...

class DescribePlanOutput(_message.Message):
    __slots__ = ["plan"]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    plan: _plan_pb2.Plan
    def __init__(self, plan: _Optional[_Union[_plan_pb2.Plan, _Mapping]] = ...) -> None: ...

class ListPlansInput(_message.Message):
    __slots__ = ["currency", "extra", "locale", "offset", "size"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    currency: str
    extra: _containers.RepeatedScalarFieldContainer[_plan_pb2.Plan.Extra]
    locale: str
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., locale: _Optional[str] = ..., currency: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_plan_pb2.Plan.Extra, str]]] = ...) -> None: ...

class ListPlansOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_plan_pb2.Plan]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_plan_pb2.Plan, _Mapping]]] = ...) -> None: ...
