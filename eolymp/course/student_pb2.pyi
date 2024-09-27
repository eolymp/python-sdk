from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Student(_message.Message):
    __slots__ = ["assign_all", "created_at", "display_name", "graded_at", "id", "inactive", "member_id", "overall_grade", "overall_progress", "picture", "updated_at", "url"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ASSIGN_ALL_FIELD_NUMBER: _ClassVar[int]
    BREAKDOWN: Student.Extra
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    GRADED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    OVERALL_GRADE_FIELD_NUMBER: _ClassVar[int]
    OVERALL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Student.Extra
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    assign_all: bool
    created_at: _timestamp_pb2.Timestamp
    display_name: str
    graded_at: _timestamp_pb2.Timestamp
    id: str
    inactive: bool
    member_id: str
    overall_grade: int
    overall_progress: float
    picture: str
    updated_at: _timestamp_pb2.Timestamp
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., member_id: _Optional[str] = ..., display_name: _Optional[str] = ..., picture: _Optional[str] = ..., inactive: bool = ..., assign_all: bool = ..., overall_progress: _Optional[float] = ..., overall_grade: _Optional[int] = ..., graded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
