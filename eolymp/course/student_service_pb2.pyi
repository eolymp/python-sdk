from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import assignment_pb2 as _assignment_pb2
from eolymp.course import material_pb2 as _material_pb2
from eolymp.course import module_pb2 as _module_pb2
from eolymp.course import student_pb2 as _student_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateStudentInput(_message.Message):
    __slots__ = ("student",)
    STUDENT_FIELD_NUMBER: _ClassVar[int]
    student: _student_pb2.Student
    def __init__(self, student: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...

class CreateStudentOutput(_message.Message):
    __slots__ = ("student_id",)
    STUDENT_ID_FIELD_NUMBER: _ClassVar[int]
    student_id: str
    def __init__(self, student_id: _Optional[str] = ...) -> None: ...

class UpdateStudentInput(_message.Message):
    __slots__ = ("patch", "member_id", "student")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateStudentInput.Patch]
        INACTIVE: _ClassVar[UpdateStudentInput.Patch]
        ASSIGN_ALL: _ClassVar[UpdateStudentInput.Patch]
    ALL: UpdateStudentInput.Patch
    INACTIVE: UpdateStudentInput.Patch
    ASSIGN_ALL: UpdateStudentInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    STUDENT_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateStudentInput.Patch]
    member_id: str
    student: _student_pb2.Student
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateStudentInput.Patch, str]]] = ..., member_id: _Optional[str] = ..., student: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...

class UpdateStudentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteStudentInput(_message.Message):
    __slots__ = ("member_id",)
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    def __init__(self, member_id: _Optional[str] = ...) -> None: ...

class DeleteStudentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeStudentInput(_message.Message):
    __slots__ = ("member_id", "extra")
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    extra: _containers.RepeatedScalarFieldContainer[_student_pb2.Student.Extra]
    def __init__(self, member_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_student_pb2.Student.Extra, str]]] = ...) -> None: ...

class DescribeStudentOutput(_message.Message):
    __slots__ = ("student",)
    STUDENT_FIELD_NUMBER: _ClassVar[int]
    student: _student_pb2.Student
    def __init__(self, student: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...

class ListStudentsInput(_message.Message):
    __slots__ = ("after", "offset", "size", "search", "filters", "sort", "order", "extra")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListStudentsInput.Sortable]
    DEFAULT: ListStudentsInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "member_id", "group_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        group_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., group_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    after: str
    offset: int
    size: int
    search: str
    filters: ListStudentsInput.Filter
    sort: ListStudentsInput.Sortable
    order: _direction_pb2.Direction
    extra: _containers.RepeatedScalarFieldContainer[_student_pb2.Student.Extra]
    def __init__(self, after: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListStudentsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListStudentsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_student_pb2.Student.Extra, str]]] = ...) -> None: ...

class ListStudentsOutput(_message.Message):
    __slots__ = ("total", "items", "next_page_cursor")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_student_pb2.Student]
    next_page_cursor: str
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_student_pb2.Student, _Mapping]]] = ..., next_page_cursor: _Optional[str] = ...) -> None: ...

class WatchStudentInput(_message.Message):
    __slots__ = ("member_id", "extra")
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    extra: _containers.RepeatedScalarFieldContainer[_student_pb2.Student.Extra]
    def __init__(self, member_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_student_pb2.Student.Extra, str]]] = ...) -> None: ...

class WatchStudentOutput(_message.Message):
    __slots__ = ("student",)
    STUDENT_FIELD_NUMBER: _ClassVar[int]
    student: _student_pb2.Student
    def __init__(self, student: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...

class JoinCourseInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JoinCourseOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeViewerInput(_message.Message):
    __slots__ = ("extra",)
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_student_pb2.Student.Extra]
    def __init__(self, extra: _Optional[_Iterable[_Union[_student_pb2.Student.Extra, str]]] = ...) -> None: ...

class DescribeViewerOutput(_message.Message):
    __slots__ = ("student",)
    STUDENT_FIELD_NUMBER: _ClassVar[int]
    student: _student_pb2.Student
    def __init__(self, student: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...

class ListStudentAssignmentsInput(_message.Message):
    __slots__ = ("member_id", "offset", "size", "search", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "module_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        MODULE_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        module_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., module_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    offset: int
    size: int
    search: str
    filters: ListStudentAssignmentsInput.Filter
    def __init__(self, member_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListStudentAssignmentsInput.Filter, _Mapping]] = ...) -> None: ...

class ListStudentAssignmentsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_assignment_pb2.Assignment]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_assignment_pb2.Assignment, _Mapping]]] = ...) -> None: ...

class UpdateStudentAssignmentInput(_message.Message):
    __slots__ = ("member_id", "module_id", "start_after", "complete_before", "duration", "upsolve")
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    START_AFTER_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    UPSOLVE_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    module_id: str
    start_after: _timestamp_pb2.Timestamp
    complete_before: _timestamp_pb2.Timestamp
    duration: int
    upsolve: bool
    def __init__(self, member_id: _Optional[str] = ..., module_id: _Optional[str] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., upsolve: bool = ...) -> None: ...

class UpdateStudentAssignmentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteStudentAssignmentInput(_message.Message):
    __slots__ = ("member_id", "module_id")
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    module_id: str
    def __init__(self, member_id: _Optional[str] = ..., module_id: _Optional[str] = ...) -> None: ...

class DeleteStudentAssignmentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListStudentGradesInput(_message.Message):
    __slots__ = ("member_id",)
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    def __init__(self, member_id: _Optional[str] = ...) -> None: ...

class ListStudentGradesOutput(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_module_pb2.Module.Progress]
    def __init__(self, items: _Optional[_Iterable[_Union[_module_pb2.Module.Progress, _Mapping]]] = ...) -> None: ...

class ListModuleGradesInput(_message.Message):
    __slots__ = ("member_id", "module_id")
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    module_id: str
    def __init__(self, member_id: _Optional[str] = ..., module_id: _Optional[str] = ...) -> None: ...

class ListModuleGradesOutput(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_material_pb2.Material.Progress]
    def __init__(self, items: _Optional[_Iterable[_Union[_material_pb2.Material.Progress, _Mapping]]] = ...) -> None: ...
