from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.wellknown import link_pb2 as _link_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Post(_message.Message):
    __slots__ = ["created_at", "id", "labels", "links", "member_id", "message", "published_at", "status", "title", "updated_at", "url", "user_id"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DRAFT: Post.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    IN_REVIEW: Post.Status
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_PREVIEW: Post.Extra
    MESSAGE_RENDER: Post.Extra
    MESSAGE_VALUE: Post.Extra
    PUBLISHED: Post.Status
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    REJECTED: Post.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Post.Extra
    UNKNOWN_STATUS: Post.Status
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    id: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    links: _containers.RepeatedCompositeFieldContainer[_link_pb2.Link]
    member_id: str
    message: _content_pb2.Content
    published_at: _timestamp_pb2.Timestamp
    status: Post.Status
    title: str
    updated_at: _timestamp_pb2.Timestamp
    url: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., status: _Optional[_Union[Post.Status, str]] = ..., user_id: _Optional[str] = ..., member_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., published_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., title: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ..., links: _Optional[_Iterable[_Union[_link_pb2.Link, _Mapping]]] = ...) -> None: ...
