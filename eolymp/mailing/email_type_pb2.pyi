from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

ACCOUNT: EmailType
COMMERCIAL: EmailType
DESCRIPTOR: _descriptor.FileDescriptor
NEWSLETTER: EmailType
OTHER: EmailType
UNKNOWN_TYPE: EmailType
UPDATES: EmailType

class EmailType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
