from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.workspace import file_pb2 as _file_pb2
from eolymp.workspace import project_pb2 as _project_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProjectInput(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _project_pb2.Project
    def __init__(self, project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ...) -> None: ...

class CreateProjectOutput(_message.Message):
    __slots__ = ["project_ern", "project_id"]
    PROJECT_ERN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_ern: str
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., project_ern: _Optional[str] = ...) -> None: ...

class DeleteProjectInput(_message.Message):
    __slots__ = ["project_ern", "project_id"]
    PROJECT_ERN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_ern: str
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., project_ern: _Optional[str] = ...) -> None: ...

class DeleteProjectOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeFileInput(_message.Message):
    __slots__ = ["file_ern", "name", "project_id"]
    FILE_ERN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    file_ern: str
    name: str
    project_id: str
    def __init__(self, file_ern: _Optional[str] = ..., project_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DescribeFileOutput(_message.Message):
    __slots__ = ["file"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _file_pb2.File
    def __init__(self, file: _Optional[_Union[_file_pb2.File, _Mapping]] = ...) -> None: ...

class DescribeProjectInput(_message.Message):
    __slots__ = ["project_ern", "project_id"]
    PROJECT_ERN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_ern: str
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., project_ern: _Optional[str] = ...) -> None: ...

class DescribeProjectOutput(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _project_pb2.Project
    def __init__(self, project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ...) -> None: ...

class ListFilesInput(_message.Message):
    __slots__ = ["offset", "project_ern", "project_id", "size"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ERN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    project_ern: str
    project_id: str
    size: int
    def __init__(self, project_id: _Optional[str] = ..., project_ern: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListFilesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...

class ListProjectsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["query"]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        query: str
        def __init__(self, query: _Optional[str] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListProjectsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListProjectsInput.Filter, _Mapping]] = ...) -> None: ...

class ListProjectsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_project_pb2.Project]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_project_pb2.Project, _Mapping]]] = ...) -> None: ...

class RemoveFileInput(_message.Message):
    __slots__ = ["file_ern", "name", "project_id"]
    FILE_ERN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    file_ern: str
    name: str
    project_id: str
    def __init__(self, file_ern: _Optional[str] = ..., project_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RemoveFileOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateProjectInput(_message.Message):
    __slots__ = ["project", "project_ern", "project_id"]
    PROJECT_ERN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project: _project_pb2.Project
    project_ern: str
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., project_ern: _Optional[str] = ..., project: _Optional[_Union[_project_pb2.Project, _Mapping]] = ...) -> None: ...

class UpdateProjectOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UploadFileInput(_message.Message):
    __slots__ = ["content", "name", "project_ern", "project_id"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ERN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    name: str
    project_ern: str
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., project_ern: _Optional[str] = ..., name: _Optional[str] = ..., content: _Optional[bytes] = ...) -> None: ...

class UploadFileOutput(_message.Message):
    __slots__ = ["file_ern"]
    FILE_ERN_FIELD_NUMBER: _ClassVar[int]
    file_ern: str
    def __init__(self, file_ern: _Optional[str] = ...) -> None: ...
