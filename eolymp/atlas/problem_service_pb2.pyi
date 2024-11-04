from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from eolymp.atlas import version_pb2 as _version_pb2
from eolymp.runtime import runtime_pb2 as _runtime_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProblemInput(_message.Message):
    __slots__ = ["problem", "statement"]
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    problem: _problem_pb2.Problem
    statement: _statement_pb2.Statement
    def __init__(self, problem: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ..., statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class CreateProblemOutput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class DeleteProblemInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class DeleteProblemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeProblemInput(_message.Message):
    __slots__ = ["extra", "problem_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_problem_pb2.Problem.Extra]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_problem_pb2.Problem.Extra, str]]] = ...) -> None: ...

class DescribeProblemOutput(_message.Message):
    __slots__ = ["problem"]
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    problem: _problem_pb2.Problem
    def __init__(self, problem: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ...) -> None: ...

class ListProblemsInput(_message.Message):
    __slots__ = ["extra", "filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["difficulty", "id", "is_bookmarked", "is_private", "is_visible", "number", "query", "score", "status", "topic_id"]
        DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        IS_BOOKMARKED_FIELD_NUMBER: _ClassVar[int]
        IS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
        IS_VISIBLE_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
        difficulty: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        is_bookmarked: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        is_private: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        is_visible: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        number: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        query: str
        score: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        topic_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., topic_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., is_visible: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., is_private: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., number: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., difficulty: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., score: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., is_bookmarked: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    DEFAULT: ListProblemsInput.Sortable
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    POPULAR: ListProblemsInput.Sortable
    RECENT: ListProblemsInput.Sortable
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_problem_pb2.Problem.Extra]
    filters: ListProblemsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListProblemsInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListProblemsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListProblemsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_problem_pb2.Problem.Extra, str]]] = ...) -> None: ...

class ListProblemsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2.Problem]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2.Problem, _Mapping]]] = ...) -> None: ...

class ListRuntimesInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListRuntimesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_runtime_pb2.Runtime]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_runtime_pb2.Runtime, _Mapping]]] = ...) -> None: ...

class ListVersionsInput(_message.Message):
    __slots__ = ["filters", "offset", "problem_id", "size"]
    class Filter(_message.Message):
        __slots__ = ["change_op", "change_path", "created_at", "created_by", "number"]
        CHANGE_OP_FIELD_NUMBER: _ClassVar[int]
        CHANGE_PATH_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        CREATED_BY_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        change_op: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        change_path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        created_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        created_by: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        number: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        def __init__(self, number: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., created_by: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., created_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., change_op: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., change_path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListVersionsInput.Filter
    offset: int
    problem_id: str
    size: int
    def __init__(self, problem_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListVersionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListVersionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_version_pb2.Version]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_version_pb2.Version, _Mapping]]] = ...) -> None: ...

class ProblemChangedEvent(_message.Message):
    __slots__ = ["after", "before"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    after: _problem_pb2.Problem
    before: _problem_pb2.Problem
    def __init__(self, before: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ..., after: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ...) -> None: ...

class SyncProblemInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class SyncProblemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdatePrivacyInput(_message.Message):
    __slots__ = ["private", "problem_id"]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    private: bool
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., private: bool = ...) -> None: ...

class UpdatePrivacyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateProblemInput(_message.Message):
    __slots__ = ["patch", "problem", "problem_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateProblemInput.Patch
    DIFFICULTY: UpdateProblemInput.Patch
    ORIGIN: UpdateProblemInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PRIVATE: UpdateProblemInput.Patch
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TOPICS: UpdateProblemInput.Patch
    TYPE: UpdateProblemInput.Patch
    VISIBLE: UpdateProblemInput.Patch
    patch: _containers.RepeatedScalarFieldContainer[UpdateProblemInput.Patch]
    problem: _problem_pb2.Problem
    problem_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateProblemInput.Patch, str]]] = ..., problem_id: _Optional[str] = ..., problem: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ...) -> None: ...

class UpdateProblemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateVisibilityInput(_message.Message):
    __slots__ = ["problem_id", "visible"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    visible: bool
    def __init__(self, problem_id: _Optional[str] = ..., visible: bool = ...) -> None: ...

class UpdateVisibilityOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VoteProblemInput(_message.Message):
    __slots__ = ["problem_id", "vote"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    vote: int
    def __init__(self, problem_id: _Optional[str] = ..., vote: _Optional[int] = ...) -> None: ...

class VoteProblemOutput(_message.Message):
    __slots__ = ["vote_count"]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    vote_count: int
    def __init__(self, vote_count: _Optional[int] = ...) -> None: ...
