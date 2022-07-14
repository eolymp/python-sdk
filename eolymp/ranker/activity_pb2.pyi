from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Activity(_message.Message):
    __slots__ = ["complete_at", "created_at", "error", "id", "progress", "progress_at", "scoreboard_id", "started_at", "status", "total", "type"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    COMPLETE: Activity.Status
    COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED: Activity.Status
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR: Activity.Status
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NONE: Activity.Type
    PROGRESS_AT_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_REBUILD: Activity.Type
    STARTED: Activity.Status
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: Activity.Status
    complete_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    error: str
    id: str
    progress: int
    progress_at: _timestamp_pb2.Timestamp
    scoreboard_id: str
    started_at: _timestamp_pb2.Timestamp
    status: Activity.Status
    total: int
    type: Activity.Type
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[Activity.Type, str]] = ..., status: _Optional[_Union[Activity.Status, str]] = ..., scoreboard_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., progress_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., progress: _Optional[int] = ..., total: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...
