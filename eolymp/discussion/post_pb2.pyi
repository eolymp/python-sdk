from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.ecm import node_pb2 as _node_pb2
from eolymp.wellknown import link_pb2 as _link_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Post(_message.Message):
    __slots__ = ["created_at", "id", "image", "labels", "links", "locale", "member_id", "message", "moderation", "preview", "published_at", "reply_count", "status", "title", "type_id", "updated_at", "url", "user_id", "vote", "vote_count"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Moderation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Image(_message.Message):
        __slots__ = ["height", "src", "width"]
        CLASS_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        SRC_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        height: int
        src: str
        width: int
        def __init__(self, src: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., **kwargs) -> None: ...
    APPROVED: Post.Moderation
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DRAFT: Post.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    IN_REVIEW: Post.Moderation
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_RENDER: Post.Extra
    MESSAGE_VALUE: Post.Extra
    MODERATION_FIELD_NUMBER: _ClassVar[int]
    PENDING: Post.Moderation
    PREVIEW: Post.Extra
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED: Post.Status
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    REJECTED: Post.Moderation
    REPLY_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Post.Extra
    UNKNOWN_MODERATION: Post.Moderation
    UNKNOWN_STATUS: Post.Status
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE: Post.Extra
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    id: str
    image: Post.Image
    labels: _containers.RepeatedScalarFieldContainer[str]
    links: _containers.RepeatedCompositeFieldContainer[_link_pb2.Link]
    locale: str
    member_id: str
    message: _content_pb2.Content
    moderation: Post.Moderation
    preview: _node_pb2.Node
    published_at: _timestamp_pb2.Timestamp
    reply_count: int
    status: Post.Status
    title: str
    type_id: str
    updated_at: _timestamp_pb2.Timestamp
    url: str
    user_id: str
    vote: int
    vote_count: int
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., status: _Optional[_Union[Post.Status, str]] = ..., moderation: _Optional[_Union[Post.Moderation, str]] = ..., type_id: _Optional[str] = ..., user_id: _Optional[str] = ..., member_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., published_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., locale: _Optional[str] = ..., title: _Optional[str] = ..., image: _Optional[_Union[Post.Image, _Mapping]] = ..., preview: _Optional[_Union[_node_pb2.Node, _Mapping]] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., vote: _Optional[int] = ..., vote_count: _Optional[int] = ..., reply_count: _Optional[int] = ..., labels: _Optional[_Iterable[str]] = ..., links: _Optional[_Iterable[_Union[_link_pb2.Link, _Mapping]]] = ...) -> None: ...
