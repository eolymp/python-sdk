from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.vendor import invoice_pb2 as _invoice_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListInvoicesInput(_message.Message):
    __slots__ = ("offset", "size", "after", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "number", "status", "vendor_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        number: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        vendor_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., number: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., vendor_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    after: str
    filters: ListInvoicesInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., after: _Optional[str] = ..., filters: _Optional[_Union[ListInvoicesInput.Filter, _Mapping]] = ...) -> None: ...

class ListInvoicesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_invoice_pb2.Invoice]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_invoice_pb2.Invoice, _Mapping]]] = ...) -> None: ...

class DescribeInvoiceInput(_message.Message):
    __slots__ = ("invoice_id",)
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class DescribeInvoiceOutput(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoice_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ...) -> None: ...

class CreateInvoiceInput(_message.Message):
    __slots__ = ("invoice",)
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoice_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ...) -> None: ...

class CreateInvoiceOutput(_message.Message):
    __slots__ = ("invoice_id",)
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class UpdateInvoiceInput(_message.Message):
    __slots__ = ("patch", "invoice_id", "invoice")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_invoice_pb2.Invoice.Patch.Field]
    invoice_id: str
    invoice: _invoice_pb2.Invoice
    def __init__(self, patch: _Optional[_Iterable[_Union[_invoice_pb2.Invoice.Patch.Field, str]]] = ..., invoice_id: _Optional[str] = ..., invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ...) -> None: ...

class UpdateInvoiceOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteInvoiceInput(_message.Message):
    __slots__ = ("invoice_id",)
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class DeleteInvoiceOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UploadInvoiceDocumentInput(_message.Message):
    __slots__ = ("invoice_id", "filename", "data")
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    filename: str
    data: bytes
    def __init__(self, invoice_id: _Optional[str] = ..., filename: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadInvoiceDocumentOutput(_message.Message):
    __slots__ = ("document_url",)
    DOCUMENT_URL_FIELD_NUMBER: _ClassVar[int]
    document_url: str
    def __init__(self, document_url: _Optional[str] = ...) -> None: ...

class ApproveInvoiceInput(_message.Message):
    __slots__ = ("invoice_id", "comment")
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    comment: str
    def __init__(self, invoice_id: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class ApproveInvoiceOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubmitInvoiceInput(_message.Message):
    __slots__ = ("invoice_id",)
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class SubmitInvoiceOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RejectInvoiceInput(_message.Message):
    __slots__ = ("invoice_id", "comment")
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    comment: str
    def __init__(self, invoice_id: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class RejectInvoiceOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
