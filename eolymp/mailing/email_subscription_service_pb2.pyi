from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.mailing import email_type_pb2 as _email_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeEmailSubscriptionInput(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class DescribeEmailSubscriptionOutput(_message.Message):
    __slots__ = ["subscriptions"]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedScalarFieldContainer[_email_type_pb2.EmailType]
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[_email_type_pb2.EmailType, str]]] = ...) -> None: ...

class UpdateEmailSubscriptionInput(_message.Message):
    __slots__ = ["subscriptions", "token"]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedScalarFieldContainer[_email_type_pb2.EmailType]
    token: str
    def __init__(self, token: _Optional[str] = ..., subscriptions: _Optional[_Iterable[_Union[_email_type_pb2.EmailType, str]]] = ...) -> None: ...

class UpdateEmailSubscriptionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
