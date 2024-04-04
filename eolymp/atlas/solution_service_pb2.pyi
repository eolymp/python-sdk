from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import solution_pb2 as _solution_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSolutionInput(_message.Message):
    __slots__ = ["problem_id", "solution"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    solution: _solution_pb2.Solution
    def __init__(self, problem_id: _Optional[str] = ..., solution: _Optional[_Union[_solution_pb2.Solution, _Mapping]] = ...) -> None: ...

class CreateSolutionOutput(_message.Message):
    __slots__ = ["solution_id"]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    solution_id: str
    def __init__(self, solution_id: _Optional[str] = ...) -> None: ...

class DeleteSolutionInput(_message.Message):
    __slots__ = ["problem_id", "solution_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    solution_id: str
    def __init__(self, problem_id: _Optional[str] = ..., solution_id: _Optional[str] = ...) -> None: ...

class DeleteSolutionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeSolutionInput(_message.Message):
    __slots__ = ["problem_id", "solution_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    solution_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., solution_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeSolutionOutput(_message.Message):
    __slots__ = ["solution"]
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    solution: _solution_pb2.Solution
    def __init__(self, solution: _Optional[_Union[_solution_pb2.Solution, _Mapping]] = ...) -> None: ...

class ListSolutionsInput(_message.Message):
    __slots__ = ["filters", "offset", "order", "problem_id", "size", "sort", "version"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["id", "name", "query", "runtime", "type"]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        runtime: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., runtime: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    NAME: ListSolutionsInput.Sortable
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    TYPE: ListSolutionsInput.Sortable
    VERSION_FIELD_NUMBER: _ClassVar[int]
    filters: ListSolutionsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    problem_id: str
    size: int
    sort: ListSolutionsInput.Sortable
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., version: _Optional[int] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSolutionsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListSolutionsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListSolutionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_solution_pb2.Solution]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_solution_pb2.Solution, _Mapping]]] = ...) -> None: ...

class UpdateSolutionInput(_message.Message):
    __slots__ = ["patch", "problem_id", "solution", "solution_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateSolutionInput.Patch
    NAME: UpdateSolutionInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME: UpdateSolutionInput.Patch
    SECRET: UpdateSolutionInput.Patch
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE: UpdateSolutionInput.Patch
    TYPE: UpdateSolutionInput.Patch
    patch: _containers.RepeatedScalarFieldContainer[UpdateSolutionInput.Patch]
    problem_id: str
    solution: _solution_pb2.Solution
    solution_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateSolutionInput.Patch, str]]] = ..., problem_id: _Optional[str] = ..., solution_id: _Optional[str] = ..., solution: _Optional[_Union[_solution_pb2.Solution, _Mapping]] = ...) -> None: ...

class UpdateSolutionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
