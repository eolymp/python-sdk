from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Assignment(_message.Message):
    __slots__ = ["complete_before", "completed_at", "duration", "explicit", "start_after", "started_at", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: Assignment.Status
    COMPLETE: Assignment.Status
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_FIELD_NUMBER: _ClassVar[int]
    READY: Assignment.Status
    SCHEDULED: Assignment.Status
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    START_AFTER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNED: Assignment.Status
    UNKNOWN_STATUS: Assignment.Status
    UPSOLVE: Assignment.Status
    complete_before: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    duration: int
    explicit: bool
    start_after: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    status: Assignment.Status
    def __init__(self, status: _Optional[_Union[Assignment.Status, str]] = ..., explicit: bool = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ...) -> None: ...
