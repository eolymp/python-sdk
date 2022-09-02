from eolymp.judge import participant_pb2 as _participant_pb2
from eolymp.judge import reply_pb2 as _reply_pb2
from eolymp.judge import score_pb2 as _score_pb2
from eolymp.judge import submission_pb2 as _submission_pb2
from eolymp.judge import ticket_pb2 as _ticket_pb2
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

class ScoreUpdatedEvent(_message.Message):
    __slots__ = ["contest_id", "out_of_competition", "participant_id", "score"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_COMPETITION_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    out_of_competition: bool
    participant_id: str
    score: _score_pb2.Score
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., out_of_competition: bool = ..., score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class SubmissionCompletedEvent(_message.Message):
    __slots__ = ["submission"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...

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
