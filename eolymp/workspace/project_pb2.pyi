from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Project(_message.Message):
    __slots__ = ["author_id", "created_on", "ern", "id", "labels", "name", "runtime", "target", "target_ern", "updated_on", "visibility"]
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Target(_message.Message):
        __slots__ = ["problem_id", "space_id"]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        problem_id: str
        space_id: str
        def __init__(self, space_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    ERN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NONE: Project.Visibility
    PRIVATE: Project.Visibility
    PUBLIC: Project.Visibility
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_ERN_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    UPDATED_ON_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    author_id: str
    created_on: _timestamp_pb2.Timestamp
    ern: str
    id: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    name: str
    runtime: str
    target: Project.Target
    target_ern: str
    updated_on: _timestamp_pb2.Timestamp
    visibility: Project.Visibility
    def __init__(self, ern: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., runtime: _Optional[str] = ..., visibility: _Optional[_Union[Project.Visibility, str]] = ..., author_id: _Optional[str] = ..., created_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., target: _Optional[_Union[Project.Target, _Mapping]] = ..., target_ern: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...
