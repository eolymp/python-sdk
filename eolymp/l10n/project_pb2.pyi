from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Project(_message.Message):
    __slots__ = ["id", "logo_url", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    logo_url: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., logo_url: _Optional[str] = ...) -> None: ...
