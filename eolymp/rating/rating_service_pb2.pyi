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

class DeleteRatingInput(_message.Message):
    __slots__ = ["rating", "rating_id"]
    RATING_FIELD_NUMBER: _ClassVar[int]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    rating: _rating_pb2.Rating
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ..., rating: _Optional[_Union[_rating_pb2.Rating, _Mapping]] = ...) -> None: ...

class DeleteRatingOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeRatingBoundariesInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeRatingBoundariesOutput(_message.Message):
    __slots__ = ["levels"]
    class Level(_message.Message):
        __slots__ = ["count", "id", "rating"]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        count: int
        id: int
        rating: int
        def __init__(self, id: _Optional[int] = ..., rating: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    levels: _containers.RepeatedCompositeFieldContainer[DescribeRatingBoundariesOutput.Level]
    def __init__(self, levels: _Optional[_Iterable[_Union[DescribeRatingBoundariesOutput.Level, _Mapping]]] = ...) -> None: ...

class DescribeRatingDistributionInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeRatingDistributionOutput(_message.Message):
    __slots__ = ["buckets"]
    class Bucket(_message.Message):
        __slots__ = ["count", "max_rating", "min_rating"]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        MAX_RATING_FIELD_NUMBER: _ClassVar[int]
        MIN_RATING_FIELD_NUMBER: _ClassVar[int]
        count: int
        max_rating: int
        min_rating: int
        def __init__(self, min_rating: _Optional[int] = ..., max_rating: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[DescribeRatingDistributionOutput.Bucket]
    def __init__(self, buckets: _Optional[_Iterable[_Union[DescribeRatingDistributionOutput.Bucket, _Mapping]]] = ...) -> None: ...

class DescribeRatingInput(_message.Message):
    __slots__ = ["rating_id"]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ...) -> None: ...

class DescribeRatingOutput(_message.Message):
    __slots__ = ["rating"]
    RATING_FIELD_NUMBER: _ClassVar[int]
    rating: _rating_pb2.Rating
    def __init__(self, rating: _Optional[_Union[_rating_pb2.Rating, _Mapping]] = ...) -> None: ...

class ListRatingInput(_message.Message):
    __slots__ = ["after", "filters", "member_id", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["contest_id", "id", "timestamp"]
        CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        contest_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        timestamp: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., contest_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., timestamp: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP: ListRatingInput.Sortable
    after: str
    filters: ListRatingInput.Filter
    member_id: str
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListRatingInput.Sortable
    def __init__(self, member_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., after: _Optional[str] = ..., filters: _Optional[_Union[ListRatingInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListRatingInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListRatingOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_rating_pb2.Rating]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_rating_pb2.Rating, _Mapping]]] = ...) -> None: ...

class SetRatingInput(_message.Message):
    __slots__ = ["rating"]
    RATING_FIELD_NUMBER: _ClassVar[int]
    rating: _rating_pb2.Rating
    def __init__(self, rating: _Optional[_Union[_rating_pb2.Rating, _Mapping]] = ...) -> None: ...

class SetRatingOutput(_message.Message):
    __slots__ = ["rating_id"]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ...) -> None: ...

class UpdateRatingInput(_message.Message):
    __slots__ = ["rating", "rating_id"]
    RATING_FIELD_NUMBER: _ClassVar[int]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    rating: _rating_pb2.Rating
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ..., rating: _Optional[_Union[_rating_pb2.Rating, _Mapping]] = ...) -> None: ...

class UpdateRatingOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
