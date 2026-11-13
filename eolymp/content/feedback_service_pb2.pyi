from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.content import content_feedback_pb2 as _content_feedback_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFeedbackInput(_message.Message):
    __slots__ = ("fragment_id", "feedback")
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    feedback: _content_feedback_pb2.Feedback
    def __init__(self, fragment_id: _Optional[str] = ..., feedback: _Optional[_Union[_content_feedback_pb2.Feedback, _Mapping]] = ...) -> None: ...

class CreateFeedbackOutput(_message.Message):
    __slots__ = ("feedback_id",)
    FEEDBACK_ID_FIELD_NUMBER: _ClassVar[int]
    feedback_id: str
    def __init__(self, feedback_id: _Optional[str] = ...) -> None: ...

class DescribeFeedbackInput(_message.Message):
    __slots__ = ("feedback_id",)
    FEEDBACK_ID_FIELD_NUMBER: _ClassVar[int]
    feedback_id: str
    def __init__(self, feedback_id: _Optional[str] = ...) -> None: ...

class DescribeFeedbackOutput(_message.Message):
    __slots__ = ("feedback",)
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    feedback: _content_feedback_pb2.Feedback
    def __init__(self, feedback: _Optional[_Union[_content_feedback_pb2.Feedback, _Mapping]] = ...) -> None: ...

class DeleteFeedbackInput(_message.Message):
    __slots__ = ("feedback_id",)
    FEEDBACK_ID_FIELD_NUMBER: _ClassVar[int]
    feedback_id: str
    def __init__(self, feedback_id: _Optional[str] = ...) -> None: ...

class DeleteFeedbackOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListFeedbackInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("fragment_id", "helpful", "has_comment", "block_index", "fragment_locale", "created_at")
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        HELPFUL_FIELD_NUMBER: _ClassVar[int]
        HAS_COMMENT_FIELD_NUMBER: _ClassVar[int]
        BLOCK_INDEX_FIELD_NUMBER: _ClassVar[int]
        FRAGMENT_LOCALE_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        fragment_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        helpful: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        has_comment: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        block_index: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        fragment_locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        created_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        def __init__(self, fragment_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., helpful: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., has_comment: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., block_index: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., fragment_locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., created_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListFeedbackInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListFeedbackInput.Filter, _Mapping]] = ...) -> None: ...

class ListFeedbackOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_content_feedback_pb2.Feedback]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_content_feedback_pb2.Feedback, _Mapping]]] = ...) -> None: ...
