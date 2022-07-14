from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
RESOURCE_FIELD_NUMBER: _ClassVar[int]
resource: _descriptor.FieldDescriptor

class Resource(_message.Message):
    __slots__ = ["id_field", "parent", "type"]
    ID_FIELD_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id_field: str
    parent: str
    type: str
    def __init__(self, id_field: _Optional[str] = ..., type: _Optional[str] = ..., parent: _Optional[str] = ...) -> None: ...
