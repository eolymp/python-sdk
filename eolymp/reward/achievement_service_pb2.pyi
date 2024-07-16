from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.reward import achievement_pb2 as _achievement_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
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

class CreateAchievementTranslationInput(_message.Message):
    __slots__ = ["achievement_id", "translation"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    translation: _achievement_pb2.Achievement.Translation
    def __init__(self, achievement_id: _Optional[str] = ..., translation: _Optional[_Union[_achievement_pb2.Achievement.Translation, _Mapping]] = ...) -> None: ...

class CreateAchievementTranslationOutput(_message.Message):
    __slots__ = ["translation_id"]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    translation_id: str
    def __init__(self, translation_id: _Optional[str] = ...) -> None: ...

class DeleteAchievementInput(_message.Message):
    __slots__ = ["achievement_id"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    def __init__(self, achievement_id: _Optional[str] = ...) -> None: ...

class DeleteAchievementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteAchievementTranslationInput(_message.Message):
    __slots__ = ["achievement_id", "translation_id"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    translation_id: str
    def __init__(self, achievement_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class DeleteAchievementTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeAchievementInput(_message.Message):
    __slots__ = ["achievement_id", "extra"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    extra: _containers.RepeatedScalarFieldContainer[_achievement_pb2.Achievement.Extra]
    def __init__(self, achievement_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_achievement_pb2.Achievement.Extra, str]]] = ...) -> None: ...

class DescribeAchievementOutput(_message.Message):
    __slots__ = ["achievement"]
    ACHIEVEMENT_FIELD_NUMBER: _ClassVar[int]
    achievement: _achievement_pb2.Achievement
    def __init__(self, achievement: _Optional[_Union[_achievement_pb2.Achievement, _Mapping]] = ...) -> None: ...

class DescribeAchievementTranslationInput(_message.Message):
    __slots__ = ["achievement_id", "extra", "translation_id"]
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    extra: _containers.RepeatedScalarFieldContainer[_achievement_pb2.Achievement.Extra]
    translation_id: str
    def __init__(self, achievement_id: _Optional[str] = ..., translation_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_achievement_pb2.Achievement.Extra, str]]] = ...) -> None: ...

class DescribeAchievementTranslationOutput(_message.Message):
    __slots__ = ["translation"]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    translation: _achievement_pb2.Achievement.Translation
    def __init__(self, translation: _Optional[_Union[_achievement_pb2.Achievement.Translation, _Mapping]] = ...) -> None: ...

class ListAchievementTranslationsInput(_message.Message):
    __slots__ = ["achievement_id", "extra", "filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "locale", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    extra: _containers.RepeatedScalarFieldContainer[_achievement_pb2.Achievement.Extra]
    filters: ListAchievementTranslationsInput.Filter
    offset: int
    size: int
    def __init__(self, achievement_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListAchievementTranslationsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_achievement_pb2.Achievement.Extra, str]]] = ...) -> None: ...

class ListAchievementTranslationsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_achievement_pb2.Achievement.Translation]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_achievement_pb2.Achievement.Translation, _Mapping]]] = ...) -> None: ...

class ListAchievementsInput(_message.Message):
    __slots__ = ["after", "extra", "filters", "offset", "size"]
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
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    after: str
    extra: _containers.RepeatedScalarFieldContainer[_achievement_pb2.Achievement.Extra]
    filters: ListAchievementsInput.Filter
    offset: int
    size: int
    def __init__(self, after: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ..., filters: _Optional[_Union[ListAchievementsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_achievement_pb2.Achievement.Extra, str]]] = ...) -> None: ...

class ListAchievementsOutput(_message.Message):
    __slots__ = ["items", "next_page_cursor", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_achievement_pb2.Achievement]
    next_page_cursor: str
    total: int
    def __init__(self, total: _Optional[int] = ..., next_page_cursor: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_achievement_pb2.Achievement, _Mapping]]] = ...) -> None: ...

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

class UpdateAchievementTranslationInput(_message.Message):
    __slots__ = ["achievement_id", "patch", "translation", "translation_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ALL: UpdateAchievementTranslationInput.Patch
    LOCALE: UpdateAchievementTranslationInput.Patch
    NAME: UpdateAchievementTranslationInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SUMMARY: UpdateAchievementTranslationInput.Patch
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateAchievementTranslationInput.Patch]
    translation: _achievement_pb2.Achievement.Translation
    translation_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateAchievementTranslationInput.Patch, str]]] = ..., achievement_id: _Optional[str] = ..., translation_id: _Optional[str] = ..., translation: _Optional[_Union[_achievement_pb2.Achievement.Translation, _Mapping]] = ...) -> None: ...

class UpdateAchievementTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
