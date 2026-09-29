import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Recording(_message.Message):
    __slots__ = ("id", "member_id", "status", "started_at", "ended_at", "gap_duration", "streams", "created_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Recording.Status]
        EMPTY: _ClassVar[Recording.Status]
        COMPLETE: _ClassVar[Recording.Status]
        INCOMPLETE: _ClassVar[Recording.Status]
        EXPIRED: _ClassVar[Recording.Status]
    UNKNOWN_STATUS: Recording.Status
    EMPTY: Recording.Status
    COMPLETE: Recording.Status
    INCOMPLETE: Recording.Status
    EXPIRED: Recording.Status
    class Stream(_message.Message):
        __slots__ = ("source", "playlist_url")
        class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_SOURCE: _ClassVar[Recording.Stream.Source]
            SCREEN: _ClassVar[Recording.Stream.Source]
            CAMERA: _ClassVar[Recording.Stream.Source]
        UNKNOWN_SOURCE: Recording.Stream.Source
        SCREEN: Recording.Stream.Source
        CAMERA: Recording.Stream.Source
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_URL_FIELD_NUMBER: _ClassVar[int]
        source: Recording.Stream.Source
        playlist_url: str
        def __init__(self, source: _Optional[_Union[Recording.Stream.Source, str]] = ..., playlist_url: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    GAP_DURATION_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    member_id: str
    status: Recording.Status
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    gap_duration: int
    streams: _containers.RepeatedCompositeFieldContainer[Recording.Stream]
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., status: _Optional[_Union[Recording.Status, str]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., gap_duration: _Optional[int] = ..., streams: _Optional[_Iterable[_Union[Recording.Stream, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
