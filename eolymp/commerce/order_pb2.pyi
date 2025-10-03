import datetime

from eolymp.commerce import address_pb2 as _address_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = ("id", "reference", "member_id", "status", "items", "billing_address", "shipping_address", "billing_same_as_shipping", "estimated_shipping_date", "currency", "total_amount", "shipping_amount", "discount_amount", "tax_amount", "tax_rate", "tax_note", "grand_total", "tracking_link", "tracking_number", "created_at", "updated_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[Order.Status]
        CREATED: _ClassVar[Order.Status]
        PENDING: _ClassVar[Order.Status]
        PROCESSING: _ClassVar[Order.Status]
        CANCELED: _ClassVar[Order.Status]
        SHIPPED: _ClassVar[Order.Status]
        COMPLETE: _ClassVar[Order.Status]
    UNSPECIFIED: Order.Status
    CREATED: Order.Status
    PENDING: Order.Status
    PROCESSING: Order.Status
    CANCELED: Order.Status
    SHIPPED: Order.Status
    COMPLETE: Order.Status
    class Item(_message.Message):
        __slots__ = ("id", "name", "image_url", "product_id", "variant_id", "quantity_ordered", "quantity_cancelled", "quantity_shipped", "quantity_returned", "quantity_allocated", "unit_amount", "total_amount", "discount_amount")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_ORDERED_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_CANCELLED_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_SHIPPED_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_RETURNED_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_ALLOCATED_FIELD_NUMBER: _ClassVar[int]
        UNIT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        image_url: str
        product_id: str
        variant_id: str
        quantity_ordered: int
        quantity_cancelled: int
        quantity_shipped: int
        quantity_returned: int
        quantity_allocated: int
        unit_amount: int
        total_amount: int
        discount_amount: int
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., product_id: _Optional[str] = ..., variant_id: _Optional[str] = ..., quantity_ordered: _Optional[int] = ..., quantity_cancelled: _Optional[int] = ..., quantity_shipped: _Optional[int] = ..., quantity_returned: _Optional[int] = ..., quantity_allocated: _Optional[int] = ..., unit_amount: _Optional[int] = ..., total_amount: _Optional[int] = ..., discount_amount: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    BILLING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BILLING_SAME_AS_SHIPPING_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_SHIPPING_DATE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TAX_RATE_FIELD_NUMBER: _ClassVar[int]
    TAX_NOTE_FIELD_NUMBER: _ClassVar[int]
    GRAND_TOTAL_FIELD_NUMBER: _ClassVar[int]
    TRACKING_LINK_FIELD_NUMBER: _ClassVar[int]
    TRACKING_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    reference: str
    member_id: str
    status: Order.Status
    items: _containers.RepeatedCompositeFieldContainer[Order.Item]
    billing_address: _address_pb2.Address
    shipping_address: _address_pb2.Address
    billing_same_as_shipping: bool
    estimated_shipping_date: _timestamp_pb2.Timestamp
    currency: str
    total_amount: int
    shipping_amount: int
    discount_amount: int
    tax_amount: int
    tax_rate: int
    tax_note: str
    grand_total: int
    tracking_link: str
    tracking_number: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., reference: _Optional[str] = ..., member_id: _Optional[str] = ..., status: _Optional[_Union[Order.Status, str]] = ..., items: _Optional[_Iterable[_Union[Order.Item, _Mapping]]] = ..., billing_address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., shipping_address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., billing_same_as_shipping: bool = ..., estimated_shipping_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., currency: _Optional[str] = ..., total_amount: _Optional[int] = ..., shipping_amount: _Optional[int] = ..., discount_amount: _Optional[int] = ..., tax_amount: _Optional[int] = ..., tax_rate: _Optional[int] = ..., tax_note: _Optional[str] = ..., grand_total: _Optional[int] = ..., tracking_link: _Optional[str] = ..., tracking_number: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
