from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Grade(_message.Message):
    __slots__ = ["breakdown", "grade", "graded_at", "id", "member_id", "progress", "updated_at"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Breakdown(_message.Message):
        __slots__ = ["entry_id", "grade", "progress"]
        ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_FIELD_NUMBER: _ClassVar[int]
        entry_id: str
        grade: int
        progress: float
        def __init__(self, entry_id: _Optional[str] = ..., progress: _Optional[float] = ..., grade: _Optional[int] = ...) -> None: ...
    BREAKDOWN: Grade.Extra
    BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    GRADED_AT_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Grade.Extra
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    breakdown: _containers.RepeatedCompositeFieldContainer[Grade.Breakdown]
    grade: int
    graded_at: _timestamp_pb2.Timestamp
    id: str
    member_id: str
    progress: float
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., progress: _Optional[float] = ..., grade: _Optional[int] = ..., breakdown: _Optional[_Iterable[_Union[Grade.Breakdown, _Mapping]]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., graded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
