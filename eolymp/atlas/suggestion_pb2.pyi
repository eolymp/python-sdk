from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Suggestion(_message.Message):
    __slots__ = ("id", "status", "locale", "title", "member_id", "created_at", "updated_at", "topics", "difficulty", "statement", "editorial")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Suggestion.Status]
        PENDING: _ClassVar[Suggestion.Status]
        IN_REVIEW: _ClassVar[Suggestion.Status]
        APPROVED: _ClassVar[Suggestion.Status]
        REJECTED: _ClassVar[Suggestion.Status]
    UNKNOWN_STATUS: Suggestion.Status
    PENDING: Suggestion.Status
    IN_REVIEW: Suggestion.Status
    APPROVED: Suggestion.Status
    REJECTED: Suggestion.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: Suggestion.Status
    locale: str
    title: str
    member_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    topics: _containers.RepeatedScalarFieldContainer[str]
    difficulty: int
    statement: _content_pb2.Content
    editorial: _content_pb2.Content
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Suggestion.Status, str]] = ..., locale: _Optional[str] = ..., title: _Optional[str] = ..., member_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., topics: _Optional[_Iterable[str]] = ..., difficulty: _Optional[int] = ..., statement: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., editorial: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
