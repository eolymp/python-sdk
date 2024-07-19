from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModuleItem(_message.Message):
    __slots__ = ["assignment", "complete_at", "depth", "document", "draft", "due_at", "grade", "grading", "id", "image_url", "index", "name", "progress", "start_at", "url"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Assignment(_message.Message):
        __slots__ = ["problem_id"]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        problem_id: str
        def __init__(self, problem_id: _Optional[str] = ...) -> None: ...
    class Document(_message.Message):
        __slots__ = ["content"]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        content: _content_pb2.Content
        def __init__(self, content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
    class Grading(_message.Message):
        __slots__ = ["max_score"]
        MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
        max_score: int
        def __init__(self, max_score: _Optional[int] = ...) -> None: ...
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
    CONTENT: ModuleItem.Extra
    CONTENT_RENDER: ModuleItem.Extra
    CONTENT_VALUE: ModuleItem.Extra
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    DUE_AT_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    GRADING_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    START_AT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: ModuleItem.Extra
    URL_FIELD_NUMBER: _ClassVar[int]
    assignment: ModuleItem.Assignment
    complete_at: _timestamp_pb2.Timestamp
    depth: int
    document: ModuleItem.Document
    draft: bool
    due_at: _timestamp_pb2.Timestamp
    grade: int
    grading: ModuleItem.Grading
    id: str
    image_url: str
    index: int
    name: str
    progress: float
    start_at: _timestamp_pb2.Timestamp
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., draft: bool = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., index: _Optional[int] = ..., depth: _Optional[int] = ..., grading: _Optional[_Union[ModuleItem.Grading, _Mapping]] = ..., document: _Optional[_Union[ModuleItem.Document, _Mapping]] = ..., assignment: _Optional[_Union[ModuleItem.Assignment, _Mapping]] = ..., progress: _Optional[float] = ..., grade: _Optional[int] = ..., due_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
