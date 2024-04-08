from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Student(_message.Message):
    __slots__ = ["complete_at", "course_id", "duration", "end_at", "id", "member_id", "name", "start_at", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: Student.Status
    COMPLETE: Student.Status
    COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE: Student.Status
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    READY: Student.Status
    SCHEDULED: Student.Status
    START_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STATUS: Student.Status
    UPSOLVE: Student.Status
    complete_at: _timestamp_pb2.Timestamp
    course_id: str
    duration: int
    end_at: _timestamp_pb2.Timestamp
    id: str
    member_id: str
    name: str
    start_at: _timestamp_pb2.Timestamp
    status: Student.Status
    def __init__(self, id: _Optional[str] = ..., course_id: _Optional[str] = ..., member_id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[Student.Status, str]] = ..., start_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ...) -> None: ...
