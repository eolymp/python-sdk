from eolymp.atlas import testing_feedback_pb2 as _testing_feedback_pb2
from eolymp.atlas import testing_scoring_pb2 as _testing_scoring_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Testset(_message.Message):
    __slots__ = ("id", "version_id", "index", "time_limit", "cpu_limit", "memory_limit", "file_size_limit", "dependencies", "dependency_mode", "scoring_mode", "feedback_policy")
    class DependencyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_DEPENDENCY_MODE: _ClassVar[Testset.DependencyMode]
        FULLY_ACCEPTED: _ClassVar[Testset.DependencyMode]
        FIRST_POINT: _ClassVar[Testset.DependencyMode]
    UNKNOWN_DEPENDENCY_MODE: Testset.DependencyMode
    FULLY_ACCEPTED: Testset.DependencyMode
    FIRST_POINT: Testset.DependencyMode
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCY_MODE_FIELD_NUMBER: _ClassVar[int]
    SCORING_MODE_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_POLICY_FIELD_NUMBER: _ClassVar[int]
    id: str
    version_id: str
    index: int
    time_limit: int
    cpu_limit: int
    memory_limit: int
    file_size_limit: int
    dependencies: _containers.RepeatedScalarFieldContainer[int]
    dependency_mode: Testset.DependencyMode
    scoring_mode: _testing_scoring_pb2.ScoringMode
    feedback_policy: _testing_feedback_pb2.FeedbackPolicy
    def __init__(self, id: _Optional[str] = ..., version_id: _Optional[str] = ..., index: _Optional[int] = ..., time_limit: _Optional[int] = ..., cpu_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., file_size_limit: _Optional[int] = ..., dependencies: _Optional[_Iterable[int]] = ..., dependency_mode: _Optional[_Union[Testset.DependencyMode, str]] = ..., scoring_mode: _Optional[_Union[_testing_scoring_pb2.ScoringMode, str]] = ..., feedback_policy: _Optional[_Union[_testing_feedback_pb2.FeedbackPolicy, str]] = ...) -> None: ...
