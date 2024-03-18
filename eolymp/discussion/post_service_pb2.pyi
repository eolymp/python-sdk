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

class CreatePostTranslationInput(_message.Message):
    __slots__ = ["post_id", "translation"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    translation: _post_pb2.Post.Translation
    def __init__(self, post_id: _Optional[str] = ..., translation: _Optional[_Union[_post_pb2.Post.Translation, _Mapping]] = ...) -> None: ...

class CreatePostTranslationOutput(_message.Message):
    __slots__ = ["translation_id"]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    translation_id: str
    def __init__(self, translation_id: _Optional[str] = ...) -> None: ...

class DeletePostInput(_message.Message):
    __slots__ = ["post_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class DeletePostOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeletePostTranslationInput(_message.Message):
    __slots__ = ["post_id", "translation_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    translation_id: str
    def __init__(self, post_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class DeletePostTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribePostInput(_message.Message):
    __slots__ = ["extra", "locale", "post_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_post_pb2.Post.Extra]
    locale: str
    post_id: str
    def __init__(self, post_id: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_post_pb2.Post.Extra, str]]] = ...) -> None: ...

class DescribePostOutput(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: _post_pb2.Post
    def __init__(self, post: _Optional[_Union[_post_pb2.Post, _Mapping]] = ...) -> None: ...

class DescribePostTranslationInput(_message.Message):
    __slots__ = ["extra", "post_id", "translation_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_post_pb2.Post.Extra]
    post_id: str
    translation_id: str
    def __init__(self, post_id: _Optional[str] = ..., translation_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_post_pb2.Post.Extra, str]]] = ...) -> None: ...

class DescribePostTranslationOutput(_message.Message):
    __slots__ = ["translation"]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    translation: _post_pb2.Post.Translation
    def __init__(self, translation: _Optional[_Union[_post_pb2.Post.Translation, _Mapping]] = ...) -> None: ...

class ListPostTranslationsInput(_message.Message):
    __slots__ = ["extra", "filters", "offset", "post_id", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "locale", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_post_pb2.Post.Extra]
    filters: ListPostTranslationsInput.Filter
    offset: int
    post_id: str
    size: int
    def __init__(self, post_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListPostTranslationsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_post_pb2.Post.Extra, str]]] = ...) -> None: ...

class ListPostTranslationsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_post_pb2.Post.Translation]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_post_pb2.Post.Translation, _Mapping]]] = ...) -> None: ...

class ListPostsInput(_message.Message):
    __slots__ = ["after", "extra", "filters", "locale", "offset", "order", "size", "sort"]
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["created_at", "draft", "id", "label", "locale", "member_id", "moderation", "public", "published_at", "query", "source_id", "type_id", "user_id"]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        DRAFT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        MODERATION_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_FIELD_NUMBER: _ClassVar[int]
        PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        created_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        draft: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        label: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        moderation: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        public: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        published_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        query: str
        source_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        type_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., source_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., type_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., created_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., published_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., draft: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., public: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., moderation: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., label: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT: ListPostsInput.Sort
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    POPULARITY: ListPostsInput.Sort
    PUBLISHED_AT: ListPostsInput.Sort
    REPLY_COUNT: ListPostsInput.Sort
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_SORT: ListPostsInput.Sort
    VOTE_COUNT: ListPostsInput.Sort
    after: str
    extra: _containers.RepeatedScalarFieldContainer[_post_pb2.Post.Extra]
    filters: ListPostsInput.Filter
    locale: str
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListPostsInput.Sort
    def __init__(self, after: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ..., sort: _Optional[_Union[ListPostsInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., filters: _Optional[_Union[ListPostsInput.Filter, _Mapping]] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_post_pb2.Post.Extra, str]]] = ...) -> None: ...

class ListPostsOutput(_message.Message):
    __slots__ = ["items", "next_page_cursor", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_post_pb2.Post]
    next_page_cursor: str
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_post_pb2.Post, _Mapping]]] = ..., next_page_cursor: _Optional[str] = ...) -> None: ...

class UpdatePostInput(_message.Message):
    __slots__ = ["patch", "post", "post_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdatePostInput.Patch
    CONTENT: UpdatePostInput.Patch
    DRAFT: UpdatePostInput.Patch
    LABELS: UpdatePostInput.Patch
    LOCALE: UpdatePostInput.Patch
    MODERATION: UpdatePostInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    POST_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID: UpdatePostInput.Patch
    patch: _containers.RepeatedScalarFieldContainer[UpdatePostInput.Patch]
    post: _post_pb2.Post
    post_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdatePostInput.Patch, str]]] = ..., post_id: _Optional[str] = ..., post: _Optional[_Union[_post_pb2.Post, _Mapping]] = ...) -> None: ...

class UpdatePostOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdatePostTranslationInput(_message.Message):
    __slots__ = ["patch", "post_id", "translation", "translation_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdatePostTranslationInput.Patch
    CONTENT: UpdatePostTranslationInput.Patch
    LABELS: UpdatePostTranslationInput.Patch
    LOCALE: UpdatePostTranslationInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdatePostTranslationInput.Patch]
    post_id: str
    translation: _post_pb2.Post.Translation
    translation_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdatePostTranslationInput.Patch, str]]] = ..., post_id: _Optional[str] = ..., translation_id: _Optional[str] = ..., translation: _Optional[_Union[_post_pb2.Post.Translation, _Mapping]] = ...) -> None: ...

class UpdatePostTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VotePostInput(_message.Message):
    __slots__ = ["post_id", "vote"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    vote: int
    def __init__(self, post_id: _Optional[str] = ..., vote: _Optional[int] = ...) -> None: ...

class VotePostOutput(_message.Message):
    __slots__ = ["vote_count"]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    vote_count: int
    def __init__(self, vote_count: _Optional[int] = ...) -> None: ...
