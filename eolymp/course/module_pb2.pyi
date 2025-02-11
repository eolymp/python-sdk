from eolymp.course import assignment_pb2 as _assignment_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Module(_message.Message):
    __slots__ = ("id", "url", "draft", "extra", "weight", "name", "image_url", "index", "description", "start_after", "complete_before", "duration", "progress", "assignment")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Module.Extra]
        DESCRIPTION_VALUE: _ClassVar[Module.Extra]
        DESCRIPTION_RENDER: _ClassVar[Module.Extra]
        PROGRESS: _ClassVar[Module.Extra]
        ASSIGNMENT: _ClassVar[Module.Extra]
    UNKNOWN_EXTRA: Module.Extra
    DESCRIPTION_VALUE: Module.Extra
    DESCRIPTION_RENDER: Module.Extra
    PROGRESS: Module.Extra
    ASSIGNMENT: Module.Extra
    class Progress(_message.Message):
        __slots__ = ("status", "percentage", "grade", "grade_automatic", "grade_override", "excused", "start_after", "complete_before", "duration", "upsolve", "assigned_at", "started_at", "completed_at")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        GRADE_AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        GRADE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        EXCUSED_FIELD_NUMBER: _ClassVar[int]
        START_AFTER_FIELD_NUMBER: _ClassVar[int]
        COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        UPSOLVE_FIELD_NUMBER: _ClassVar[int]
        ASSIGNED_AT_FIELD_NUMBER: _ClassVar[int]
        STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
        status: _assignment_pb2.Assignment.Status
        percentage: float
        grade: int
        grade_automatic: int
        grade_override: int
        excused: bool
        start_after: _timestamp_pb2.Timestamp
        complete_before: _timestamp_pb2.Timestamp
        duration: int
        upsolve: bool
        assigned_at: _timestamp_pb2.Timestamp
        started_at: _timestamp_pb2.Timestamp
        completed_at: _timestamp_pb2.Timestamp
        def __init__(self, status: _Optional[_Union[_assignment_pb2.Assignment.Status, str]] = ..., percentage: _Optional[float] = ..., grade: _Optional[int] = ..., grade_automatic: _Optional[int] = ..., grade_override: _Optional[int] = ..., excused: bool = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., upsolve: bool = ..., assigned_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    START_AFTER_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    draft: bool
    extra: bool
    weight: float
    name: str
    image_url: str
    index: int
    description: _content_pb2.Content
    start_after: _timestamp_pb2.Timestamp
    complete_before: _timestamp_pb2.Timestamp
    duration: int
    progress: Module.Progress
    assignment: _assignment_pb2.Assignment
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., draft: bool = ..., extra: bool = ..., weight: _Optional[float] = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., index: _Optional[int] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., progress: _Optional[_Union[Module.Progress, _Mapping]] = ..., assignment: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ...) -> None: ...
