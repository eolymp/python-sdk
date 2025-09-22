from eolymp.commerce import address_pb2 as _address_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShoppingCart(_message.Message):
    __slots__ = ("id", "items", "billing_address", "shipping_address", "billing_same_as_shipping", "currency", "shipping_method_id", "total_amount", "shipping_amount", "discount_amount", "tax_amount", "tax_rate", "tax_note", "grand_total")
    class Item(_message.Message):
        __slots__ = ("id", "product_id", "variant_id", "quantity", "unit_amount", "total_amount", "discount_amount")
        ID_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        UNIT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        id: str
        product_id: str
        variant_id: str
        quantity: int
        unit_amount: int
        total_amount: int
        discount_amount: int
        def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., variant_id: _Optional[str] = ..., quantity: _Optional[int] = ..., unit_amount: _Optional[int] = ..., total_amount: _Optional[int] = ..., discount_amount: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BILLING_SAME_AS_SHIPPING_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TAX_RATE_FIELD_NUMBER: _ClassVar[int]
    TAX_NOTE_FIELD_NUMBER: _ClassVar[int]
    GRAND_TOTAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    items: _containers.RepeatedCompositeFieldContainer[ShoppingCart.Item]
    billing_address: _address_pb2.Address
    shipping_address: _address_pb2.Address
    billing_same_as_shipping: bool
    currency: str
    shipping_method_id: str
    total_amount: int
    shipping_amount: int
    discount_amount: int
    tax_amount: int
    tax_rate: int
    tax_note: str
    grand_total: int
    def __init__(self, id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[ShoppingCart.Item, _Mapping]]] = ..., billing_address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., shipping_address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., billing_same_as_shipping: bool = ..., currency: _Optional[str] = ..., shipping_method_id: _Optional[str] = ..., total_amount: _Optional[int] = ..., shipping_amount: _Optional[int] = ..., discount_amount: _Optional[int] = ..., tax_amount: _Optional[int] = ..., tax_rate: _Optional[int] = ..., tax_note: _Optional[str] = ..., grand_total: _Optional[int] = ...) -> None: ...
