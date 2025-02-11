from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.rating import rating_pb2 as _rating_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetRatingInput(_message.Message):
    __slots__ = ("rating",)
    RATING_FIELD_NUMBER: _ClassVar[int]
    rating: _rating_pb2.Rating
    def __init__(self, rating: _Optional[_Union[_rating_pb2.Rating, _Mapping]] = ...) -> None: ...

class SetRatingOutput(_message.Message):
    __slots__ = ("rating_id",)
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ...) -> None: ...

class UpdateRatingInput(_message.Message):
    __slots__ = ("rating_id", "rating")
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    rating_id: str
    rating: _rating_pb2.Rating
    def __init__(self, rating_id: _Optional[str] = ..., rating: _Optional[_Union[_rating_pb2.Rating, _Mapping]] = ...) -> None: ...

class UpdateRatingOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRatingInput(_message.Message):
    __slots__ = ("rating_id", "rating")
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    rating_id: str
    rating: _rating_pb2.Rating
    def __init__(self, rating_id: _Optional[str] = ..., rating: _Optional[_Union[_rating_pb2.Rating, _Mapping]] = ...) -> None: ...

class DeleteRatingOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeRatingInput(_message.Message):
    __slots__ = ("rating_id",)
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ...) -> None: ...

class DescribeRatingOutput(_message.Message):
    __slots__ = ("rating",)
    RATING_FIELD_NUMBER: _ClassVar[int]
    rating: _rating_pb2.Rating
    def __init__(self, rating: _Optional[_Union[_rating_pb2.Rating, _Mapping]] = ...) -> None: ...

class ListRatingInput(_message.Message):
    __slots__ = ("member_id", "offset", "size", "after", "filters", "sort", "order")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIMESTAMP: _ClassVar[ListRatingInput.Sortable]
    TIMESTAMP: ListRatingInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "contest_id", "timestamp")
        ID_FIELD_NUMBER: _ClassVar[int]
        CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        contest_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        timestamp: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., contest_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., timestamp: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ...) -> None: ...
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    offset: int
    size: int
    after: str
    filters: ListRatingInput.Filter
    sort: ListRatingInput.Sortable
    order: _direction_pb2.Direction
    def __init__(self, member_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., after: _Optional[str] = ..., filters: _Optional[_Union[ListRatingInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListRatingInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListRatingOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_rating_pb2.Rating]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_rating_pb2.Rating, _Mapping]]] = ...) -> None: ...

class DescribeRatingBoundariesInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeRatingBoundariesOutput(_message.Message):
    __slots__ = ("levels",)
    class Level(_message.Message):
        __slots__ = ("id", "rating", "count")
        ID_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        id: int
        rating: int
        count: int
        def __init__(self, id: _Optional[int] = ..., rating: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    levels: _containers.RepeatedCompositeFieldContainer[DescribeRatingBoundariesOutput.Level]
    def __init__(self, levels: _Optional[_Iterable[_Union[DescribeRatingBoundariesOutput.Level, _Mapping]]] = ...) -> None: ...

class DescribeRatingDistributionInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeRatingDistributionOutput(_message.Message):
    __slots__ = ("buckets",)
    class Bucket(_message.Message):
        __slots__ = ("min_rating", "max_rating", "count")
        MIN_RATING_FIELD_NUMBER: _ClassVar[int]
        MAX_RATING_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        min_rating: int
        max_rating: int
        count: int
        def __init__(self, min_rating: _Optional[int] = ..., max_rating: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[DescribeRatingDistributionOutput.Bucket]
    def __init__(self, buckets: _Optional[_Iterable[_Union[DescribeRatingDistributionOutput.Bucket, _Mapping]]] = ...) -> None: ...
