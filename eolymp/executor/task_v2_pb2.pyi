from eolymp.executor import interactor_pb2 as _interactor_pb2
from eolymp.executor import task_pb2 as _task_pb2
from eolymp.executor import verifier_pb2 as _verifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskV2(_message.Message):
    __slots__ = ["actors", "constraints", "origin", "preconditions", "reference", "runs"]
    class Actor(_message.Message):
        __slots__ = ["args", "env", "init_env", "init_files", "mount", "name", "runtime", "source_ern", "stderr", "stdin", "stdout"]
        class EnvEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class InitEnvEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ARGS_FIELD_NUMBER: _ClassVar[int]
        ENV_FIELD_NUMBER: _ClassVar[int]
        INIT_ENV_FIELD_NUMBER: _ClassVar[int]
        INIT_FILES_FIELD_NUMBER: _ClassVar[int]
        MOUNT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ERN_FIELD_NUMBER: _ClassVar[int]
        STDERR_FIELD_NUMBER: _ClassVar[int]
        STDIN_FIELD_NUMBER: _ClassVar[int]
        STDOUT_FIELD_NUMBER: _ClassVar[int]
        args: _containers.RepeatedScalarFieldContainer[str]
        env: _containers.ScalarMap[str, str]
        init_env: _containers.ScalarMap[str, str]
        init_files: _containers.RepeatedCompositeFieldContainer[TaskV2.File]
        mount: _containers.RepeatedCompositeFieldContainer[TaskV2.Mount]
        name: str
        runtime: str
        source_ern: str
        stderr: str
        stdin: str
        stdout: str
        def __init__(self, name: _Optional[str] = ..., runtime: _Optional[str] = ..., source_ern: _Optional[str] = ..., init_env: _Optional[_Mapping[str, str]] = ..., init_files: _Optional[_Iterable[_Union[TaskV2.File, _Mapping]]] = ..., args: _Optional[_Iterable[str]] = ..., env: _Optional[_Mapping[str, str]] = ..., stdin: _Optional[str] = ..., stdout: _Optional[str] = ..., stderr: _Optional[str] = ..., mount: _Optional[_Iterable[_Union[TaskV2.Mount, _Mapping]]] = ...) -> None: ...
    class CopyOp(_message.Message):
        __slots__ = ["optionally", "source_actor", "source_path", "target_actor", "target_path"]
        OPTIONALLY_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ACTOR_FIELD_NUMBER: _ClassVar[int]
        SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
        TARGET_ACTOR_FIELD_NUMBER: _ClassVar[int]
        TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
        optionally: bool
        source_actor: str
        source_path: str
        target_actor: str
        target_path: str
        def __init__(self, source_actor: _Optional[str] = ..., source_path: _Optional[str] = ..., target_actor: _Optional[str] = ..., target_path: _Optional[str] = ..., optionally: bool = ...) -> None: ...
    class ExecuteOp(_message.Message):
        __slots__ = ["actor", "args", "env"]
        class EnvEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ACTOR_FIELD_NUMBER: _ClassVar[int]
        ARGS_FIELD_NUMBER: _ClassVar[int]
        ENV_FIELD_NUMBER: _ClassVar[int]
        actor: str
        args: _containers.RepeatedScalarFieldContainer[str]
        env: _containers.ScalarMap[str, str]
        def __init__(self, actor: _Optional[str] = ..., args: _Optional[_Iterable[str]] = ..., env: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class File(_message.Message):
        __slots__ = ["path", "source_ern"]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ERN_FIELD_NUMBER: _ClassVar[int]
        path: str
        source_ern: str
        def __init__(self, path: _Optional[str] = ..., source_ern: _Optional[str] = ...) -> None: ...
    class Mount(_message.Message):
        __slots__ = ["from_actor", "to_path"]
        FROM_ACTOR_FIELD_NUMBER: _ClassVar[int]
        TO_PATH_FIELD_NUMBER: _ClassVar[int]
        from_actor: str
        to_path: str
        def __init__(self, from_actor: _Optional[str] = ..., to_path: _Optional[str] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["index", "labels", "reference", "steps"]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        STEPS_FIELD_NUMBER: _ClassVar[int]
        index: int
        labels: _containers.RepeatedScalarFieldContainer[str]
        reference: str
        steps: _containers.RepeatedCompositeFieldContainer[TaskV2.Step]
        def __init__(self, reference: _Optional[str] = ..., index: _Optional[int] = ..., labels: _Optional[_Iterable[str]] = ..., steps: _Optional[_Iterable[_Union[TaskV2.Step, _Mapping]]] = ...) -> None: ...
    class Step(_message.Message):
        __slots__ = ["copy", "execute", "name", "upload", "write"]
        COPY_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_FIELD_NUMBER: _ClassVar[int]
        WRITE_FIELD_NUMBER: _ClassVar[int]
        copy: _containers.RepeatedCompositeFieldContainer[TaskV2.CopyOp]
        execute: _containers.RepeatedCompositeFieldContainer[TaskV2.ExecuteOp]
        name: str
        upload: _containers.RepeatedCompositeFieldContainer[TaskV2.UploadOp]
        write: _containers.RepeatedCompositeFieldContainer[TaskV2.WriteOp]
        def __init__(self, name: _Optional[str] = ..., write: _Optional[_Iterable[_Union[TaskV2.WriteOp, _Mapping]]] = ..., copy: _Optional[_Iterable[_Union[TaskV2.CopyOp, _Mapping]]] = ..., execute: _Optional[_Iterable[_Union[TaskV2.ExecuteOp, _Mapping]]] = ..., upload: _Optional[_Iterable[_Union[TaskV2.UploadOp, _Mapping]]] = ...) -> None: ...
    class UploadOp(_message.Message):
        __slots__ = ["max_size", "optionally", "source_actor", "source_path", "target_name", "ttl"]
        MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
        OPTIONALLY_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ACTOR_FIELD_NUMBER: _ClassVar[int]
        SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
        TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
        TTL_FIELD_NUMBER: _ClassVar[int]
        max_size: int
        optionally: bool
        source_actor: str
        source_path: str
        target_name: str
        ttl: int
        def __init__(self, source_actor: _Optional[str] = ..., source_path: _Optional[str] = ..., target_name: _Optional[str] = ..., optionally: bool = ..., ttl: _Optional[int] = ..., max_size: _Optional[int] = ...) -> None: ...
    class WriteOp(_message.Message):
        __slots__ = ["source_ern", "target_actor", "target_path"]
        SOURCE_ERN_FIELD_NUMBER: _ClassVar[int]
        TARGET_ACTOR_FIELD_NUMBER: _ClassVar[int]
        TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
        source_ern: str
        target_actor: str
        target_path: str
        def __init__(self, source_ern: _Optional[str] = ..., target_actor: _Optional[str] = ..., target_path: _Optional[str] = ...) -> None: ...
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    actors: _containers.RepeatedCompositeFieldContainer[TaskV2.Actor]
    constraints: _containers.RepeatedCompositeFieldContainer[_task_pb2.Task.Constraint]
    origin: str
    preconditions: _containers.RepeatedCompositeFieldContainer[_task_pb2.Task.Precondition]
    reference: str
    runs: _containers.RepeatedCompositeFieldContainer[TaskV2.Run]
    def __init__(self, reference: _Optional[str] = ..., origin: _Optional[str] = ..., preconditions: _Optional[_Iterable[_Union[_task_pb2.Task.Precondition, _Mapping]]] = ..., constraints: _Optional[_Iterable[_Union[_task_pb2.Task.Constraint, _Mapping]]] = ..., actors: _Optional[_Iterable[_Union[TaskV2.Actor, _Mapping]]] = ..., runs: _Optional[_Iterable[_Union[TaskV2.Run, _Mapping]]] = ...) -> None: ...