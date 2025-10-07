from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.commerce import address_pb2 as _address_pb2
from eolymp.commerce import shipping_method_pb2 as _shipping_method_pb2
from eolymp.commerce import shopping_cart_pb2 as _shopping_cart_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeShoppingCartInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeShoppingCartOutput(_message.Message):
    __slots__ = ("cart",)
    CART_FIELD_NUMBER: _ClassVar[int]
    cart: _shopping_cart_pb2.ShoppingCart
    def __init__(self, cart: _Optional[_Union[_shopping_cart_pb2.ShoppingCart, _Mapping]] = ...) -> None: ...

class CreateShoppingCartItemInput(_message.Message):
    __slots__ = ("product_id", "variant_id", "quantity")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    product_id: str
    variant_id: str
    quantity: int
    def __init__(self, product_id: _Optional[str] = ..., variant_id: _Optional[str] = ..., quantity: _Optional[int] = ...) -> None: ...

class CreateShoppingCartItemOutput(_message.Message):
    __slots__ = ("item_id",)
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    def __init__(self, item_id: _Optional[str] = ...) -> None: ...

class UpdateShoppingCartItemInput(_message.Message):
    __slots__ = ("item_id", "quantity")
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    quantity: int
    def __init__(self, item_id: _Optional[str] = ..., quantity: _Optional[int] = ...) -> None: ...

class UpdateShoppingCartItemOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteShoppingCartItemInput(_message.Message):
    __slots__ = ("item_id",)
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    def __init__(self, item_id: _Optional[str] = ...) -> None: ...

class DeleteShoppingCartItemOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateShippingAddressInput(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: _address_pb2.Address
    def __init__(self, address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ...) -> None: ...

class UpdateShippingAddressOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateBillingAddressInput(_message.Message):
    __slots__ = ("address", "same_as_shipping")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SAME_AS_SHIPPING_FIELD_NUMBER: _ClassVar[int]
    address: _address_pb2.Address
    same_as_shipping: bool
    def __init__(self, address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., same_as_shipping: bool = ...) -> None: ...

class UpdateBillingAddressOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateShippingMethodInput(_message.Message):
    __slots__ = ("shipping_method_id",)
    SHIPPING_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    shipping_method_id: str
    def __init__(self, shipping_method_id: _Optional[str] = ...) -> None: ...

class UpdateShippingMethodOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListShippingMethodsInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListShippingMethodsOutput(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_shipping_method_pb2.ShippingMethod]
    def __init__(self, items: _Optional[_Iterable[_Union[_shipping_method_pb2.ShippingMethod, _Mapping]]] = ...) -> None: ...

class PlaceOrderInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PlaceOrderOutput(_message.Message):
    __slots__ = ("order_id", "order_number")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    order_number: str
    def __init__(self, order_id: _Optional[str] = ..., order_number: _Optional[str] = ...) -> None: ...
