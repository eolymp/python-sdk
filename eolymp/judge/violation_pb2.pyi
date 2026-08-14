import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Violation(_message.Message):
    __slots__ = ("id", "participant_id", "status", "type", "confidence", "problem_id", "case_ref", "summary", "created_by", "created_at", "confirmed_by", "confirmed_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Violation.Status]
        PENDING: _ClassVar[Violation.Status]
        CONFIRMED: _ClassVar[Violation.Status]
        CANCELLED: _ClassVar[Violation.Status]
    UNKNOWN_STATUS: Violation.Status
    PENDING: Violation.Status
    CONFIRMED: Violation.Status
    CANCELLED: Violation.Status
    class Confidence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_CONFIDENCE: _ClassVar[Violation.Confidence]
        LOW: _ClassVar[Violation.Confidence]
        MEDIUM: _ClassVar[Violation.Confidence]
        HIGH: _ClassVar[Violation.Confidence]
    UNKNOWN_CONFIDENCE: Violation.Confidence
    LOW: Violation.Confidence
    MEDIUM: Violation.Confidence
    HIGH: Violation.Confidence
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TYPE: _ClassVar[Violation.Type]
        OTHER: _ClassVar[Violation.Type]
        PLAGIARISM: _ClassVar[Violation.Type]
        GEN_AI_USAGE: _ClassVar[Violation.Type]
        BEHAVIOUR: _ClassVar[Violation.Type]
    UNKNOWN_TYPE: Violation.Type
    OTHER: Violation.Type
    PLAGIARISM: Violation.Type
    GEN_AI_USAGE: Violation.Type
    BEHAVIOUR: Violation.Type
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNSPECIFIED: _ClassVar[Violation.Patch.Field]
            SUMMARY: _ClassVar[Violation.Patch.Field]
            STATUS: _ClassVar[Violation.Patch.Field]
        UNSPECIFIED: Violation.Patch.Field
        SUMMARY: Violation.Patch.Field
        STATUS: Violation.Patch.Field
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    CASE_REF_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_BY_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    participant_id: str
    status: Violation.Status
    type: Violation.Type
    confidence: Violation.Confidence
    problem_id: str
    case_ref: str
    summary: _content_pb2.Content
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    confirmed_by: str
    confirmed_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., participant_id: _Optional[str] = ..., status: _Optional[_Union[Violation.Status, str]] = ..., type: _Optional[_Union[Violation.Type, str]] = ..., confidence: _Optional[_Union[Violation.Confidence, str]] = ..., problem_id: _Optional[str] = ..., case_ref: _Optional[str] = ..., summary: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., confirmed_by: _Optional[str] = ..., confirmed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
