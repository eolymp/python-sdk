import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Notebook(_message.Message):
    __slots__ = ("id", "member_id", "name", "type", "status", "content_url", "created_at", "reviewed_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Notebook.Status]
        PENDING: _ClassVar[Notebook.Status]
        APPROVED: _ClassVar[Notebook.Status]
        REJECTED: _ClassVar[Notebook.Status]
    UNKNOWN_STATUS: Notebook.Status
    PENDING: Notebook.Status
    APPROVED: Notebook.Status
    REJECTED: Notebook.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    REVIEWED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    member_id: str
    name: str
    type: str
    status: Notebook.Status
    content_url: str
    created_at: _timestamp_pb2.Timestamp
    reviewed_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., status: _Optional[_Union[Notebook.Status, str]] = ..., content_url: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reviewed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
