from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Staff(_message.Message):
    __slots__ = ("id", "member_id", "role")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_ROLE: _ClassVar[Staff.Role]
        TESTER: _ClassVar[Staff.Role]
        AUTHOR: _ClassVar[Staff.Role]
        COORDINATOR: _ClassVar[Staff.Role]
    UNKNOWN_ROLE: Staff.Role
    TESTER: Staff.Role
    AUTHOR: Staff.Role
    COORDINATOR: Staff.Role
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    member_id: str
    role: Staff.Role
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., role: _Optional[_Union[Staff.Role, str]] = ...) -> None: ...
