from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subscription(_message.Message):
    __slots__ = ("type",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Subscription.Type]
        MUTED: _ClassVar[Subscription.Type]
        SUBSCRIBED: _ClassVar[Subscription.Type]
        WATCHING: _ClassVar[Subscription.Type]
    NONE: Subscription.Type
    MUTED: Subscription.Type
    SUBSCRIBED: Subscription.Type
    WATCHING: Subscription.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: Subscription.Type
    def __init__(self, type: _Optional[_Union[Subscription.Type, str]] = ...) -> None: ...
