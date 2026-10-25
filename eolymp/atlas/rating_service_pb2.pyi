from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import rating_pb2 as _rating_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteRatingInput(_message.Message):
    __slots__ = ("problem_id", "rating_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    rating_id: str
    def __init__(self, problem_id: _Optional[str] = ..., rating_id: _Optional[str] = ...) -> None: ...

class DeleteRatingOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeRatingInput(_message.Message):
    __slots__ = ("problem_id", "rating_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    rating_id: str
    def __init__(self, problem_id: _Optional[str] = ..., rating_id: _Optional[str] = ...) -> None: ...

class DescribeRatingOutput(_message.Message):
    __slots__ = ("rating",)
    RATING_FIELD_NUMBER: _ClassVar[int]
    rating: _rating_pb2.Rating
    def __init__(self, rating: _Optional[_Union[_rating_pb2.Rating, _Mapping]] = ...) -> None: ...

class ListRatingsInput(_message.Message):
    __slots__ = ("problem_id", "offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("stars", "has_comment")
        STARS_FIELD_NUMBER: _ClassVar[int]
        HAS_COMMENT_FIELD_NUMBER: _ClassVar[int]
        stars: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        has_comment: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, stars: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., has_comment: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    offset: int
    size: int
    filters: ListRatingsInput.Filter
    def __init__(self, problem_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListRatingsInput.Filter, _Mapping]] = ...) -> None: ...

class ListRatingsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_rating_pb2.Rating]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_rating_pb2.Rating, _Mapping]]] = ...) -> None: ...
