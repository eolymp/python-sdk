from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Assignment(_message.Message):
    __slots__ = ("id", "module_id", "status", "member_id", "group_id", "start_after", "complete_before", "duration", "upsolve")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Assignment.Status]
        UNASSIGNED: _ClassVar[Assignment.Status]
        SCHEDULED: _ClassVar[Assignment.Status]
        READY: _ClassVar[Assignment.Status]
        ACTIVE: _ClassVar[Assignment.Status]
        COMPLETE: _ClassVar[Assignment.Status]
        UPSOLVE: _ClassVar[Assignment.Status]
    UNKNOWN_STATUS: Assignment.Status
    UNASSIGNED: Assignment.Status
    SCHEDULED: Assignment.Status
    READY: Assignment.Status
    ACTIVE: Assignment.Status
    COMPLETE: Assignment.Status
    UPSOLVE: Assignment.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    START_AFTER_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    UPSOLVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    module_id: str
    status: Assignment.Status
    member_id: str
    group_id: str
    start_after: _timestamp_pb2.Timestamp
    complete_before: _timestamp_pb2.Timestamp
    duration: int
    upsolve: bool
    def __init__(self, id: _Optional[str] = ..., module_id: _Optional[str] = ..., status: _Optional[_Union[Assignment.Status, str]] = ..., member_id: _Optional[str] = ..., group_id: _Optional[str] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., upsolve: bool = ...) -> None: ...
