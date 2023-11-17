from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.commerce import order_pb2 as _order_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CancelOrderInput(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class CancelOrderOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateOrderInput(_message.Message):
    __slots__ = ["order"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: _order_pb2.Order
    def __init__(self, order: _Optional[_Union[_order_pb2.Order, _Mapping]] = ...) -> None: ...

class CreateOrderOutput(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class DescribeOrderInput(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class DescribeOrderOutput(_message.Message):
    __slots__ = ["order"]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: _order_pb2.Order
    def __init__(self, order: _Optional[_Union[_order_pb2.Order, _Mapping]] = ...) -> None: ...

class PlaceOrderInput(_message.Message):
    __slots__ = ["order_id"]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    def __init__(self, order_id: _Optional[str] = ...) -> None: ...

class PlaceOrderOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateOrderInput(_message.Message):
    __slots__ = ["order", "order_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateOrderInput.Patch
    BILLING_ADDRESS: UpdateOrderInput.Patch
    ORDER_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    order: _order_pb2.Order
    order_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateOrderInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateOrderInput.Patch, str]]] = ..., order_id: _Optional[str] = ..., order: _Optional[_Union[_order_pb2.Order, _Mapping]] = ...) -> None: ...

class UpdateOrderOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
