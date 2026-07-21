import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.automation import action_pb2 as _action_pb2
from eolymp.automation import condition_pb2 as _condition_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Rule(_message.Message):
    __slots__ = ("id", "name", "trigger", "condition", "inactive", "dry_run", "debug", "trigger_count", "actions", "created_at", "updated_at")
    class Trigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TRIGGER: _ClassVar[Rule.Trigger]
        SUBMISSION_COMPLETED: _ClassVar[Rule.Trigger]
        SCORE_CHANGED: _ClassVar[Rule.Trigger]
        PARTICIPANT_REGISTERED: _ClassVar[Rule.Trigger]
        PARTICIPANT_CHANGED: _ClassVar[Rule.Trigger]
        TICKET_CHANGED: _ClassVar[Rule.Trigger]
        COMMENT_ADDED: _ClassVar[Rule.Trigger]
        MEMBER_CHANGED: _ClassVar[Rule.Trigger]
        STUDENT_CHANGED: _ClassVar[Rule.Trigger]
        ASSIGNMENT_CHANGED: _ClassVar[Rule.Trigger]
    UNKNOWN_TRIGGER: Rule.Trigger
    SUBMISSION_COMPLETED: Rule.Trigger
    SCORE_CHANGED: Rule.Trigger
    PARTICIPANT_REGISTERED: Rule.Trigger
    PARTICIPANT_CHANGED: Rule.Trigger
    TICKET_CHANGED: Rule.Trigger
    COMMENT_ADDED: Rule.Trigger
    MEMBER_CHANGED: Rule.Trigger
    STUDENT_CHANGED: Rule.Trigger
    ASSIGNMENT_CHANGED: Rule.Trigger
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Rule.Patch.Field]
            NAME: _ClassVar[Rule.Patch.Field]
            TRIGGER: _ClassVar[Rule.Patch.Field]
            CONDITION: _ClassVar[Rule.Patch.Field]
            ACTIONS: _ClassVar[Rule.Patch.Field]
            INACTIVE: _ClassVar[Rule.Patch.Field]
            DRY_RUN: _ClassVar[Rule.Patch.Field]
            DEBUG: _ClassVar[Rule.Patch.Field]
        UNKNOWN_FIELD: Rule.Patch.Field
        NAME: Rule.Patch.Field
        TRIGGER: Rule.Patch.Field
        CONDITION: Rule.Patch.Field
        ACTIONS: Rule.Patch.Field
        INACTIVE: Rule.Patch.Field
        DRY_RUN: Rule.Patch.Field
        DEBUG: Rule.Patch.Field
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    trigger: Rule.Trigger
    condition: _condition_pb2.Condition
    inactive: bool
    dry_run: bool
    debug: bool
    trigger_count: int
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., trigger: _Optional[_Union[Rule.Trigger, str]] = ..., condition: _Optional[_Union[_condition_pb2.Condition, _Mapping]] = ..., inactive: _Optional[bool] = ..., dry_run: _Optional[bool] = ..., debug: _Optional[bool] = ..., trigger_count: _Optional[int] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
