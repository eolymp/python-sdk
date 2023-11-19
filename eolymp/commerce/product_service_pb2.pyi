from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.commerce import product_pb2 as _product_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddProductPriceInput(_message.Message):
    __slots__ = ["price", "product_id", "set_default"]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SET_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    price: _product_pb2.Product.Price
    product_id: str
    set_default: bool
    def __init__(self, product_id: _Optional[str] = ..., price: _Optional[_Union[_product_pb2.Product.Price, _Mapping]] = ..., set_default: bool = ...) -> None: ...

class AddProductPriceOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

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

class DeleteProductInput(_message.Message):
    __slots__ = ["product_id"]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    def __init__(self, product_id: _Optional[str] = ...) -> None: ...

class DeleteProductOutput(_message.Message):
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

class ListProductPricesInput(_message.Message):
    __slots__ = ["currency"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    currency: str
    def __init__(self, currency: _Optional[str] = ...) -> None: ...

class ListProductPricesOutput(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_product_pb2.Product.Price]
    def __init__(self, items: _Optional[_Iterable[_Union[_product_pb2.Product.Price, _Mapping]]] = ...) -> None: ...

class RemoveProductPriceInput(_message.Message):
    __slots__ = ["price_id", "product_id"]
    PRICE_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    price_id: str
    product_id: str
    def __init__(self, product_id: _Optional[str] = ..., price_id: _Optional[str] = ...) -> None: ...

class RemoveProductPriceOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

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
