from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Term(_message.Message):
    __slots__ = ["description", "id", "message", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: Term.Status
    DEPRECATED: Term.Status
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NONE: Term.Status
    OUTDATED: Term.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    message: str
    status: str
    def __init__(self, id: _Optional[str] = ..., message: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...
