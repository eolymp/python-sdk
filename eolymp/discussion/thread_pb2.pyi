from eolymp.discussion import subscription_pb2 as _subscription_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Thread(_message.Message):
    __slots__ = ("id", "url", "name", "vote", "vote_count", "reply_count", "subscription")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPLY_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    vote: int
    vote_count: int
    reply_count: int
    subscription: _subscription_pb2.Subscription
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., vote: _Optional[int] = ..., vote_count: _Optional[int] = ..., reply_count: _Optional[int] = ..., subscription: _Optional[_Union[_subscription_pb2.Subscription, _Mapping]] = ...) -> None: ...
