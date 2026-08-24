from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
AUDIT_FIELD_NUMBER: _ClassVar[int]
audit: _descriptor.FieldDescriptor

class Audit(_message.Message):
    __slots__ = ("operation_type",)
    class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_OPERATION_TYPE: _ClassVar[Audit.OperationType]
        READ: _ClassVar[Audit.OperationType]
        WRITE: _ClassVar[Audit.OperationType]
        DELETE: _ClassVar[Audit.OperationType]
    UNKNOWN_OPERATION_TYPE: Audit.OperationType
    READ: Audit.OperationType
    WRITE: Audit.OperationType
    DELETE: Audit.OperationType
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    operation_type: Audit.OperationType
    def __init__(self, operation_type: _Optional[_Union[Audit.OperationType, str]] = ...) -> None: ...
