from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Admission(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Admission.Status]
        ACCEPTED: _ClassVar[Admission.Status]
        EXPIRED: _ClassVar[Admission.Status]
    UNKNOWN_STATUS: Admission.Status
    ACCEPTED: Admission.Status
    EXPIRED: Admission.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: Admission.Status
    def __init__(self, status: _Optional[_Union[Admission.Status, str]] = ...) -> None: ...
