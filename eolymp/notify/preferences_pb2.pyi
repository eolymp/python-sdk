from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Preferences(_message.Message):
    __slots__ = ("subscriptions",)
    class Digest(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_DIGEST: _ClassVar[Preferences.Digest]
        IMMEDIATE: _ClassVar[Preferences.Digest]
        HOURLY: _ClassVar[Preferences.Digest]
        DAILY: _ClassVar[Preferences.Digest]
    UNKNOWN_DIGEST: Preferences.Digest
    IMMEDIATE: Preferences.Digest
    HOURLY: Preferences.Digest
    DAILY: Preferences.Digest
    class Subscription(_message.Message):
        __slots__ = ("topic", "digest")
        TOPIC_FIELD_NUMBER: _ClassVar[int]
        DIGEST_FIELD_NUMBER: _ClassVar[int]
        topic: str
        digest: Preferences.Digest
        def __init__(self, topic: _Optional[str] = ..., digest: _Optional[_Union[Preferences.Digest, str]] = ...) -> None: ...
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[Preferences.Subscription]
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[Preferences.Subscription, _Mapping]]] = ...) -> None: ...
