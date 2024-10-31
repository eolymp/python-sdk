from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import problem_pb2 as _problem_pb2
from eolymp.judge import template_pb2 as _template_pb2
from eolymp.runtime import runtime_pb2 as _runtime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteProblemInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class DeleteProblemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeCodeTemplateInput(_message.Message):
    __slots__ = ["contest_id", "problem_id", "template_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    template_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., template_id: _Optional[str] = ...) -> None: ...

class DescribeCodeTemplateOutput(_message.Message):
    __slots__ = ["template"]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...

class DescribeProblemInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class DescribeProblemOutput(_message.Message):
    __slots__ = ["problem"]
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    problem: _problem_pb2.Problem
    def __init__(self, problem: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ...) -> None: ...

class ImportProblemInput(_message.Message):
    __slots__ = ["contest_id", "import_id", "index", "score_by_best_testset", "submit_limit"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    IMPORT_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SCORE_BY_BEST_TESTSET_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    import_id: str
    index: int
    score_by_best_testset: bool
    submit_limit: int
    def __init__(self, contest_id: _Optional[str] = ..., import_id: _Optional[str] = ..., index: _Optional[int] = ..., submit_limit: _Optional[int] = ..., score_by_best_testset: bool = ...) -> None: ...

class ImportProblemOutput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListAttachmentsInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class ListAttachmentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2.Problem.Attachment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2.Problem.Attachment, _Mapping]]] = ...) -> None: ...

class ListExamplesInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class ListExamplesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2.Problem.Test]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2.Problem.Test, _Mapping]]] = ...) -> None: ...

class ListProblemsInput(_message.Message):
    __slots__ = ["contest_id", "offset", "size"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    offset: int
    size: int
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListProblemsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2.Problem]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2.Problem, _Mapping]]] = ...) -> None: ...

class ListRuntimesInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class ListRuntimesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_runtime_pb2.Runtime]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_runtime_pb2.Runtime, _Mapping]]] = ...) -> None: ...

class ListStatementsInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class ListStatementsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2.Problem.Statement]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2.Problem.Statement, _Mapping]]] = ...) -> None: ...

class LookupCodeTemplateInput(_message.Message):
    __slots__ = ["contest_id", "problem_id", "runtime"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    runtime: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., runtime: _Optional[str] = ...) -> None: ...

class LookupCodeTemplateOutput(_message.Message):
    __slots__ = ["template"]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...

class SyncProblemInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class SyncProblemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateProblemInput(_message.Message):
    __slots__ = ["contest_id", "index", "problem_id", "score_by_best_testset", "submit_limit"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_BY_BEST_TESTSET_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    index: int
    problem_id: str
    score_by_best_testset: bool
    submit_limit: int
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., index: _Optional[int] = ..., submit_limit: _Optional[int] = ..., score_by_best_testset: bool = ...) -> None: ...

class UpdateProblemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
