from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Suggestion(_message.Message):
    __slots__ = ["difficulty", "editorial", "id", "locale", "member_id", "problem_id", "statement", "status", "topics"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    APPROVED: Suggestion.Status
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IN_REVIEW: Suggestion.Status
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PENDING: Suggestion.Status
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    REJECTED: Suggestion.Status
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STATUS: Suggestion.Status
    difficulty: int
    editorial: _content_pb2.Content
    id: str
    locale: str
    member_id: str
    problem_id: str
    statement: _content_pb2.Content
    status: Suggestion.Status
    topics: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Suggestion.Status, str]] = ..., problem_id: _Optional[str] = ..., locale: _Optional[str] = ..., member_id: _Optional[str] = ..., topics: _Optional[_Iterable[str]] = ..., difficulty: _Optional[int] = ..., statement: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., editorial: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
