from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Student(_message.Message):
    __slots__ = ["bonus_time", "complete_at", "complete_in", "course_id", "end_at", "end_in", "id", "member_id", "name", "started_at", "started_in", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: Student.Status
    BONUS_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: Student.Status
    COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_IN_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    END_IN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NONE: Student.Status
    READY: Student.Status
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_IN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    bonus_time: int
    complete_at: _timestamp_pb2.Timestamp
    complete_in: int
    course_id: str
    end_at: _timestamp_pb2.Timestamp
    end_in: int
    id: str
    member_id: str
    name: str
    started_at: _timestamp_pb2.Timestamp
    started_in: int
    status: Student.Status
    def __init__(self, id: _Optional[str] = ..., course_id: _Optional[str] = ..., member_id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[Student.Status, str]] = ..., bonus_time: _Optional[int] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_in: _Optional[int] = ..., end_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_in: _Optional[int] = ..., complete_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_in: _Optional[int] = ...) -> None: ...
