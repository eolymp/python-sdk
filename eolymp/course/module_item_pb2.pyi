from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModuleItem(_message.Message):
    __slots__ = ["complete_at", "depth", "draft", "due_at", "grade", "grading", "id", "image_url", "index", "name", "progress", "start_at", "target", "url"]
    class Grading(_message.Message):
        __slots__ = ["max_score"]
        MAX_SCORE_FIELD_NUMBER: _ClassVar[int]
        max_score: int
        def __init__(self, max_score: _Optional[int] = ...) -> None: ...
    class Target(_message.Message):
        __slots__ = ["attrs", "ref", "type"]
        class AttrsEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ATTRS_FIELD_NUMBER: _ClassVar[int]
        REF_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        attrs: _containers.ScalarMap[str, str]
        ref: str
        type: str
        def __init__(self, type: _Optional[str] = ..., ref: _Optional[str] = ..., attrs: _Optional[_Mapping[str, str]] = ...) -> None: ...
    COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
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
    TARGET_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    complete_at: _timestamp_pb2.Timestamp
    depth: int
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
    target: ModuleItem.Target
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., draft: bool = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., index: _Optional[int] = ..., depth: _Optional[int] = ..., target: _Optional[_Union[ModuleItem.Target, _Mapping]] = ..., grading: _Optional[_Union[ModuleItem.Grading, _Mapping]] = ..., progress: _Optional[float] = ..., grade: _Optional[int] = ..., due_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
