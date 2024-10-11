from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Preferences(_message.Message):
    __slots__ = ["subscriptions"]
    class Digest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Subscription(_message.Message):
        __slots__ = ["digest", "topic"]
        DIGEST_FIELD_NUMBER: _ClassVar[int]
        TOPIC_FIELD_NUMBER: _ClassVar[int]
        digest: Preferences.Digest
        topic: str
        def __init__(self, topic: _Optional[str] = ..., digest: _Optional[_Union[Preferences.Digest, str]] = ...) -> None: ...
    DAILY: Preferences.Digest
    HOURLY: Preferences.Digest
    IMMEDIATE: Preferences.Digest
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DIGEST: Preferences.Digest
    subscriptions: _containers.RepeatedCompositeFieldContainer[Preferences.Subscription]
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[Preferences.Subscription, _Mapping]]] = ...) -> None: ...
