from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Printer(_message.Message):
    __slots__ = ("id", "secret", "status", "name")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Printer.Status]
        OFFLINE: _ClassVar[Printer.Status]
        READY: _ClassVar[Printer.Status]
        BUSY: _ClassVar[Printer.Status]
    UNKNOWN_STATUS: Printer.Status
    OFFLINE: Printer.Status
    READY: Printer.Status
    BUSY: Printer.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    secret: str
    status: Printer.Status
    name: str
    def __init__(self, id: _Optional[str] = ..., secret: _Optional[str] = ..., status: _Optional[_Union[Printer.Status, str]] = ..., name: _Optional[str] = ...) -> None: ...
