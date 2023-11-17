from eolymp.commerce import address_pb2 as _address_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = ["billing_address", "created_at", "currency", "discount_amount", "discount_percentage", "expires_at", "grand_total", "id", "items", "member_id", "paid_at", "recurrence", "reference", "space_id", "status", "subtotal", "tax_amount", "tax_percentage", "user_id"]
    class Recurrence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Item(_message.Message):
        __slots__ = ["description", "discount_percentage", "item_price", "name", "quantity", "sku", "tax_percentage", "total_discount_amount", "total_price", "total_tax_amount"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        ITEM_PRICE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        SKU_FIELD_NUMBER: _ClassVar[int]
        TAX_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_DISCOUNT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_PRICE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        description: str
        discount_percentage: float
        item_price: float
        name: str
        quantity: float
        sku: str
        tax_percentage: float
        total_discount_amount: float
        total_price: float
        total_tax_amount: float
        def __init__(self, sku: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., quantity: _Optional[float] = ..., item_price: _Optional[float] = ..., tax_percentage: _Optional[float] = ..., discount_percentage: _Optional[float] = ..., total_tax_amount: _Optional[float] = ..., total_discount_amount: _Optional[float] = ..., total_price: _Optional[float] = ...) -> None: ...
    ACTIVE: Order.Status
    BILLING_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: Order.Status
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    GRAND_TOTAL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE: Order.Status
    INCOMPLETE: Order.Status
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MONTHLY: Order.Recurrence
    NONE: Order.Recurrence
    PAID_AT_FIELD_NUMBER: _ClassVar[int]
    PENDING: Order.Status
    RECURRENCE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TAX_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_RECURRENCE: Order.Recurrence
    UNKNOWN_STATUS: Order.Status
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    YEARLY: Order.Recurrence
    billing_address: _address_pb2.Address
    created_at: _timestamp_pb2.Timestamp
    currency: str
    discount_amount: float
    discount_percentage: float
    expires_at: _timestamp_pb2.Timestamp
    grand_total: float
    id: str
    items: _containers.RepeatedCompositeFieldContainer[Order.Item]
    member_id: str
    paid_at: _timestamp_pb2.Timestamp
    recurrence: Order.Recurrence
    reference: str
    space_id: str
    status: Order.Status
    subtotal: float
    tax_amount: float
    tax_percentage: float
    user_id: str
    def __init__(self, id: _Optional[str] = ..., reference: _Optional[str] = ..., space_id: _Optional[str] = ..., member_id: _Optional[str] = ..., user_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., paid_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[Order.Status, str]] = ..., recurrence: _Optional[_Union[Order.Recurrence, str]] = ..., billing_address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., currency: _Optional[str] = ..., subtotal: _Optional[float] = ..., tax_amount: _Optional[float] = ..., tax_percentage: _Optional[float] = ..., discount_amount: _Optional[float] = ..., discount_percentage: _Optional[float] = ..., grand_total: _Optional[float] = ..., items: _Optional[_Iterable[_Union[Order.Item, _Mapping]]] = ...) -> None: ...
