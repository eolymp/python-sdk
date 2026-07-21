import datetime

from eolymp.automation import rule_pb2 as _rule_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Log(_message.Message):
    __slots__ = ("id", "rule_id", "trigger", "dry_run", "context", "messages", "created_at")
    class ToolCall(_message.Message):
        __slots__ = ("id", "name", "status", "arguments", "result", "error")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_STATUS: _ClassVar[Log.ToolCall.Status]
            SUCCESS: _ClassVar[Log.ToolCall.Status]
            ERROR: _ClassVar[Log.ToolCall.Status]
            DRY_RUN: _ClassVar[Log.ToolCall.Status]
        UNKNOWN_STATUS: Log.ToolCall.Status
        SUCCESS: Log.ToolCall.Status
        ERROR: Log.ToolCall.Status
        DRY_RUN: Log.ToolCall.Status
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        status: Log.ToolCall.Status
        arguments: str
        result: str
        error: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[Log.ToolCall.Status, str]] = ..., arguments: _Optional[str] = ..., result: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...
    class Message(_message.Message):
        __slots__ = ("id", "timestamp", "text", "tool_call")
        ID_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
        id: str
        timestamp: _timestamp_pb2.Timestamp
        text: str
        tool_call: Log.ToolCall
        def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., text: _Optional[str] = ..., tool_call: _Optional[_Union[Log.ToolCall, _Mapping]] = ...) -> None: ...
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    rule_id: str
    trigger: _rule_pb2.Rule.Trigger
    dry_run: bool
    context: _containers.ScalarMap[str, str]
    messages: _containers.RepeatedCompositeFieldContainer[Log.Message]
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., rule_id: _Optional[str] = ..., trigger: _Optional[_Union[_rule_pb2.Rule.Trigger, str]] = ..., dry_run: _Optional[bool] = ..., context: _Optional[_Mapping[str, str]] = ..., messages: _Optional[_Iterable[_Union[Log.Message, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
