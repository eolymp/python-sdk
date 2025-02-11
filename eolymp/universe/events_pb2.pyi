from eolymp.universe import space_pb2 as _space_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceChangeRecord(_message.Message):
    __slots__ = ("op", "space")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_OPERATION: _ClassVar[SpaceChangeRecord.Operation]
        CREATE: _ClassVar[SpaceChangeRecord.Operation]
        UPDATE: _ClassVar[SpaceChangeRecord.Operation]
        DELETE: _ClassVar[SpaceChangeRecord.Operation]
        SOFT_DELETE: _ClassVar[SpaceChangeRecord.Operation]
    NO_OPERATION: SpaceChangeRecord.Operation
    CREATE: SpaceChangeRecord.Operation
    UPDATE: SpaceChangeRecord.Operation
    DELETE: SpaceChangeRecord.Operation
    SOFT_DELETE: SpaceChangeRecord.Operation
    OP_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    op: SpaceChangeRecord.Operation
    space: _space_pb2.Space
    def __init__(self, op: _Optional[_Union[SpaceChangeRecord.Operation, str]] = ..., space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...
