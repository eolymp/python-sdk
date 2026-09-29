from eolymp.executor import checker_pb2 as _checker_pb2
from eolymp.executor import script_pb2 as _script_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationTask(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "checker", "validator", "runs")
    class Run(_message.Message):
        __slots__ = ("reference", "index", "group", "input_url", "answer_url")
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        GROUP_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        reference: str
        index: int
        group: int
        input_url: str
        answer_url: str
        def __init__(self, reference: _Optional[str] = ..., index: _Optional[int] = ..., group: _Optional[int] = ..., input_url: _Optional[str] = ..., answer_url: _Optional[str] = ...) -> None: ...
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
    CHECKER_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    checker: _checker_pb2.Checker
    validator: _script_pb2.Script
    runs: _containers.RepeatedCompositeFieldContainer[ValidationTask.Run]
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., checker: _Optional[_Union[_checker_pb2.Checker, _Mapping]] = ..., validator: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., runs: _Optional[_Iterable[_Union[ValidationTask.Run, _Mapping]]] = ...) -> None: ...
