from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatusV2(_message.Message):
    __slots__ = ["actors", "agent", "error", "origin", "reference", "runs", "type", "version"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
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
    class CopyOp(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class ExecuteOp(_message.Message):
        __slots__ = ["actor", "cpu_time_limit", "cpu_time_usage", "exit_code", "memory_limit", "memory_usage", "signal", "status", "wall_time_limit", "wall_time_usage"]
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ACTOR_FIELD_NUMBER: _ClassVar[int]
        CPU_EXHAUSTED: StatusV2.ExecuteOp.Status
        CPU_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        MEMORY_OVERFLOW: StatusV2.ExecuteOp.Status
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_ERROR: StatusV2.ExecuteOp.Status
        SIGNAL_FIELD_NUMBER: _ClassVar[int]
        SKIPPED: StatusV2.ExecuteOp.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SUCCESS: StatusV2.ExecuteOp.Status
        TIMEOUT: StatusV2.ExecuteOp.Status
        UNSPECIFIED: StatusV2.ExecuteOp.Status
        WALL_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        actor: str
        cpu_time_limit: int
        cpu_time_usage: int
        exit_code: int
        memory_limit: int
        memory_usage: int
        signal: int
        status: StatusV2.ExecuteOp.Status
        wall_time_limit: int
        wall_time_usage: int
        def __init__(self, actor: _Optional[str] = ..., status: _Optional[_Union[StatusV2.ExecuteOp.Status, str]] = ..., wall_time_usage: _Optional[int] = ..., wall_time_limit: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., cpu_time_limit: _Optional[int] = ..., memory_usage: _Optional[int] = ..., memory_limit: _Optional[int] = ..., exit_code: _Optional[int] = ..., signal: _Optional[int] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["reference", "status", "steps"]
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        COMPLETE: StatusV2.Run.Status
        EXECUTING: StatusV2.Run.Status
        PENDING: StatusV2.Run.Status
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        RUN_ERROR: StatusV2.Run.Status
        SKIPPED: StatusV2.Run.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        STEPS_FIELD_NUMBER: _ClassVar[int]
        UNSPECIFIED: StatusV2.Run.Status
        reference: str
        status: StatusV2.Run.Status
        steps: _containers.RepeatedCompositeFieldContainer[StatusV2.Step]
        def __init__(self, reference: _Optional[str] = ..., status: _Optional[_Union[StatusV2.Run.Status, str]] = ..., steps: _Optional[_Iterable[_Union[StatusV2.Step, _Mapping]]] = ...) -> None: ...
    class Step(_message.Message):
        __slots__ = ["copy", "execute", "name", "upload", "write"]
        COPY_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_FIELD_NUMBER: _ClassVar[int]
        WRITE_FIELD_NUMBER: _ClassVar[int]
        copy: _containers.RepeatedCompositeFieldContainer[StatusV2.CopyOp]
        execute: _containers.RepeatedCompositeFieldContainer[StatusV2.ExecuteOp]
        name: str
        upload: _containers.RepeatedCompositeFieldContainer[StatusV2.UploadOp]
        write: _containers.RepeatedCompositeFieldContainer[StatusV2.WriteOp]
        def __init__(self, name: _Optional[str] = ..., write: _Optional[_Iterable[_Union[StatusV2.WriteOp, _Mapping]]] = ..., copy: _Optional[_Iterable[_Union[StatusV2.CopyOp, _Mapping]]] = ..., execute: _Optional[_Iterable[_Union[StatusV2.ExecuteOp, _Mapping]]] = ..., upload: _Optional[_Iterable[_Union[StatusV2.UploadOp, _Mapping]]] = ...) -> None: ...
    class UploadOp(_message.Message):
        __slots__ = ["target_ern", "target_name"]
        TARGET_ERN_FIELD_NUMBER: _ClassVar[int]
        TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
        target_ern: str
        target_name: str
        def __init__(self, target_name: _Optional[str] = ..., target_ern: _Optional[str] = ...) -> None: ...
    class WriteOp(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    ERROR: StatusV2.Type
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNSPECIFIED: StatusV2.Type
    UPDATE: StatusV2.Type
    VERSION_FIELD_NUMBER: _ClassVar[int]
    actors: _containers.RepeatedCompositeFieldContainer[StatusV2.Actor]
    agent: str
    error: str
    origin: str
    reference: str
    runs: _containers.RepeatedCompositeFieldContainer[StatusV2.Run]
    type: StatusV2.Type
    version: int
    def __init__(self, reference: _Optional[str] = ..., origin: _Optional[str] = ..., type: _Optional[_Union[StatusV2.Type, str]] = ..., version: _Optional[int] = ..., agent: _Optional[str] = ..., actors: _Optional[_Iterable[_Union[StatusV2.Actor, _Mapping]]] = ..., runs: _Optional[_Iterable[_Union[StatusV2.Run, _Mapping]]] = ..., error: _Optional[str] = ...) -> None: ...
