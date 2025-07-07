from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Violation(_message.Message):
    __slots__ = ("id", "cancelled", "summary", "automatic", "participant_id", "given_by", "given_at")
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNSPECIFIED: _ClassVar[Violation.Patch.Field]
            SUMMARY: _ClassVar[Violation.Patch.Field]
            CANCELLED: _ClassVar[Violation.Patch.Field]
            AUTOMATIC: _ClassVar[Violation.Patch.Field]
        UNSPECIFIED: Violation.Patch.Field
        SUMMARY: Violation.Patch.Field
        CANCELLED: Violation.Patch.Field
        AUTOMATIC: Violation.Patch.Field
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    GIVEN_BY_FIELD_NUMBER: _ClassVar[int]
    GIVEN_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    cancelled: bool
    summary: str
    automatic: bool
    participant_id: str
    given_by: str
    given_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., cancelled: bool = ..., summary: _Optional[str] = ..., automatic: bool = ..., participant_id: _Optional[str] = ..., given_by: _Optional[str] = ..., given_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
