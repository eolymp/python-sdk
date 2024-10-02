from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import module_pb2 as _module_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateModuleInput(_message.Message):
    __slots__ = ["module"]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    module: _module_pb2.Module
    def __init__(self, module: _Optional[_Union[_module_pb2.Module, _Mapping]] = ...) -> None: ...

class CreateModuleOutput(_message.Message):
    __slots__ = ["module_id"]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    module_id: str
    def __init__(self, module_id: _Optional[str] = ...) -> None: ...

class DeleteModuleInput(_message.Message):
    __slots__ = ["module_id"]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    module_id: str
    def __init__(self, module_id: _Optional[str] = ...) -> None: ...

class DeleteModuleOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeModuleInput(_message.Message):
    __slots__ = ["extra", "group_id", "member_id", "module_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_module_pb2.Module.Extra]
    group_id: str
    member_id: str
    module_id: str
    def __init__(self, module_id: _Optional[str] = ..., member_id: _Optional[str] = ..., group_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_module_pb2.Module.Extra, str]]] = ...) -> None: ...

class DescribeModuleOutput(_message.Message):
    __slots__ = ["module"]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    module: _module_pb2.Module
    def __init__(self, module: _Optional[_Union[_module_pb2.Module, _Mapping]] = ...) -> None: ...

class GradeModuleInput(_message.Message):
    __slots__ = ["excused", "grade", "member_id", "module_id"]
    EXCUSED_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    excused: bool
    grade: int
    member_id: str
    module_id: str
    def __init__(self, module_id: _Optional[str] = ..., member_id: _Optional[str] = ..., grade: _Optional[int] = ..., excused: bool = ...) -> None: ...

class GradeModuleOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListModulesInput(_message.Message):
    __slots__ = ["extra", "filters", "group_id", "member_id", "offset", "order", "size", "sort"]
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["draft", "extra", "graded", "query", "weight"]
        DRAFT_FIELD_NUMBER: _ClassVar[int]
        EXTRA_FIELD_NUMBER: _ClassVar[int]
        GRADED_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        draft: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        extra: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        graded: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        query: str
        weight: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        def __init__(self, query: _Optional[str] = ..., draft: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., extra: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., graded: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., weight: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ...) -> None: ...
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX: ListModulesInput.Sort
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_module_pb2.Module.Extra]
    filters: ListModulesInput.Filter
    group_id: str
    member_id: str
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListModulesInput.Sort
    def __init__(self, member_id: _Optional[str] = ..., group_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListModulesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListModulesInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_module_pb2.Module.Extra, str]]] = ...) -> None: ...

class ListModulesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_module_pb2.Module]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_module_pb2.Module, _Mapping]]] = ...) -> None: ...

class StartModuleInput(_message.Message):
    __slots__ = ["module_id"]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    module_id: str
    def __init__(self, module_id: _Optional[str] = ...) -> None: ...

class StartModuleOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateModuleInput(_message.Message):
    __slots__ = ["module", "module_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateModuleInput.Patch
    DESCRIPTION: UpdateModuleInput.Patch
    DRAFT: UpdateModuleInput.Patch
    EXTRA: UpdateModuleInput.Patch
    IMAGE_URL: UpdateModuleInput.Patch
    INDEX: UpdateModuleInput.Patch
    MODULE_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME: UpdateModuleInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    WEIGHT: UpdateModuleInput.Patch
    module: _module_pb2.Module
    module_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateModuleInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateModuleInput.Patch, str]]] = ..., module_id: _Optional[str] = ..., module: _Optional[_Union[_module_pb2.Module, _Mapping]] = ...) -> None: ...

class UpdateModuleOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
