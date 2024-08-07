from eolymp.course import module_pb2 as _module_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignmentV2(_message.Message):
    __slots__ = ["assigned_at", "complete_before", "completed_at", "duration", "module", "start_after", "started_at", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: AssignmentV2.Status
    ASSIGNED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: AssignmentV2.Status
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    READY: AssignmentV2.Status
    SCHEDULED: AssignmentV2.Status
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    START_AFTER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNASSIGNED: AssignmentV2.Status
    UNKNOWN_STATUS: AssignmentV2.Status
    UPSOLVE: AssignmentV2.Status
    assigned_at: _timestamp_pb2.Timestamp
    complete_before: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    duration: int
    module: _module_pb2.Module
    start_after: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    status: AssignmentV2.Status
    def __init__(self, module: _Optional[_Union[_module_pb2.Module, _Mapping]] = ..., status: _Optional[_Union[AssignmentV2.Status, str]] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., assigned_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
