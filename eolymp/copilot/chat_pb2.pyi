import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Chat(_message.Message):
    __slots__ = ("id", "title", "timestamp", "archived")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    timestamp: _timestamp_pb2.Timestamp
    archived: bool
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., archived: _Optional[bool] = ...) -> None: ...

class Context(_message.Message):
    __slots__ = ("url", "title", "description")
    URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    url: str
    title: str
    description: str
    def __init__(self, url: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("id", "timestamp", "user_message", "assistant_message")
    class UserContent(_message.Message):
        __slots__ = ("text", "context")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        context: Context
        def __init__(self, text: _Optional[str] = ..., context: _Optional[_Union[Context, _Mapping]] = ...) -> None: ...
    class AssistantContent(_message.Message):
        __slots__ = ("content", "model")
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        content: _containers.RepeatedCompositeFieldContainer[Message.AssistantBlock]
        model: str
        def __init__(self, content: _Optional[_Iterable[_Union[Message.AssistantBlock, _Mapping]]] = ..., model: _Optional[str] = ...) -> None: ...
    class AssistantBlock(_message.Message):
        __slots__ = ("text", "tool_call")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
        text: str
        tool_call: Message.ToolCall
        def __init__(self, text: _Optional[str] = ..., tool_call: _Optional[_Union[Message.ToolCall, _Mapping]] = ...) -> None: ...
    class ToolCall(_message.Message):
        __slots__ = ("id", "name", "status", "arguments", "result", "error")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_STATUS: _ClassVar[Message.ToolCall.Status]
            PENDING: _ClassVar[Message.ToolCall.Status]
            EXECUTING: _ClassVar[Message.ToolCall.Status]
            SUCCESS: _ClassVar[Message.ToolCall.Status]
            ERROR: _ClassVar[Message.ToolCall.Status]
            REJECTED: _ClassVar[Message.ToolCall.Status]
        UNKNOWN_STATUS: Message.ToolCall.Status
        PENDING: Message.ToolCall.Status
        EXECUTING: Message.ToolCall.Status
        SUCCESS: Message.ToolCall.Status
        ERROR: Message.ToolCall.Status
        REJECTED: Message.ToolCall.Status
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        status: Message.ToolCall.Status
        arguments: str
        result: str
        error: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[Message.ToolCall.Status, str]] = ..., arguments: _Optional[str] = ..., result: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASSISTANT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    timestamp: _timestamp_pb2.Timestamp
    user_message: Message.UserContent
    assistant_message: Message.AssistantContent
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_message: _Optional[_Union[Message.UserContent, _Mapping]] = ..., assistant_message: _Optional[_Union[Message.AssistantContent, _Mapping]] = ...) -> None: ...
