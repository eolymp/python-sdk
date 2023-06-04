from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Term(_message.Message):
    __slots__ = ["description", "id", "key", "message", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: Term.Status
    DEPRECATED: Term.Status
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NONE: Term.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    key: str
    message: str
    status: Term.Status
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., message: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[Term.Status, str]] = ...) -> None: ...
