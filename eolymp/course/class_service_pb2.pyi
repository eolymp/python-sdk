from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import assignment_pb2 as _assignment_pb2
from eolymp.course import class_pb2 as _class_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateClassInput(_message.Message):
    __slots__ = ()
    CLASS_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class CreateClassOutput(_message.Message):
    __slots__ = ("class_id",)
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    def __init__(self, class_id: _Optional[str] = ...) -> None: ...

class UpdateClassInput(_message.Message):
    __slots__ = ("patch", "group_id")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateClassInput.Patch]
        INACTIVE: _ClassVar[UpdateClassInput.Patch]
        ASSIGN_ALL: _ClassVar[UpdateClassInput.Patch]
    ALL: UpdateClassInput.Patch
    INACTIVE: UpdateClassInput.Patch
    ASSIGN_ALL: UpdateClassInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateClassInput.Patch]
    group_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateClassInput.Patch, str]]] = ..., group_id: _Optional[str] = ..., **kwargs) -> None: ...

class UpdateClassOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteClassInput(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DeleteClassOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeClassInput(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DescribeClassOutput(_message.Message):
    __slots__ = ()
    CLASS_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class ListClassesInput(_message.Message):
    __slots__ = ("offset", "size", "search", "filters", "sort", "order")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListClassesInput.Sortable]
    DEFAULT: ListClassesInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "group_id", "member_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        group_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., group_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    search: str
    filters: ListClassesInput.Filter
    sort: ListClassesInput.Sortable
    order: _direction_pb2.Direction
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListClassesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListClassesInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListClassesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_class_pb2.Class]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_class_pb2.Class, _Mapping]]] = ...) -> None: ...

class ListClassAssignmentsInput(_message.Message):
    __slots__ = ("group_id", "offset", "size", "search", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "module_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        MODULE_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        module_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., module_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    offset: int
    size: int
    search: str
    filters: ListClassAssignmentsInput.Filter
    def __init__(self, group_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListClassAssignmentsInput.Filter, _Mapping]] = ...) -> None: ...

class ListClassAssignmentsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_assignment_pb2.Assignment]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_assignment_pb2.Assignment, _Mapping]]] = ...) -> None: ...

class UpdateClassAssignmentInput(_message.Message):
    __slots__ = ("group_id", "module_id", "start_after", "complete_before", "duration", "upsolve")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    START_AFTER_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    UPSOLVE_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    module_id: str
    start_after: _timestamp_pb2.Timestamp
    complete_before: _timestamp_pb2.Timestamp
    duration: int
    upsolve: bool
    def __init__(self, group_id: _Optional[str] = ..., module_id: _Optional[str] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., upsolve: bool = ...) -> None: ...

class UpdateClassAssignmentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteClassAssignmentInput(_message.Message):
    __slots__ = ("group_id", "module_id")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    module_id: str
    def __init__(self, group_id: _Optional[str] = ..., module_id: _Optional[str] = ...) -> None: ...

class DeleteClassAssignmentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
