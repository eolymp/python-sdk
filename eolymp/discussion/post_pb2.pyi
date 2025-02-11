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
    __slots__ = ("id", "url", "source_id", "source_url", "draft", "public", "featured", "pinned", "moderation", "user_id", "member_id", "created_at", "published_at", "updated_at", "type_id", "locale", "title", "image_url", "content", "preview", "vote", "vote_count", "reply_count", "labels", "links")
    class Moderation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_MODERATION: _ClassVar[Post.Moderation]
        PENDING: _ClassVar[Post.Moderation]
        IN_REVIEW: _ClassVar[Post.Moderation]
        APPROVED: _ClassVar[Post.Moderation]
        REJECTED: _ClassVar[Post.Moderation]
    UNKNOWN_MODERATION: Post.Moderation
    PENDING: Post.Moderation
    IN_REVIEW: Post.Moderation
    APPROVED: Post.Moderation
    REJECTED: Post.Moderation
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Post.Extra]
        CONTENT_VALUE: _ClassVar[Post.Extra]
        CONTENT_RENDER: _ClassVar[Post.Extra]
        PREVIEW: _ClassVar[Post.Extra]
        VOTE: _ClassVar[Post.Extra]
    UNKNOWN_EXTRA: Post.Extra
    CONTENT_VALUE: Post.Extra
    CONTENT_RENDER: Post.Extra
    PREVIEW: Post.Extra
    VOTE: Post.Extra
    class Translation(_message.Message):
        __slots__ = ("id", "locale", "content", "labels", "automatic")
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        id: str
        locale: str
        content: _content_pb2.Content
        labels: _containers.RepeatedScalarFieldContainer[str]
        automatic: bool
        def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ..., automatic: bool = ...) -> None: ...
    class Image(_message.Message):
        __slots__ = ("src", "width", "height")
        SRC_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        CLASS_FIELD_NUMBER: _ClassVar[int]
        src: str
        width: int
        height: int
        def __init__(self, src: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., **kwargs) -> None: ...
    class Preview(_message.Message):
        __slots__ = ("title", "image", "content")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        title: str
        image: Post.Image
        content: _node_pb2.Node
        def __init__(self, title: _Optional[str] = ..., image: _Optional[_Union[Post.Image, _Mapping]] = ..., content: _Optional[_Union[_node_pb2.Node, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    FEATURED_FIELD_NUMBER: _ClassVar[int]
    PINNED_FIELD_NUMBER: _ClassVar[int]
    MODERATION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPLY_COUNT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    source_id: str
    source_url: str
    draft: bool
    public: bool
    featured: bool
    pinned: bool
    moderation: Post.Moderation
    user_id: str
    member_id: str
    created_at: _timestamp_pb2.Timestamp
    published_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    type_id: str
    locale: str
    title: str
    image_url: str
    content: _content_pb2.Content
    preview: Post.Preview
    vote: int
    vote_count: int
    reply_count: int
    labels: _containers.RepeatedScalarFieldContainer[str]
    links: _containers.RepeatedCompositeFieldContainer[_link_pb2.Link]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., source_id: _Optional[str] = ..., source_url: _Optional[str] = ..., draft: bool = ..., public: bool = ..., featured: bool = ..., pinned: bool = ..., moderation: _Optional[_Union[Post.Moderation, str]] = ..., user_id: _Optional[str] = ..., member_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., published_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type_id: _Optional[str] = ..., locale: _Optional[str] = ..., title: _Optional[str] = ..., image_url: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., preview: _Optional[_Union[Post.Preview, _Mapping]] = ..., vote: _Optional[int] = ..., vote_count: _Optional[int] = ..., reply_count: _Optional[int] = ..., labels: _Optional[_Iterable[str]] = ..., links: _Optional[_Iterable[_Union[_link_pb2.Link, _Mapping]]] = ...) -> None: ...
