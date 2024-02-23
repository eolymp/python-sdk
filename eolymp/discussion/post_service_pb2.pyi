from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.discussion import post_pb2 as _post_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePostInput(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: _post_pb2.Post
    def __init__(self, post: _Optional[_Union[_post_pb2.Post, _Mapping]] = ...) -> None: ...

class CreatePostOutput(_message.Message):
    __slots__ = ["post_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class DeletePostInput(_message.Message):
    __slots__ = ["post_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class DeletePostOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribePostInput(_message.Message):
    __slots__ = ["extra", "post_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_post_pb2.Post.Extra]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_post_pb2.Post.Extra, str]]] = ...) -> None: ...

class DescribePostOutput(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: _post_pb2.Post
    def __init__(self, post: _Optional[_Union[_post_pb2.Post, _Mapping]] = ...) -> None: ...

class ListPostsInput(_message.Message):
    __slots__ = ["after", "extra", "filters", "order", "size", "sort"]
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["created_at", "id", "member_id", "published_at", "query", "status", "user_id"]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        created_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        published_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        query: str
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., created_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., published_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT: ListPostsInput.Sort
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_AT: ListPostsInput.Sort
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_SORT: ListPostsInput.Sort
    after: str
    extra: _containers.RepeatedScalarFieldContainer[_post_pb2.Post.Extra]
    filters: ListPostsInput.Filter
    order: _direction_pb2.Direction
    size: int
    sort: ListPostsInput.Sort
    def __init__(self, after: _Optional[str] = ..., size: _Optional[int] = ..., sort: _Optional[_Union[ListPostsInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., filters: _Optional[_Union[ListPostsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_post_pb2.Post.Extra, str]]] = ...) -> None: ...

class ListPostsOutput(_message.Message):
    __slots__ = ["has_more", "items"]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    has_more: bool
    items: _containers.RepeatedCompositeFieldContainer[_post_pb2.Post]
    def __init__(self, items: _Optional[_Iterable[_Union[_post_pb2.Post, _Mapping]]] = ..., has_more: bool = ...) -> None: ...

class UpdatePostInput(_message.Message):
    __slots__ = ["post", "post_id"]
    POST_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post: _post_pb2.Post
    post_id: str
    def __init__(self, post_id: _Optional[str] = ..., post: _Optional[_Union[_post_pb2.Post, _Mapping]] = ...) -> None: ...

class UpdatePostOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
