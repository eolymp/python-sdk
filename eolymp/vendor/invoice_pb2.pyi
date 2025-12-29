import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Invoice(_message.Message):
    __slots__ = ("id", "number", "currency", "status", "status_reason", "vendor_id", "invoice_date", "due_date", "lines", "subtotal_amount", "tax_amount", "grand_total", "document_url", "created_at", "updated_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Invoice.Status]
        DRAFT: _ClassVar[Invoice.Status]
        PENDING: _ClassVar[Invoice.Status]
        APPROVED: _ClassVar[Invoice.Status]
        PAID: _ClassVar[Invoice.Status]
        REJECTED: _ClassVar[Invoice.Status]
    UNKNOWN_STATUS: Invoice.Status
    DRAFT: Invoice.Status
    PENDING: Invoice.Status
    APPROVED: Invoice.Status
    PAID: Invoice.Status
    REJECTED: Invoice.Status
    class Line(_message.Message):
        __slots__ = ("index", "name", "summary", "total_price")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        TOTAL_PRICE_FIELD_NUMBER: _ClassVar[int]
        index: int
        name: str
        summary: str
        total_price: int
        def __init__(self, index: _Optional[int] = ..., name: _Optional[str] = ..., summary: _Optional[str] = ..., total_price: _Optional[int] = ...) -> None: ...
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Invoice.Patch.Field]
            NUMBER: _ClassVar[Invoice.Patch.Field]
            CURRENCY: _ClassVar[Invoice.Patch.Field]
            INVOICE_DATE: _ClassVar[Invoice.Patch.Field]
            DUE_DATE: _ClassVar[Invoice.Patch.Field]
            LINES: _ClassVar[Invoice.Patch.Field]
        UNKNOWN_FIELD: Invoice.Patch.Field
        NUMBER: Invoice.Patch.Field
        CURRENCY: Invoice.Patch.Field
        INVOICE_DATE: Invoice.Patch.Field
        DUE_DATE: Invoice.Patch.Field
        LINES: Invoice.Patch.Field
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_REASON_FIELD_NUMBER: _ClassVar[int]
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_DATE_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    GRAND_TOTAL_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    number: str
    currency: str
    status: Invoice.Status
    status_reason: str
    vendor_id: str
    invoice_date: _timestamp_pb2.Timestamp
    due_date: _timestamp_pb2.Timestamp
    lines: _containers.RepeatedCompositeFieldContainer[Invoice.Line]
    subtotal_amount: int
    tax_amount: int
    grand_total: int
    document_url: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., number: _Optional[str] = ..., currency: _Optional[str] = ..., status: _Optional[_Union[Invoice.Status, str]] = ..., status_reason: _Optional[str] = ..., vendor_id: _Optional[str] = ..., invoice_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., due_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., lines: _Optional[_Iterable[_Union[Invoice.Line, _Mapping]]] = ..., subtotal_amount: _Optional[int] = ..., tax_amount: _Optional[int] = ..., grand_total: _Optional[int] = ..., document_url: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
