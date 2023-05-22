from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetBookmarkInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class GetBookmarkOutput(_message.Message):
    __slots__ = ["bookmark"]
    BOOKMARK_FIELD_NUMBER: _ClassVar[int]
    bookmark: bool
    def __init__(self, bookmark: bool = ...) -> None: ...

class SetBookmarkInput(_message.Message):
    __slots__ = ["bookmark", "problem_id"]
    BOOKMARK_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    bookmark: bool
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., bookmark: bool = ...) -> None: ...

class SetBookmarkOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
