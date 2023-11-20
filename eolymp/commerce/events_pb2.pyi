from eolymp.commerce import subscription_pb2 as _subscription_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionChangedEvent(_message.Message):
    __slots__ = ["after", "before"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    after: _subscription_pb2.Subscription
    before: _subscription_pb2.Subscription
    def __init__(self, before: _Optional[_Union[_subscription_pb2.Subscription, _Mapping]] = ..., after: _Optional[_Union[_subscription_pb2.Subscription, _Mapping]] = ...) -> None: ...
