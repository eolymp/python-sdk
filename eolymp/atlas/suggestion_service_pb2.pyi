from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.atlas import suggestion_pb2 as _suggestion_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SuggestionChangedEvent(_message.Message):
    __slots__ = ("problem_id", "before", "after")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    before: _suggestion_pb2.Suggestion
    after: _suggestion_pb2.Suggestion
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_suggestion_pb2.Suggestion, _Mapping]] = ..., after: _Optional[_Union[_suggestion_pb2.Suggestion, _Mapping]] = ...) -> None: ...

class CreateSuggestionInput(_message.Message):
    __slots__ = ("suggestion",)
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    suggestion: _suggestion_pb2.Suggestion
    def __init__(self, suggestion: _Optional[_Union[_suggestion_pb2.Suggestion, _Mapping]] = ...) -> None: ...

class CreateSuggestionOutput(_message.Message):
    __slots__ = ("suggestion_id",)
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    suggestion_id: str
    def __init__(self, suggestion_id: _Optional[str] = ...) -> None: ...

class UpdateSuggestionInput(_message.Message):
    __slots__ = ("suggestion_id", "suggestion")
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    suggestion_id: str
    suggestion: _suggestion_pb2.Suggestion
    def __init__(self, suggestion_id: _Optional[str] = ..., suggestion: _Optional[_Union[_suggestion_pb2.Suggestion, _Mapping]] = ...) -> None: ...

class UpdateSuggestionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteSuggestionInput(_message.Message):
    __slots__ = ("suggestion_id",)
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    suggestion_id: str
    def __init__(self, suggestion_id: _Optional[str] = ...) -> None: ...

class DeleteSuggestionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReviewSuggestionInput(_message.Message):
    __slots__ = ("suggestion_id", "status", "comment")
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    suggestion_id: str
    status: _suggestion_pb2.Suggestion.Status
    comment: _content_pb2.Content
    def __init__(self, suggestion_id: _Optional[str] = ..., status: _Optional[_Union[_suggestion_pb2.Suggestion.Status, str]] = ..., comment: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class ReviewSuggestionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResubmitSuggestionInput(_message.Message):
    __slots__ = ("suggestion_id",)
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    suggestion_id: str
    def __init__(self, suggestion_id: _Optional[str] = ...) -> None: ...

class ResubmitSuggestionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSuggestionsInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "member_id", "status")
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListSuggestionsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSuggestionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListSuggestionsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_suggestion_pb2.Suggestion]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_suggestion_pb2.Suggestion, _Mapping]]] = ...) -> None: ...

class DescribeSuggestionInput(_message.Message):
    __slots__ = ("suggestion_id",)
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    suggestion_id: str
    def __init__(self, suggestion_id: _Optional[str] = ...) -> None: ...

class DescribeSuggestionOutput(_message.Message):
    __slots__ = ("suggestion",)
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    suggestion: _suggestion_pb2.Suggestion
    def __init__(self, suggestion: _Optional[_Union[_suggestion_pb2.Suggestion, _Mapping]] = ...) -> None: ...
