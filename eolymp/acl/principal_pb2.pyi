from eolymp.acl import action_pb2 as _action_pb2
from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Principal(_message.Message):
    __slots__ = ("id", "user_id", "name", "role", "allows")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_ROLE: _ClassVar[Principal.Role]
        OWNER: _ClassVar[Principal.Role]
    UNKNOWN_ROLE: Principal.Role
    OWNER: Principal.Role
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_PATCH: _ClassVar[Principal.Patch.Field]
            ALL: _ClassVar[Principal.Patch.Field]
            NAME: _ClassVar[Principal.Patch.Field]
            ROLE: _ClassVar[Principal.Patch.Field]
            ALLOWS: _ClassVar[Principal.Patch.Field]
        UNKNOWN_PATCH: Principal.Patch.Field
        ALL: Principal.Patch.Field
        NAME: Principal.Patch.Field
        ROLE: Principal.Patch.Field
        ALLOWS: Principal.Patch.Field
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ALLOWS_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    name: str
    role: Principal.Role
    allows: _containers.RepeatedScalarFieldContainer[_action_pb2.Action]
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., name: _Optional[str] = ..., role: _Optional[_Union[Principal.Role, str]] = ..., allows: _Optional[_Iterable[_Union[_action_pb2.Action, str]]] = ...) -> None: ...
