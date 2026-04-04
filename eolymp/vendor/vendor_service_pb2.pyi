from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.vendor import vendor_pb2 as _vendor_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VendorChangedEvent(_message.Message):
    __slots__ = ("before", "after")
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    before: _vendor_pb2.Vendor
    after: _vendor_pb2.Vendor
    def __init__(self, before: _Optional[_Union[_vendor_pb2.Vendor, _Mapping]] = ..., after: _Optional[_Union[_vendor_pb2.Vendor, _Mapping]] = ...) -> None: ...

class ListVendorsInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "user_id", "status", "email", "country")
        ID_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        email: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        country: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., email: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., country: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListVendorsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListVendorsInput.Filter, _Mapping]] = ...) -> None: ...

class ListVendorsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_vendor_pb2.Vendor]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_vendor_pb2.Vendor, _Mapping]]] = ...) -> None: ...

class DescribeVendorInput(_message.Message):
    __slots__ = ("vendor_id",)
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    vendor_id: str
    def __init__(self, vendor_id: _Optional[str] = ...) -> None: ...

class DescribeVendorOutput(_message.Message):
    __slots__ = ("vendor",)
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    vendor: _vendor_pb2.Vendor
    def __init__(self, vendor: _Optional[_Union[_vendor_pb2.Vendor, _Mapping]] = ...) -> None: ...

class ApproveVendorInput(_message.Message):
    __slots__ = ("vendor_id", "comment")
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    vendor_id: str
    comment: str
    def __init__(self, vendor_id: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class ApproveVendorOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RejectVendorInput(_message.Message):
    __slots__ = ("vendor_id", "comment")
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    vendor_id: str
    comment: str
    def __init__(self, vendor_id: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class RejectVendorOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
