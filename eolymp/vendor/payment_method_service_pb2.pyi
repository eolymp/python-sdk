from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.vendor import payment_method_pb2 as _payment_method_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePaymentMethodInput(_message.Message):
    __slots__ = ("method",)
    METHOD_FIELD_NUMBER: _ClassVar[int]
    method: _payment_method_pb2.PaymentMethod
    def __init__(self, method: _Optional[_Union[_payment_method_pb2.PaymentMethod, _Mapping]] = ...) -> None: ...

class CreatePaymentMethodOutput(_message.Message):
    __slots__ = ("method_id",)
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    method_id: str
    def __init__(self, method_id: _Optional[str] = ...) -> None: ...

class UpdatePaymentMethodInput(_message.Message):
    __slots__ = ("method_id", "method")
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    method_id: str
    method: _payment_method_pb2.PaymentMethod
    def __init__(self, method_id: _Optional[str] = ..., method: _Optional[_Union[_payment_method_pb2.PaymentMethod, _Mapping]] = ...) -> None: ...

class UpdatePaymentMethodOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeletePaymentMethodInput(_message.Message):
    __slots__ = ("method_id",)
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    method_id: str
    def __init__(self, method_id: _Optional[str] = ...) -> None: ...

class DeletePaymentMethodOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribePaymentMethodInput(_message.Message):
    __slots__ = ("method_id",)
    METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    method_id: str
    def __init__(self, method_id: _Optional[str] = ...) -> None: ...

class DescribePaymentMethodOutput(_message.Message):
    __slots__ = ("method",)
    METHOD_FIELD_NUMBER: _ClassVar[int]
    method: _payment_method_pb2.PaymentMethod
    def __init__(self, method: _Optional[_Union[_payment_method_pb2.PaymentMethod, _Mapping]] = ...) -> None: ...

class ListPaymentMethodsInput(_message.Message):
    __slots__ = ("after", "size", "offset", "filters")
    class Filter(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    after: str
    size: int
    offset: int
    filters: ListPaymentMethodsInput.Filter
    def __init__(self, after: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ..., filters: _Optional[_Union[ListPaymentMethodsInput.Filter, _Mapping]] = ...) -> None: ...

class ListPaymentMethodsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_payment_method_pb2.PaymentMethod]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_payment_method_pb2.PaymentMethod, _Mapping]]] = ...) -> None: ...
