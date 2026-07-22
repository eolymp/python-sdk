from eolymp.ai import finish_reason_pb2 as _finish_reason_pb2
from eolymp.ai import message_pb2 as _message_pb2
from eolymp.ai import usage_pb2 as _usage_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteInput(_message.Message):
    __slots__ = ("model", "messages", "tools", "tool_choice", "parallel_tool_calls", "max_tokens", "temperature", "top_p", "top_k", "use_cache", "container", "betas", "reasoning")
    class ToolChoice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TOOL_CHOICE: _ClassVar[CompleteInput.ToolChoice]
        AUTO: _ClassVar[CompleteInput.ToolChoice]
        REQUIRED: _ClassVar[CompleteInput.ToolChoice]
        NONE: _ClassVar[CompleteInput.ToolChoice]
    UNKNOWN_TOOL_CHOICE: CompleteInput.ToolChoice
    AUTO: CompleteInput.ToolChoice
    REQUIRED: CompleteInput.ToolChoice
    NONE: CompleteInput.ToolChoice
    class Tool(_message.Message):
        __slots__ = ("name", "type", "description", "input_schema", "output_schema", "defer_loading")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        DEFER_LOADING_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: str
        description: str
        input_schema: str
        output_schema: str
        defer_loading: bool
        def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., description: _Optional[str] = ..., input_schema: _Optional[str] = ..., output_schema: _Optional[str] = ..., defer_loading: _Optional[bool] = ...) -> None: ...
    class Reasoning(_message.Message):
        __slots__ = ("enabled", "budget", "effort")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        BUDGET_FIELD_NUMBER: _ClassVar[int]
        EFFORT_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        budget: int
        effort: str
        def __init__(self, enabled: _Optional[bool] = ..., budget: _Optional[int] = ..., effort: _Optional[str] = ...) -> None: ...
    class Container(_message.Message):
        __slots__ = ("id", "skills")
        class Skill(_message.Message):
            __slots__ = ("skill_id", "type", "version")
            SKILL_ID_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            skill_id: str
            type: str
            version: str
            def __init__(self, skill_id: _Optional[str] = ..., type: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        SKILLS_FIELD_NUMBER: _ClassVar[int]
        id: str
        skills: _containers.RepeatedCompositeFieldContainer[CompleteInput.Container.Skill]
        def __init__(self, id: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[CompleteInput.Container.Skill, _Mapping]]] = ...) -> None: ...
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CHOICE_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    USE_CACHE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    BETAS_FIELD_NUMBER: _ClassVar[int]
    REASONING_FIELD_NUMBER: _ClassVar[int]
    model: str
    messages: _containers.RepeatedCompositeFieldContainer[_message_pb2.Message]
    tools: _containers.RepeatedCompositeFieldContainer[CompleteInput.Tool]
    tool_choice: CompleteInput.ToolChoice
    parallel_tool_calls: bool
    max_tokens: int
    temperature: float
    top_p: float
    top_k: int
    use_cache: bool
    container: CompleteInput.Container
    betas: _containers.RepeatedScalarFieldContainer[str]
    reasoning: CompleteInput.Reasoning
    def __init__(self, model: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[_message_pb2.Message, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[CompleteInput.Tool, _Mapping]]] = ..., tool_choice: _Optional[_Union[CompleteInput.ToolChoice, str]] = ..., parallel_tool_calls: _Optional[bool] = ..., max_tokens: _Optional[int] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., top_k: _Optional[int] = ..., use_cache: _Optional[bool] = ..., container: _Optional[_Union[CompleteInput.Container, _Mapping]] = ..., betas: _Optional[_Iterable[str]] = ..., reasoning: _Optional[_Union[CompleteInput.Reasoning, _Mapping]] = ...) -> None: ...

class CompleteOutput(_message.Message):
    __slots__ = ("content", "finish_reason", "usage", "model")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedCompositeFieldContainer[_message_pb2.Message.ContentBlock]
    finish_reason: _finish_reason_pb2.FinishReason
    usage: _usage_pb2.Usage
    model: str
    def __init__(self, content: _Optional[_Iterable[_Union[_message_pb2.Message.ContentBlock, _Mapping]]] = ..., finish_reason: _Optional[_Union[_finish_reason_pb2.FinishReason, str]] = ..., usage: _Optional[_Union[_usage_pb2.Usage, _Mapping]] = ..., model: _Optional[str] = ...) -> None: ...

class CompleteChunk(_message.Message):
    __slots__ = ("type", "index", "text", "call", "signature", "result", "usage", "finish_reason")
    class ChunkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_CHUNK_TYPE: _ClassVar[CompleteChunk.ChunkType]
        TEXT: _ClassVar[CompleteChunk.ChunkType]
        TOOL_CALL_START: _ClassVar[CompleteChunk.ChunkType]
        TOOL_CALL_DELTA: _ClassVar[CompleteChunk.ChunkType]
        REASONING: _ClassVar[CompleteChunk.ChunkType]
        SIGNATURE: _ClassVar[CompleteChunk.ChunkType]
        SERVER_TOOL_CALL_START: _ClassVar[CompleteChunk.ChunkType]
        SERVER_TOOL_CALL_DELTA: _ClassVar[CompleteChunk.ChunkType]
        TOOL_RESULT: _ClassVar[CompleteChunk.ChunkType]
        USAGE: _ClassVar[CompleteChunk.ChunkType]
        FINISH: _ClassVar[CompleteChunk.ChunkType]
    UNKNOWN_CHUNK_TYPE: CompleteChunk.ChunkType
    TEXT: CompleteChunk.ChunkType
    TOOL_CALL_START: CompleteChunk.ChunkType
    TOOL_CALL_DELTA: CompleteChunk.ChunkType
    REASONING: CompleteChunk.ChunkType
    SIGNATURE: CompleteChunk.ChunkType
    SERVER_TOOL_CALL_START: CompleteChunk.ChunkType
    SERVER_TOOL_CALL_DELTA: CompleteChunk.ChunkType
    TOOL_RESULT: CompleteChunk.ChunkType
    USAGE: CompleteChunk.ChunkType
    FINISH: CompleteChunk.ChunkType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CALL_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    type: CompleteChunk.ChunkType
    index: int
    text: str
    call: _message_pb2.Message.ToolCall
    signature: str
    result: _message_pb2.Message.ToolResult
    usage: _usage_pb2.Usage
    finish_reason: _finish_reason_pb2.FinishReason
    def __init__(self, type: _Optional[_Union[CompleteChunk.ChunkType, str]] = ..., index: _Optional[int] = ..., text: _Optional[str] = ..., call: _Optional[_Union[_message_pb2.Message.ToolCall, _Mapping]] = ..., signature: _Optional[str] = ..., result: _Optional[_Union[_message_pb2.Message.ToolResult, _Mapping]] = ..., usage: _Optional[_Union[_usage_pb2.Usage, _Mapping]] = ..., finish_reason: _Optional[_Union[_finish_reason_pb2.FinishReason, str]] = ...) -> None: ...
