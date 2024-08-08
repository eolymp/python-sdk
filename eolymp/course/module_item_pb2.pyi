from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModuleItem(_message.Message):
    __slots__ = ["depth", "document", "draft", "grading", "id", "image_url", "index", "name", "task", "url"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Document(_message.Message):
        __slots__ = ["content"]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        content: _content_pb2.Content
        def __init__(self, content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
    class Grading(_message.Message):
        __slots__ = ["max_score", "weight"]
        MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        max_score: int
        weight: float
        def __init__(self, max_score: _Optional[int] = ..., weight: _Optional[float] = ...) -> None: ...
    class Task(_message.Message):
        __slots__ = ["problem_id"]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        problem_id: str
        def __init__(self, problem_id: _Optional[str] = ...) -> None: ...
    CONTENT: ModuleItem.Extra
    CONTENT_RENDER: ModuleItem.Extra
    CONTENT_VALUE: ModuleItem.Extra
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    GRADING_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: ModuleItem.Extra
    URL_FIELD_NUMBER: _ClassVar[int]
    depth: int
    document: ModuleItem.Document
    draft: bool
    grading: ModuleItem.Grading
    id: str
    image_url: str
    index: int
    name: str
    task: ModuleItem.Task
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., draft: bool = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., index: _Optional[int] = ..., depth: _Optional[int] = ..., grading: _Optional[_Union[ModuleItem.Grading, _Mapping]] = ..., document: _Optional[_Union[ModuleItem.Document, _Mapping]] = ..., task: _Optional[_Union[ModuleItem.Task, _Mapping]] = ...) -> None: ...
