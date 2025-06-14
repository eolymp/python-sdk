from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import staff_pb2 as _staff_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StaffChangedEvent(_message.Message):
    __slots__ = ("contest_id", "before", "after")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    before: _staff_pb2.Staff
    after: _staff_pb2.Staff
    def __init__(self, contest_id: _Optional[str] = ..., before: _Optional[_Union[_staff_pb2.Staff, _Mapping]] = ..., after: _Optional[_Union[_staff_pb2.Staff, _Mapping]] = ...) -> None: ...

class CreateStaffMemberInput(_message.Message):
    __slots__ = ("contest_id", "staff")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    STAFF_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    staff: _staff_pb2.Staff
    def __init__(self, contest_id: _Optional[str] = ..., staff: _Optional[_Union[_staff_pb2.Staff, _Mapping]] = ...) -> None: ...

class CreateStaffMemberOutput(_message.Message):
    __slots__ = ("staff_id",)
    STAFF_ID_FIELD_NUMBER: _ClassVar[int]
    staff_id: str
    def __init__(self, staff_id: _Optional[str] = ...) -> None: ...

class UpdateStaffMemberInput(_message.Message):
    __slots__ = ("patch", "contest_id", "staff_id", "staff")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateStaffMemberInput.Patch]
        ROLE: _ClassVar[UpdateStaffMemberInput.Patch]
    ALL: UpdateStaffMemberInput.Patch
    ROLE: UpdateStaffMemberInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    STAFF_ID_FIELD_NUMBER: _ClassVar[int]
    STAFF_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateStaffMemberInput.Patch]
    contest_id: str
    staff_id: str
    staff: _staff_pb2.Staff
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateStaffMemberInput.Patch, str]]] = ..., contest_id: _Optional[str] = ..., staff_id: _Optional[str] = ..., staff: _Optional[_Union[_staff_pb2.Staff, _Mapping]] = ...) -> None: ...

class UpdateStaffMemberOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteStaffMemberInput(_message.Message):
    __slots__ = ("contest_id", "staff_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    STAFF_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    staff_id: str
    def __init__(self, contest_id: _Optional[str] = ..., staff_id: _Optional[str] = ...) -> None: ...

class DeleteStaffMemberOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeStaffMemberInput(_message.Message):
    __slots__ = ("contest_id", "staff_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    STAFF_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    staff_id: str
    def __init__(self, contest_id: _Optional[str] = ..., staff_id: _Optional[str] = ...) -> None: ...

class DescribeStaffMemberOutput(_message.Message):
    __slots__ = ("staff",)
    STAFF_FIELD_NUMBER: _ClassVar[int]
    staff: _staff_pb2.Staff
    def __init__(self, staff: _Optional[_Union[_staff_pb2.Staff, _Mapping]] = ...) -> None: ...

class ListStaffMembersInput(_message.Message):
    __slots__ = ("contest_id", "offset", "size", "search", "filters", "sort", "order")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListStaffMembersInput.Sortable]
        MEMBER_ID: _ClassVar[ListStaffMembersInput.Sortable]
    DEFAULT: ListStaffMembersInput.Sortable
    MEMBER_ID: ListStaffMembersInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "member_id", "role")
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        role: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., role: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    offset: int
    size: int
    search: str
    filters: ListStaffMembersInput.Filter
    sort: ListStaffMembersInput.Sortable
    order: _direction_pb2.Direction
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListStaffMembersInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListStaffMembersInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListStaffMembersOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_staff_pb2.Staff]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_staff_pb2.Staff, _Mapping]]] = ...) -> None: ...
