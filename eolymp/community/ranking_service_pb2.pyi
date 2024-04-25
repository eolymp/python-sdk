from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import ranking_event_pb2 as _ranking_event_pb2
from eolymp.community import ranking_point_pb2 as _ranking_point_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRankingEventInput(_message.Message):
    __slots__ = ["event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _ranking_event_pb2.RankingEvent
    def __init__(self, event: _Optional[_Union[_ranking_event_pb2.RankingEvent, _Mapping]] = ...) -> None: ...

class CreateRankingEventOutput(_message.Message):
    __slots__ = ["event_id"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    def __init__(self, event_id: _Optional[str] = ...) -> None: ...

class DeleteRankingEventInput(_message.Message):
    __slots__ = ["event_id"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    def __init__(self, event_id: _Optional[str] = ...) -> None: ...

class DeleteRankingEventOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteRankingPointInput(_message.Message):
    __slots__ = ["event_id", "member_id", "point"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    member_id: str
    point: _ranking_point_pb2.RankingPoint
    def __init__(self, member_id: _Optional[str] = ..., event_id: _Optional[str] = ..., point: _Optional[_Union[_ranking_point_pb2.RankingPoint, _Mapping]] = ...) -> None: ...

class DeleteRankingPointOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeRankingEventInput(_message.Message):
    __slots__ = ["event_id"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    def __init__(self, event_id: _Optional[str] = ...) -> None: ...

class DescribeRankingEventOutput(_message.Message):
    __slots__ = ["event"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: _ranking_event_pb2.RankingEvent
    def __init__(self, event: _Optional[_Union[_ranking_event_pb2.RankingEvent, _Mapping]] = ...) -> None: ...

class DescribeRankingPointInput(_message.Message):
    __slots__ = ["event_id", "member_id"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    member_id: str
    def __init__(self, member_id: _Optional[str] = ..., event_id: _Optional[str] = ...) -> None: ...

class DescribeRankingPointOutput(_message.Message):
    __slots__ = ["point"]
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _ranking_point_pb2.RankingPoint
    def __init__(self, point: _Optional[_Union[_ranking_point_pb2.RankingPoint, _Mapping]] = ...) -> None: ...

class ListRankingEventsInput(_message.Message):
    __slots__ = ["filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["contest_id", "id", "name", "timestamp"]
        CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        contest_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        timestamp: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., timestamp: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., contest_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    NAME: ListRankingEventsInput.Sortable
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP: ListRankingEventsInput.Sortable
    filters: ListRankingEventsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListRankingEventsInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListRankingEventsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListRankingEventsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListRankingEventsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_ranking_event_pb2.RankingEvent]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_ranking_event_pb2.RankingEvent, _Mapping]]] = ...) -> None: ...

class ListRankingPointsInput(_message.Message):
    __slots__ = ["filters", "member_id", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["event_id", "id"]
        EVENT_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        event_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., event_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP: ListRankingPointsInput.Sortable
    filters: ListRankingPointsInput.Filter
    member_id: str
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListRankingPointsInput.Sortable
    def __init__(self, member_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListRankingPointsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListRankingPointsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListRankingPointsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_ranking_point_pb2.RankingPoint]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_ranking_point_pb2.RankingPoint, _Mapping]]] = ...) -> None: ...

class UpdateRankingEventInput(_message.Message):
    __slots__ = ["event", "event_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateRankingEventInput.Patch
    CONTEST_ID: UpdateRankingEventInput.Patch
    EVENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME: UpdateRankingEventInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP: UpdateRankingEventInput.Patch
    event: _ranking_event_pb2.RankingEvent
    event_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateRankingEventInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateRankingEventInput.Patch, str]]] = ..., event_id: _Optional[str] = ..., event: _Optional[_Union[_ranking_event_pb2.RankingEvent, _Mapping]] = ...) -> None: ...

class UpdateRankingEventOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateRankingPointInput(_message.Message):
    __slots__ = ["event_id", "member_id", "point"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    member_id: str
    point: _ranking_point_pb2.RankingPoint
    def __init__(self, member_id: _Optional[str] = ..., event_id: _Optional[str] = ..., point: _Optional[_Union[_ranking_point_pb2.RankingPoint, _Mapping]] = ...) -> None: ...

class UpdateRankingPointOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
