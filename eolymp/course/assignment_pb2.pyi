from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Assignment(_message.Message):
    __slots__ = ["complete_before", "duration", "group_id", "id", "member_id", "module_id", "start_after", "status", "upsolve"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: Assignment.Status
    COMPLETE: Assignment.Status
    COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    READY: Assignment.Status
    SCHEDULED: Assignment.Status
    START_AFTER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNED: Assignment.Status
    UNKNOWN_STATUS: Assignment.Status
    UPSOLVE: Assignment.Status
    UPSOLVE_FIELD_NUMBER: _ClassVar[int]
    complete_before: _timestamp_pb2.Timestamp
    duration: int
    group_id: str
    id: str
    member_id: str
    module_id: str
    start_after: _timestamp_pb2.Timestamp
    status: Assignment.Status
    upsolve: bool
    def __init__(self, id: _Optional[str] = ..., module_id: _Optional[str] = ..., status: _Optional[_Union[Assignment.Status, str]] = ..., member_id: _Optional[str] = ..., group_id: _Optional[str] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., upsolve: bool = ...) -> None: ...
