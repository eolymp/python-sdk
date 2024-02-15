from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.wellknown import link_pb2 as _link_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ["edited_at", "id", "links", "member_id", "message", "posted_at", "reply_count", "reply_to", "thread_url", "url", "vote", "vote_count"]
    EDITED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    POSTED_AT_FIELD_NUMBER: _ClassVar[int]
    REPLY_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    THREAD_URL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    edited_at: _timestamp_pb2.Timestamp
    id: str
    links: _containers.RepeatedCompositeFieldContainer[_link_pb2.Link]
    member_id: str
    message: _content_pb2.Content
    posted_at: _timestamp_pb2.Timestamp
    reply_count: int
    reply_to: str
    thread_url: str
    url: str
    vote: int
    vote_count: int
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., thread_url: _Optional[str] = ..., member_id: _Optional[str] = ..., reply_to: _Optional[str] = ..., vote: _Optional[int] = ..., vote_count: _Optional[int] = ..., reply_count: _Optional[int] = ..., posted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., edited_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., links: _Optional[_Iterable[_Union[_link_pb2.Link, _Mapping]]] = ...) -> None: ...
