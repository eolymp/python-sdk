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

class DescribeStudentInput(_message.Message):
    __slots__ = ["extra", "member_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_student_pb2.Student.Extra]
    member_id: str
    def __init__(self, member_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_student_pb2.Student.Extra, str]]] = ...) -> None: ...

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
    __slots__ = ["extra", "filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["id", "member_id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    DEFAULT: ListStudentsInput.Sortable
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_student_pb2.Student.Extra]
    filters: ListStudentsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListStudentsInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListStudentsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListStudentsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_student_pb2.Student.Extra, str]]] = ...) -> None: ...

class ListStudentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_student_pb2.Student]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_student_pb2.Student, _Mapping]]] = ...) -> None: ...

class WatchStudentInput(_message.Message):
    __slots__ = ["member_id"]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    def __init__(self, member_id: _Optional[str] = ...) -> None: ...

class WatchStudentOutput(_message.Message):
    __slots__ = ["student"]
    STUDENT_FIELD_NUMBER: _ClassVar[int]
    student: _student_pb2.Student
    def __init__(self, student: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...
