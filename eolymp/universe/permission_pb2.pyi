from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Permission(_message.Message):
    __slots__ = ["id", "role", "user_id"]
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADMIN: Permission.Role
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER: Permission.Role
    ROLE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWER: Permission.Role
    id: str
    role: Permission.Role
    user_id: str
    def __init__(self, id: _Optional[str] = ..., role: _Optional[_Union[Permission.Role, str]] = ..., user_id: _Optional[str] = ...) -> None: ...
