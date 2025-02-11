from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.discussion import post_pb2 as _post_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostChangedEvent(_message.Message):
    __slots__ = ("before", "after", "reason")
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    before: _post_pb2.Post
    after: _post_pb2.Post
    reason: _content_pb2.Content
    def __init__(self, before: _Optional[_Union[_post_pb2.Post, _Mapping]] = ..., after: _Optional[_Union[_post_pb2.Post, _Mapping]] = ..., reason: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class PostPublishedEvent(_message.Message):
    __slots__ = ("published", "post", "reason")
    PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    POST_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    published: bool
    post: _post_pb2.Post
    reason: _content_pb2.Content
    def __init__(self, published: bool = ..., post: _Optional[_Union[_post_pb2.Post, _Mapping]] = ..., reason: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class PostTranslationChangedEvent(_message.Message):
    __slots__ = ("post_id", "before", "after", "reason")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    before: _post_pb2.Post.Translation
    after: _post_pb2.Post.Translation
    reason: _content_pb2.Content
    def __init__(self, post_id: _Optional[str] = ..., before: _Optional[_Union[_post_pb2.Post.Translation, _Mapping]] = ..., after: _Optional[_Union[_post_pb2.Post.Translation, _Mapping]] = ..., reason: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class DescribePostInput(_message.Message):
    __slots__ = ("post_id", "locale", "extra")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_post_pb2.Post.Extra]
    def __init__(self, post_id: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_post_pb2.Post.Extra, str]]] = ...) -> None: ...

class DescribePostOutput(_message.Message):
    __slots__ = ("post",)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: _post_pb2.Post
    def __init__(self, post: _Optional[_Union[_post_pb2.Post, _Mapping]] = ...) -> None: ...

class ListPostsInput(_message.Message):
    __slots__ = ("after", "size", "offset", "sort", "order", "filters", "locale", "extra")
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_SORT: _ClassVar[ListPostsInput.Sort]
        PUBLISHED_AT: _ClassVar[ListPostsInput.Sort]
        CREATED_AT: _ClassVar[ListPostsInput.Sort]
        VOTE_COUNT: _ClassVar[ListPostsInput.Sort]
        REPLY_COUNT: _ClassVar[ListPostsInput.Sort]
        POPULARITY: _ClassVar[ListPostsInput.Sort]
    UNKNOWN_SORT: ListPostsInput.Sort
    PUBLISHED_AT: ListPostsInput.Sort
    CREATED_AT: ListPostsInput.Sort
    VOTE_COUNT: ListPostsInput.Sort
    REPLY_COUNT: ListPostsInput.Sort
    POPULARITY: ListPostsInput.Sort
    class Filter(_message.Message):
        __slots__ = ("query", "id", "source_id", "user_id", "member_id", "type_id", "created_at", "published_at", "draft", "public", "featured", "moderation", "locale", "label")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_ID_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        PUBLISHED_AT_FIELD_NUMBER: _ClassVar[int]
        DRAFT_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_FIELD_NUMBER: _ClassVar[int]
        FEATURED_FIELD_NUMBER: _ClassVar[int]
        MODERATION_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        source_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        type_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        created_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        published_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        draft: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        public: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        featured: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        moderation: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        label: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., source_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., type_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., created_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., published_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., draft: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., public: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., featured: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., moderation: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., label: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    after: str
    size: int
    offset: int
    sort: ListPostsInput.Sort
    order: _direction_pb2.Direction
    filters: ListPostsInput.Filter
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_post_pb2.Post.Extra]
    def __init__(self, after: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ..., sort: _Optional[_Union[ListPostsInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., filters: _Optional[_Union[ListPostsInput.Filter, _Mapping]] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_post_pb2.Post.Extra, str]]] = ...) -> None: ...

class ListPostsOutput(_message.Message):
    __slots__ = ("total", "items", "next_page_cursor")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_post_pb2.Post]
    next_page_cursor: str
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_post_pb2.Post, _Mapping]]] = ..., next_page_cursor: _Optional[str] = ...) -> None: ...

class CreatePostInput(_message.Message):
    __slots__ = ("post",)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: _post_pb2.Post
    def __init__(self, post: _Optional[_Union[_post_pb2.Post, _Mapping]] = ...) -> None: ...

class CreatePostOutput(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class UpdatePostInput(_message.Message):
    __slots__ = ("patch", "post_id", "post")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdatePostInput.Patch]
        CONTENT: _ClassVar[UpdatePostInput.Patch]
        LABELS: _ClassVar[UpdatePostInput.Patch]
        TYPE_ID: _ClassVar[UpdatePostInput.Patch]
        LOCALE: _ClassVar[UpdatePostInput.Patch]
        DRAFT: _ClassVar[UpdatePostInput.Patch]
        FEATURED: _ClassVar[UpdatePostInput.Patch]
        PINNED: _ClassVar[UpdatePostInput.Patch]
        MODERATION: _ClassVar[UpdatePostInput.Patch]
    ALL: UpdatePostInput.Patch
    CONTENT: UpdatePostInput.Patch
    LABELS: UpdatePostInput.Patch
    TYPE_ID: UpdatePostInput.Patch
    LOCALE: UpdatePostInput.Patch
    DRAFT: UpdatePostInput.Patch
    FEATURED: UpdatePostInput.Patch
    PINNED: UpdatePostInput.Patch
    MODERATION: UpdatePostInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    POST_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdatePostInput.Patch]
    post_id: str
    post: _post_pb2.Post
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdatePostInput.Patch, str]]] = ..., post_id: _Optional[str] = ..., post: _Optional[_Union[_post_pb2.Post, _Mapping]] = ...) -> None: ...

class UpdatePostOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PublishPostInput(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class PublishPostOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnpublishPostInput(_message.Message):
    __slots__ = ("post_id", "reason")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    reason: _content_pb2.Content
    def __init__(self, post_id: _Optional[str] = ..., reason: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class UnpublishPostOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ModeratePostInput(_message.Message):
    __slots__ = ("post_id", "outcome", "reason")
    class Outcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_OUTCOME: _ClassVar[ModeratePostInput.Outcome]
        APPROVED: _ClassVar[ModeratePostInput.Outcome]
        REJECTED: _ClassVar[ModeratePostInput.Outcome]
        IN_REVIEW: _ClassVar[ModeratePostInput.Outcome]
    UNKNOWN_OUTCOME: ModeratePostInput.Outcome
    APPROVED: ModeratePostInput.Outcome
    REJECTED: ModeratePostInput.Outcome
    IN_REVIEW: ModeratePostInput.Outcome
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    outcome: ModeratePostInput.Outcome
    reason: _content_pb2.Content
    def __init__(self, post_id: _Optional[str] = ..., outcome: _Optional[_Union[ModeratePostInput.Outcome, str]] = ..., reason: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class ModeratePostOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeletePostInput(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class DeletePostOutput(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: _content_pb2.Content
    def __init__(self, reason: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class VotePostInput(_message.Message):
    __slots__ = ("post_id", "vote")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    vote: int
    def __init__(self, post_id: _Optional[str] = ..., vote: _Optional[int] = ...) -> None: ...

class VotePostOutput(_message.Message):
    __slots__ = ("vote_count",)
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    vote_count: int
    def __init__(self, vote_count: _Optional[int] = ...) -> None: ...

class TranslatePostInput(_message.Message):
    __slots__ = ("post_id", "source", "target", "target_automatic", "override_manual")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_MANUAL_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    source: str
    target: _containers.RepeatedScalarFieldContainer[str]
    target_automatic: bool
    override_manual: bool
    def __init__(self, post_id: _Optional[str] = ..., source: _Optional[str] = ..., target: _Optional[_Iterable[str]] = ..., target_automatic: bool = ..., override_manual: bool = ...) -> None: ...

class TranslatePostOutput(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class DescribePostTranslationInput(_message.Message):
    __slots__ = ("post_id", "translation_id", "extra")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    translation_id: str
    extra: _containers.RepeatedScalarFieldContainer[_post_pb2.Post.Extra]
    def __init__(self, post_id: _Optional[str] = ..., translation_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_post_pb2.Post.Extra, str]]] = ...) -> None: ...

class DescribePostTranslationOutput(_message.Message):
    __slots__ = ("translation",)
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    translation: _post_pb2.Post.Translation
    def __init__(self, translation: _Optional[_Union[_post_pb2.Post.Translation, _Mapping]] = ...) -> None: ...

class ListPostTranslationsInput(_message.Message):
    __slots__ = ("post_id", "offset", "size", "filters", "extra")
    class Filter(_message.Message):
        __slots__ = ("query", "id", "locale")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    offset: int
    size: int
    filters: ListPostTranslationsInput.Filter
    extra: _containers.RepeatedScalarFieldContainer[_post_pb2.Post.Extra]
    def __init__(self, post_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListPostTranslationsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_post_pb2.Post.Extra, str]]] = ...) -> None: ...

class ListPostTranslationsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_post_pb2.Post.Translation]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_post_pb2.Post.Translation, _Mapping]]] = ...) -> None: ...

class CreatePostTranslationInput(_message.Message):
    __slots__ = ("post_id", "translation")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    translation: _post_pb2.Post.Translation
    def __init__(self, post_id: _Optional[str] = ..., translation: _Optional[_Union[_post_pb2.Post.Translation, _Mapping]] = ...) -> None: ...

class CreatePostTranslationOutput(_message.Message):
    __slots__ = ("translation_id",)
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    translation_id: str
    def __init__(self, translation_id: _Optional[str] = ...) -> None: ...

class UpdatePostTranslationInput(_message.Message):
    __slots__ = ("patch", "post_id", "translation_id", "translation")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdatePostTranslationInput.Patch]
        CONTENT: _ClassVar[UpdatePostTranslationInput.Patch]
        LABELS: _ClassVar[UpdatePostTranslationInput.Patch]
        LOCALE: _ClassVar[UpdatePostTranslationInput.Patch]
    ALL: UpdatePostTranslationInput.Patch
    CONTENT: UpdatePostTranslationInput.Patch
    LABELS: UpdatePostTranslationInput.Patch
    LOCALE: UpdatePostTranslationInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdatePostTranslationInput.Patch]
    post_id: str
    translation_id: str
    translation: _post_pb2.Post.Translation
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdatePostTranslationInput.Patch, str]]] = ..., post_id: _Optional[str] = ..., translation_id: _Optional[str] = ..., translation: _Optional[_Union[_post_pb2.Post.Translation, _Mapping]] = ...) -> None: ...

class UpdatePostTranslationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeletePostTranslationInput(_message.Message):
    __slots__ = ("post_id", "translation_id")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    translation_id: str
    def __init__(self, post_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class DeletePostTranslationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
