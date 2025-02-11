from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.content import fragment_pb2 as _fragment_pb2
from eolymp.content import variant_pb2 as _variant_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeFragmentInput(_message.Message):
    __slots__ = ("fragment_id", "extra")
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    extra: _containers.RepeatedScalarFieldContainer[_fragment_pb2.Fragment.Extra]
    def __init__(self, fragment_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_fragment_pb2.Fragment.Extra, str]]] = ...) -> None: ...

class DescribeFragmentOutput(_message.Message):
    __slots__ = ("fragment",)
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    fragment: _fragment_pb2.Fragment
    def __init__(self, fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class ListFragmentsInput(_message.Message):
    __slots__ = ("offset", "size", "filters", "sort", "order", "locale", "extra")
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListFragmentsInput.Sort]
        PATH: _ClassVar[ListFragmentsInput.Sort]
        CREATED_AT: _ClassVar[ListFragmentsInput.Sort]
    DEFAULT: ListFragmentsInput.Sort
    PATH: ListFragmentsInput.Sort
    CREATED_AT: ListFragmentsInput.Sort
    class Filter(_message.Message):
        __slots__ = ("query", "id", "path", "locale", "label")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        label: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., label: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListFragmentsInput.Filter
    sort: ListFragmentsInput.Sort
    order: _direction_pb2.Direction
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_fragment_pb2.Fragment.Extra]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListFragmentsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListFragmentsInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_fragment_pb2.Fragment.Extra, str]]] = ...) -> None: ...

class ListFragmentsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_fragment_pb2.Fragment]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_fragment_pb2.Fragment, _Mapping]]] = ...) -> None: ...

class CreateFragmentInput(_message.Message):
    __slots__ = ("fragment",)
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    fragment: _fragment_pb2.Fragment
    def __init__(self, fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class CreateFragmentOutput(_message.Message):
    __slots__ = ("fragment_id",)
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    def __init__(self, fragment_id: _Optional[str] = ...) -> None: ...

class UpdateFragmentInput(_message.Message):
    __slots__ = ("patch", "fragment_id", "fragment")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_fragment_pb2.Fragment.Patch]
    fragment_id: str
    fragment: _fragment_pb2.Fragment
    def __init__(self, patch: _Optional[_Iterable[_Union[_fragment_pb2.Fragment.Patch, str]]] = ..., fragment_id: _Optional[str] = ..., fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class UpdateFragmentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteFragmentInput(_message.Message):
    __slots__ = ("fragment_id",)
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    def __init__(self, fragment_id: _Optional[str] = ...) -> None: ...

class DeleteFragmentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TranslateFragmentInput(_message.Message):
    __slots__ = ("fragment_id", "source", "target", "target_automatic", "override_manual")
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_MANUAL_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    source: str
    target: _containers.RepeatedScalarFieldContainer[str]
    target_automatic: bool
    override_manual: bool
    def __init__(self, fragment_id: _Optional[str] = ..., source: _Optional[str] = ..., target: _Optional[_Iterable[str]] = ..., target_automatic: bool = ..., override_manual: bool = ...) -> None: ...

class TranslateFragmentOutput(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class DescribeVariantInput(_message.Message):
    __slots__ = ("fragment_id", "variant_id", "extra")
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    variant_id: str
    extra: _containers.RepeatedScalarFieldContainer[_variant_pb2.Variant.Extra]
    def __init__(self, fragment_id: _Optional[str] = ..., variant_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_variant_pb2.Variant.Extra, str]]] = ...) -> None: ...

class DescribeVariantOutput(_message.Message):
    __slots__ = ("variant",)
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    variant: _variant_pb2.Variant
    def __init__(self, variant: _Optional[_Union[_variant_pb2.Variant, _Mapping]] = ...) -> None: ...

class ListVariantsInput(_message.Message):
    __slots__ = ("fragment_id", "offset", "size", "filters", "extra")
    class Filter(_message.Message):
        __slots__ = ("query", "id", "locale")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    offset: int
    size: int
    filters: ListVariantsInput.Filter
    extra: _containers.RepeatedScalarFieldContainer[_variant_pb2.Variant.Extra]
    def __init__(self, fragment_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListVariantsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_variant_pb2.Variant.Extra, str]]] = ...) -> None: ...

class ListVariantsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_variant_pb2.Variant]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_variant_pb2.Variant, _Mapping]]] = ...) -> None: ...

class CreateVariantInput(_message.Message):
    __slots__ = ("fragment_id", "variant")
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    variant: _variant_pb2.Variant
    def __init__(self, fragment_id: _Optional[str] = ..., variant: _Optional[_Union[_variant_pb2.Variant, _Mapping]] = ...) -> None: ...

class CreateVariantOutput(_message.Message):
    __slots__ = ("variant_id",)
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    variant_id: str
    def __init__(self, variant_id: _Optional[str] = ...) -> None: ...

class UpdateVariantInput(_message.Message):
    __slots__ = ("fragment_id", "variant_id", "variant")
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    variant_id: str
    variant: _variant_pb2.Variant
    def __init__(self, fragment_id: _Optional[str] = ..., variant_id: _Optional[str] = ..., variant: _Optional[_Union[_variant_pb2.Variant, _Mapping]] = ...) -> None: ...

class UpdateVariantOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteVariantInput(_message.Message):
    __slots__ = ("fragment_id", "variant_id")
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    variant_id: str
    def __init__(self, fragment_id: _Optional[str] = ..., variant_id: _Optional[str] = ...) -> None: ...

class DeleteVariantOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribePathInput(_message.Message):
    __slots__ = ("path", "locale", "extra")
    PATH_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    path: str
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_fragment_pb2.Fragment.Extra]
    def __init__(self, path: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_fragment_pb2.Fragment.Extra, str]]] = ...) -> None: ...

class DescribePathOutput(_message.Message):
    __slots__ = ("fragment",)
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    fragment: _fragment_pb2.Fragment
    def __init__(self, fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class ListParentsInput(_message.Message):
    __slots__ = ("path", "locale", "extra")
    PATH_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    path: str
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_fragment_pb2.Fragment.Extra]
    def __init__(self, path: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_fragment_pb2.Fragment.Extra, str]]] = ...) -> None: ...

class ListParentsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_fragment_pb2.Fragment]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_fragment_pb2.Fragment, _Mapping]]] = ...) -> None: ...
