from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Activity(_message.Message):
    __slots__ = ("id", "type", "status", "scoreboard_id", "created_at", "started_at", "progress_at", "complete_at", "progress", "total", "error")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Activity.Type]
        SCOREBOARD_REBUILD: _ClassVar[Activity.Type]
    NONE: Activity.Type
    SCOREBOARD_REBUILD: Activity.Type
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Activity.Status]
        CREATED: _ClassVar[Activity.Status]
        STARTED: _ClassVar[Activity.Status]
        COMPLETE: _ClassVar[Activity.Status]
        ERROR: _ClassVar[Activity.Status]
    UNKNOWN: Activity.Status
    CREATED: Activity.Status
    STARTED: Activity.Status
    COMPLETE: Activity.Status
    ERROR: Activity.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: Activity.Type
    status: Activity.Status
    scoreboard_id: str
    created_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    progress_at: _timestamp_pb2.Timestamp
    complete_at: _timestamp_pb2.Timestamp
    progress: int
    total: int
    error: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[Activity.Type, str]] = ..., status: _Optional[_Union[Activity.Status, str]] = ..., scoreboard_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., progress_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., progress: _Optional[int] = ..., total: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...
