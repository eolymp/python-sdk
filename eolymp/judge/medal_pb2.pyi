from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

BRONZE: Medal
DESCRIPTOR: _descriptor.FileDescriptor
GOLD: Medal
MENTION: Medal
SILVER: Medal
UNKNOWN_MEDAL: Medal

class Medal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
