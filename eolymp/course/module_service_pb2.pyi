from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import module_pb2 as _module_pb2
from eolymp.course import module_item_pb2 as _module_item_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
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

class CreateModuleItemInput(_message.Message):
    __slots__ = ["item"]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _module_item_pb2.ModuleItem
    def __init__(self, item: _Optional[_Union[_module_item_pb2.ModuleItem, _Mapping]] = ...) -> None: ...

class CreateModuleItemOutput(_message.Message):
    __slots__ = ["item_id"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    def __init__(self, item_id: _Optional[str] = ...) -> None: ...

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

class DeleteModuleItemInput(_message.Message):
    __slots__ = ["item_id"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    def __init__(self, item_id: _Optional[str] = ...) -> None: ...

class DeleteModuleItemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteModuleOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeModuleInput(_message.Message):
    __slots__ = ["extra", "module_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_module_pb2.Module.Extra]
    module_id: str
    def __init__(self, module_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_module_pb2.Module.Extra, str]]] = ...) -> None: ...

class DescribeModuleItemInput(_message.Message):
    __slots__ = ["extra", "item_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_module_item_pb2.ModuleItem.Extra]
    item_id: str
    def __init__(self, item_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_module_item_pb2.ModuleItem.Extra, str]]] = ...) -> None: ...

class DescribeModuleItemOutput(_message.Message):
    __slots__ = ["item"]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _module_item_pb2.ModuleItem
    def __init__(self, item: _Optional[_Union[_module_item_pb2.ModuleItem, _Mapping]] = ...) -> None: ...

class DescribeModuleOutput(_message.Message):
    __slots__ = ["module"]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    module: _module_pb2.Module
    def __init__(self, module: _Optional[_Union[_module_pb2.Module, _Mapping]] = ...) -> None: ...

class ListModuleItemsInput(_message.Message):
    __slots__ = ["extra", "filters", "offset", "order", "size", "sort"]
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["query"]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        query: str
        def __init__(self, query: _Optional[str] = ...) -> None: ...
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    INDEX: ListModuleItemsInput.Sort
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_module_item_pb2.ModuleItem.Extra]
    filters: ListModuleItemsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListModuleItemsInput.Sort
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListModuleItemsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListModuleItemsInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_module_item_pb2.ModuleItem.Extra, str]]] = ...) -> None: ...

class ListModuleItemsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_module_item_pb2.ModuleItem]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_module_item_pb2.ModuleItem, _Mapping]]] = ...) -> None: ...

class ListModulesInput(_message.Message):
    __slots__ = ["extra", "filters", "offset", "order", "size", "sort"]
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["query"]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        query: str
        def __init__(self, query: _Optional[str] = ...) -> None: ...
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    INDEX: ListModulesInput.Sort
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_module_pb2.Module.Extra]
    filters: ListModulesInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListModulesInput.Sort
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListModulesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListModulesInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_module_pb2.Module.Extra, str]]] = ...) -> None: ...

class ListModulesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_module_pb2.Module]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_module_pb2.Module, _Mapping]]] = ...) -> None: ...

class MoveModuleItemInput(_message.Message):
    __slots__ = ["item_id", "new_depth", "new_index", "new_module_id"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_DEPTH_FIELD_NUMBER: _ClassVar[int]
    NEW_INDEX_FIELD_NUMBER: _ClassVar[int]
    NEW_MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    new_depth: int
    new_index: int
    new_module_id: str
    def __init__(self, item_id: _Optional[str] = ..., new_module_id: _Optional[str] = ..., new_index: _Optional[int] = ..., new_depth: _Optional[int] = ...) -> None: ...

class MoveModuleItemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateModuleInput(_message.Message):
    __slots__ = ["module", "module_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateModuleInput.Patch
    DESCRIPTION: UpdateModuleInput.Patch
    DRAFT: UpdateModuleInput.Patch
    IMAGE_URL: UpdateModuleInput.Patch
    INDEX: UpdateModuleInput.Patch
    MODULE_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME: UpdateModuleInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    module: _module_pb2.Module
    module_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateModuleInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateModuleInput.Patch, str]]] = ..., module_id: _Optional[str] = ..., module: _Optional[_Union[_module_pb2.Module, _Mapping]] = ...) -> None: ...

class UpdateModuleItemInput(_message.Message):
    __slots__ = ["item", "item_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateModuleItemInput.Patch
    CONTENT: UpdateModuleItemInput.Patch
    DEPTH: UpdateModuleItemInput.Patch
    DRAFT: UpdateModuleItemInput.Patch
    GRADING: UpdateModuleItemInput.Patch
    IMAGE_URL: UpdateModuleItemInput.Patch
    INDEX: UpdateModuleItemInput.Patch
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    NAME: UpdateModuleItemInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    item: _module_item_pb2.ModuleItem
    item_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateModuleItemInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateModuleItemInput.Patch, str]]] = ..., item_id: _Optional[str] = ..., item: _Optional[_Union[_module_item_pb2.ModuleItem, _Mapping]] = ...) -> None: ...

class UpdateModuleItemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateModuleOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
