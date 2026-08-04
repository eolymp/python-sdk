from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.mail import template_pb2 as _template_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTemplateInput(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...

class CreateTemplateOutput(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class UpdateTemplateInput(_message.Message):
    __slots__ = ("template_id", "locale", "template")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    locale: str
    template: _template_pb2.Template.Patch
    def __init__(self, template_id: _Optional[str] = ..., locale: _Optional[str] = ..., template: _Optional[_Union[_template_pb2.Template.Patch, _Mapping]] = ...) -> None: ...

class UpdateTemplateOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTemplateInput(_message.Message):
    __slots__ = ("template_id", "locale")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    locale: str
    def __init__(self, template_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class DeleteTemplateOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeTemplateInput(_message.Message):
    __slots__ = ("template_id", "locale", "extra")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_template_pb2.Template.Extra.Field]
    def __init__(self, template_id: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_template_pb2.Template.Extra.Field, str]]] = ...) -> None: ...

class DescribeTemplateOutput(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...

class ListTemplatesInput(_message.Message):
    __slots__ = ("offset", "size", "filters", "sort", "order", "locale", "extra")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListTemplatesInput.Sortable]
        KEY: _ClassVar[ListTemplatesInput.Sortable]
        CREATED_AT: _ClassVar[ListTemplatesInput.Sortable]
    DEFAULT: ListTemplatesInput.Sortable
    KEY: ListTemplatesInput.Sortable
    CREATED_AT: ListTemplatesInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "key")
        ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        key: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., key: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListTemplatesInput.Filter
    sort: ListTemplatesInput.Sortable
    order: _direction_pb2.Direction
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_template_pb2.Template.Extra.Field]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTemplatesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListTemplatesInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_template_pb2.Template.Extra.Field, str]]] = ...) -> None: ...

class ListTemplatesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_template_pb2.Template]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_template_pb2.Template, _Mapping]]] = ...) -> None: ...
