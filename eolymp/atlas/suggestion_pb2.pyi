import datetime

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
    __slots__ = ("id", "status", "version", "member_id", "contribution", "created_at", "updated_at", "classification", "statement_change", "editorial_change")
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
    class Classification(_message.Message):
        __slots__ = ("topics", "difficulty")
        TOPICS_FIELD_NUMBER: _ClassVar[int]
        DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
        topics: _containers.RepeatedScalarFieldContainer[str]
        difficulty: int
        def __init__(self, topics: _Optional[_Iterable[str]] = ..., difficulty: _Optional[int] = ...) -> None: ...
    class StatementChange(_message.Message):
        __slots__ = ("locale", "title", "statement")
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        STATEMENT_FIELD_NUMBER: _ClassVar[int]
        locale: str
        title: str
        statement: _content_pb2.Content
        def __init__(self, locale: _Optional[str] = ..., title: _Optional[str] = ..., statement: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
    class EditorialChange(_message.Message):
        __slots__ = ("locale", "editorial")
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        EDITORIAL_FIELD_NUMBER: _ClassVar[int]
        locale: str
        editorial: _content_pb2.Content
        def __init__(self, locale: _Optional[str] = ..., editorial: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_CHANGE_FIELD_NUMBER: _ClassVar[int]
    EDITORIAL_CHANGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: Suggestion.Status
    version: int
    member_id: str
    contribution: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    classification: Suggestion.Classification
    statement_change: Suggestion.StatementChange
    editorial_change: Suggestion.EditorialChange
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Suggestion.Status, str]] = ..., version: _Optional[int] = ..., member_id: _Optional[str] = ..., contribution: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., classification: _Optional[_Union[Suggestion.Classification, _Mapping]] = ..., statement_change: _Optional[_Union[Suggestion.StatementChange, _Mapping]] = ..., editorial_change: _Optional[_Union[Suggestion.EditorialChange, _Mapping]] = ...) -> None: ...
