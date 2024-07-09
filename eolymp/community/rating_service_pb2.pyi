from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import rating_point_pb2 as _rating_point_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteRatingInput(_message.Message):
    __slots__ = ["point", "rating_id"]
    POINT_FIELD_NUMBER: _ClassVar[int]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    point: _rating_point_pb2.RatingPoint
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ..., point: _Optional[_Union[_rating_point_pb2.RatingPoint, _Mapping]] = ...) -> None: ...

class DeleteRatingOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeRatingInput(_message.Message):
    __slots__ = ["rating_id"]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ...) -> None: ...

class DescribeRatingOutput(_message.Message):
    __slots__ = ["point"]
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _rating_point_pb2.RatingPoint
    def __init__(self, point: _Optional[_Union[_rating_point_pb2.RatingPoint, _Mapping]] = ...) -> None: ...

class ListRatingInput(_message.Message):
    __slots__ = ["filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["id", "ref", "timestamp"]
        ID_FIELD_NUMBER: _ClassVar[int]
        REF_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        ref: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        timestamp: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., ref: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., timestamp: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP: ListRatingInput.Sortable
    filters: ListRatingInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListRatingInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListRatingInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListRatingInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListRatingOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_rating_point_pb2.RatingPoint]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_rating_point_pb2.RatingPoint, _Mapping]]] = ...) -> None: ...

class SetRatingInput(_message.Message):
    __slots__ = ["rating", "rating_id"]
    RATING_FIELD_NUMBER: _ClassVar[int]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    rating: _rating_point_pb2.RatingPoint
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ..., rating: _Optional[_Union[_rating_point_pb2.RatingPoint, _Mapping]] = ...) -> None: ...

class SetRatingOutput(_message.Message):
    __slots__ = ["rating_id"]
    RATING_ID_FIELD_NUMBER: _ClassVar[int]
    rating_id: str
    def __init__(self, rating_id: _Optional[str] = ...) -> None: ...
