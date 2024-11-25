from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Webhook(_message.Message):
    __slots__ = ["events", "id", "inactive", "link", "secret"]
    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CONTEST_PARTICIPANT_CHANGED: Webhook.Event
    CONTEST_PARTICIPANT_JOINED: Webhook.Event
    CONTEST_SCORE_CHANGED: Webhook.Event
    CONTEST_SUBMISSION_COMPLETED: Webhook.Event
    COURSE_ASSIGNMENT_CHANGED: Webhook.Event
    COURSE_MATERIAL_CHANGED: Webhook.Event
    COURSE_MODULE_CHANGED: Webhook.Event
    COURSE_STUDENT_CHANGED: Webhook.Event
    DISCUSSION_MESSAGE_CHANGED: Webhook.Event
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    GROUP_CHANGED: Webhook.Event
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    MEMBER_CHANGED: Webhook.Event
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
    events: _containers.RepeatedScalarFieldContainer[Webhook.Event]
    id: str
    inactive: bool
    link: str
    secret: str
    def __init__(self, id: _Optional[str] = ..., inactive: bool = ..., link: _Optional[str] = ..., secret: _Optional[str] = ..., events: _Optional[_Iterable[_Union[Webhook.Event, str]]] = ...) -> None: ...
