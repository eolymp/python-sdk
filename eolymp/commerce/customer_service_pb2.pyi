from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.commerce import customer_pb2 as _customer_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCustomerInput(_message.Message):
    __slots__ = ["customer"]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: _customer_pb2.Customer
    def __init__(self, customer: _Optional[_Union[_customer_pb2.Customer, _Mapping]] = ...) -> None: ...

class CreateCustomerOutput(_message.Message):
    __slots__ = ["customer_id"]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    def __init__(self, customer_id: _Optional[str] = ...) -> None: ...

class DeleteCustomerInput(_message.Message):
    __slots__ = ["customer_id"]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    def __init__(self, customer_id: _Optional[str] = ...) -> None: ...

class DeleteCustomerOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeCustomerInput(_message.Message):
    __slots__ = ["customer_id"]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    def __init__(self, customer_id: _Optional[str] = ...) -> None: ...

class DescribeCustomerOutput(_message.Message):
    __slots__ = ["customer"]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    customer: _customer_pb2.Customer
    def __init__(self, customer: _Optional[_Union[_customer_pb2.Customer, _Mapping]] = ...) -> None: ...

class ListCustomersInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListCustomersOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_customer_pb2.Customer]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_customer_pb2.Customer, _Mapping]]] = ...) -> None: ...

class UpdateCustomerInput(_message.Message):
    __slots__ = ["customer", "customer_id"]
    CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    customer: _customer_pb2.Customer
    customer_id: str
    def __init__(self, customer_id: _Optional[str] = ..., customer: _Optional[_Union[_customer_pb2.Customer, _Mapping]] = ...) -> None: ...

class UpdateCustomerOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
