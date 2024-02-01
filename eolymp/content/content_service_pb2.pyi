from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.content import fragment_pb2 as _fragment_pb2
from eolymp.content import variant_pb2 as _variant_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFragmentInput(_message.Message):
    __slots__ = ["fragment"]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    fragment: _fragment_pb2.Fragment
    def __init__(self, fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class CreateFragmentOutput(_message.Message):
    __slots__ = ["fragment_id"]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    def __init__(self, fragment_id: _Optional[str] = ...) -> None: ...

class CreateVariantInput(_message.Message):
    __slots__ = ["fragment_id", "variant"]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    variant: _variant_pb2.Variant
    def __init__(self, fragment_id: _Optional[str] = ..., variant: _Optional[_Union[_variant_pb2.Variant, _Mapping]] = ...) -> None: ...

class CreateVariantOutput(_message.Message):
    __slots__ = ["variant_id"]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    variant_id: str
    def __init__(self, variant_id: _Optional[str] = ...) -> None: ...

class DeleteFragmentInput(_message.Message):
    __slots__ = ["fragment_id"]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    def __init__(self, fragment_id: _Optional[str] = ...) -> None: ...

class DeleteFragmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteVariantInput(_message.Message):
    __slots__ = ["fragment_id", "variant_id"]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    variant_id: str
    def __init__(self, fragment_id: _Optional[str] = ..., variant_id: _Optional[str] = ...) -> None: ...

class DeleteVariantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeFragmentInput(_message.Message):
    __slots__ = ["extra", "fragment_id", "render"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_fragment_pb2.Fragment.Extra]
    fragment_id: str
    render: bool
    def __init__(self, fragment_id: _Optional[str] = ..., render: bool = ..., extra: _Optional[_Iterable[_Union[_fragment_pb2.Fragment.Extra, str]]] = ...) -> None: ...

class DescribeFragmentOutput(_message.Message):
    __slots__ = ["fragment"]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    fragment: _fragment_pb2.Fragment
    def __init__(self, fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class DescribePathInput(_message.Message):
    __slots__ = ["extra", "locale", "path", "render"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_fragment_pb2.Fragment.Extra]
    locale: str
    path: str
    render: bool
    def __init__(self, path: _Optional[str] = ..., locale: _Optional[str] = ..., render: bool = ..., extra: _Optional[_Iterable[_Union[_fragment_pb2.Fragment.Extra, str]]] = ...) -> None: ...

class DescribePathOutput(_message.Message):
    __slots__ = ["fragment"]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    fragment: _fragment_pb2.Fragment
    def __init__(self, fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class DescribeVariantInput(_message.Message):
    __slots__ = ["extra", "fragment_id", "render", "variant_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_variant_pb2.Variant.Extra]
    fragment_id: str
    render: bool
    variant_id: str
    def __init__(self, fragment_id: _Optional[str] = ..., variant_id: _Optional[str] = ..., render: bool = ..., extra: _Optional[_Iterable[_Union[_variant_pb2.Variant.Extra, str]]] = ...) -> None: ...

class DescribeVariantOutput(_message.Message):
    __slots__ = ["variant"]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    variant: _variant_pb2.Variant
    def __init__(self, variant: _Optional[_Union[_variant_pb2.Variant, _Mapping]] = ...) -> None: ...

class ListFragmentsInput(_message.Message):
    __slots__ = ["extra", "filters", "offset", "render", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "label", "locale", "path", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        label: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., label: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_fragment_pb2.Fragment.Extra]
    filters: ListFragmentsInput.Filter
    offset: int
    render: bool
    size: int
    def __init__(self, render: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListFragmentsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_fragment_pb2.Fragment.Extra, str]]] = ...) -> None: ...

class ListFragmentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_fragment_pb2.Fragment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_fragment_pb2.Fragment, _Mapping]]] = ...) -> None: ...

class ListParentsInput(_message.Message):
    __slots__ = ["extra", "locale", "path", "render"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_fragment_pb2.Fragment.Extra]
    locale: str
    path: str
    render: bool
    def __init__(self, path: _Optional[str] = ..., locale: _Optional[str] = ..., render: bool = ..., extra: _Optional[_Iterable[_Union[_fragment_pb2.Fragment.Extra, str]]] = ...) -> None: ...

class ListParentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_fragment_pb2.Fragment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_fragment_pb2.Fragment, _Mapping]]] = ...) -> None: ...

class ListPathsInput(_message.Message):
    __slots__ = ["extra", "filters", "locale", "offset", "render", "size"]
    class Filter(_message.Message):
        __slots__ = ["label", "path", "query"]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        label: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        def __init__(self, query: _Optional[str] = ..., path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., label: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_fragment_pb2.Fragment.Extra]
    filters: ListPathsInput.Filter
    locale: str
    offset: int
    render: bool
    size: int
    def __init__(self, locale: _Optional[str] = ..., render: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListPathsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_fragment_pb2.Fragment.Extra, str]]] = ...) -> None: ...

class ListPathsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_fragment_pb2.Fragment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_fragment_pb2.Fragment, _Mapping]]] = ...) -> None: ...

class ListVariantsInput(_message.Message):
    __slots__ = ["extra", "filters", "fragment_id", "offset", "render", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "locale", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_variant_pb2.Variant.Extra]
    filters: ListVariantsInput.Filter
    fragment_id: str
    offset: int
    render: bool
    size: int
    def __init__(self, render: bool = ..., fragment_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListVariantsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_variant_pb2.Variant.Extra, str]]] = ...) -> None: ...

class ListVariantsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_variant_pb2.Variant]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_variant_pb2.Variant, _Mapping]]] = ...) -> None: ...

class UpdateFragmentInput(_message.Message):
    __slots__ = ["fragment", "fragment_id"]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment: _fragment_pb2.Fragment
    fragment_id: str
    def __init__(self, fragment_id: _Optional[str] = ..., fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class UpdateFragmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateVariantInput(_message.Message):
    __slots__ = ["fragment_id", "variant", "variant_id"]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    variant: _variant_pb2.Variant
    variant_id: str
    def __init__(self, fragment_id: _Optional[str] = ..., variant_id: _Optional[str] = ..., variant: _Optional[_Union[_variant_pb2.Variant, _Mapping]] = ...) -> None: ...

class UpdateVariantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
