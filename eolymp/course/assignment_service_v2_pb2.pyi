from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import assignment_v2_pb2 as _assignment_v2_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAssignmentV2Input(_message.Message):
    __slots__ = ["assignment"]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    assignment: _assignment_v2_pb2.AssignmentV2
    def __init__(self, assignment: _Optional[_Union[_assignment_v2_pb2.AssignmentV2, _Mapping]] = ...) -> None: ...

class CreateAssignmentV2Output(_message.Message):
    __slots__ = ["assignment_id"]
    ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    assignment_id: str
    def __init__(self, assignment_id: _Optional[str] = ...) -> None: ...

class DeleteAssignmentV2Input(_message.Message):
    __slots__ = ["assignment_id"]
    ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    assignment_id: str
    def __init__(self, assignment_id: _Optional[str] = ...) -> None: ...

class DeleteAssignmentV2Output(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeAssignmentV2Input(_message.Message):
    __slots__ = ["assignment_id"]
    ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    assignment_id: str
    def __init__(self, assignment_id: _Optional[str] = ...) -> None: ...

class DescribeAssignmentV2Output(_message.Message):
    __slots__ = ["assignment"]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    assignment: _assignment_v2_pb2.AssignmentV2
    def __init__(self, assignment: _Optional[_Union[_assignment_v2_pb2.AssignmentV2, _Mapping]] = ...) -> None: ...

class ListAssignmentsV2Input(_message.Message):
    __slots__ = ["filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["group_id", "id", "member_id"]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        group_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., group_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    DEFAULT: ListAssignmentsV2Input.Sortable
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    filters: ListAssignmentsV2Input.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListAssignmentsV2Input.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListAssignmentsV2Input.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListAssignmentsV2Input.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListAssignmentsV2Output(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_assignment_v2_pb2.AssignmentV2]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_assignment_v2_pb2.AssignmentV2, _Mapping]]] = ...) -> None: ...

class UpdateAssignmentV2Input(_message.Message):
    __slots__ = ["assignment", "assignment_id"]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    assignment: _assignment_v2_pb2.AssignmentV2
    assignment_id: str
    def __init__(self, assignment_id: _Optional[str] = ..., assignment: _Optional[_Union[_assignment_v2_pb2.AssignmentV2, _Mapping]] = ...) -> None: ...

class UpdateAssignmentV2Output(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
