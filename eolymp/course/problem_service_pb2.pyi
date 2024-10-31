from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import code_template_pb2 as _code_template_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from eolymp.atlas import submission_pb2 as _submission_pb2
from eolymp.atlas import testing_test_pb2 as _testing_test_pb2
from eolymp.playground import run_pb2 as _run_pb2
from eolymp.runtime import runtime_pb2 as _runtime_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRunInput(_message.Message):
    __slots__ = ["input_data", "input_ref", "runtime", "source"]
    INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
    INPUT_REF_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    input_data: bytes
    input_ref: str
    runtime: str
    source: str
    def __init__(self, runtime: _Optional[str] = ..., source: _Optional[str] = ..., input_data: _Optional[bytes] = ..., input_ref: _Optional[str] = ...) -> None: ...

class CreateRunOutput(_message.Message):
    __slots__ = ["run_id"]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class CreateSubmissionInput(_message.Message):
    __slots__ = ["problem_id", "runtime", "source"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    runtime: str
    source: str
    def __init__(self, problem_id: _Optional[str] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class CreateSubmissionOutput(_message.Message):
    __slots__ = ["submission_id"]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    def __init__(self, submission_id: _Optional[str] = ...) -> None: ...

class DescribeRunInput(_message.Message):
    __slots__ = ["run_id"]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class DescribeRunOutput(_message.Message):
    __slots__ = ["run"]
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: _run_pb2.Run
    def __init__(self, run: _Optional[_Union[_run_pb2.Run, _Mapping]] = ...) -> None: ...

class DescribeSubmissionInput(_message.Message):
    __slots__ = ["problem_id", "submission_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    submission_id: str
    def __init__(self, problem_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class DescribeSubmissionOutput(_message.Message):
    __slots__ = ["submission"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...

class ListExamplesInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListExamplesOutput(_message.Message):
    __slots__ = ["examples"]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[_testing_test_pb2.Test]
    def __init__(self, examples: _Optional[_Iterable[_Union[_testing_test_pb2.Test, _Mapping]]] = ...) -> None: ...

class ListRuntimesInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListRuntimesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_runtime_pb2.Runtime]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_runtime_pb2.Runtime, _Mapping]]] = ...) -> None: ...

class ListStatementsInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListStatementsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_statement_pb2.Statement]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_statement_pb2.Statement, _Mapping]]] = ...) -> None: ...

class ListSubmissionsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "member_id", "percentage", "runtime", "score", "status", "submitted_at", "user_id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        percentage: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        runtime: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        score: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        submitted_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., submitted_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., runtime: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., score: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., percentage: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListSubmissionsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSubmissionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListSubmissionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_submission_pb2.Submission]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_submission_pb2.Submission, _Mapping]]] = ...) -> None: ...

class LookupCodeTemplateInput(_message.Message):
    __slots__ = ["runtime"]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    runtime: str
    def __init__(self, runtime: _Optional[str] = ...) -> None: ...

class LookupCodeTemplateOutput(_message.Message):
    __slots__ = ["template"]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _code_template_pb2.Template
    def __init__(self, template: _Optional[_Union[_code_template_pb2.Template, _Mapping]] = ...) -> None: ...

class WatchRunInput(_message.Message):
    __slots__ = ["run_id"]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class WatchRunOutput(_message.Message):
    __slots__ = ["run"]
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: _run_pb2.Run
    def __init__(self, run: _Optional[_Union[_run_pb2.Run, _Mapping]] = ...) -> None: ...

class WatchSubmissionInput(_message.Message):
    __slots__ = ["problem_id", "submission_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    submission_id: str
    def __init__(self, problem_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class WatchSubmissionOutput(_message.Message):
    __slots__ = ["submission"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...
