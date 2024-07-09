from eolymp.executor import usage_pb2 as _usage_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Report(_message.Message):
    __slots__ = ["actors", "agent_name", "error", "origin", "reference", "runs", "state", "version"]
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Actor(_message.Message):
        __slots__ = ["error_code", "error_message", "name", "signature"]
        class Error(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        INIT_ERROR: Report.Actor.Error
        INTERNAL: Report.Actor.Error
        NAME_FIELD_NUMBER: _ClassVar[int]
        NONE: Report.Actor.Error
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        error_code: Report.Actor.Error
        error_message: str
        name: str
        signature: str
        def __init__(self, name: _Optional[str] = ..., signature: _Optional[str] = ..., error_code: _Optional[_Union[Report.Actor.Error, str]] = ..., error_message: _Optional[str] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["error_message", "reference", "state", "steps"]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        STEPS_FIELD_NUMBER: _ClassVar[int]
        error_message: str
        reference: str
        state: Report.State
        steps: _containers.RepeatedCompositeFieldContainer[Report.Step]
        def __init__(self, reference: _Optional[str] = ..., state: _Optional[_Union[Report.State, str]] = ..., error_message: _Optional[str] = ..., steps: _Optional[_Iterable[_Union[Report.Step, _Mapping]]] = ...) -> None: ...
    class Step(_message.Message):
        __slots__ = ["execute", "group", "name", "outcome", "upload"]
        class Outcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class Execute(_message.Message):
            __slots__ = ["actor", "cpu_time_limit", "cpu_time_usage", "exit_code", "exit_status", "memory_limit", "memory_usage", "resource_usage", "signal", "values", "wall_time_limit", "wall_time_usage"]
            class Exit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = []
            class ValuesEntry(_message.Message):
                __slots__ = ["key", "value"]
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str
                def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
            ACTOR_FIELD_NUMBER: _ClassVar[int]
            CPU_EXHAUSTED: Report.Step.Execute.Exit
            CPU_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
            CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
            EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
            EXIT_STATUS_FIELD_NUMBER: _ClassVar[int]
            MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
            MEMORY_OVERFLOW: Report.Step.Execute.Exit
            MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
            RUNTIME_ERROR: Report.Step.Execute.Exit
            SIGNAL_FIELD_NUMBER: _ClassVar[int]
            SKIPPED: Report.Step.Execute.Exit
            SUCCESS: Report.Step.Execute.Exit
            TIMEOUT: Report.Step.Execute.Exit
            UNSPECIFIED: Report.Step.Execute.Exit
            VALUES_FIELD_NUMBER: _ClassVar[int]
            WALL_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
            WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
            actor: str
            cpu_time_limit: int
            cpu_time_usage: int
            exit_code: int
            exit_status: Report.Step.Execute.Exit
            memory_limit: int
            memory_usage: int
            resource_usage: _usage_pb2.ResourceUsage
            signal: int
            values: _containers.ScalarMap[str, str]
            wall_time_limit: int
            wall_time_usage: int
            def __init__(self, actor: _Optional[str] = ..., exit_status: _Optional[_Union[Report.Step.Execute.Exit, str]] = ..., values: _Optional[_Mapping[str, str]] = ..., wall_time_usage: _Optional[int] = ..., wall_time_limit: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., cpu_time_limit: _Optional[int] = ..., memory_usage: _Optional[int] = ..., memory_limit: _Optional[int] = ..., exit_code: _Optional[int] = ..., signal: _Optional[int] = ..., resource_usage: _Optional[_Union[_usage_pb2.ResourceUsage, _Mapping]] = ...) -> None: ...
        class Group(_message.Message):
            __slots__ = ["processes"]
            PROCESSES_FIELD_NUMBER: _ClassVar[int]
            processes: _containers.RepeatedCompositeFieldContainer[Report.Step.Execute]
            def __init__(self, processes: _Optional[_Iterable[_Union[Report.Step.Execute, _Mapping]]] = ...) -> None: ...
        class Upload(_message.Message):
            __slots__ = ["target_name", "target_url"]
            TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
            TARGET_URL_FIELD_NUMBER: _ClassVar[int]
            target_name: str
            target_url: str
            def __init__(self, target_name: _Optional[str] = ..., target_url: _Optional[str] = ...) -> None: ...
        COMPLETE: Report.Step.Outcome
        EXECUTE_FIELD_NUMBER: _ClassVar[int]
        FAILED: Report.Step.Outcome
        GROUP_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OUTCOME_FIELD_NUMBER: _ClassVar[int]
        UNSPECIFIED: Report.Step.Outcome
        UPLOAD_FIELD_NUMBER: _ClassVar[int]
        execute: Report.Step.Execute
        group: Report.Step.Group
        name: str
        outcome: Report.Step.Outcome
        upload: Report.Step.Upload
        def __init__(self, name: _Optional[str] = ..., outcome: _Optional[_Union[Report.Step.Outcome, str]] = ..., execute: _Optional[_Union[Report.Step.Execute, _Mapping]] = ..., upload: _Optional[_Union[Report.Step.Upload, _Mapping]] = ..., group: _Optional[_Union[Report.Step.Group, _Mapping]] = ...) -> None: ...
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    BLOCKED: Report.State
    COMPLETE: Report.State
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXECUTING: Report.State
    FAILED: Report.State
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PENDING: Report.State
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    SKIPPED: Report.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    UNSPECIFIED: Report.State
    VERSION_FIELD_NUMBER: _ClassVar[int]
    actors: _containers.RepeatedCompositeFieldContainer[Report.Actor]
    agent_name: str
    error: str
    origin: str
    reference: str
    runs: _containers.RepeatedCompositeFieldContainer[Report.Run]
    state: Report.State
    version: int
    def __init__(self, reference: _Optional[str] = ..., origin: _Optional[str] = ..., agent_name: _Optional[str] = ..., version: _Optional[int] = ..., state: _Optional[_Union[Report.State, str]] = ..., actors: _Optional[_Iterable[_Union[Report.Actor, _Mapping]]] = ..., runs: _Optional[_Iterable[_Union[Report.Run, _Mapping]]] = ..., error: _Optional[str] = ...) -> None: ...
