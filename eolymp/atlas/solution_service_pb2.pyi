from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import solution_pb2 as _solution_pb2
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
    __slots__ = ["problem_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

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
