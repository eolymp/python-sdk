from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import material_pb2 as _material_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateMaterialInput(_message.Message):
    __slots__ = ("material", "module_id")
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    material: _material_pb2.Material
    module_id: str
    def __init__(self, material: _Optional[_Union[_material_pb2.Material, _Mapping]] = ..., module_id: _Optional[str] = ...) -> None: ...

class CreateMaterialOutput(_message.Message):
    __slots__ = ("material_id",)
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    material_id: str
    def __init__(self, material_id: _Optional[str] = ...) -> None: ...

class UpdateMaterialInput(_message.Message):
    __slots__ = ("patch", "material_id", "material")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateMaterialInput.Patch]
        DRAFT: _ClassVar[UpdateMaterialInput.Patch]
        NAME: _ClassVar[UpdateMaterialInput.Patch]
        IMAGE_URL: _ClassVar[UpdateMaterialInput.Patch]
        INDEX: _ClassVar[UpdateMaterialInput.Patch]
        DEPTH: _ClassVar[UpdateMaterialInput.Patch]
        CONTENT: _ClassVar[UpdateMaterialInput.Patch]
        GRADING: _ClassVar[UpdateMaterialInput.Patch]
    ALL: UpdateMaterialInput.Patch
    DRAFT: UpdateMaterialInput.Patch
    NAME: UpdateMaterialInput.Patch
    IMAGE_URL: UpdateMaterialInput.Patch
    INDEX: UpdateMaterialInput.Patch
    DEPTH: UpdateMaterialInput.Patch
    CONTENT: UpdateMaterialInput.Patch
    GRADING: UpdateMaterialInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateMaterialInput.Patch]
    material_id: str
    material: _material_pb2.Material
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateMaterialInput.Patch, str]]] = ..., material_id: _Optional[str] = ..., material: _Optional[_Union[_material_pb2.Material, _Mapping]] = ...) -> None: ...

class UpdateMaterialOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MoveMaterialInput(_message.Message):
    __slots__ = ("material_id", "new_module_id", "new_index", "new_depth")
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_INDEX_FIELD_NUMBER: _ClassVar[int]
    NEW_DEPTH_FIELD_NUMBER: _ClassVar[int]
    material_id: str
    new_module_id: str
    new_index: int
    new_depth: int
    def __init__(self, material_id: _Optional[str] = ..., new_module_id: _Optional[str] = ..., new_index: _Optional[int] = ..., new_depth: _Optional[int] = ...) -> None: ...

class MoveMaterialOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteMaterialInput(_message.Message):
    __slots__ = ("material_id",)
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    material_id: str
    def __init__(self, material_id: _Optional[str] = ...) -> None: ...

class DeleteMaterialOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeMaterialInput(_message.Message):
    __slots__ = ("material_id", "member_id", "extra")
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    material_id: str
    member_id: str
    extra: _containers.RepeatedScalarFieldContainer[_material_pb2.Material.Extra]
    def __init__(self, material_id: _Optional[str] = ..., member_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_material_pb2.Material.Extra, str]]] = ...) -> None: ...

class DescribeMaterialOutput(_message.Message):
    __slots__ = ("material",)
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    material: _material_pb2.Material
    def __init__(self, material: _Optional[_Union[_material_pb2.Material, _Mapping]] = ...) -> None: ...

class ListMaterialsInput(_message.Message):
    __slots__ = ("module_id", "member_id", "search", "offset", "size", "filters", "sort", "order", "extra")
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDEX: _ClassVar[ListMaterialsInput.Sort]
    INDEX: ListMaterialsInput.Sort
    class Filter(_message.Message):
        __slots__ = ("graded", "weight")
        GRADED_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        graded: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        weight: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        def __init__(self, graded: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., weight: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ...) -> None: ...
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    module_id: str
    member_id: str
    search: str
    offset: int
    size: int
    filters: ListMaterialsInput.Filter
    sort: ListMaterialsInput.Sort
    order: _direction_pb2.Direction
    extra: _containers.RepeatedScalarFieldContainer[_material_pb2.Material.Extra]
    def __init__(self, module_id: _Optional[str] = ..., member_id: _Optional[str] = ..., search: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListMaterialsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListMaterialsInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_material_pb2.Material.Extra, str]]] = ...) -> None: ...

class ListMaterialsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_material_pb2.Material]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_material_pb2.Material, _Mapping]]] = ...) -> None: ...

class ReportProgressInput(_message.Message):
    __slots__ = ("material_id", "progress")
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    material_id: str
    progress: float
    def __init__(self, material_id: _Optional[str] = ..., progress: _Optional[float] = ...) -> None: ...

class ReportProgressOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GradeMaterialInput(_message.Message):
    __slots__ = ("material_id", "member_id", "grade", "excused")
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    EXCUSED_FIELD_NUMBER: _ClassVar[int]
    material_id: str
    member_id: str
    grade: int
    excused: bool
    def __init__(self, material_id: _Optional[str] = ..., member_id: _Optional[str] = ..., grade: _Optional[int] = ..., excused: bool = ...) -> None: ...

class GradeMaterialOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
