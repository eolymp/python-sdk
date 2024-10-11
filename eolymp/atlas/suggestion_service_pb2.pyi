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

class CreateSuggestionInput(_message.Message):
    __slots__ = ["suggestion"]
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    suggestion: _suggestion_pb2.Suggestion
    def __init__(self, suggestion: _Optional[_Union[_suggestion_pb2.Suggestion, _Mapping]] = ...) -> None: ...

class CreateSuggestionOutput(_message.Message):
    __slots__ = ["suggestion_id"]
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    suggestion_id: str
    def __init__(self, suggestion_id: _Optional[str] = ...) -> None: ...

class DeleteSuggestionInput(_message.Message):
    __slots__ = ["suggestion_id"]
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    suggestion_id: str
    def __init__(self, suggestion_id: _Optional[str] = ...) -> None: ...

class DeleteSuggestionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeSuggestionInput(_message.Message):
    __slots__ = ["suggestion_id"]
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    suggestion_id: str
    def __init__(self, suggestion_id: _Optional[str] = ...) -> None: ...

class DescribeSuggestionOutput(_message.Message):
    __slots__ = ["suggestion"]
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    suggestion: _suggestion_pb2.Suggestion
    def __init__(self, suggestion: _Optional[_Union[_suggestion_pb2.Suggestion, _Mapping]] = ...) -> None: ...

class ListSuggestionsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "member_id", "status"]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListSuggestionsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSuggestionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListSuggestionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_suggestion_pb2.Suggestion]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_suggestion_pb2.Suggestion, _Mapping]]] = ...) -> None: ...

class ResubmitSuggestionInput(_message.Message):
    __slots__ = ["suggestion_id"]
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    suggestion_id: str
    def __init__(self, suggestion_id: _Optional[str] = ...) -> None: ...

class ResubmitSuggestionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReviewSuggestionInput(_message.Message):
    __slots__ = ["comment", "status", "suggestion_id"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    comment: _content_pb2.Content
    status: _suggestion_pb2.Suggestion.Status
    suggestion_id: str
    def __init__(self, suggestion_id: _Optional[str] = ..., status: _Optional[_Union[_suggestion_pb2.Suggestion.Status, str]] = ..., comment: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class ReviewSuggestionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SuggestionChangedEvent(_message.Message):
    __slots__ = ["after", "before", "problem_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    after: _suggestion_pb2.Suggestion
    before: _suggestion_pb2.Suggestion
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_suggestion_pb2.Suggestion, _Mapping]] = ..., after: _Optional[_Union[_suggestion_pb2.Suggestion, _Mapping]] = ...) -> None: ...

class UpdateSuggestionInput(_message.Message):
    __slots__ = ["suggestion", "suggestion_id"]
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    suggestion: _suggestion_pb2.Suggestion
    suggestion_id: str
    def __init__(self, suggestion_id: _Optional[str] = ..., suggestion: _Optional[_Union[_suggestion_pb2.Suggestion, _Mapping]] = ...) -> None: ...

class UpdateSuggestionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
