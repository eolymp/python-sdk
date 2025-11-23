from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.atlas import form_pb2 as _form_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.atlas import testing_feedback_pb2 as _testing_feedback_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.ecm import node_pb2 as _node_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Problem(_message.Message):
    __slots__ = ("contest_id", "id", "url", "type", "index", "base_id", "feedback_policy", "score_by_best_testset", "time_limit", "cpu_limit", "memory_limit", "file_size_limit", "submit_limit", "score", "constraints", "language", "title", "content", "download_link", "languages", "submission_form", "examples")
    class Statement(_message.Message):
        __slots__ = ("locale", "title", "content", "download_link")
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
        locale: str
        title: str
        content: _node_pb2.Node
        download_link: str
        def __init__(self, locale: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_node_pb2.Node, _Mapping]] = ..., download_link: _Optional[str] = ...) -> None: ...
    class Test(_message.Message):
        __slots__ = ("index", "example", "input_url", "answer_url", "score")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        EXAMPLE_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        index: int
        example: bool
        input_url: str
        answer_url: str
        score: float
        def __init__(self, index: _Optional[int] = ..., example: bool = ..., input_url: _Optional[str] = ..., answer_url: _Optional[str] = ..., score: _Optional[float] = ...) -> None: ...
    class Attachment(_message.Message):
        __slots__ = ("id", "name", "link")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        link: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., link: _Optional[str] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    BASE_ID_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_POLICY_FIELD_NUMBER: _ClassVar[int]
    SCORE_BY_BEST_TESTSET_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_FORM_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    id: str
    url: str
    type: _problem_pb2.Problem.Type
    index: int
    base_id: str
    feedback_policy: _testing_feedback_pb2.FeedbackPolicy
    score_by_best_testset: bool
    time_limit: int
    cpu_limit: int
    memory_limit: int
    file_size_limit: int
    submit_limit: int
    score: float
    constraints: _problem_pb2.Problem.Constraints
    language: str
    title: str
    content: _content_pb2.Content
    download_link: str
    languages: _containers.RepeatedScalarFieldContainer[str]
    submission_form: _form_pb2.Form
    examples: _containers.RepeatedCompositeFieldContainer[_problem_pb2.Problem.Example]
    def __init__(self, contest_id: _Optional[str] = ..., id: _Optional[str] = ..., url: _Optional[str] = ..., type: _Optional[_Union[_problem_pb2.Problem.Type, str]] = ..., index: _Optional[int] = ..., base_id: _Optional[str] = ..., feedback_policy: _Optional[_Union[_testing_feedback_pb2.FeedbackPolicy, str]] = ..., score_by_best_testset: bool = ..., time_limit: _Optional[int] = ..., cpu_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., file_size_limit: _Optional[int] = ..., submit_limit: _Optional[int] = ..., score: _Optional[float] = ..., constraints: _Optional[_Union[_problem_pb2.Problem.Constraints, _Mapping]] = ..., language: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., download_link: _Optional[str] = ..., languages: _Optional[_Iterable[str]] = ..., submission_form: _Optional[_Union[_form_pb2.Form, _Mapping]] = ..., examples: _Optional[_Iterable[_Union[_problem_pb2.Problem.Example, _Mapping]]] = ...) -> None: ...
