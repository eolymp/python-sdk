from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.reward import achievement_pb2 as _achievement_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAchievementInput(_message.Message):
    __slots__ = ["achievement"]
    ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    achievement: _achievement_pb2.Achievement
    def __init__(self, achievement: _Optional[_Union[_achievement_pb2.Achievement, _Mapping]] = ...) -> None: ...

class CreateAchievementOutput(_message.Message):
    __slots__ = ["achievement_id"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    def __init__(self, achievement_id: _Optional[str] = ...) -> None: ...

class DeleteAchievementInput(_message.Message):
    __slots__ = ["achievement_id"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    def __init__(self, achievement_id: _Optional[str] = ...) -> None: ...

class DeleteAchievementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeAchievementInput(_message.Message):
    __slots__ = ["achievement_id"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    def __init__(self, achievement_id: _Optional[str] = ...) -> None: ...

class DescribeAchievementOutput(_message.Message):
    __slots__ = ["achievement"]
    ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    achievement: _achievement_pb2.Achievement
    def __init__(self, achievement: _Optional[_Union[_achievement_pb2.Achievement, _Mapping]] = ...) -> None: ...

class ListAchievementsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListAchievementsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListAchievementsInput.Filter, _Mapping]] = ...) -> None: ...

class ListAchievementsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_achievement_pb2.Achievement]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_achievement_pb2.Achievement, _Mapping]]] = ...) -> None: ...

class UpdateAchievementInput(_message.Message):
    __slots__ = ["achievement", "achievement_id"]
    ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    achievement: _achievement_pb2.Achievement
    achievement_id: str
    def __init__(self, achievement_id: _Optional[str] = ..., achievement: _Optional[_Union[_achievement_pb2.Achievement, _Mapping]] = ...) -> None: ...

class UpdateAchievementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
