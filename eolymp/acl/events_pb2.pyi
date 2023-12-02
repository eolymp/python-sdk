from eolymp.acl import acl_service_pb2 as _acl_service_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionChangeRecord(_message.Message):
    __slots__ = ["op", "permission", "space_id"]
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    GRANT: PermissionChangeRecord.Operation
    NO_OPERATION: PermissionChangeRecord.Operation
    OP_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    REVOKE: PermissionChangeRecord.Operation
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    op: PermissionChangeRecord.Operation
    permission: _acl_service_pb2.Permission
    space_id: str
    def __init__(self, op: _Optional[_Union[PermissionChangeRecord.Operation, str]] = ..., space_id: _Optional[str] = ..., permission: _Optional[_Union[_acl_service_pb2.Permission, _Mapping]] = ...) -> None: ...
