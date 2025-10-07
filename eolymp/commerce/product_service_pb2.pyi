from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.commerce import product_pb2 as _product_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProductInput(_message.Message):
    __slots__ = ("product",)
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: _product_pb2.Product
    def __init__(self, product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ...) -> None: ...

class CreateProductOutput(_message.Message):
    __slots__ = ("product_id",)
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class UpdateProductInput(_message.Message):
    __slots__ = ("patch", "product_id", "product")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_product_pb2.Product.Patch.Field]
    product_id: str
    product: _product_pb2.Product
    def __init__(self, patch: _Optional[_Iterable[_Union[_product_pb2.Product.Patch.Field, str]]] = ..., product_id: _Optional[str] = ..., product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ...) -> None: ...

class UpdateProductOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteProductInput(_message.Message):
    __slots__ = ("product_id",)
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class DeleteProductOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeProductInput(_message.Message):
    __slots__ = ("product_id", "locale", "extra")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_product_pb2.Product.Extra.Field]
    def __init__(self, product_id: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_product_pb2.Product.Extra.Field, str]]] = ...) -> None: ...

class DescribeProductOutput(_message.Message):
    __slots__ = ("product",)
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: _product_pb2.Product
    def __init__(self, product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ...) -> None: ...

class ListProductsInput(_message.Message):
    __slots__ = ("offset", "size", "after", "search", "filters", "sort", "order", "locale", "extra")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListProductsInput.Sortable]
    DEFAULT: ListProductsInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "name", "out_of_stock", "price")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OUT_OF_STOCK_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        out_of_stock: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        price: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., out_of_stock: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., price: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    after: str
    search: str
    filters: ListProductsInput.Filter
    sort: ListProductsInput.Sortable
    order: _direction_pb2.Direction
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_product_pb2.Product.Extra.Field]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., after: _Optional[str] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListProductsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListProductsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_product_pb2.Product.Extra.Field, str]]] = ...) -> None: ...

class ListProductsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_product_pb2.Product]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_product_pb2.Product, _Mapping]]] = ...) -> None: ...
