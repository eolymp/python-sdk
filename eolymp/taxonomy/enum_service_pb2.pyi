from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.taxonomy import enum_pb2 as _enum_pb2
from eolymp.taxonomy import enum_value_pb2 as _enum_value_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEnumInput(_message.Message):
    __slots__ = ("enum",)
    ENUM_FIELD_NUMBER: _ClassVar[int]
    enum: _enum_pb2.Enum
    def __init__(self, enum: _Optional[_Union[_enum_pb2.Enum, _Mapping]] = ...) -> None: ...

class CreateEnumOutput(_message.Message):
    __slots__ = ("enum_id",)
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    enum_id: str
    def __init__(self, enum_id: _Optional[str] = ...) -> None: ...

class DeleteEnumInput(_message.Message):
    __slots__ = ("enum_id",)
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    enum_id: str
    def __init__(self, enum_id: _Optional[str] = ...) -> None: ...

class DeleteEnumOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateEnumInput(_message.Message):
    __slots__ = ("patch", "enum_id", "enum")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateEnumInput.Patch]
        NAME: _ClassVar[UpdateEnumInput.Patch]
    ALL: UpdateEnumInput.Patch
    NAME: UpdateEnumInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateEnumInput.Patch]
    enum_id: str
    enum: _enum_pb2.Enum
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateEnumInput.Patch, str]]] = ..., enum_id: _Optional[str] = ..., enum: _Optional[_Union[_enum_pb2.Enum, _Mapping]] = ...) -> None: ...

class UpdateEnumOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeEnumInput(_message.Message):
    __slots__ = ("enum_id",)
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    enum_id: str
    def __init__(self, enum_id: _Optional[str] = ...) -> None: ...

class DescribeEnumOutput(_message.Message):
    __slots__ = ("enum",)
    ENUM_FIELD_NUMBER: _ClassVar[int]
    enum: _enum_pb2.Enum
    def __init__(self, enum: _Optional[_Union[_enum_pb2.Enum, _Mapping]] = ...) -> None: ...

class ListEnumsInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("query", "id", "name")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListEnumsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListEnumsInput.Filter, _Mapping]] = ...) -> None: ...

class ListEnumsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_enum_pb2.Enum]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_enum_pb2.Enum, _Mapping]]] = ...) -> None: ...

class CreateValueInput(_message.Message):
    __slots__ = ("enum_id", "value")
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    enum_id: str
    value: _enum_value_pb2.Value
    def __init__(self, enum_id: _Optional[str] = ..., value: _Optional[_Union[_enum_value_pb2.Value, _Mapping]] = ...) -> None: ...

class CreateValueOutput(_message.Message):
    __slots__ = ("value_id",)
    VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    value_id: str
    def __init__(self, value_id: _Optional[str] = ...) -> None: ...

class DeleteValueInput(_message.Message):
    __slots__ = ("enum_id", "value_id")
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    enum_id: str
    value_id: str
    def __init__(self, enum_id: _Optional[str] = ..., value_id: _Optional[str] = ...) -> None: ...

class DeleteValueOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateValueInput(_message.Message):
    __slots__ = ("patch", "enum_id", "value_id", "value")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateValueInput.Patch]
        NAME: _ClassVar[UpdateValueInput.Patch]
        ABBR: _ClassVar[UpdateValueInput.Patch]
        SUMMARY: _ClassVar[UpdateValueInput.Patch]
        IMAGE: _ClassVar[UpdateValueInput.Patch]
        KEYWORDS: _ClassVar[UpdateValueInput.Patch]
    ALL: UpdateValueInput.Patch
    NAME: UpdateValueInput.Patch
    ABBR: UpdateValueInput.Patch
    SUMMARY: UpdateValueInput.Patch
    IMAGE: UpdateValueInput.Patch
    KEYWORDS: UpdateValueInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateValueInput.Patch]
    enum_id: str
    value_id: str
    value: _enum_value_pb2.Value
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateValueInput.Patch, str]]] = ..., enum_id: _Optional[str] = ..., value_id: _Optional[str] = ..., value: _Optional[_Union[_enum_value_pb2.Value, _Mapping]] = ...) -> None: ...

class UpdateValueOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeValueInput(_message.Message):
    __slots__ = ("enum_id", "value_id", "locale")
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    enum_id: str
    value_id: str
    locale: str
    def __init__(self, enum_id: _Optional[str] = ..., value_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class DescribeValueOutput(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _enum_value_pb2.Value
    def __init__(self, value: _Optional[_Union[_enum_value_pb2.Value, _Mapping]] = ...) -> None: ...

class ListValuesInput(_message.Message):
    __slots__ = ("enum_id", "offset", "size", "filters", "locale")
    class Filter(_message.Message):
        __slots__ = ("query", "id", "name")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    enum_id: str
    offset: int
    size: int
    filters: ListValuesInput.Filter
    locale: str
    def __init__(self, enum_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListValuesInput.Filter, _Mapping]] = ..., locale: _Optional[str] = ...) -> None: ...

class ListValuesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_enum_value_pb2.Value]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_enum_value_pb2.Value, _Mapping]]] = ...) -> None: ...

class TranslateValueInput(_message.Message):
    __slots__ = ("enum_id", "value_id", "locale", "translation")
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    enum_id: str
    value_id: str
    locale: str
    translation: _enum_value_pb2.Value.Translation
    def __init__(self, enum_id: _Optional[str] = ..., value_id: _Optional[str] = ..., locale: _Optional[str] = ..., translation: _Optional[_Union[_enum_value_pb2.Value.Translation, _Mapping]] = ...) -> None: ...

class TranslateValueOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTranslationInput(_message.Message):
    __slots__ = ("enum_id", "value_id", "locale")
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    enum_id: str
    value_id: str
    locale: str
    def __init__(self, enum_id: _Optional[str] = ..., value_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class DeleteTranslationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTranslationsInput(_message.Message):
    __slots__ = ("enum_id", "value_id", "offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("locale",)
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    ENUM_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    enum_id: str
    value_id: str
    offset: int
    size: int
    filters: ListTranslationsInput.Filter
    def __init__(self, enum_id: _Optional[str] = ..., value_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTranslationsInput.Filter, _Mapping]] = ...) -> None: ...

class ListTranslationsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_enum_value_pb2.Value.Translation]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_enum_value_pb2.Value.Translation, _Mapping]]] = ...) -> None: ...
