import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Feedback(_message.Message):
    __slots__ = ("id", "fragment_id", "fragment_locale", "helpful", "comment", "block_index", "block_text", "member_id", "status", "resolution", "labels", "created_at", "resolved_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Feedback.Status]
        OPEN: _ClassVar[Feedback.Status]
        RESOLVED: _ClassVar[Feedback.Status]
        DISMISSED: _ClassVar[Feedback.Status]
    UNKNOWN_STATUS: Feedback.Status
    OPEN: Feedback.Status
    RESOLVED: Feedback.Status
    DISMISSED: Feedback.Status
    class Patch(_message.Message):
        __slots__ = ("status", "resolution", "labels", "unset_labels")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        UNSET_LABELS_FIELD_NUMBER: _ClassVar[int]
        status: Feedback.Status
        resolution: str
        labels: _containers.RepeatedScalarFieldContainer[str]
        unset_labels: bool
        def __init__(self, status: _Optional[_Union[Feedback.Status, str]] = ..., resolution: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ..., unset_labels: _Optional[bool] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_LOCALE_FIELD_NUMBER: _ClassVar[int]
    HELPFUL_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    BLOCK_TEXT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    fragment_id: str
    fragment_locale: str
    helpful: bool
    comment: str
    block_index: int
    block_text: str
    member_id: str
    status: Feedback.Status
    resolution: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    resolved_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., fragment_id: _Optional[str] = ..., fragment_locale: _Optional[str] = ..., helpful: _Optional[bool] = ..., comment: _Optional[str] = ..., block_index: _Optional[int] = ..., block_text: _Optional[str] = ..., member_id: _Optional[str] = ..., status: _Optional[_Union[Feedback.Status, str]] = ..., resolution: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., resolved_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
