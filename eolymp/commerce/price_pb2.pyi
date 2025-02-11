from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Price(_message.Message):
    __slots__ = ("id", "recurrence", "currency", "unit_amount")
    class Recurrence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_RECURRENCE: _ClassVar[Price.Recurrence]
        ONETIME: _ClassVar[Price.Recurrence]
        MONTHLY: _ClassVar[Price.Recurrence]
        YEARLY: _ClassVar[Price.Recurrence]
    UNKNOWN_RECURRENCE: Price.Recurrence
    ONETIME: Price.Recurrence
    MONTHLY: Price.Recurrence
    YEARLY: Price.Recurrence
    ID_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    UNIT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    recurrence: Price.Recurrence
    currency: str
    unit_amount: int
    def __init__(self, id: _Optional[str] = ..., recurrence: _Optional[_Union[Price.Recurrence, str]] = ..., currency: _Optional[str] = ..., unit_amount: _Optional[int] = ...) -> None: ...
