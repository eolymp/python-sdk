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
    __slots__ = ("id", "member_id", "status", "started_at", "ended_at", "gap_duration", "streams", "created_at", "capture_from", "capture_to", "upload_until", "required_sources", "state", "slots")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATE: _ClassVar[Recording.State]
        PENDING: _ClassVar[Recording.State]
        ACTIVE: _ClassVar[Recording.State]
        UPLOAD_ONLY: _ClassVar[Recording.State]
        CLOSED: _ClassVar[Recording.State]
    UNKNOWN_STATE: Recording.State
    PENDING: Recording.State
    ACTIVE: Recording.State
    UPLOAD_ONLY: Recording.State
    CLOSED: Recording.State
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
    class Patch(_message.Message):
        __slots__ = ("capture_from", "capture_to", "upload_until", "required_sources")
        CAPTURE_FROM_FIELD_NUMBER: _ClassVar[int]
        CAPTURE_TO_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_UNTIL_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_SOURCES_FIELD_NUMBER: _ClassVar[int]
        capture_from: _timestamp_pb2.Timestamp
        capture_to: _timestamp_pb2.Timestamp
        upload_until: _timestamp_pb2.Timestamp
        required_sources: _containers.RepeatedScalarFieldContainer[Recording.Stream.Source]
        def __init__(self, capture_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., capture_to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., upload_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., required_sources: _Optional[_Iterable[_Union[Recording.Stream.Source, str]]] = ...) -> None: ...
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Recording.Extra.Field]
            SLOTS: _ClassVar[Recording.Extra.Field]
        UNKNOWN_EXTRA: Recording.Extra.Field
        SLOTS: Recording.Extra.Field
        def __init__(self) -> None: ...
    class Slot(_message.Message):
        __slots__ = ("source", "state", "holder")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_STATE: _ClassVar[Recording.Slot.State]
            MISSING: _ClassVar[Recording.Slot.State]
            LIVE: _ClassVar[Recording.Slot.State]
            STALLED: _ClassVar[Recording.Slot.State]
        UNKNOWN_STATE: Recording.Slot.State
        MISSING: Recording.Slot.State
        LIVE: Recording.Slot.State
        STALLED: Recording.Slot.State
        class Holder(_message.Message):
            __slots__ = ("kind", "version")
            class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UNKNOWN_KIND: _ClassVar[Recording.Slot.Holder.Kind]
                BROWSER: _ClassVar[Recording.Slot.Holder.Kind]
                APP: _ClassVar[Recording.Slot.Holder.Kind]
                PHONE: _ClassVar[Recording.Slot.Holder.Kind]
            UNKNOWN_KIND: Recording.Slot.Holder.Kind
            BROWSER: Recording.Slot.Holder.Kind
            APP: Recording.Slot.Holder.Kind
            PHONE: Recording.Slot.Holder.Kind
            KIND_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            kind: Recording.Slot.Holder.Kind
            version: str
            def __init__(self, kind: _Optional[_Union[Recording.Slot.Holder.Kind, str]] = ..., version: _Optional[str] = ...) -> None: ...
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        HOLDER_FIELD_NUMBER: _ClassVar[int]
        source: Recording.Stream.Source
        state: Recording.Slot.State
        holder: Recording.Slot.Holder
        def __init__(self, source: _Optional[_Union[Recording.Stream.Source, str]] = ..., state: _Optional[_Union[Recording.Slot.State, str]] = ..., holder: _Optional[_Union[Recording.Slot.Holder, _Mapping]] = ...) -> None: ...
    class Stream(_message.Message):
        __slots__ = ("source", "playlist_url")
        class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_SOURCE: _ClassVar[Recording.Stream.Source]
            SCREEN: _ClassVar[Recording.Stream.Source]
            CAMERA: _ClassVar[Recording.Stream.Source]
            ADDITIONAL_CAMERA: _ClassVar[Recording.Stream.Source]
        UNKNOWN_SOURCE: Recording.Stream.Source
        SCREEN: Recording.Stream.Source
        CAMERA: Recording.Stream.Source
        ADDITIONAL_CAMERA: Recording.Stream.Source
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
    CAPTURE_FROM_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_TO_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_UNTIL_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SOURCES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    member_id: str
    status: Recording.Status
    started_at: _timestamp_pb2.Timestamp
    ended_at: _timestamp_pb2.Timestamp
    gap_duration: int
    streams: _containers.RepeatedCompositeFieldContainer[Recording.Stream]
    created_at: _timestamp_pb2.Timestamp
    capture_from: _timestamp_pb2.Timestamp
    capture_to: _timestamp_pb2.Timestamp
    upload_until: _timestamp_pb2.Timestamp
    required_sources: _containers.RepeatedScalarFieldContainer[Recording.Stream.Source]
    state: Recording.State
    slots: _containers.RepeatedCompositeFieldContainer[Recording.Slot]
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., status: _Optional[_Union[Recording.Status, str]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., gap_duration: _Optional[int] = ..., streams: _Optional[_Iterable[_Union[Recording.Stream, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., capture_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., capture_to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., upload_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., required_sources: _Optional[_Iterable[_Union[Recording.Stream.Source, str]]] = ..., state: _Optional[_Union[Recording.State, str]] = ..., slots: _Optional[_Iterable[_Union[Recording.Slot, _Mapping]]] = ...) -> None: ...
