from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.atlas import submission_pb2 as _submission_pb2
from eolymp.atlas import testing_test_pb2 as _testing_test_pb2
from eolymp.runtime import runtime_pb2 as _runtime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Editor(_message.Message):
    __slots__ = ("state", "features", "runtimes", "type")
    class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_FEATURE: _ClassVar[Editor.Feature]
        PRINT_CODE: _ClassVar[Editor.Feature]
        RUN_CODE: _ClassVar[Editor.Feature]
        UPLOAD_CODE: _ClassVar[Editor.Feature]
        EDIT_CODE: _ClassVar[Editor.Feature]
        TRACE_CODE: _ClassVar[Editor.Feature]
    UNKNOWN_FEATURE: Editor.Feature
    PRINT_CODE: Editor.Feature
    RUN_CODE: Editor.Feature
    UPLOAD_CODE: Editor.Feature
    EDIT_CODE: Editor.Feature
    TRACE_CODE: Editor.Feature
    class State(_message.Message):
        __slots__ = ("runtime", "source_code", "input_data", "output")
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
        INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        runtime: str
        source_code: str
        input_data: str
        output: _submission_pb2.Submission.Output
        def __init__(self, runtime: _Optional[str] = ..., source_code: _Optional[str] = ..., input_data: _Optional[str] = ..., output: _Optional[_Union[_submission_pb2.Submission.Output, _Mapping]] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    RUNTIMES_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    state: Editor.State
    features: _containers.RepeatedScalarFieldContainer[Editor.Feature]
    runtimes: _containers.RepeatedCompositeFieldContainer[_runtime_pb2.Runtime]
    type: _problem_pb2.Problem.Type
    def __init__(self, state: _Optional[_Union[Editor.State, _Mapping]] = ..., features: _Optional[_Iterable[_Union[Editor.Feature, str]]] = ..., runtimes: _Optional[_Iterable[_Union[_runtime_pb2.Runtime, _Mapping]]] = ..., type: _Optional[_Union[_problem_pb2.Problem.Type, str]] = ...) -> None: ...

class DescribeEditorInput(_message.Message):
    __slots__ = ("contest_id", "problem_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class DescribeEditorOutput(_message.Message):
    __slots__ = ("editor",)
    EDITOR_FIELD_NUMBER: _ClassVar[int]
    editor: Editor
    def __init__(self, editor: _Optional[_Union[Editor, _Mapping]] = ...) -> None: ...

class DescribeEditorStateInput(_message.Message):
    __slots__ = ("contest_id", "problem_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class DescribeEditorStateOutput(_message.Message):
    __slots__ = ("runtime", "source_code", "input_data", "output", "features")
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    runtime: str
    source_code: str
    input_data: str
    output: _submission_pb2.Submission.Output
    features: _containers.RepeatedScalarFieldContainer[Editor.Feature]
    def __init__(self, runtime: _Optional[str] = ..., source_code: _Optional[str] = ..., input_data: _Optional[str] = ..., output: _Optional[_Union[_submission_pb2.Submission.Output, _Mapping]] = ..., features: _Optional[_Iterable[_Union[Editor.Feature, str]]] = ...) -> None: ...

class UpdateEditorStateInput(_message.Message):
    __slots__ = ("contest_id", "problem_id", "runtime", "source_code", "input_data", "output")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    runtime: str
    source_code: str
    input_data: str
    output: _submission_pb2.Submission.Output
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., runtime: _Optional[str] = ..., source_code: _Optional[str] = ..., input_data: _Optional[str] = ..., output: _Optional[_Union[_submission_pb2.Submission.Output, _Mapping]] = ...) -> None: ...

class UpdateEditorStateOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListInputsInput(_message.Message):
    __slots__ = ("contest_id", "problem_id", "version")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    version: int
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ListInputsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_testing_test_pb2.Test]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_testing_test_pb2.Test, _Mapping]]] = ...) -> None: ...

class PrintEditorCodeInput(_message.Message):
    __slots__ = ("contest_id", "problem_id", "runtime", "source_code")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    runtime: str
    source_code: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., runtime: _Optional[str] = ..., source_code: _Optional[str] = ...) -> None: ...

class PrintEditorCodeOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
