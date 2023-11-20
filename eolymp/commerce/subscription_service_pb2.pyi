from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.commerce import subscription_pb2 as _subscription_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CancelSubscriptionInput(_message.Message):
    __slots__ = ["subscription_id"]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    def __init__(self, subscription_id: _Optional[str] = ...) -> None: ...

class CancelSubscriptionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateSubscriptionInput(_message.Message):
    __slots__ = ["subscription"]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: _subscription_pb2.Subscription
    def __init__(self, subscription: _Optional[_Union[_subscription_pb2.Subscription, _Mapping]] = ...) -> None: ...

class CreateSubscriptionOutput(_message.Message):
    __slots__ = ["checkout_url", "subscription_id"]
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    subscription_id: str
    def __init__(self, subscription_id: _Optional[str] = ..., checkout_url: _Optional[str] = ...) -> None: ...

class UpdateSubscriptionInput(_message.Message):
    __slots__ = ["subscription", "subscription_id"]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    subscription: _subscription_pb2.Subscription
    subscription_id: str
    def __init__(self, subscription_id: _Optional[str] = ..., subscription: _Optional[_Union[_subscription_pb2.Subscription, _Mapping]] = ...) -> None: ...

class UpdateSubscriptionOutput(_message.Message):
    __slots__ = ["checkout_url"]
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    def __init__(self, checkout_url: _Optional[str] = ...) -> None: ...
