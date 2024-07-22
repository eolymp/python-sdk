from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import enrollment_pb2 as _enrollment_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEnrollmentInput(_message.Message):
    __slots__ = ["enrollment"]
    ENROLLMENT_FIELD_NUMBER: _ClassVar[int]
    enrollment: _enrollment_pb2.Enrollment
    def __init__(self, enrollment: _Optional[_Union[_enrollment_pb2.Enrollment, _Mapping]] = ...) -> None: ...

class CreateEnrollmentOutput(_message.Message):
    __slots__ = ["enrollment_id"]
    ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    enrollment_id: str
    def __init__(self, enrollment_id: _Optional[str] = ...) -> None: ...

class DeleteEnrollmentInput(_message.Message):
    __slots__ = ["enrollment_id"]
    ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    enrollment_id: str
    def __init__(self, enrollment_id: _Optional[str] = ...) -> None: ...

class DeleteEnrollmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeEnrollmentInput(_message.Message):
    __slots__ = ["enrollment_id", "extra"]
    ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    enrollment_id: str
    extra: _containers.RepeatedScalarFieldContainer[_enrollment_pb2.Enrollment.Extra]
    def __init__(self, enrollment_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_enrollment_pb2.Enrollment.Extra, str]]] = ...) -> None: ...

class DescribeEnrollmentOutput(_message.Message):
    __slots__ = ["enrollment"]
    ENROLLMENT_FIELD_NUMBER: _ClassVar[int]
    enrollment: _enrollment_pb2.Enrollment
    def __init__(self, enrollment: _Optional[_Union[_enrollment_pb2.Enrollment, _Mapping]] = ...) -> None: ...

class ListEnrollmentsInput(_message.Message):
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
    DEFAULT: ListEnrollmentsInput.Sortable
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_enrollment_pb2.Enrollment.Extra]
    filters: ListEnrollmentsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListEnrollmentsInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListEnrollmentsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListEnrollmentsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_enrollment_pb2.Enrollment.Extra, str]]] = ...) -> None: ...

class ListEnrollmentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_enrollment_pb2.Enrollment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_enrollment_pb2.Enrollment, _Mapping]]] = ...) -> None: ...

class UpdateEnrollmentInput(_message.Message):
    __slots__ = ["enrollment", "enrollment_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateEnrollmentInput.Patch
    ASSIGNMENTS: UpdateEnrollmentInput.Patch
    ASSIGNMENTS_ADD: UpdateEnrollmentInput.Patch
    ASSIGNMENTS_REMOVE: UpdateEnrollmentInput.Patch
    ENROLLMENT_FIELD_NUMBER: _ClassVar[int]
    ENROLLMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    enrollment: _enrollment_pb2.Enrollment
    enrollment_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateEnrollmentInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateEnrollmentInput.Patch, str]]] = ..., enrollment_id: _Optional[str] = ..., enrollment: _Optional[_Union[_enrollment_pb2.Enrollment, _Mapping]] = ...) -> None: ...

class UpdateEnrollmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
