from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Student(_message.Message):
    __slots__ = ["assign_all", "assignments", "graded_at", "grades", "id", "inactive", "member_id", "overall_grade", "overall_progress", "updated_at"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Assignment(_message.Message):
        __slots__ = ["assigned_at", "complete_before", "completed_at", "duration", "grades", "module_id", "overall_grade", "overall_progress", "start_after", "started_at", "status"]
        ASSIGNED_AT_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
        COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        GRADES_FIELD_NUMBER: _ClassVar[int]
        MODULE_ID_FIELD_NUMBER: _ClassVar[int]
        OVERALL_GRADE_FIELD_NUMBER: _ClassVar[int]
        OVERALL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        START_AFTER_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        assigned_at: _timestamp_pb2.Timestamp
        complete_before: _timestamp_pb2.Timestamp
        completed_at: _timestamp_pb2.Timestamp
        duration: int
        grades: _containers.RepeatedCompositeFieldContainer[Student.Grade]
        module_id: str
        overall_grade: int
        overall_progress: float
        start_after: _timestamp_pb2.Timestamp
        started_at: _timestamp_pb2.Timestamp
        status: Student.Status
        def __init__(self, module_id: _Optional[str] = ..., status: _Optional[_Union[Student.Status, str]] = ..., overall_progress: _Optional[float] = ..., overall_grade: _Optional[int] = ..., assigned_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., grades: _Optional[_Iterable[_Union[Student.Grade, _Mapping]]] = ...) -> None: ...
    class Grade(_message.Message):
        __slots__ = ["entry_id", "grade", "progress"]
        ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_FIELD_NUMBER: _ClassVar[int]
        entry_id: str
        grade: int
        progress: float
        def __init__(self, entry_id: _Optional[str] = ..., progress: _Optional[float] = ..., grade: _Optional[int] = ...) -> None: ...
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    ASSIGN_ALL_FIELD_NUMBER: _ClassVar[int]
    BLOCKED: Student.Status
    BREAKDOWN: Student.Extra
    COMPLETED: Student.Status
    GRADED_AT_FIELD_NUMBER: _ClassVar[int]
    GRADES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    OVERALL_GRADE_FIELD_NUMBER: _ClassVar[int]
    OVERALL_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    PENDING: Student.Status
    READY: Student.Status
    STARTED: Student.Status
    UNASSIGNED: Student.Status
    UNKNOWN_EXTRA: Student.Extra
    UNKNOWN_STATUS: Student.Status
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    assign_all: bool
    assignments: _containers.RepeatedCompositeFieldContainer[Student.Assignment]
    graded_at: _timestamp_pb2.Timestamp
    grades: _containers.RepeatedCompositeFieldContainer[Student.Grade]
    id: str
    inactive: bool
    member_id: str
    overall_grade: int
    overall_progress: float
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., inactive: bool = ..., assign_all: bool = ..., overall_progress: _Optional[float] = ..., overall_grade: _Optional[int] = ..., grades: _Optional[_Iterable[_Union[Student.Grade, _Mapping]]] = ..., assignments: _Optional[_Iterable[_Union[Student.Assignment, _Mapping]]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., graded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
