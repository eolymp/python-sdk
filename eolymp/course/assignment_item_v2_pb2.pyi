from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignmentItemV2(_message.Message):
    __slots__ = ["excused", "grade", "grade_automatic", "grade_override", "graded_at", "module_item_id", "progress"]
    EXCUSED_FIELD_NUMBER: _ClassVar[int]
    GRADED_AT_FIELD_NUMBER: _ClassVar[int]
    GRADE_AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    GRADE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    MODULE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    excused: bool
    grade: int
    grade_automatic: int
    grade_override: int
    graded_at: _timestamp_pb2.Timestamp
    module_item_id: str
    progress: float
    def __init__(self, module_item_id: _Optional[str] = ..., progress: _Optional[float] = ..., grade: _Optional[int] = ..., excused: bool = ..., grade_automatic: _Optional[int] = ..., grade_override: _Optional[int] = ..., graded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
