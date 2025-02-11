from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Reply(_message.Message):
    __slots__ = ("id", "ticket_id", "user_id", "member_id", "message", "created_at")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Reply.Extra]
        MESSAGE_RENDER: _ClassVar[Reply.Extra]
        MESSAGE_VALUE: _ClassVar[Reply.Extra]
    NO_EXTRA: Reply.Extra
    MESSAGE_RENDER: Reply.Extra
    MESSAGE_VALUE: Reply.Extra
    ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ticket_id: str
    user_id: str
    member_id: str
    message: _content_pb2.Content
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., ticket_id: _Optional[str] = ..., user_id: _Optional[str] = ..., member_id: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
