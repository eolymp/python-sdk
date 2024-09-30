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
    __slots__ = []
    CLASS_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class CreateClassOutput(_message.Message):
    __slots__ = ["class_id"]
    CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    class_id: str
    def __init__(self, class_id: _Optional[str] = ...) -> None: ...

class DeleteClassAssignmentInput(_message.Message):
    __slots__ = ["group_id", "module_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    module_id: str
    def __init__(self, group_id: _Optional[str] = ..., module_id: _Optional[str] = ...) -> None: ...

class DeleteClassAssignmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteClassInput(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DeleteClassOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeClassInput(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DescribeClassOutput(_message.Message):
    __slots__ = []
    CLASS_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, **kwargs) -> None: ...

class ListClassAssignmentsInput(_message.Message):
    __slots__ = ["filters", "group_id", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "module_id", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        MODULE_ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        module_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., module_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListClassAssignmentsInput.Filter
    group_id: str
    offset: int
    size: int
    def __init__(self, group_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListClassAssignmentsInput.Filter, _Mapping]] = ...) -> None: ...

class ListClassAssignmentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_assignment_pb2.Assignment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_assignment_pb2.Assignment, _Mapping]]] = ...) -> None: ...

class ListClassesInput(_message.Message):
    __slots__ = ["filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["group_id", "id", "member_id", "query"]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        group_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., group_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    DEFAULT: ListClassesInput.Sortable
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    filters: ListClassesInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListClassesInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListClassesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListClassesInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListClassesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_class_pb2.Class]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_class_pb2.Class, _Mapping]]] = ...) -> None: ...

class UpdateClassAssignmentInput(_message.Message):
    __slots__ = ["complete_before", "duration", "group_id", "module_id", "start_after", "upsolve"]
    COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    START_AFTER_FIELD_NUMBER: _ClassVar[int]
    UPSOLVE_FIELD_NUMBER: _ClassVar[int]
    complete_before: _timestamp_pb2.Timestamp
    duration: int
    group_id: str
    module_id: str
    start_after: _timestamp_pb2.Timestamp
    upsolve: bool
    def __init__(self, group_id: _Optional[str] = ..., module_id: _Optional[str] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., upsolve: bool = ...) -> None: ...

class UpdateClassAssignmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateClassInput(_message.Message):
    __slots__ = ["group_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateClassInput.Patch
    ASSIGN_ALL: UpdateClassInput.Patch
    CLASS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE: UpdateClassInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateClassInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateClassInput.Patch, str]]] = ..., group_id: _Optional[str] = ..., **kwargs) -> None: ...

class UpdateClassOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
