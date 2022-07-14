from eolymp.workspace import project_pb2 as _project_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProjectCreatedEvent(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _project_pb2.Project
    def __init__(self, project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ...) -> None: ...

class ProjectDeletedEvent(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _project_pb2.Project
    def __init__(self, project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ...) -> None: ...

class ProjectUpdatedEvent(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _project_pb2.Project
    def __init__(self, project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ...) -> None: ...
