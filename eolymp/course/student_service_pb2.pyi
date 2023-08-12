from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import student_pb2 as _student_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateStudentInput(_message.Message):
    __slots__ = ["student"]
    STUDENT_FIELD_NUMBER: _ClassVar[int]
    student: _student_pb2.Student
    def __init__(self, student: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...

class CreateStudentOutput(_message.Message):
    __slots__ = ["student_id"]
    STUDENT_ID_FIELD_NUMBER: _ClassVar[int]
    student_id: str
    def __init__(self, student_id: _Optional[str] = ...) -> None: ...

class DeleteStudentInput(_message.Message):
    __slots__ = ["student_id"]
    STUDENT_ID_FIELD_NUMBER: _ClassVar[int]
    student_id: str
    def __init__(self, student_id: _Optional[str] = ...) -> None: ...

class DeleteStudentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeStudentInput(_message.Message):
    __slots__ = ["student_id"]
    STUDENT_ID_FIELD_NUMBER: _ClassVar[int]
    student_id: str
    def __init__(self, student_id: _Optional[str] = ...) -> None: ...

class DescribeStudentOutput(_message.Message):
    __slots__ = ["student"]
    STUDENT_FIELD_NUMBER: _ClassVar[int]
    student: _student_pb2.Student
    def __init__(self, student: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...

class DescribeViewerInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeViewerOutput(_message.Message):
    __slots__ = ["student"]
    STUDENT_FIELD_NUMBER: _ClassVar[int]
    student: _student_pb2.Student
    def __init__(self, student: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...

class ListStudentsInput(_message.Message):
    __slots__ = ["filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["id", "member_id", "name", "query", "status"]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    COMPLETE_AT: ListStudentsInput.Sortable
    DEFAULT: ListStudentsInput.Sortable
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    NAME: ListStudentsInput.Sortable
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT: ListStudentsInput.Sortable
    filters: ListStudentsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListStudentsInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListStudentsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListStudentsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListStudentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_student_pb2.Student]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_student_pb2.Student, _Mapping]]] = ...) -> None: ...

class StartCourseInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StartCourseOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateStudentInput(_message.Message):
    __slots__ = ["patch", "student", "student_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateStudentInput.Patch
    BONUS_TIME: UpdateStudentInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    STUDENT_FIELD_NUMBER: _ClassVar[int]
    STUDENT_ID_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateStudentInput.Patch]
    student: _student_pb2.Student
    student_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateStudentInput.Patch, str]]] = ..., student_id: _Optional[str] = ..., student: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...

class UpdateStudentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
