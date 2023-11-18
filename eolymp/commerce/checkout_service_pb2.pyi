from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.commerce import checkout_pb2 as _checkout_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCheckoutInput(_message.Message):
    __slots__ = ["checkout"]
    CHECKOUT_FIELD_NUMBER: _ClassVar[int]
    checkout: _checkout_pb2.Checkout
    def __init__(self, checkout: _Optional[_Union[_checkout_pb2.Checkout, _Mapping]] = ...) -> None: ...

class CreateCheckoutOutput(_message.Message):
    __slots__ = ["checkout_url"]
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    def __init__(self, checkout_url: _Optional[str] = ...) -> None: ...
