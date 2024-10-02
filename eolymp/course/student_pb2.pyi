from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Student(_message.Message):
    __slots__ = ["assign_all", "created_at", "cursor", "graded_at", "grades", "id", "inactive", "member_id", "overall_grade", "overall_progress", "updated_at", "url"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Grade(_message.Message):
        __slots__ = ["excused", "grade", "grade_automatic", "grade_override", "module_id"]
        EXCUSED_FIELD_NUMBER: _ClassVar[int]
        GRADE_AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        GRADE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        MODULE_ID_FIELD_NUMBER: _ClassVar[int]
        excused: bool
        grade: int
        grade_automatic: int
        grade_override: int
        module_id: str
        def __init__(self, module_id: _Optional[str] = ..., grade: _Optional[int] = ..., grade_automatic: _Optional[int] = ..., grade_override: _Optional[int] = ..., excused: bool = ...) -> None: ...
    ASSIGN_ALL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    GRADED_AT_FIELD_NUMBER: _ClassVar[int]
    GRADES: Student.Extra
    GRADES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    OVERALL_GRADE_FIELD_NUMBER: _ClassVar[int]
    OVERALL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Student.Extra
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    assign_all: bool
    created_at: _timestamp_pb2.Timestamp
    cursor: str
    graded_at: _timestamp_pb2.Timestamp
    grades: _containers.RepeatedCompositeFieldContainer[Student.Grade]
    id: str
    inactive: bool
    member_id: str
    overall_grade: int
    overall_progress: float
    updated_at: _timestamp_pb2.Timestamp
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., member_id: _Optional[str] = ..., inactive: bool = ..., assign_all: bool = ..., overall_progress: _Optional[float] = ..., overall_grade: _Optional[int] = ..., grades: _Optional[_Iterable[_Union[Student.Grade, _Mapping]]] = ..., graded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cursor: _Optional[str] = ...) -> None: ...
