from eolymp.executor import task_pb2 as _task_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ["actors", "origin", "preconditions", "reference", "runs", "scenario"]
    class Actor(_message.Message):
        __slots__ = ["env", "files", "footer_url", "header_url", "mount", "name", "output_format", "runtime", "source_url"]
        class OutputFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class EnvEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ENV_FIELD_NUMBER: _ClassVar[int]
        EXIT_CODE: Job.Actor.OutputFormat
        FILES_FIELD_NUMBER: _ClassVar[int]
        FOOTER_URL_FIELD_NUMBER: _ClassVar[int]
        HEADER_URL_FIELD_NUMBER: _ClassVar[int]
        MOUNT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
        TESTLIB_OUTPUT: Job.Actor.OutputFormat
        env: _containers.ScalarMap[str, str]
        files: _containers.RepeatedCompositeFieldContainer[Job.File]
        footer_url: str
        header_url: str
        mount: _containers.RepeatedCompositeFieldContainer[Job.Mount]
        name: str
        output_format: Job.Actor.OutputFormat
        runtime: str
        source_url: str
        def __init__(self, name: _Optional[str] = ..., runtime: _Optional[str] = ..., source_url: _Optional[str] = ..., header_url: _Optional[str] = ..., footer_url: _Optional[str] = ..., env: _Optional[_Mapping[str, str]] = ..., files: _Optional[_Iterable[_Union[Job.File, _Mapping]]] = ..., output_format: _Optional[_Union[Job.Actor.OutputFormat, str]] = ..., mount: _Optional[_Iterable[_Union[Job.Mount, _Mapping]]] = ...) -> None: ...
    class File(_message.Message):
        __slots__ = ["path", "source_url"]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
        path: str
        source_url: str
        def __init__(self, path: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...
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
        steps: _containers.RepeatedCompositeFieldContainer[Job.Step]
        def __init__(self, reference: _Optional[str] = ..., index: _Optional[int] = ..., labels: _Optional[_Iterable[str]] = ..., steps: _Optional[_Iterable[_Union[Job.Step, _Mapping]]] = ...) -> None: ...
    class Step(_message.Message):
        __slots__ = ["copy", "even_on_failure", "execute", "group", "name", "only_on_failure", "upload", "write"]
        class Copy(_message.Message):
            __slots__ = ["optionally", "remove_source", "source_actor", "source_path", "target_actor", "target_path"]
            OPTIONALLY_FIELD_NUMBER: _ClassVar[int]
            REMOVE_SOURCE_FIELD_NUMBER: _ClassVar[int]
            SOURCE_ACTOR_FIELD_NUMBER: _ClassVar[int]
            SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
            TARGET_ACTOR_FIELD_NUMBER: _ClassVar[int]
            TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
            optionally: bool
            remove_source: bool
            source_actor: str
            source_path: str
            target_actor: str
            target_path: str
            def __init__(self, source_actor: _Optional[str] = ..., source_path: _Optional[str] = ..., target_actor: _Optional[str] = ..., target_path: _Optional[str] = ..., optionally: bool = ..., remove_source: bool = ...) -> None: ...
        class Execute(_message.Message):
            __slots__ = ["actor", "args", "cpu_time_limit", "env", "file_size_limit", "memory_limit", "stderr", "stdin", "stdin_last", "stdout", "wall_time_limit"]
            class EnvEntry(_message.Message):
                __slots__ = ["key", "value"]
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str
                def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
            ACTOR_FIELD_NUMBER: _ClassVar[int]
            ARGS_FIELD_NUMBER: _ClassVar[int]
            CPU_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
            ENV_FIELD_NUMBER: _ClassVar[int]
            FILE_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
            MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
            STDERR_FIELD_NUMBER: _ClassVar[int]
            STDIN_FIELD_NUMBER: _ClassVar[int]
            STDIN_LAST_FIELD_NUMBER: _ClassVar[int]
            STDOUT_FIELD_NUMBER: _ClassVar[int]
            WALL_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
            actor: str
            args: _containers.RepeatedScalarFieldContainer[str]
            cpu_time_limit: int
            env: _containers.ScalarMap[str, str]
            file_size_limit: int
            memory_limit: int
            stderr: str
            stdin: str
            stdin_last: bool
            stdout: str
            wall_time_limit: int
            def __init__(self, actor: _Optional[str] = ..., args: _Optional[_Iterable[str]] = ..., env: _Optional[_Mapping[str, str]] = ..., stdin: _Optional[str] = ..., stdout: _Optional[str] = ..., stderr: _Optional[str] = ..., stdin_last: bool = ..., wall_time_limit: _Optional[int] = ..., cpu_time_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., file_size_limit: _Optional[int] = ...) -> None: ...
        class Group(_message.Message):
            __slots__ = ["processes"]
            PROCESSES_FIELD_NUMBER: _ClassVar[int]
            processes: _containers.RepeatedCompositeFieldContainer[Job.Step.Execute]
            def __init__(self, processes: _Optional[_Iterable[_Union[Job.Step.Execute, _Mapping]]] = ...) -> None: ...
        class Upload(_message.Message):
            __slots__ = ["force_upload", "max_data_size", "max_size", "optionally", "source_actor", "source_path", "target_name", "ttl"]
            FORCE_UPLOAD_FIELD_NUMBER: _ClassVar[int]
            MAX_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
            MAX_SIZE_FIELD_NUMBER: _ClassVar[int]
            OPTIONALLY_FIELD_NUMBER: _ClassVar[int]
            SOURCE_ACTOR_FIELD_NUMBER: _ClassVar[int]
            SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
            TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
            TTL_FIELD_NUMBER: _ClassVar[int]
            force_upload: bool
            max_data_size: int
            max_size: int
            optionally: bool
            source_actor: str
            source_path: str
            target_name: str
            ttl: int
            def __init__(self, source_actor: _Optional[str] = ..., source_path: _Optional[str] = ..., target_name: _Optional[str] = ..., optionally: bool = ..., ttl: _Optional[int] = ..., max_size: _Optional[int] = ..., max_data_size: _Optional[int] = ..., force_upload: bool = ...) -> None: ...
        class Write(_message.Message):
            __slots__ = ["fix_crlf", "source_url", "target_actor", "target_path"]
            FIX_CRLF_FIELD_NUMBER: _ClassVar[int]
            SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
            TARGET_ACTOR_FIELD_NUMBER: _ClassVar[int]
            TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
            fix_crlf: bool
            source_url: str
            target_actor: str
            target_path: str
            def __init__(self, source_url: _Optional[str] = ..., target_actor: _Optional[str] = ..., target_path: _Optional[str] = ..., fix_crlf: bool = ...) -> None: ...
        COPY_FIELD_NUMBER: _ClassVar[int]
        EVEN_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_FIELD_NUMBER: _ClassVar[int]
        GROUP_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ONLY_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_FIELD_NUMBER: _ClassVar[int]
        WRITE_FIELD_NUMBER: _ClassVar[int]
        copy: Job.Step.Copy
        even_on_failure: bool
        execute: Job.Step.Execute
        group: Job.Step.Group
        name: str
        only_on_failure: bool
        upload: Job.Step.Upload
        write: Job.Step.Write
        def __init__(self, name: _Optional[str] = ..., even_on_failure: bool = ..., only_on_failure: bool = ..., write: _Optional[_Union[Job.Step.Write, _Mapping]] = ..., copy: _Optional[_Union[Job.Step.Copy, _Mapping]] = ..., execute: _Optional[_Union[Job.Step.Execute, _Mapping]] = ..., upload: _Optional[_Union[Job.Step.Upload, _Mapping]] = ..., group: _Optional[_Union[Job.Step.Group, _Mapping]] = ...) -> None: ...
    ACTORS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_FIELD_NUMBER: _ClassVar[int]
    actors: _containers.RepeatedCompositeFieldContainer[Job.Actor]
    origin: str
    preconditions: _containers.RepeatedCompositeFieldContainer[_task_pb2.Task.Precondition]
    reference: str
    runs: _containers.RepeatedCompositeFieldContainer[Job.Run]
    scenario: _containers.RepeatedCompositeFieldContainer[Job.Step]
    def __init__(self, reference: _Optional[str] = ..., origin: _Optional[str] = ..., preconditions: _Optional[_Iterable[_Union[_task_pb2.Task.Precondition, _Mapping]]] = ..., actors: _Optional[_Iterable[_Union[Job.Actor, _Mapping]]] = ..., scenario: _Optional[_Iterable[_Union[Job.Step, _Mapping]]] = ..., runs: _Optional[_Iterable[_Union[Job.Run, _Mapping]]] = ...) -> None: ...
