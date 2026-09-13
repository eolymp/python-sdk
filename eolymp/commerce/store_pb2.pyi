from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Store(_message.Message):
    __slots__ = ("currency", "credit_value")
    class Patch(_message.Message):
        __slots__ = ("currency", "credit_value")
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        CREDIT_VALUE_FIELD_NUMBER: _ClassVar[int]
        currency: str
        credit_value: int
        def __init__(self, currency: _Optional[str] = ..., credit_value: _Optional[int] = ...) -> None: ...
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CREDIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    currency: str
    credit_value: int
    def __init__(self, currency: _Optional[str] = ..., credit_value: _Optional[int] = ...) -> None: ...
