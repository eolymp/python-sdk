from eolymp.annotations import endpoint_pb2 as _endpoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Problem(_message.Message):
    __slots__ = ["difficulty", "id", "number", "private", "topics", "url", "visible"]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    difficulty: int
    id: str
    number: int
    private: bool
    topics: _containers.RepeatedScalarFieldContainer[str]
    url: str
    visible: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., number: _Optional[int] = ..., visible: bool = ..., private: bool = ..., topics: _Optional[_Iterable[str]] = ..., difficulty: _Optional[int] = ...) -> None: ...
