from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import assignment_pb2 as _assignment_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAssignmentInput(_message.Message):
    __slots__ = ["assignment"]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    assignment: _assignment_pb2.Assignment
    def __init__(self, assignment: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ...) -> None: ...

class CreateAssignmentOutput(_message.Message):
    __slots__ = ["assignment_id"]
    ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    assignment_id: str
    def __init__(self, assignment_id: _Optional[str] = ...) -> None: ...

class DeleteAssignmentInput(_message.Message):
    __slots__ = ["assignment_id"]
    ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    assignment_id: str
    def __init__(self, assignment_id: _Optional[str] = ...) -> None: ...

class DeleteAssignmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeAssignmentInput(_message.Message):
    __slots__ = ["assignment_id", "extra"]
    ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    assignment_id: str
    extra: _containers.RepeatedScalarFieldContainer[_assignment_pb2.Assignment.Extra]
    def __init__(self, assignment_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_assignment_pb2.Assignment.Extra, str]]] = ...) -> None: ...

class DescribeAssignmentOutput(_message.Message):
    __slots__ = ["assignment"]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    assignment: _assignment_pb2.Assignment
    def __init__(self, assignment: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ...) -> None: ...

class IntrospectAssignmentInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectAssignmentOutput(_message.Message):
    __slots__ = ["assignment"]
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    assignment: _assignment_pb2.Assignment
    def __init__(self, assignment: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ...) -> None: ...

class ListAssignmentsInput(_message.Message):
    __slots__ = ["extra", "filters", "offset", "order", "size", "sort"]
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
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., group_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    DEFAULT: ListAssignmentsInput.Sortable
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_assignment_pb2.Assignment.Extra]
    filters: ListAssignmentsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListAssignmentsInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListAssignmentsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListAssignmentsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_assignment_pb2.Assignment.Extra, str]]] = ...) -> None: ...

class ListAssignmentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_assignment_pb2.Assignment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_assignment_pb2.Assignment, _Mapping]]] = ...) -> None: ...

class StartAssignmentInput(_message.Message):
    __slots__ = ["entry_id"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    def __init__(self, entry_id: _Optional[str] = ...) -> None: ...

class StartAssignmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAssignmentInput(_message.Message):
    __slots__ = ["assignment", "assignment_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateAssignmentInput.Patch
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ASSIGNMENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_BEFORE: UpdateAssignmentInput.Patch
    DURATION: UpdateAssignmentInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    START_AFTER: UpdateAssignmentInput.Patch
    assignment: _assignment_pb2.Assignment
    assignment_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateAssignmentInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateAssignmentInput.Patch, str]]] = ..., assignment_id: _Optional[str] = ..., assignment: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ...) -> None: ...

class UpdateAssignmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
