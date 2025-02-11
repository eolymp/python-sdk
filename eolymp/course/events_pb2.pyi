from eolymp.course import assignment_pb2 as _assignment_pb2
from eolymp.course import material_pb2 as _material_pb2
from eolymp.course import module_pb2 as _module_pb2
from eolymp.course import student_pb2 as _student_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModuleChangedEvent(_message.Message):
    __slots__ = ("course_id", "before", "after")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    before: _module_pb2.Module
    after: _module_pb2.Module
    def __init__(self, course_id: _Optional[str] = ..., before: _Optional[_Union[_module_pb2.Module, _Mapping]] = ..., after: _Optional[_Union[_module_pb2.Module, _Mapping]] = ...) -> None: ...

class MaterialChangedEvent(_message.Message):
    __slots__ = ("course_id", "before", "after")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    before: _material_pb2.Material
    after: _material_pb2.Material
    def __init__(self, course_id: _Optional[str] = ..., before: _Optional[_Union[_material_pb2.Material, _Mapping]] = ..., after: _Optional[_Union[_material_pb2.Material, _Mapping]] = ...) -> None: ...

class StudentChangedEvent(_message.Message):
    __slots__ = ("course_id", "before", "after")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    before: _student_pb2.Student
    after: _student_pb2.Student
    def __init__(self, course_id: _Optional[str] = ..., before: _Optional[_Union[_student_pb2.Student, _Mapping]] = ..., after: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...

class AssignmentChangedEvent(_message.Message):
    __slots__ = ("course_id", "module_id", "before", "after")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    module_id: str
    before: _assignment_pb2.Assignment
    after: _assignment_pb2.Assignment
    def __init__(self, course_id: _Optional[str] = ..., module_id: _Optional[str] = ..., before: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ..., after: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ...) -> None: ...
