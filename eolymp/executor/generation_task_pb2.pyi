from eolymp.executor import script_pb2 as _script_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerationTask(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "run_count", "interactor", "validator", "scripts", "runs")
    class Generator(_message.Message):
        __slots__ = ("script_name", "arguments")
        SCRIPT_NAME_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        script_name: str
        arguments: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, script_name: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ("reference", "index", "cost", "env", "input_url", "input_content", "input_generator", "answer_url", "answer_content", "answer_generator")
        class EnvEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        ENV_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        INPUT_GENERATOR_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        ANSWER_CONTENT_FIELD_NUMBER: _ClassVar[int]
        ANSWER_GENERATOR_FIELD_NUMBER: _ClassVar[int]
        reference: str
        index: int
        cost: float
        env: _containers.ScalarMap[str, str]
        input_url: str
        input_content: str
        input_generator: GenerationTask.Generator
        answer_url: str
        answer_content: str
        answer_generator: GenerationTask.Generator
        def __init__(self, reference: _Optional[str] = ..., index: _Optional[int] = ..., cost: _Optional[float] = ..., env: _Optional[_Mapping[str, str]] = ..., input_url: _Optional[str] = ..., input_content: _Optional[str] = ..., input_generator: _Optional[_Union[GenerationTask.Generator, _Mapping]] = ..., answer_url: _Optional[str] = ..., answer_content: _Optional[str] = ..., answer_generator: _Optional[_Union[GenerationTask.Generator, _Mapping]] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    run_count: int
    interactor: _script_pb2.Script
    validator: _script_pb2.Script
    scripts: _containers.RepeatedCompositeFieldContainer[_script_pb2.Script]
    runs: _containers.RepeatedCompositeFieldContainer[GenerationTask.Run]
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., run_count: _Optional[int] = ..., interactor: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., validator: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., scripts: _Optional[_Iterable[_Union[_script_pb2.Script, _Mapping]]] = ..., runs: _Optional[_Iterable[_Union[GenerationTask.Run, _Mapping]]] = ...) -> None: ...
