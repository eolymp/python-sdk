from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Solution(_message.Message):
    __slots__ = ["author_id", "content", "format", "id", "locale", "moderation_comment", "moderation_status", "problem_id", "published"]
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Moderation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    APPROVED: Solution.Moderation
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DRAFT: Solution.Moderation
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    HTML: Solution.Format
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MARKDOWN: Solution.Format
    MODERATION_COMMENT_FIELD_NUMBER: _ClassVar[int]
    MODERATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    NONE: Solution.Format
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    REJECTED: Solution.Moderation
    REVIEW: Solution.Moderation
    TEX: Solution.Format
    author_id: str
    content: str
    format: Solution.Format
    id: str
    locale: str
    moderation_comment: str
    moderation_status: Solution.Moderation
    problem_id: str
    published: bool
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., author_id: _Optional[str] = ..., published: bool = ..., moderation_status: _Optional[_Union[Solution.Moderation, str]] = ..., moderation_comment: _Optional[str] = ..., locale: _Optional[str] = ..., format: _Optional[_Union[Solution.Format, str]] = ..., content: _Optional[str] = ...) -> None: ...
