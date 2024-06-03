from eolymp.executor import checker_pb2 as _checker_pb2
from eolymp.executor import interactor_pb2 as _interactor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Task(_message.Message):
    __slots__ = ["checker", "constraints", "files", "footer_url", "header_url", "interactor", "origin", "preconditions", "priority", "redirect_stderr_to_stdout", "reference", "run_count", "runs", "runtime", "source", "source_url"]
    class Constraint(_message.Message):
        __slots__ = ["actor", "cpu_time_limit", "file_size_limit", "memory_limit", "selector", "wall_time_limit"]
        ACTOR_FIELD_NUMBER: _ClassVar[int]
        CPU_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        SELECTOR_FIELD_NUMBER: _ClassVar[int]
        WALL_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        actor: str
        cpu_time_limit: int
        file_size_limit: int
        memory_limit: int
        selector: _containers.RepeatedScalarFieldContainer[str]
        wall_time_limit: int
        def __init__(self, selector: _Optional[_Iterable[str]] = ..., actor: _Optional[str] = ..., wall_time_limit: _Optional[int] = ..., cpu_time_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., file_size_limit: _Optional[int] = ...) -> None: ...
    class File(_message.Message):
        __slots__ = ["path", "source_url"]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
        path: str
        source_url: str
        def __init__(self, path: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...
    class Precondition(_message.Message):
        __slots__ = ["depends_on", "max_execution_time", "selector", "stop_on_failure"]
        DEPENDS_ON_FIELD_NUMBER: _ClassVar[int]
        MAX_EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
        SELECTOR_FIELD_NUMBER: _ClassVar[int]
        STOP_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
        depends_on: _containers.RepeatedScalarFieldContainer[str]
        max_execution_time: int
        selector: _containers.RepeatedScalarFieldContainer[str]
        stop_on_failure: bool
        def __init__(self, selector: _Optional[_Iterable[str]] = ..., depends_on: _Optional[_Iterable[str]] = ..., stop_on_failure: bool = ..., max_execution_time: _Optional[int] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["answer_content", "answer_object_id", "answer_url", "cost", "debug", "index", "input_content", "input_object_id", "input_url", "labels", "reference"]
        ANSWER_CONTENT_FIELD_NUMBER: _ClassVar[int]
        ANSWER_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        DEBUG_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        INPUT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        answer_content: str
        answer_object_id: str
        answer_url: str
        cost: float
        debug: bool
        index: int
        input_content: str
        input_object_id: str
        input_url: str
        labels: _containers.RepeatedScalarFieldContainer[str]
        reference: str
        def __init__(self, reference: _Optional[str] = ..., index: _Optional[int] = ..., debug: bool = ..., cost: _Optional[float] = ..., labels: _Optional[_Iterable[str]] = ..., input_object_id: _Optional[str] = ..., input_content: _Optional[str] = ..., input_url: _Optional[str] = ..., answer_object_id: _Optional[str] = ..., answer_content: _Optional[str] = ..., answer_url: _Optional[str] = ...) -> None: ...
    CHECKER_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    FOOTER_URL_FIELD_NUMBER: _ClassVar[int]
    HEADER_URL_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_STDERR_TO_STDOUT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    checker: _checker_pb2.Checker
    constraints: _containers.RepeatedCompositeFieldContainer[Task.Constraint]
    files: _containers.RepeatedCompositeFieldContainer[Task.File]
    footer_url: str
    header_url: str
    interactor: _interactor_pb2.Interactor
    origin: str
    preconditions: _containers.RepeatedCompositeFieldContainer[Task.Precondition]
    priority: int
    redirect_stderr_to_stdout: bool
    reference: str
    run_count: int
    runs: _containers.RepeatedCompositeFieldContainer[Task.Run]
    runtime: str
    source: str
    source_url: str
    def __init__(self, reference: _Optional[str] = ..., origin: _Optional[str] = ..., priority: _Optional[int] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., source_url: _Optional[str] = ..., header_url: _Optional[str] = ..., footer_url: _Optional[str] = ..., redirect_stderr_to_stdout: bool = ..., run_count: _Optional[int] = ..., preconditions: _Optional[_Iterable[_Union[Task.Precondition, _Mapping]]] = ..., constraints: _Optional[_Iterable[_Union[Task.Constraint, _Mapping]]] = ..., checker: _Optional[_Union[_checker_pb2.Checker, _Mapping]] = ..., interactor: _Optional[_Union[_interactor_pb2.Interactor, _Mapping]] = ..., runs: _Optional[_Iterable[_Union[Task.Run, _Mapping]]] = ..., files: _Optional[_Iterable[_Union[Task.File, _Mapping]]] = ...) -> None: ...
