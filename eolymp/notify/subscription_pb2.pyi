from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subscription(_message.Message):
    __slots__ = ["digest", "topic"]
    class Digest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DAILY: Subscription.Digest
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    HOURLY: Subscription.Digest
    IMMEDIATE: Subscription.Digest
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DIGEST: Subscription.Digest
    digest: Subscription.Digest
    topic: str
    def __init__(self, topic: _Optional[str] = ..., digest: _Optional[_Union[Subscription.Digest, str]] = ...) -> None: ...
