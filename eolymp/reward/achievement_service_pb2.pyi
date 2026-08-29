from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.reward import achievement_pb2 as _achievement_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAchievementInput(_message.Message):
    __slots__ = ("achievement",)
    ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    achievement: _achievement_pb2.Achievement
    def __init__(self, achievement: _Optional[_Union[_achievement_pb2.Achievement, _Mapping]] = ...) -> None: ...

class CreateAchievementOutput(_message.Message):
    __slots__ = ("achievement_id",)
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    def __init__(self, achievement_id: _Optional[str] = ...) -> None: ...

class UpdateAchievementInput(_message.Message):
    __slots__ = ("achievement_id", "locale", "achievement")
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    locale: str
    achievement: _achievement_pb2.Achievement.Patch
    def __init__(self, achievement_id: _Optional[str] = ..., locale: _Optional[str] = ..., achievement: _Optional[_Union[_achievement_pb2.Achievement.Patch, _Mapping]] = ...) -> None: ...

class UpdateAchievementOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAchievementInput(_message.Message):
    __slots__ = ("achievement_id", "locale")
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    locale: str
    def __init__(self, achievement_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class DeleteAchievementOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeAchievementInput(_message.Message):
    __slots__ = ("achievement_id", "locale", "extra")
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_achievement_pb2.Achievement.Extra]
    def __init__(self, achievement_id: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_achievement_pb2.Achievement.Extra, str]]] = ...) -> None: ...

class DescribeAchievementOutput(_message.Message):
    __slots__ = ("achievement",)
    ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    achievement: _achievement_pb2.Achievement
    def __init__(self, achievement: _Optional[_Union[_achievement_pb2.Achievement, _Mapping]] = ...) -> None: ...

class ListAchievementsInput(_message.Message):
    __slots__ = ("after", "size", "offset", "filters", "locale", "extra")
    class Filter(_message.Message):
        __slots__ = ("query", "id")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    after: str
    size: int
    offset: int
    filters: ListAchievementsInput.Filter
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_achievement_pb2.Achievement.Extra]
    def __init__(self, after: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ..., filters: _Optional[_Union[ListAchievementsInput.Filter, _Mapping]] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_achievement_pb2.Achievement.Extra, str]]] = ...) -> None: ...

class ListAchievementsOutput(_message.Message):
    __slots__ = ("total", "next_page_cursor", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    next_page_cursor: str
    items: _containers.RepeatedCompositeFieldContainer[_achievement_pb2.Achievement]
    def __init__(self, total: _Optional[int] = ..., next_page_cursor: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_achievement_pb2.Achievement, _Mapping]]] = ...) -> None: ...
