import datetime

from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Issue(_message.Message):
    __slots__ = ("id", "problem_id", "number", "status", "title", "description", "assignee", "reporter_id", "tester_id", "tags", "created_at", "updated_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Issue.Status]
        OPEN: _ClassVar[Issue.Status]
        CLOSED: _ClassVar[Issue.Status]
    UNKNOWN_STATUS: Issue.Status
    OPEN: Issue.Status
    CLOSED: Issue.Status
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Issue.Extra.Field]
            DESCRIPTION_VALUE: _ClassVar[Issue.Extra.Field]
            DESCRIPTION_RENDER: _ClassVar[Issue.Extra.Field]
        UNKNOWN_FIELD: Issue.Extra.Field
        DESCRIPTION_VALUE: Issue.Extra.Field
        DESCRIPTION_RENDER: Issue.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Issue.Patch.Field]
            STATUS: _ClassVar[Issue.Patch.Field]
            DESCRIPTION: _ClassVar[Issue.Patch.Field]
            TITLE: _ClassVar[Issue.Patch.Field]
            ASSIGNEE: _ClassVar[Issue.Patch.Field]
            TAGS: _ClassVar[Issue.Patch.Field]
        UNKNOWN_FIELD: Issue.Patch.Field
        STATUS: Issue.Patch.Field
        DESCRIPTION: Issue.Patch.Field
        TITLE: Issue.Patch.Field
        ASSIGNEE: Issue.Patch.Field
        TAGS: Issue.Patch.Field
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ASSIGNEE_FIELD_NUMBER: _ClassVar[int]
    REPORTER_ID_FIELD_NUMBER: _ClassVar[int]
    TESTER_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    problem_id: str
    number: int
    status: Issue.Status
    title: str
    description: _content_pb2.Content
    assignee: str
    reporter_id: str
    tester_id: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., number: _Optional[int] = ..., status: _Optional[_Union[Issue.Status, str]] = ..., title: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., assignee: _Optional[str] = ..., reporter_id: _Optional[str] = ..., tester_id: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
