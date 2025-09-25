from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
MCP_TOOL_FIELD_NUMBER: _ClassVar[int]
mcp_tool: _descriptor.FieldDescriptor
MCP_VALUE_DESC_FIELD_NUMBER: _ClassVar[int]
mcp_value_desc: _descriptor.FieldDescriptor
MCP_FIELD_DESC_FIELD_NUMBER: _ClassVar[int]
mcp_field_desc: _descriptor.FieldDescriptor

class MCP(_message.Message):
    __slots__ = ()
    class Tool(_message.Message):
        __slots__ = ("name", "description", "require_confirmation")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        REQUIRE_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        require_confirmation: bool
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., require_confirmation: bool = ...) -> None: ...
    def __init__(self) -> None: ...
