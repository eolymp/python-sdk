from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ShippingMethod(_message.Message):
    __slots__ = ("id", "name", "cost", "min_order_value")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    MIN_ORDER_VALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    cost: int
    min_order_value: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., cost: _Optional[int] = ..., min_order_value: _Optional[int] = ...) -> None: ...
