import datetime

from eolymp.automation import action_pb2 as _action_pb2
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
    __slots__ = ("id", "rule_id", "trigger", "dry_run", "context", "records", "created_at")
    class Record(_message.Message):
        __slots__ = ("action", "status", "message")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_STATUS: _ClassVar[Log.Record.Status]
            SUCCESS: _ClassVar[Log.Record.Status]
            ERROR: _ClassVar[Log.Record.Status]
            SKIPPED: _ClassVar[Log.Record.Status]
        UNKNOWN_STATUS: Log.Record.Status
        SUCCESS: Log.Record.Status
        ERROR: Log.Record.Status
        SKIPPED: Log.Record.Status
        ACTION_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        action: _action_pb2.Action
        status: Log.Record.Status
        message: str
        def __init__(self, action: _Optional[_Union[_action_pb2.Action, _Mapping]] = ..., status: _Optional[_Union[Log.Record.Status, str]] = ..., message: _Optional[str] = ...) -> None: ...
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
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    rule_id: str
    trigger: _rule_pb2.Rule.Trigger
    dry_run: bool
    context: _containers.ScalarMap[str, str]
    records: _containers.RepeatedCompositeFieldContainer[Log.Record]
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., rule_id: _Optional[str] = ..., trigger: _Optional[_Union[_rule_pb2.Rule.Trigger, str]] = ..., dry_run: _Optional[bool] = ..., context: _Optional[_Mapping[str, str]] = ..., records: _Optional[_Iterable[_Union[Log.Record, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
