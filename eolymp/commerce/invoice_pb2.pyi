from eolymp.commerce import price_pb2 as _price_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Invoice(_message.Message):
    __slots__ = ["amount_due", "amount_paid", "amount_remaining", "created_at", "currency", "customer_id", "description", "discount_amounts", "due_at", "from_invoice", "hosted_invoice_url", "id", "invoice_pdf_url", "items", "number", "status", "subtotal", "subtotal_excluding_tax", "tax", "tax_amounts", "total", "total_excluding_tax"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class DiscountAmount(_message.Message):
        __slots__ = ["amount", "discount"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_FIELD_NUMBER: _ClassVar[int]
        amount: int
        discount: str
        def __init__(self, amount: _Optional[int] = ..., discount: _Optional[str] = ...) -> None: ...
    class FromInvoice(_message.Message):
        __slots__ = ["invoice", "relation"]
        INVOICE_FIELD_NUMBER: _ClassVar[int]
        RELATION_FIELD_NUMBER: _ClassVar[int]
        invoice: str
        relation: str
        def __init__(self, relation: _Optional[str] = ..., invoice: _Optional[str] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ["amount", "amount_excluding_tax", "currency", "description", "discount_amounts", "id", "price", "quantity", "tax_amounts", "unit_amount_excluding_tax"]
        AMOUNT_EXCLUDING_TAX_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_AMOUNTS_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        TAX_AMOUNTS_FIELD_NUMBER: _ClassVar[int]
        UNIT_AMOUNT_EXCLUDING_TAX_FIELD_NUMBER: _ClassVar[int]
        amount: int
        amount_excluding_tax: int
        currency: str
        description: str
        discount_amounts: _containers.RepeatedCompositeFieldContainer[Invoice.DiscountAmount]
        id: str
        price: _price_pb2.Price
        quantity: int
        tax_amounts: _containers.RepeatedCompositeFieldContainer[Invoice.TaxAmount]
        unit_amount_excluding_tax: int
        def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[_Union[_price_pb2.Price, _Mapping]] = ..., currency: _Optional[str] = ..., amount: _Optional[int] = ..., amount_excluding_tax: _Optional[int] = ..., unit_amount_excluding_tax: _Optional[int] = ..., discount_amounts: _Optional[_Iterable[_Union[Invoice.DiscountAmount, _Mapping]]] = ..., tax_amounts: _Optional[_Iterable[_Union[Invoice.TaxAmount, _Mapping]]] = ...) -> None: ...
    class TaxAmount(_message.Message):
        __slots__ = ["amount", "inclusive", "tax_rate", "taxability_reason", "taxable_amount"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
        TAXABILITY_REASON_FIELD_NUMBER: _ClassVar[int]
        TAXABLE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        TAX_RATE_FIELD_NUMBER: _ClassVar[int]
        amount: int
        inclusive: bool
        tax_rate: str
        taxability_reason: str
        taxable_amount: int
        def __init__(self, amount: _Optional[int] = ..., inclusive: bool = ..., tax_rate: _Optional[str] = ..., taxability_reason: _Optional[str] = ..., taxable_amount: _Optional[int] = ...) -> None: ...
    AMOUNT_DUE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_PAID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_REMAINING_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_AMOUNTS_FIELD_NUMBER: _ClassVar[int]
    DRAFT: Invoice.Status
    DUE_AT_FIELD_NUMBER: _ClassVar[int]
    FROM_INVOICE_FIELD_NUMBER: _ClassVar[int]
    HOSTED_INVOICE_URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_PDF_URL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    OPEN: Invoice.Status
    PAID: Invoice.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_EXCLUDING_TAX_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    TAX_AMOUNTS_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EXCLUDING_TAX_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    UNCOLLECTIBLE: Invoice.Status
    UNKNOWN_STATUS: Invoice.Status
    VOID: Invoice.Status
    amount_due: int
    amount_paid: int
    amount_remaining: int
    created_at: _timestamp_pb2.Timestamp
    currency: str
    customer_id: str
    description: str
    discount_amounts: _containers.RepeatedCompositeFieldContainer[Invoice.DiscountAmount]
    due_at: _timestamp_pb2.Timestamp
    from_invoice: Invoice.FromInvoice
    hosted_invoice_url: str
    id: str
    invoice_pdf_url: str
    items: _containers.RepeatedCompositeFieldContainer[Invoice.Item]
    number: str
    status: Invoice.Status
    subtotal: int
    subtotal_excluding_tax: int
    tax: int
    tax_amounts: _containers.RepeatedCompositeFieldContainer[Invoice.TaxAmount]
    total: int
    total_excluding_tax: int
    def __init__(self, id: _Optional[str] = ..., number: _Optional[str] = ..., status: _Optional[_Union[Invoice.Status, str]] = ..., customer_id: _Optional[str] = ..., description: _Optional[str] = ..., from_invoice: _Optional[_Union[Invoice.FromInvoice, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., due_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., hosted_invoice_url: _Optional[str] = ..., invoice_pdf_url: _Optional[str] = ..., currency: _Optional[str] = ..., amount_due: _Optional[int] = ..., amount_paid: _Optional[int] = ..., amount_remaining: _Optional[int] = ..., subtotal: _Optional[int] = ..., subtotal_excluding_tax: _Optional[int] = ..., tax_amounts: _Optional[_Iterable[_Union[Invoice.TaxAmount, _Mapping]]] = ..., tax: _Optional[int] = ..., discount_amounts: _Optional[_Iterable[_Union[Invoice.DiscountAmount, _Mapping]]] = ..., total: _Optional[int] = ..., total_excluding_tax: _Optional[int] = ..., items: _Optional[_Iterable[_Union[Invoice.Item, _Mapping]]] = ...) -> None: ...
