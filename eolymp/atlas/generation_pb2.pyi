import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Generation(_message.Message):
    __slots__ = ("id", "problem_id", "status", "total", "ready", "invalid", "error", "created_at", "finished_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Generation.Status]
        PENDING: _ClassVar[Generation.Status]
        RUNNING: _ClassVar[Generation.Status]
        COMPLETE: _ClassVar[Generation.Status]
        FAILURE: _ClassVar[Generation.Status]
    NONE: Generation.Status
    PENDING: Generation.Status
    RUNNING: Generation.Status
    COMPLETE: Generation.Status
    FAILURE: Generation.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    READY_FIELD_NUMBER: _ClassVar[int]
    INVALID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    problem_id: str
    status: Generation.Status
    total: int
    ready: int
    invalid: int
    error: str
    created_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., status: _Optional[_Union[Generation.Status, str]] = ..., total: _Optional[int] = ..., ready: _Optional[int] = ..., invalid: _Optional[int] = ..., error: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
