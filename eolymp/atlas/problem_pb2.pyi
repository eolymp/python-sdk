from eolymp.annotations import endpoint_pb2 as _endpoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Problem(_message.Message):
    __slots__ = ["difficulty", "id", "links", "number", "origin", "private", "topics", "url", "visible"]
    class LinksEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    difficulty: int
    id: str
    links: _containers.ScalarMap[str, str]
    number: int
    origin: str
    private: bool
    topics: _containers.RepeatedScalarFieldContainer[str]
    url: str
    visible: bool
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., links: _Optional[_Mapping[str, str]] = ..., number: _Optional[int] = ..., visible: bool = ..., private: bool = ..., origin: _Optional[str] = ..., topics: _Optional[_Iterable[str]] = ..., difficulty: _Optional[int] = ...) -> None: ...
