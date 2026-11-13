import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Feedback(_message.Message):
    __slots__ = ("id", "fragment_id", "fragment_locale", "helpful", "comment", "block_index", "block_text", "member_id", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_LOCALE_FIELD_NUMBER: _ClassVar[int]
    HELPFUL_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
    BLOCK_TEXT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    fragment_id: str
    fragment_locale: str
    helpful: bool
    comment: str
    block_index: int
    block_text: str
    member_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., fragment_id: _Optional[str] = ..., fragment_locale: _Optional[str] = ..., helpful: _Optional[bool] = ..., comment: _Optional[str] = ..., block_index: _Optional[int] = ..., block_text: _Optional[str] = ..., member_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
