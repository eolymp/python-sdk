from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.commerce import subscription_pb2 as _subscription_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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

class DescribeSubscriptionInput(_message.Message):
    __slots__ = ["subscription_id"]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    def __init__(self, subscription_id: _Optional[str] = ...) -> None: ...

class DescribeSubscriptionOutput(_message.Message):
    __slots__ = ["subscription"]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: _subscription_pb2.Subscription
    def __init__(self, subscription: _Optional[_Union[_subscription_pb2.Subscription, _Mapping]] = ...) -> None: ...

class ListSubscriptionsInput(_message.Message):
    __slots__ = ["after", "before", "customer_id", "price_id", "size", "status"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    after: str
    before: str
    customer_id: str
    price_id: str
    size: int
    status: str
    def __init__(self, customer_id: _Optional[str] = ..., price_id: _Optional[str] = ..., status: _Optional[str] = ..., size: _Optional[int] = ..., after: _Optional[str] = ..., before: _Optional[str] = ...) -> None: ...

class ListSubscriptionsOutput(_message.Message):
    __slots__ = ["has_more", "items"]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    has_more: bool
    items: _containers.RepeatedCompositeFieldContainer[_subscription_pb2.Subscription]
    def __init__(self, has_more: bool = ..., items: _Optional[_Iterable[_Union[_subscription_pb2.Subscription, _Mapping]]] = ...) -> None: ...

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
