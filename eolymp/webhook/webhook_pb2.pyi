from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Webhook(_message.Message):
    __slots__ = ("id", "name", "secret", "endpoint", "inactive", "events", "created_at", "last_failure_at", "last_success_at", "delivery_count", "failure_count")
    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EVENT: _ClassVar[Webhook.Event]
        PROBLEM_CHANGED: _ClassVar[Webhook.Event]
        PROBLEM_STATEMENT_CHANGED: _ClassVar[Webhook.Event]
        PROBLEM_SCORE_CHANGED: _ClassVar[Webhook.Event]
        SUBMISSION_CHANGED: _ClassVar[Webhook.Event]
        SUBMISSION_COMPLETED: _ClassVar[Webhook.Event]
        MEMBER_CHANGED: _ClassVar[Webhook.Event]
        GROUP_CHANGED: _ClassVar[Webhook.Event]
        COURSE_MODULE_CHANGED: _ClassVar[Webhook.Event]
        COURSE_MATERIAL_CHANGED: _ClassVar[Webhook.Event]
        COURSE_STUDENT_CHANGED: _ClassVar[Webhook.Event]
        COURSE_ASSIGNMENT_CHANGED: _ClassVar[Webhook.Event]
        DISCUSSION_MESSAGE_CHANGED: _ClassVar[Webhook.Event]
        POST_CHANGED: _ClassVar[Webhook.Event]
        POST_TRANSLATION_CHANGED: _ClassVar[Webhook.Event]
        POST_PUBLISHED: _ClassVar[Webhook.Event]
        TICKET_CHANGED: _ClassVar[Webhook.Event]
        TICKET_REPLY_CHANGED: _ClassVar[Webhook.Event]
        CONTEST_SUBMISSION_COMPLETED: _ClassVar[Webhook.Event]
        CONTEST_SCORE_CHANGED: _ClassVar[Webhook.Event]
        CONTEST_PARTICIPANT_CHANGED: _ClassVar[Webhook.Event]
        CONTEST_PARTICIPANT_JOINED: _ClassVar[Webhook.Event]
    UNKNOWN_EVENT: Webhook.Event
    PROBLEM_CHANGED: Webhook.Event
    PROBLEM_STATEMENT_CHANGED: Webhook.Event
    PROBLEM_SCORE_CHANGED: Webhook.Event
    SUBMISSION_CHANGED: Webhook.Event
    SUBMISSION_COMPLETED: Webhook.Event
    MEMBER_CHANGED: Webhook.Event
    GROUP_CHANGED: Webhook.Event
    COURSE_MODULE_CHANGED: Webhook.Event
    COURSE_MATERIAL_CHANGED: Webhook.Event
    COURSE_STUDENT_CHANGED: Webhook.Event
    COURSE_ASSIGNMENT_CHANGED: Webhook.Event
    DISCUSSION_MESSAGE_CHANGED: Webhook.Event
    POST_CHANGED: Webhook.Event
    POST_TRANSLATION_CHANGED: Webhook.Event
    POST_PUBLISHED: Webhook.Event
    TICKET_CHANGED: Webhook.Event
    TICKET_REPLY_CHANGED: Webhook.Event
    CONTEST_SUBMISSION_COMPLETED: Webhook.Event
    CONTEST_SCORE_CHANGED: Webhook.Event
    CONTEST_PARTICIPANT_CHANGED: Webhook.Event
    CONTEST_PARTICIPANT_JOINED: Webhook.Event
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PATCH_UNKNOWN: _ClassVar[Webhook.Patch]
        PATCH_ALL: _ClassVar[Webhook.Patch]
        PATCH_NAME: _ClassVar[Webhook.Patch]
        PATCH_ENDPOINT: _ClassVar[Webhook.Patch]
        PATCH_INACTIVE: _ClassVar[Webhook.Patch]
        PATCH_EVENTS: _ClassVar[Webhook.Patch]
    PATCH_UNKNOWN: Webhook.Patch
    PATCH_ALL: Webhook.Patch
    PATCH_NAME: Webhook.Patch
    PATCH_ENDPOINT: Webhook.Patch
    PATCH_INACTIVE: Webhook.Patch
    PATCH_EVENTS: Webhook.Patch
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_FAILURE_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESS_AT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    secret: str
    endpoint: str
    inactive: bool
    events: _containers.RepeatedScalarFieldContainer[Webhook.Event]
    created_at: _timestamp_pb2.Timestamp
    last_failure_at: _timestamp_pb2.Timestamp
    last_success_at: _timestamp_pb2.Timestamp
    delivery_count: int
    failure_count: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., secret: _Optional[str] = ..., endpoint: _Optional[str] = ..., inactive: bool = ..., events: _Optional[_Iterable[_Union[Webhook.Event, str]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_failure_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_success_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delivery_count: _Optional[int] = ..., failure_count: _Optional[int] = ...) -> None: ...
