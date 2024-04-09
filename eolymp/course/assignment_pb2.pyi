from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Assignment(_message.Message):
    __slots__ = ["complete_at", "duration", "end_at", "grade", "progress", "start_at", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: Assignment.Status
    COMPLETE: Assignment.Status
    COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    READY: Assignment.Status
    SCHEDULED: Assignment.Status
    START_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNED: Assignment.Status
    UNKNOWN_STATUS: Assignment.Status
    UPSOLVE: Assignment.Status
    complete_at: _timestamp_pb2.Timestamp
    duration: int
    end_at: _timestamp_pb2.Timestamp
    grade: int
    progress: float
    start_at: _timestamp_pb2.Timestamp
    status: Assignment.Status
    def __init__(self, status: _Optional[_Union[Assignment.Status, str]] = ..., start_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., progress: _Optional[float] = ..., grade: _Optional[int] = ...) -> None: ...
