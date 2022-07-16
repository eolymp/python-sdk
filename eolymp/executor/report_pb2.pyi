from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Report(_message.Message):
    __slots__ = ["actors", "agent", "error", "origin", "reference", "runs", "state", "version"]
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Actor(_message.Message):
        __slots__ = ["error", "name", "signature"]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        error: str
        name: str
        signature: str
        def __init__(self, name: _Optional[str] = ..., signature: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["reference", "state", "steps"]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        STEPS_FIELD_NUMBER: _ClassVar[int]
        reference: str
        state: Report.State
        steps: _containers.RepeatedCompositeFieldContainer[Report.Step]
        def __init__(self, reference: _Optional[str] = ..., state: _Optional[_Union[Report.State, str]] = ..., steps: _Optional[_Iterable[_Union[Report.Step, _Mapping]]] = ...) -> None: ...
    class Step(_message.Message):
        __slots__ = ["execute", "name", "state", "upload"]
        class Execute(_message.Message):
            __slots__ = ["actor", "cpu_time_limit", "cpu_time_usage", "exit", "exit_code", "memory_limit", "memory_usage", "outputs", "signal", "wall_time_limit", "wall_time_usage"]
            class Exit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = []
            class OutputsEntry(_message.Message):
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
            EXIT_FIELD_NUMBER: _ClassVar[int]
            MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
            MEMORY_OVERFLOW: Report.Step.Execute.Exit
            MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
            OUTPUTS_FIELD_NUMBER: _ClassVar[int]
            RUNTIME_ERROR: Report.Step.Execute.Exit
            SIGNAL_FIELD_NUMBER: _ClassVar[int]
            SKIPPED: Report.Step.Execute.Exit
            SUCCESS: Report.Step.Execute.Exit
            TIMEOUT: Report.Step.Execute.Exit
            UNSPECIFIED: Report.Step.Execute.Exit
            WALL_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
            WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
            actor: str
            cpu_time_limit: int
            cpu_time_usage: int
            exit: Report.Step.Execute.Exit
            exit_code: int
            memory_limit: int
            memory_usage: int
            outputs: _containers.ScalarMap[str, str]
            signal: int
            wall_time_limit: int
            wall_time_usage: int
            def __init__(self, actor: _Optional[str] = ..., exit: _Optional[_Union[Report.Step.Execute.Exit, str]] = ..., outputs: _Optional[_Mapping[str, str]] = ..., wall_time_usage: _Optional[int] = ..., wall_time_limit: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., cpu_time_limit: _Optional[int] = ..., memory_usage: _Optional[int] = ..., memory_limit: _Optional[int] = ..., exit_code: _Optional[int] = ..., signal: _Optional[int] = ...) -> None: ...
        class Upload(_message.Message):
            __slots__ = ["target_ern", "target_name"]
            TARGET_ERN_FIELD_NUMBER: _ClassVar[int]
            TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
            target_ern: str
            target_name: str
            def __init__(self, target_name: _Optional[str] = ..., target_ern: _Optional[str] = ...) -> None: ...
        EXECUTE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_FIELD_NUMBER: _ClassVar[int]
        execute: Report.Step.Execute
        name: str
        state: Report.State
        upload: Report.Step.Upload
        def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[Report.State, str]] = ..., execute: _Optional[_Union[Report.Step.Execute, _Mapping]] = ..., upload: _Optional[_Union[Report.Step.Upload, _Mapping]] = ...) -> None: ...
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: Report.State
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXECUTING: Report.State
    FAILED: Report.State
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PENDING: Report.State
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    UNSPECIFIED: Report.State
    VERSION_FIELD_NUMBER: _ClassVar[int]
    actors: _containers.RepeatedCompositeFieldContainer[Report.Actor]
    agent: str
    error: str
    origin: str
    reference: str
    runs: _containers.RepeatedCompositeFieldContainer[Report.Run]
    state: Report.State
    version: int
    def __init__(self, reference: _Optional[str] = ..., origin: _Optional[str] = ..., agent: _Optional[str] = ..., version: _Optional[int] = ..., state: _Optional[_Union[Report.State, str]] = ..., actors: _Optional[_Iterable[_Union[Report.Actor, _Mapping]]] = ..., runs: _Optional[_Iterable[_Union[Report.Run, _Mapping]]] = ..., error: _Optional[str] = ...) -> None: ...
