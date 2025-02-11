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

class ListSolutionsInput(_message.Message):
    __slots__ = ("version", "offset", "size", "search", "filters", "sort", "order")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NAME: _ClassVar[ListSolutionsInput.Sortable]
        TYPE: _ClassVar[ListSolutionsInput.Sortable]
    NAME: ListSolutionsInput.Sortable
    TYPE: ListSolutionsInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "type", "name", "runtime")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        runtime: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., runtime: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    version: int
    offset: int
    size: int
    search: str
    filters: ListSolutionsInput.Filter
    sort: ListSolutionsInput.Sortable
    order: _direction_pb2.Direction
    def __init__(self, version: _Optional[int] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListSolutionsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListSolutionsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListSolutionsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_solution_pb2.Solution]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_solution_pb2.Solution, _Mapping]]] = ...) -> None: ...

class CheckSolutionsInput(_message.Message):
    __slots__ = ("filters",)
    class Filter(_message.Message):
        __slots__ = ("id", "type", "name", "runtime")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        runtime: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., runtime: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: CheckSolutionsInput.Filter
    def __init__(self, filters: _Optional[_Union[CheckSolutionsInput.Filter, _Mapping]] = ...) -> None: ...

class CheckSolutionsOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeSolutionInput(_message.Message):
    __slots__ = ("solution_id", "version")
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    solution_id: str
    version: int
    def __init__(self, solution_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeSolutionOutput(_message.Message):
    __slots__ = ("solution",)
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    solution: _solution_pb2.Solution
    def __init__(self, solution: _Optional[_Union[_solution_pb2.Solution, _Mapping]] = ...) -> None: ...

class CreateSolutionInput(_message.Message):
    __slots__ = ("solution",)
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    solution: _solution_pb2.Solution
    def __init__(self, solution: _Optional[_Union[_solution_pb2.Solution, _Mapping]] = ...) -> None: ...

class CreateSolutionOutput(_message.Message):
    __slots__ = ("solution_id",)
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    solution_id: str
    def __init__(self, solution_id: _Optional[str] = ...) -> None: ...

class UpdateSolutionInput(_message.Message):
    __slots__ = ("patch", "solution_id", "solution")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateSolutionInput.Patch]
        NAME: _ClassVar[UpdateSolutionInput.Patch]
        TYPE: _ClassVar[UpdateSolutionInput.Patch]
        RUNTIME: _ClassVar[UpdateSolutionInput.Patch]
        SOURCE: _ClassVar[UpdateSolutionInput.Patch]
        SECRET: _ClassVar[UpdateSolutionInput.Patch]
    ALL: UpdateSolutionInput.Patch
    NAME: UpdateSolutionInput.Patch
    TYPE: UpdateSolutionInput.Patch
    RUNTIME: UpdateSolutionInput.Patch
    SOURCE: UpdateSolutionInput.Patch
    SECRET: UpdateSolutionInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateSolutionInput.Patch]
    solution_id: str
    solution: _solution_pb2.Solution
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateSolutionInput.Patch, str]]] = ..., solution_id: _Optional[str] = ..., solution: _Optional[_Union[_solution_pb2.Solution, _Mapping]] = ...) -> None: ...

class UpdateSolutionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteSolutionInput(_message.Message):
    __slots__ = ("solution_id",)
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    solution_id: str
    def __init__(self, solution_id: _Optional[str] = ...) -> None: ...

class DeleteSolutionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
