from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ("role", "content")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_ROLE: _ClassVar[Message.Role]
        SYSTEM: _ClassVar[Message.Role]
        USER: _ClassVar[Message.Role]
        ASSISTANT: _ClassVar[Message.Role]
        TOOL: _ClassVar[Message.Role]
    UNKNOWN_ROLE: Message.Role
    SYSTEM: Message.Role
    USER: Message.Role
    ASSISTANT: Message.Role
    TOOL: Message.Role
    class BlockType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_BLOCK_TYPE: _ClassVar[Message.BlockType]
        TEXT: _ClassVar[Message.BlockType]
        REASONING: _ClassVar[Message.BlockType]
        SIGNATURE: _ClassVar[Message.BlockType]
        TOOL_CALL: _ClassVar[Message.BlockType]
        TOOL_RESULT: _ClassVar[Message.BlockType]
        SERVER_TOOL_CALL: _ClassVar[Message.BlockType]
    UNKNOWN_BLOCK_TYPE: Message.BlockType
    TEXT: Message.BlockType
    REASONING: Message.BlockType
    SIGNATURE: Message.BlockType
    TOOL_CALL: Message.BlockType
    TOOL_RESULT: Message.BlockType
    SERVER_TOOL_CALL: Message.BlockType
    class ContentBlock(_message.Message):
        __slots__ = ("type", "text", "signature", "tool_call", "tool_result")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
        TOOL_RESULT_FIELD_NUMBER: _ClassVar[int]
        type: Message.BlockType
        text: str
        signature: str
        tool_call: Message.ToolCall
        tool_result: Message.ToolResult
        def __init__(self, type: _Optional[_Union[Message.BlockType, str]] = ..., text: _Optional[str] = ..., signature: _Optional[str] = ..., tool_call: _Optional[_Union[Message.ToolCall, _Mapping]] = ..., tool_result: _Optional[_Union[Message.ToolResult, _Mapping]] = ...) -> None: ...
    class ToolCall(_message.Message):
        __slots__ = ("id", "name", "arguments")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        arguments: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., arguments: _Optional[str] = ...) -> None: ...
    class ToolResult(_message.Message):
        __slots__ = ("call_id", "result", "is_error", "error")
        CALL_ID_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        IS_ERROR_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        call_id: str
        result: str
        is_error: bool
        error: str
        def __init__(self, call_id: _Optional[str] = ..., result: _Optional[str] = ..., is_error: _Optional[bool] = ..., error: _Optional[str] = ...) -> None: ...
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    role: Message.Role
    content: _containers.RepeatedCompositeFieldContainer[Message.ContentBlock]
    def __init__(self, role: _Optional[_Union[Message.Role, str]] = ..., content: _Optional[_Iterable[_Union[Message.ContentBlock, _Mapping]]] = ...) -> None: ...
