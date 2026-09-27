import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Recording(_message.Message):
    __slots__ = ("stream", "started_at", "duration", "size", "content_type", "url")
    class Stream(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STREAM: _ClassVar[Recording.Stream]
        SCREEN: _ClassVar[Recording.Stream]
        CAMERA: _ClassVar[Recording.Stream]
    UNKNOWN_STREAM: Recording.Stream
    SCREEN: Recording.Stream
    CAMERA: Recording.Stream
    STREAM_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    stream: Recording.Stream
    started_at: _timestamp_pb2.Timestamp
    duration: int
    size: int
    content_type: str
    url: str
    def __init__(self, stream: _Optional[_Union[Recording.Stream, str]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., size: _Optional[int] = ..., content_type: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
