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
    __slots__ = ("achievement_id", "set_to", "inc_by")
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SET_TO_FIELD_NUMBER: _ClassVar[int]
    INC_BY_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    set_to: int
    inc_by: int
    def __init__(self, achievement_id: _Optional[str] = ..., set_to: _Optional[int] = ..., inc_by: _Optional[int] = ...) -> None: ...

class AssignAchievementOutput(_message.Message):
    __slots__ = ("quantity",)
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    quantity: int
    def __init__(self, quantity: _Optional[int] = ...) -> None: ...

class UnassignAchievementInput(_message.Message):
    __slots__ = ("achievement_id",)
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    def __init__(self, achievement_id: _Optional[str] = ...) -> None: ...

class UnassignAchievementOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAchievementsInput(_message.Message):
    __slots__ = ("locale", "after", "size", "offset", "filters", "extra")
    class Filter(_message.Message):
        __slots__ = ("query", "id")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    locale: str
    after: str
    size: int
    offset: int
    filters: ListAchievementsInput.Filter
    extra: _containers.RepeatedScalarFieldContainer[_achievement_pb2.Achievement.Extra]
    def __init__(self, locale: _Optional[str] = ..., after: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ..., filters: _Optional[_Union[ListAchievementsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_achievement_pb2.Achievement.Extra, str]]] = ...) -> None: ...

class ListAchievementsOutput(_message.Message):
    __slots__ = ("total", "next_page_cursor", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    next_page_cursor: str
    items: _containers.RepeatedCompositeFieldContainer[_achievement_pb2.Achievement]
    def __init__(self, total: _Optional[int] = ..., next_page_cursor: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_achievement_pb2.Achievement, _Mapping]]] = ...) -> None: ...
