from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AllocateStockInput(_message.Message):
    __slots__ = ("order_id",)
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class AllocateStockOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RejectOrderInput(_message.Message):
    __slots__ = ("order_id", "reason")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    reason: _content_pb2.Content
    def __init__(self, order_id: _Optional[str] = ..., reason: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class RejectOrderOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ShipOrderInput(_message.Message):
    __slots__ = ("order_id",)
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class ShipOrderOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
