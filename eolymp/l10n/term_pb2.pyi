from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Term(_message.Message):
    __slots__ = ("id", "key", "message", "description", "status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Term.Status]
        ACTIVE: _ClassVar[Term.Status]
        DEPRECATED: _ClassVar[Term.Status]
    NONE: Term.Status
    ACTIVE: Term.Status
    DEPRECATED: Term.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    message: str
    description: str
    status: Term.Status
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., message: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[Term.Status, str]] = ...) -> None: ...
