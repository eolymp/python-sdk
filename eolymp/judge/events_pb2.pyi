from eolymp.judge import participant_pb2 as _participant_pb2
from eolymp.judge import reply_pb2 as _reply_pb2
from eolymp.judge import score_pb2 as _score_pb2
from eolymp.judge import submission_pb2 as _submission_pb2
from eolymp.judge import ticket_pb2 as _ticket_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParticipantCreatedEvent(_message.Message):
    __slots__ = ["participant"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    participant: _participant_pb2.Participant
    def __init__(self, participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class ParticipantDeletedEvent(_message.Message):
    __slots__ = ["participant"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    participant: _participant_pb2.Participant
    def __init__(self, participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class ParticipantUpdatedEvent(_message.Message):
    __slots__ = ["participant"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    participant: _participant_pb2.Participant
    def __init__(self, participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class RebuildScoreEvent(_message.Message):
    __slots__ = ["activity_id", "contest_id"]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., activity_id: _Optional[str] = ...) -> None: ...

class RetestProblemEvent(_message.Message):
    __slots__ = ["activity_id", "contest_id", "problem_id"]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., activity_id: _Optional[str] = ...) -> None: ...

class ScoreUpdatedEvent(_message.Message):
    __slots__ = ["contest_id", "participant_id", "score", "unofficial"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    score: _score_pb2.Score
    unofficial: bool
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., unofficial: bool = ..., score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class SubmissionCompletedEvent(_message.Message):
    __slots__ = ["submission"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...

class TicketChangeRecord(_message.Message):
    __slots__ = ["op", "ticket"]
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CREATE: TicketChangeRecord.Operation
    DELETE: TicketChangeRecord.Operation
    NO_OPERATION: TicketChangeRecord.Operation
    OP_FIELD_NUMBER: _ClassVar[int]
    REPLY: TicketChangeRecord.Operation
    TICKET_FIELD_NUMBER: _ClassVar[int]
    UPDATE: TicketChangeRecord.Operation
    op: TicketChangeRecord.Operation
    ticket: _ticket_pb2.Ticket
    def __init__(self, op: _Optional[_Union[TicketChangeRecord.Operation, str]] = ..., ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class TicketCreatedEvent(_message.Message):
    __slots__ = ["ticket"]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: _ticket_pb2.Ticket
    def __init__(self, ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class TicketUpdatedEvent(_message.Message):
    __slots__ = ["reply", "ticket"]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    reply: _reply_pb2.Reply
    ticket: _ticket_pb2.Ticket
    def __init__(self, ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ..., reply: _Optional[_Union[_reply_pb2.Reply, _Mapping]] = ...) -> None: ...
