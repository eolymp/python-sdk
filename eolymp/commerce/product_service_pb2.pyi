from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.commerce import price_pb2 as _price_pb2
from eolymp.commerce import product_pb2 as _product_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProductInput(_message.Message):
    __slots__ = ["product"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: _product_pb2.Product
    def __init__(self, product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ...) -> None: ...

class CreateProductOutput(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class CreateProductPriceInput(_message.Message):
    __slots__ = ["price", "product_id"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    price: _price_pb2.Price
    product_id: str
    def __init__(self, product_id: _Optional[str] = ..., price: _Optional[_Union[_price_pb2.Price, _Mapping]] = ...) -> None: ...

class CreateProductPriceOutput(_message.Message):
    __slots__ = ["price_id"]
    PRICE_ID_FIELD_NUMBER: _ClassVar[int]
    price_id: str
    def __init__(self, price_id: _Optional[str] = ...) -> None: ...

class DeleteProductInput(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class DeleteProductOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteProductPriceInput(_message.Message):
    __slots__ = ["price_id", "product_id"]
    PRICE_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    price_id: str
    product_id: str
    def __init__(self, product_id: _Optional[str] = ..., price_id: _Optional[str] = ...) -> None: ...

class DeleteProductPriceOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeProductInput(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class DescribeProductOutput(_message.Message):
    __slots__ = ["product"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: _product_pb2.Product
    def __init__(self, product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ...) -> None: ...

class DescribeProductPriceInput(_message.Message):
    __slots__ = ["price_id", "product_id"]
    PRICE_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    price_id: str
    product_id: str
    def __init__(self, product_id: _Optional[str] = ..., price_id: _Optional[str] = ...) -> None: ...

class DescribeProductPriceOutput(_message.Message):
    __slots__ = ["price"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    price: _price_pb2.Price
    def __init__(self, price: _Optional[_Union[_price_pb2.Price, _Mapping]] = ...) -> None: ...

class ListProductPricesInput(_message.Message):
    __slots__ = ["currency", "product_id"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    currency: str
    product_id: str
    def __init__(self, product_id: _Optional[str] = ..., currency: _Optional[str] = ...) -> None: ...

class ListProductPricesOutput(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    def __init__(self, items: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]] = ...) -> None: ...

class ListProductsInput(_message.Message):
    __slots__ = ["filters"]
    class FiltersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.ScalarMap[str, str]
    def __init__(self, filters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListProductsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_product_pb2.Product]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_product_pb2.Product, _Mapping]]] = ...) -> None: ...

class UpdateProductInput(_message.Message):
    __slots__ = ["product", "product_id"]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product: _product_pb2.Product
    product_id: str
    def __init__(self, product_id: _Optional[str] = ..., product: _Optional[_Union[_product_pb2.Product, _Mapping]] = ...) -> None: ...

class UpdateProductOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
