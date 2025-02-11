from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Material(_message.Message):
    __slots__ = ("id", "url", "draft", "name", "image_url", "module_id", "index", "depth", "grading", "document", "task", "percentage", "grade", "progress")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Material.Extra]
        CONTENT: _ClassVar[Material.Extra]
        CONTENT_VALUE: _ClassVar[Material.Extra]
        CONTENT_RENDER: _ClassVar[Material.Extra]
        PERCENTAGE: _ClassVar[Material.Extra]
        GRADE: _ClassVar[Material.Extra]
        PROGRESS: _ClassVar[Material.Extra]
    UNKNOWN_EXTRA: Material.Extra
    CONTENT: Material.Extra
    CONTENT_VALUE: Material.Extra
    CONTENT_RENDER: Material.Extra
    PERCENTAGE: Material.Extra
    GRADE: Material.Extra
    PROGRESS: Material.Extra
    class Document(_message.Message):
        __slots__ = ("content",)
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        content: _content_pb2.Content
        def __init__(self, content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
    class Task(_message.Message):
        __slots__ = ("problem_id",)
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        problem_id: str
        def __init__(self, problem_id: _Optional[str] = ...) -> None: ...
    class Grading(_message.Message):
        __slots__ = ("max_score", "weight")
        MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        max_score: int
        weight: float
        def __init__(self, max_score: _Optional[int] = ..., weight: _Optional[float] = ...) -> None: ...
    class Progress(_message.Message):
        __slots__ = ("percentage", "grade", "grade_automatic", "grade_override", "excused")
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        GRADE_AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        GRADE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        EXCUSED_FIELD_NUMBER: _ClassVar[int]
        percentage: float
        grade: int
        grade_automatic: int
        grade_override: int
        excused: bool
        def __init__(self, percentage: _Optional[float] = ..., grade: _Optional[int] = ..., grade_automatic: _Optional[int] = ..., grade_override: _Optional[int] = ..., excused: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    GRADING_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    draft: bool
    name: str
    image_url: str
    module_id: str
    index: int
    depth: int
    grading: Material.Grading
    document: Material.Document
    task: Material.Task
    percentage: float
    grade: int
    progress: Material.Progress
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., draft: bool = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., module_id: _Optional[str] = ..., index: _Optional[int] = ..., depth: _Optional[int] = ..., grading: _Optional[_Union[Material.Grading, _Mapping]] = ..., document: _Optional[_Union[Material.Document, _Mapping]] = ..., task: _Optional[_Union[Material.Task, _Mapping]] = ..., percentage: _Optional[float] = ..., grade: _Optional[int] = ..., progress: _Optional[_Union[Material.Progress, _Mapping]] = ...) -> None: ...
