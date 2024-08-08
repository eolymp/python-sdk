from eolymp.course import module_item_pb2 as _module_item_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignmentItemV2(_message.Message):
    __slots__ = ["excused", "grade", "graded_at", "item_id", "progress"]
    EXCUSED_FIELD_NUMBER: _ClassVar[int]
    GRADED_AT_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    excused: bool
    grade: int
    graded_at: _timestamp_pb2.Timestamp
    item_id: str
    progress: float
    def __init__(self, item_id: _Optional[str] = ..., progress: _Optional[float] = ..., grade: _Optional[int] = ..., excused: bool = ..., graded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
