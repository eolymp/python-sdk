from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ["path", "source_ern", "source_url"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ERN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    path: str
    source_ern: str
    source_url: str
    def __init__(self, path: _Optional[str] = ..., source_ern: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...
