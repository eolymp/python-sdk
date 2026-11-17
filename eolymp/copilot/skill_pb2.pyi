from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Skill(_message.Message):
    __slots__ = ("id", "path", "title", "content")
    class Patch(_message.Message):
        __slots__ = ("path", "title", "content")
        PATH_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        path: str
        title: str
        content: str
        def __init__(self, path: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    path: str
    title: str
    content: str
    def __init__(self, id: _Optional[str] = ..., path: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
