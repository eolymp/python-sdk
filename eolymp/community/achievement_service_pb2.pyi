from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import achievement_pb2 as _achievement_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignAchievementInput(_message.Message):
    __slots__ = ["achievement_id", "inc_by", "set_to"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    INC_BY_FIELD_NUMBER: _ClassVar[int]
    SET_TO_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    inc_by: int
    set_to: int
    def __init__(self, achievement_id: _Optional[str] = ..., set_to: _Optional[int] = ..., inc_by: _Optional[int] = ...) -> None: ...

class AssignAchievementOutput(_message.Message):
    __slots__ = ["quantity"]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    quantity: int
    def __init__(self, quantity: _Optional[int] = ...) -> None: ...

class ListAchievementsInput(_message.Message):
    __slots__ = ["after", "extra", "filters", "locale", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    after: str
    extra: _containers.RepeatedScalarFieldContainer[_achievement_pb2.Achievement.Extra]
    filters: ListAchievementsInput.Filter
    locale: str
    offset: int
    size: int
    def __init__(self, locale: _Optional[str] = ..., after: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ..., filters: _Optional[_Union[ListAchievementsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_achievement_pb2.Achievement.Extra, str]]] = ...) -> None: ...

class ListAchievementsOutput(_message.Message):
    __slots__ = ["items", "next_page_cursor", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_achievement_pb2.Achievement]
    next_page_cursor: str
    total: int
    def __init__(self, total: _Optional[int] = ..., next_page_cursor: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_achievement_pb2.Achievement, _Mapping]]] = ...) -> None: ...

class UnassignAchievementInput(_message.Message):
    __slots__ = ["achievement_id"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    def __init__(self, achievement_id: _Optional[str] = ...) -> None: ...

class UnassignAchievementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
