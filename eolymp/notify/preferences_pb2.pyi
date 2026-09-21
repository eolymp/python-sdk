from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

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
    class Patch(_message.Message):
        __slots__ = ("subscriptions", "unset_subscriptions", "remove_subscriptions", "add_subscriptions")
        SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        UNSET_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        REMOVE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        ADD_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        subscriptions: _containers.RepeatedCompositeFieldContainer[Preferences.Subscription]
        unset_subscriptions: bool
        remove_subscriptions: _containers.RepeatedCompositeFieldContainer[Preferences.Subscription]
        add_subscriptions: _containers.RepeatedCompositeFieldContainer[Preferences.Subscription]
        def __init__(self, subscriptions: _Optional[_Iterable[_Union[Preferences.Subscription, _Mapping]]] = ..., unset_subscriptions: _Optional[bool] = ..., remove_subscriptions: _Optional[_Iterable[_Union[Preferences.Subscription, _Mapping]]] = ..., add_subscriptions: _Optional[_Iterable[_Union[Preferences.Subscription, _Mapping]]] = ...) -> None: ...
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
