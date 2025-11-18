from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import editorial_pb2 as _editorial_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.judge import problem_pb2 as _problem_pb2_1
from eolymp.judge import template_pb2 as _template_pb2
from eolymp.runtime import runtime_pb2 as _runtime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImportProblemInput(_message.Message):
    __slots__ = ("import_id", "index", "submit_limit", "score_by_best_testset")
    IMPORT_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SCORE_BY_BEST_TESTSET_FIELD_NUMBER: _ClassVar[int]
    import_id: str
    index: int
    submit_limit: int
    score_by_best_testset: bool
    def __init__(self, import_id: _Optional[str] = ..., index: _Optional[int] = ..., submit_limit: _Optional[int] = ..., score_by_best_testset: bool = ...) -> None: ...

class ImportProblemOutput(_message.Message):
    __slots__ = ("problem_id",)
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class SyncProblemInput(_message.Message):
    __slots__ = ("problem_id",)
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class SyncProblemOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateProblemInput(_message.Message):
    __slots__ = ("patch", "problem_id", "problem")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateProblemInput.Patch]
        INDEX: _ClassVar[UpdateProblemInput.Patch]
        SUBMIT_LIMIT: _ClassVar[UpdateProblemInput.Patch]
        SCORE_BY_BEST_TESTSET: _ClassVar[UpdateProblemInput.Patch]
    ALL: UpdateProblemInput.Patch
    INDEX: UpdateProblemInput.Patch
    SUBMIT_LIMIT: UpdateProblemInput.Patch
    SCORE_BY_BEST_TESTSET: UpdateProblemInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateProblemInput.Patch]
    problem_id: str
    problem: _problem_pb2_1.Problem
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateProblemInput.Patch, str]]] = ..., problem_id: _Optional[str] = ..., problem: _Optional[_Union[_problem_pb2_1.Problem, _Mapping]] = ...) -> None: ...

class UpdateProblemOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteProblemInput(_message.Message):
    __slots__ = ("problem_id",)
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class DeleteProblemOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProblemsInput(_message.Message):
    __slots__ = ("offset", "size", "locale", "extra")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_problem_pb2.Problem.Extra.Field]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_problem_pb2.Problem.Extra.Field, str]]] = ...) -> None: ...

class ListProblemsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2_1.Problem]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2_1.Problem, _Mapping]]] = ...) -> None: ...

class DescribeProblemInput(_message.Message):
    __slots__ = ("problem_id", "locale", "extra")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_problem_pb2.Problem.Extra.Field]
    def __init__(self, problem_id: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_problem_pb2.Problem.Extra.Field, str]]] = ...) -> None: ...

class DescribeProblemOutput(_message.Message):
    __slots__ = ("problem",)
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    problem: _problem_pb2_1.Problem
    def __init__(self, problem: _Optional[_Union[_problem_pb2_1.Problem, _Mapping]] = ...) -> None: ...

class DescribeCodeTemplateInput(_message.Message):
    __slots__ = ("problem_id", "template_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    template_id: str
    def __init__(self, problem_id: _Optional[str] = ..., template_id: _Optional[str] = ...) -> None: ...

class DescribeCodeTemplateOutput(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...

class LookupCodeTemplateInput(_message.Message):
    __slots__ = ("problem_id", "runtime")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    runtime: str
    def __init__(self, problem_id: _Optional[str] = ..., runtime: _Optional[str] = ...) -> None: ...

class LookupCodeTemplateOutput(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...

class ListStatementsInput(_message.Message):
    __slots__ = ("problem_id",)
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListStatementsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2_1.Problem.Statement]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2_1.Problem.Statement, _Mapping]]] = ...) -> None: ...

class DescribeEditorialInput(_message.Message):
    __slots__ = ("problem_id", "locale", "extra")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_editorial_pb2.Editorial.Extra.Field]
    def __init__(self, problem_id: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_editorial_pb2.Editorial.Extra.Field, str]]] = ...) -> None: ...

class DescribeEditorialOutput(_message.Message):
    __slots__ = ("editorial",)
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    def __init__(self, editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class ListAttachmentsInput(_message.Message):
    __slots__ = ("problem_id",)
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListAttachmentsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2_1.Problem.Attachment]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2_1.Problem.Attachment, _Mapping]]] = ...) -> None: ...

class ListExamplesInput(_message.Message):
    __slots__ = ("problem_id",)
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListExamplesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2_1.Problem.Test]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2_1.Problem.Test, _Mapping]]] = ...) -> None: ...

class ListRuntimesInput(_message.Message):
    __slots__ = ("problem_id",)
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListRuntimesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_runtime_pb2.Runtime]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_runtime_pb2.Runtime, _Mapping]]] = ...) -> None: ...
