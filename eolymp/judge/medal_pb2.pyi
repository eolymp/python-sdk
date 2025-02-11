from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Medal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_MEDAL: _ClassVar[Medal]
    GOLD_MEDAL: _ClassVar[Medal]
    SILVER_MEDAL: _ClassVar[Medal]
    BRONZE_MEDAL: _ClassVar[Medal]
    HONORABLE_MENTION: _ClassVar[Medal]
NO_MEDAL: Medal
GOLD_MEDAL: Medal
SILVER_MEDAL: Medal
BRONZE_MEDAL: Medal
HONORABLE_MENTION: Medal
