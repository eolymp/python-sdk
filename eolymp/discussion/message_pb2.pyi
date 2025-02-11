from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.wellknown import link_pb2 as _link_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ("id", "url", "thread_url", "member_id", "reply_to", "vote", "vote_count", "reply_count", "posted_at", "edited_at", "deleted_at", "revision", "message", "links")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Message.Extra]
        MESSAGE_VALUE: _ClassVar[Message.Extra]
        MESSAGE_RENDER: _ClassVar[Message.Extra]
        MESSAGE_PREVIEW: _ClassVar[Message.Extra]
        VOTE: _ClassVar[Message.Extra]
    UNKNOWN_EXTRA: Message.Extra
    MESSAGE_VALUE: Message.Extra
    MESSAGE_RENDER: Message.Extra
    MESSAGE_PREVIEW: Message.Extra
    VOTE: Message.Extra
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    THREAD_URL_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPLY_COUNT_FIELD_NUMBER: _ClassVar[int]
    POSTED_AT_FIELD_NUMBER: _ClassVar[int]
    EDITED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    thread_url: str
    member_id: str
    reply_to: str
    vote: int
    vote_count: int
    reply_count: int
    posted_at: _timestamp_pb2.Timestamp
    edited_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    revision: int
    message: _content_pb2.Content
    links: _containers.RepeatedCompositeFieldContainer[_link_pb2.Link]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., thread_url: _Optional[str] = ..., member_id: _Optional[str] = ..., reply_to: _Optional[str] = ..., vote: _Optional[int] = ..., vote_count: _Optional[int] = ..., reply_count: _Optional[int] = ..., posted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., edited_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., revision: _Optional[int] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., links: _Optional[_Iterable[_Union[_link_pb2.Link, _Mapping]]] = ...) -> None: ...
