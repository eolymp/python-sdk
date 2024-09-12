from eolymp.atlas import testing_feedback_pb2 as _testing_feedback_pb2
from eolymp.ecm import node_pb2 as _node_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Problem(_message.Message):
    __slots__ = ["base_id", "base_number", "base_space_id", "contest_id", "cpu_limit", "feedback_policy", "file_size_limit", "id", "index", "memory_limit", "score", "score_by_best_testset", "submit_limit", "time_limit", "url"]
    class Attachment(_message.Message):
        __slots__ = ["id", "link", "name"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: str
        link: str
        name: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., link: _Optional[str] = ...) -> None: ...
    class Statement(_message.Message):
        __slots__ = ["content", "download_link", "locale", "title"]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        content: _node_pb2.Node
        download_link: str
        locale: str
        title: str
        def __init__(self, locale: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_node_pb2.Node, _Mapping]] = ..., download_link: _Optional[str] = ...) -> None: ...
    class Test(_message.Message):
        __slots__ = ["answer_url", "example", "index", "input_url", "score"]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        EXAMPLE_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        answer_url: str
        example: bool
        index: int
        input_url: str
        score: float
        def __init__(self, index: _Optional[int] = ..., example: bool = ..., input_url: _Optional[str] = ..., answer_url: _Optional[str] = ..., score: _Optional[float] = ...) -> None: ...
    BASE_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BASE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_POLICY_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SCORE_BY_BEST_TESTSET_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    base_id: str
    base_number: int
    base_space_id: str
    contest_id: str
    cpu_limit: int
    feedback_policy: _testing_feedback_pb2.FeedbackPolicy
    file_size_limit: int
    id: str
    index: int
    memory_limit: int
    score: float
    score_by_best_testset: bool
    submit_limit: int
    time_limit: int
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., index: _Optional[int] = ..., score: _Optional[float] = ..., base_id: _Optional[str] = ..., base_number: _Optional[int] = ..., base_space_id: _Optional[str] = ..., contest_id: _Optional[str] = ..., feedback_policy: _Optional[_Union[_testing_feedback_pb2.FeedbackPolicy, str]] = ..., time_limit: _Optional[int] = ..., cpu_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., file_size_limit: _Optional[int] = ..., submit_limit: _Optional[int] = ..., score_by_best_testset: bool = ...) -> None: ...
