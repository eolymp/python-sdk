from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

BRONZE_MEDAL: Medal
DESCRIPTOR: _descriptor.FileDescriptor
GOLD_MEDAL: Medal
HONORABLE_MENTION: Medal
NO_MEDAL: Medal
SILVER_MEDAL: Medal

class Medal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
