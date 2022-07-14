from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

CREATE_CONTEST: Entitlement
CREATE_SUBMISSION: Entitlement
CREATE_TICKET: Entitlement
DESCRIPTOR: _descriptor.FileDescriptor
LOOKUP_CONTEST: Entitlement
MANAGE_ANNOUNCEMENT: Entitlement
MANAGE_CONTEST: Entitlement
MANAGE_PARTICIPANT: Entitlement
MANAGE_PROBLEM: Entitlement
MANAGE_SUBMISSION: Entitlement
MANAGE_TICKET: Entitlement
NONE: Entitlement
VIEW_ANNOUNCEMENT: Entitlement
VIEW_PARTICIPANT: Entitlement
VIEW_PROBLEM: Entitlement
VIEW_REGISTRATION_FORM: Entitlement
VIEW_RUNTIME: Entitlement
VIEW_SUBMISSION: Entitlement
VIEW_TICKET: Entitlement

class Entitlement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
