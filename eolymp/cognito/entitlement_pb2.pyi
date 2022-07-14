from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

BLOCK_USERS: Entitlement
DESCRIPTOR: _descriptor.FileDescriptor
MANAGE_ROLES: Entitlement
VIEW_BLOCKED_PROFILE: Entitlement
VIEW_PRIVATE_DATA: Entitlement
VIEW_PUBLIC_PROFILE: Entitlement

class Entitlement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
