from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BookmarkChangedEvent(_message.Message):
    __slots__ = ["after", "before", "member_id", "problem_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    after: bool
    before: bool
    member_id: str
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., member_id: _Optional[str] = ..., before: bool = ..., after: bool = ...) -> None: ...

class GetBookmarkInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetBookmarkOutput(_message.Message):
    __slots__ = ["bookmark"]
    BOOKMARK_FIELD_NUMBER: _ClassVar[int]
    bookmark: bool
    def __init__(self, bookmark: bool = ...) -> None: ...

class SetBookmarkInput(_message.Message):
    __slots__ = ["bookmark"]
    BOOKMARK_FIELD_NUMBER: _ClassVar[int]
    bookmark: bool
    def __init__(self, bookmark: bool = ...) -> None: ...

class SetBookmarkOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
