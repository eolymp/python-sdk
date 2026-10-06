from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestDataProcessingAgreementInput(_message.Message):
    __slots__ = ("organization_name", "organization_address", "organization_tax_id")
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_TAX_ID_FIELD_NUMBER: _ClassVar[int]
    organization_name: str
    organization_address: str
    organization_tax_id: str
    def __init__(self, organization_name: _Optional[str] = ..., organization_address: _Optional[str] = ..., organization_tax_id: _Optional[str] = ...) -> None: ...

class RequestDataProcessingAgreementOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
