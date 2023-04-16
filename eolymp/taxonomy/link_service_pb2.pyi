from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetLinkedTopicsInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetLinkedTopicsOutput(_message.Message):
    __slots__ = ["topics"]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, topics: _Optional[_Iterable[str]] = ...) -> None: ...

class SetLinkedTopicsInput(_message.Message):
    __slots__ = ["topics"]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, topics: _Optional[_Iterable[str]] = ...) -> None: ...

class SetLinkedTopicsOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
