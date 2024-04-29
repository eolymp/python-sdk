from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import course_pb2 as _course_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCourseInput(_message.Message):
    __slots__ = ["course"]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    course: _course_pb2.Course
    def __init__(self, course: _Optional[_Union[_course_pb2.Course, _Mapping]] = ...) -> None: ...

class CreateCourseOutput(_message.Message):
    __slots__ = ["course_id"]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    def __init__(self, course_id: _Optional[str] = ...) -> None: ...

class DeleteCourseInput(_message.Message):
    __slots__ = ["course_id"]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    def __init__(self, course_id: _Optional[str] = ...) -> None: ...

class DeleteCourseOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeCourseInput(_message.Message):
    __slots__ = ["course_id", "extra"]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    extra: _containers.RepeatedScalarFieldContainer[_course_pb2.Course.Extra]
    def __init__(self, course_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_course_pb2.Course.Extra, str]]] = ...) -> None: ...

class DescribeCourseOutput(_message.Message):
    __slots__ = ["course"]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    course: _course_pb2.Course
    def __init__(self, course: _Optional[_Union[_course_pb2.Course, _Mapping]] = ...) -> None: ...

class ListCoursesInput(_message.Message):
    __slots__ = ["extra", "filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["id", "locale", "query", "topic_id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        query: str
        topic_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., topic_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    DEFAULT: ListCoursesInput.Sortable
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_course_pb2.Course.Extra]
    filters: ListCoursesInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListCoursesInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListCoursesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListCoursesInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_course_pb2.Course.Extra, str]]] = ...) -> None: ...

class ListCoursesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_course_pb2.Course]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_course_pb2.Course, _Mapping]]] = ...) -> None: ...

class StartCourseInput(_message.Message):
    __slots__ = ["course_id"]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    def __init__(self, course_id: _Optional[str] = ...) -> None: ...

class StartCourseOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateCourseInput(_message.Message):
    __slots__ = ["course", "course_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateCourseInput.Patch
    COURSE_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION: UpdateCourseInput.Patch
    DURATION: UpdateCourseInput.Patch
    IMAGE: UpdateCourseInput.Patch
    LOCALE: UpdateCourseInput.Patch
    NAME: UpdateCourseInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    TOPICS: UpdateCourseInput.Patch
    VISIBILITY: UpdateCourseInput.Patch
    course: _course_pb2.Course
    course_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateCourseInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateCourseInput.Patch, str]]] = ..., course_id: _Optional[str] = ..., course: _Optional[_Union[_course_pb2.Course, _Mapping]] = ...) -> None: ...

class UpdateCourseOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
