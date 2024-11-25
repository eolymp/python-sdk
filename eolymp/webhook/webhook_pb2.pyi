from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Webhook(_message.Message):
    __slots__ = ["created_at", "delivery_count", "endpoint", "events", "failure_count", "id", "inactive", "last_failure_at", "last_success_at", "name", "secret"]
    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CONTEST_PARTICIPANT_CHANGED: Webhook.Event
    CONTEST_PARTICIPANT_JOINED: Webhook.Event
    CONTEST_SCORE_CHANGED: Webhook.Event
    CONTEST_SUBMISSION_COMPLETED: Webhook.Event
    COURSE_ASSIGNMENT_CHANGED: Webhook.Event
    COURSE_MATERIAL_CHANGED: Webhook.Event
    COURSE_MODULE_CHANGED: Webhook.Event
    COURSE_STUDENT_CHANGED: Webhook.Event
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_COUNT_FIELD_NUMBER: _ClassVar[int]
    DISCUSSION_MESSAGE_CHANGED: Webhook.Event
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    GROUP_CHANGED: Webhook.Event
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    LAST_FAILURE_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESS_AT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CHANGED: Webhook.Event
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATCH_ALL: Webhook.Patch
    PATCH_ENDPOINT: Webhook.Patch
    PATCH_EVENTS: Webhook.Patch
    PATCH_INACTIVE: Webhook.Patch
    PATCH_NAME: Webhook.Patch
    PATCH_UNKNOWN: Webhook.Patch
    POST_CHANGED: Webhook.Event
    POST_PUBLISHED: Webhook.Event
    POST_TRANSLATION_CHANGED: Webhook.Event
    PROBLEM_CHANGED: Webhook.Event
    PROBLEM_SCORE_CHANGED: Webhook.Event
    PROBLEM_STATEMENT_CHANGED: Webhook.Event
    SECRET_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_CHANGED: Webhook.Event
    SUBMISSION_COMPLETED: Webhook.Event
    TICKET_CHANGED: Webhook.Event
    TICKET_REPLY_CHANGED: Webhook.Event
    UNKNOWN_EVENT: Webhook.Event
    created_at: _timestamp_pb2.Timestamp
    delivery_count: int
    endpoint: str
    events: _containers.RepeatedScalarFieldContainer[Webhook.Event]
    failure_count: int
    id: str
    inactive: bool
    last_failure_at: _timestamp_pb2.Timestamp
    last_success_at: _timestamp_pb2.Timestamp
    name: str
    secret: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., secret: _Optional[str] = ..., endpoint: _Optional[str] = ..., inactive: bool = ..., events: _Optional[_Iterable[_Union[Webhook.Event, str]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_failure_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_success_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delivery_count: _Optional[int] = ..., failure_count: _Optional[int] = ...) -> None: ...
