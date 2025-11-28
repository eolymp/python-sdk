from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EmailType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_TYPE: _ClassVar[EmailType]
    ACCOUNT: _ClassVar[EmailType]
    NEWSLETTER: _ClassVar[EmailType]
    UPDATES: _ClassVar[EmailType]
    COMMERCIAL: _ClassVar[EmailType]
    OTHER: _ClassVar[EmailType]
UNKNOWN_TYPE: EmailType
ACCOUNT: EmailType
NEWSLETTER: EmailType
UPDATES: EmailType
COMMERCIAL: EmailType
OTHER: EmailType
