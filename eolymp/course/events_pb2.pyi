from eolymp.course import assignment_pb2 as _assignment_pb2
from eolymp.course import material_pb2 as _material_pb2
from eolymp.course import module_pb2 as _module_pb2
from eolymp.course import student_pb2 as _student_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignmentChangedEvent(_message.Message):
    __slots__ = ["after", "before", "course_id", "module_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    after: _assignment_pb2.Assignment
    before: _assignment_pb2.Assignment
    course_id: str
    module_id: str
    def __init__(self, course_id: _Optional[str] = ..., module_id: _Optional[str] = ..., before: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ..., after: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ...) -> None: ...

class MaterialChangedEvent(_message.Message):
    __slots__ = ["after", "before", "course_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    after: _material_pb2.Material
    before: _material_pb2.Material
    course_id: str
    def __init__(self, course_id: _Optional[str] = ..., before: _Optional[_Union[_material_pb2.Material, _Mapping]] = ..., after: _Optional[_Union[_material_pb2.Material, _Mapping]] = ...) -> None: ...

class ModuleChangedEvent(_message.Message):
    __slots__ = ["after", "before", "course_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    after: _module_pb2.Module
    before: _module_pb2.Module
    course_id: str
    def __init__(self, course_id: _Optional[str] = ..., before: _Optional[_Union[_module_pb2.Module, _Mapping]] = ..., after: _Optional[_Union[_module_pb2.Module, _Mapping]] = ...) -> None: ...

class StudentChangedEvent(_message.Message):
    __slots__ = ["after", "before", "course_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    after: _student_pb2.Student
    before: _student_pb2.Student
    course_id: str
    def __init__(self, course_id: _Optional[str] = ..., before: _Optional[_Union[_student_pb2.Student, _Mapping]] = ..., after: _Optional[_Union[_student_pb2.Student, _Mapping]] = ...) -> None: ...
