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

class ListCoursesInput(_message.Message):
    __slots__ = ("offset", "size", "search", "filters", "sort", "order", "extra")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListCoursesInput.Sortable]
    DEFAULT: ListCoursesInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "topic_id", "locale")
        ID_FIELD_NUMBER: _ClassVar[int]
        TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        topic_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., topic_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    search: str
    filters: ListCoursesInput.Filter
    sort: ListCoursesInput.Sortable
    order: _direction_pb2.Direction
    extra: _containers.RepeatedScalarFieldContainer[_course_pb2.Course.Extra]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListCoursesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListCoursesInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_course_pb2.Course.Extra, str]]] = ...) -> None: ...

class ListCoursesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_course_pb2.Course]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_course_pb2.Course, _Mapping]]] = ...) -> None: ...

class DescribeCourseInput(_message.Message):
    __slots__ = ("course_id", "extra")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    extra: _containers.RepeatedScalarFieldContainer[_course_pb2.Course.Extra]
    def __init__(self, course_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_course_pb2.Course.Extra, str]]] = ...) -> None: ...

class DescribeCourseOutput(_message.Message):
    __slots__ = ("course",)
    COURSE_FIELD_NUMBER: _ClassVar[int]
    course: _course_pb2.Course
    def __init__(self, course: _Optional[_Union[_course_pb2.Course, _Mapping]] = ...) -> None: ...

class CreateCourseInput(_message.Message):
    __slots__ = ("course",)
    COURSE_FIELD_NUMBER: _ClassVar[int]
    course: _course_pb2.Course
    def __init__(self, course: _Optional[_Union[_course_pb2.Course, _Mapping]] = ...) -> None: ...

class CreateCourseOutput(_message.Message):
    __slots__ = ("course_id",)
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    def __init__(self, course_id: _Optional[str] = ...) -> None: ...

class UpdateCourseInput(_message.Message):
    __slots__ = ("patch", "course_id", "course")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateCourseInput.Patch]
        LOCALE: _ClassVar[UpdateCourseInput.Patch]
        NAME: _ClassVar[UpdateCourseInput.Patch]
        DESCRIPTION: _ClassVar[UpdateCourseInput.Patch]
        IMAGE: _ClassVar[UpdateCourseInput.Patch]
        VISIBILITY: _ClassVar[UpdateCourseInput.Patch]
        DURATION: _ClassVar[UpdateCourseInput.Patch]
        TOPICS: _ClassVar[UpdateCourseInput.Patch]
    ALL: UpdateCourseInput.Patch
    LOCALE: UpdateCourseInput.Patch
    NAME: UpdateCourseInput.Patch
    DESCRIPTION: UpdateCourseInput.Patch
    IMAGE: UpdateCourseInput.Patch
    VISIBILITY: UpdateCourseInput.Patch
    DURATION: UpdateCourseInput.Patch
    TOPICS: UpdateCourseInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    COURSE_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateCourseInput.Patch]
    course_id: str
    course: _course_pb2.Course
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateCourseInput.Patch, str]]] = ..., course_id: _Optional[str] = ..., course: _Optional[_Union[_course_pb2.Course, _Mapping]] = ...) -> None: ...

class UpdateCourseOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCourseInput(_message.Message):
    __slots__ = ("course_id",)
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    def __init__(self, course_id: _Optional[str] = ...) -> None: ...

class DeleteCourseOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CopyCourseInput(_message.Message):
    __slots__ = ("course_id", "copy_scope", "copy_name")
    class Scope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[CopyCourseInput.Scope]
        MODULES: _ClassVar[CopyCourseInput.Scope]
        STUDENTS: _ClassVar[CopyCourseInput.Scope]
        ASSIGNMENTS: _ClassVar[CopyCourseInput.Scope]
        PERMISSIONS: _ClassVar[CopyCourseInput.Scope]
    ALL: CopyCourseInput.Scope
    MODULES: CopyCourseInput.Scope
    STUDENTS: CopyCourseInput.Scope
    ASSIGNMENTS: CopyCourseInput.Scope
    PERMISSIONS: CopyCourseInput.Scope
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    COPY_SCOPE_FIELD_NUMBER: _ClassVar[int]
    COPY_NAME_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    copy_scope: _containers.RepeatedScalarFieldContainer[CopyCourseInput.Scope]
    copy_name: str
    def __init__(self, course_id: _Optional[str] = ..., copy_scope: _Optional[_Iterable[_Union[CopyCourseInput.Scope, str]]] = ..., copy_name: _Optional[str] = ...) -> None: ...

class CopyCourseOutput(_message.Message):
    __slots__ = ("copy_course_id",)
    COPY_COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    copy_course_id: str
    def __init__(self, copy_course_id: _Optional[str] = ...) -> None: ...
