from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Student(_message.Message):
    __slots__ = ["display_name", "graded_at", "grades", "id", "member_id", "overall_grade", "overall_progress", "updated_at"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Grade(_message.Message):
        __slots__ = ["entry_id", "grade", "progress"]
        ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_FIELD_NUMBER: _ClassVar[int]
        entry_id: str
        grade: int
        progress: float
        def __init__(self, entry_id: _Optional[str] = ..., progress: _Optional[float] = ..., grade: _Optional[int] = ...) -> None: ...
    BREAKDOWN: Student.Extra
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    GRADED_AT_FIELD_NUMBER: _ClassVar[int]
    GRADES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    OVERALL_GRADE_FIELD_NUMBER: _ClassVar[int]
    OVERALL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Student.Extra
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    graded_at: _timestamp_pb2.Timestamp
    grades: _containers.RepeatedCompositeFieldContainer[Student.Grade]
    id: str
    member_id: str
    overall_grade: int
    overall_progress: float
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., display_name: _Optional[str] = ..., overall_progress: _Optional[float] = ..., overall_grade: _Optional[int] = ..., grades: _Optional[_Iterable[_Union[Student.Grade, _Mapping]]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., graded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
