from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Link(_message.Message):
    __slots__ = ("rel", "ref", "type")
    REL_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    rel: str
    ref: str
    type: str
    def __init__(self, rel: _Optional[str] = ..., ref: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
