import datetime

from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Task(_message.Message):
    __slots__ = ("id", "type", "reference", "status", "payload", "progress", "total", "status_message", "error", "log_url", "attempt", "created_at", "started_at", "finished_at", "created_by")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Task.Status]
        PENDING: _ClassVar[Task.Status]
        RUNNING: _ClassVar[Task.Status]
        COMPLETE: _ClassVar[Task.Status]
        FAILED: _ClassVar[Task.Status]
        EXPIRED: _ClassVar[Task.Status]
        CANCELLED: _ClassVar[Task.Status]
    UNKNOWN: Task.Status
    PENDING: Task.Status
    RUNNING: Task.Status
    COMPLETE: Task.Status
    FAILED: Task.Status
    EXPIRED: Task.Status
    CANCELLED: Task.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LOG_URL_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    reference: str
    status: Task.Status
    payload: _struct_pb2.Struct
    progress: int
    total: int
    status_message: str
    error: str
    log_url: str
    attempt: int
    created_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    created_by: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., reference: _Optional[str] = ..., status: _Optional[_Union[Task.Status, str]] = ..., payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., progress: _Optional[int] = ..., total: _Optional[int] = ..., status_message: _Optional[str] = ..., error: _Optional[str] = ..., log_url: _Optional[str] = ..., attempt: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ...) -> None: ...
