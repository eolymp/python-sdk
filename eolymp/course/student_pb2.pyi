from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Student(_message.Message):
    __slots__ = ("id", "url", "member_id", "inactive", "assign_all", "overall_progress", "overall_grade", "grades", "graded_at", "updated_at", "created_at", "cursor")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Student.Extra]
        GRADES: _ClassVar[Student.Extra]
    UNKNOWN_EXTRA: Student.Extra
    GRADES: Student.Extra
    class Grade(_message.Message):
        __slots__ = ("module_id", "grade", "grade_automatic", "grade_override", "excused")
        MODULE_ID_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        GRADE_AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        GRADE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        EXCUSED_FIELD_NUMBER: _ClassVar[int]
        module_id: str
        grade: int
        grade_automatic: int
        grade_override: int
        excused: bool
        def __init__(self, module_id: _Optional[str] = ..., grade: _Optional[int] = ..., grade_automatic: _Optional[int] = ..., grade_override: _Optional[int] = ..., excused: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_ALL_FIELD_NUMBER: _ClassVar[int]
    OVERALL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    OVERALL_GRADE_FIELD_NUMBER: _ClassVar[int]
    GRADES_FIELD_NUMBER: _ClassVar[int]
    GRADED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    member_id: str
    inactive: bool
    assign_all: bool
    overall_progress: float
    overall_grade: int
    grades: _containers.RepeatedCompositeFieldContainer[Student.Grade]
    graded_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    cursor: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., member_id: _Optional[str] = ..., inactive: bool = ..., assign_all: bool = ..., overall_progress: _Optional[float] = ..., overall_grade: _Optional[int] = ..., grades: _Optional[_Iterable[_Union[Student.Grade, _Mapping]]] = ..., graded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cursor: _Optional[str] = ...) -> None: ...
