import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Sitemap(_message.Message):
    __slots__ = ()
    class Chunk(_message.Message):
        __slots__ = ("id", "size", "updated_at")
        ID_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        id: str
        size: int
        updated_at: _timestamp_pb2.Timestamp
        def __init__(self, id: _Optional[str] = ..., size: _Optional[int] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Entry(_message.Message):
        __slots__ = ("url", "languages", "updated_at")
        URL_FIELD_NUMBER: _ClassVar[int]
        LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        url: str
        languages: _containers.RepeatedScalarFieldContainer[str]
        updated_at: _timestamp_pb2.Timestamp
        def __init__(self, url: _Optional[str] = ..., languages: _Optional[_Iterable[str]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
