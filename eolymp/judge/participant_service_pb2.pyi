from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import participant_pb2 as _participant_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant: _participant_pb2.Participant
    def __init__(self, contest_id: _Optional[str] = ..., participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class AddParticipantOutput(_message.Message):
    __slots__ = ["participant_id"]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    participant_id: str
    def __init__(self, participant_id: _Optional[str] = ...) -> None: ...

class DescribeParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class DescribeParticipantOutput(_message.Message):
    __slots__ = ["participant"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    participant: _participant_pb2.Participant
    def __init__(self, participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class DisableParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class DisableParticipantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EnableParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class EnableParticipantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EnterPasscodeInput(_message.Message):
    __slots__ = ["contest_id", "passcode"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    passcode: str
    def __init__(self, contest_id: _Optional[str] = ..., passcode: _Optional[str] = ...) -> None: ...

class EnterPasscodeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectParticipantInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class IntrospectParticipantOutput(_message.Message):
    __slots__ = ["participant"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    participant: _participant_pb2.Participant
    def __init__(self, participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class JoinContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class JoinContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListParticipantsInput(_message.Message):
    __slots__ = ["contest_id", "filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["complete_at", "id", "member_id", "name", "penalty", "score", "started_at", "status"]
        COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        complete_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        penalty: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        score: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        started_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., score: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., penalty: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., started_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., complete_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ...) -> None: ...
    COMPLETE_AT: ListParticipantsInput.Sortable
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PENALTY: ListParticipantsInput.Sortable
    RANK: ListParticipantsInput.Sortable
    SCORE: ListParticipantsInput.Sortable
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT: ListParticipantsInput.Sortable
    contest_id: str
    filters: ListParticipantsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListParticipantsInput.Sortable
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListParticipantsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListParticipantsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListParticipantsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_participant_pb2.Participant]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_participant_pb2.Participant, _Mapping]]] = ...) -> None: ...

class RemoveParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class RemoveParticipantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemovePasscodeInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class RemovePasscodeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ResetPasscodeInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class ResetPasscodeOutput(_message.Message):
    __slots__ = ["passcode"]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    passcode: str
    def __init__(self, passcode: _Optional[str] = ...) -> None: ...

class SetPasscodeInput(_message.Message):
    __slots__ = ["contest_id", "participant_id", "passcode"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    passcode: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., passcode: _Optional[str] = ...) -> None: ...

class SetPasscodeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StartContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class StartContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant", "participant_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: UpdateParticipantInput.Patch
    ALL: UpdateParticipantInput.Patch
    BONUS_TIME: UpdateParticipantInput.Patch
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MEDAL: UpdateParticipantInput.Patch
    NAME: UpdateParticipantInput.Patch
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    PASSCODE: UpdateParticipantInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL: UpdateParticipantInput.Patch
    contest_id: str
    participant: _participant_pb2.Participant
    participant_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateParticipantInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateParticipantInput.Patch, str]]] = ..., contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class UpdateParticipantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VerifyPasscodeInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class VerifyPasscodeOutput(_message.Message):
    __slots__ = ["required", "valid"]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    VALID_FIELD_NUMBER: _ClassVar[int]
    required: bool
    valid: bool
    def __init__(self, required: bool = ..., valid: bool = ...) -> None: ...

class WatchParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class WatchParticipantOutput(_message.Message):
    __slots__ = ["participant"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    participant: _participant_pb2.Participant
    def __init__(self, participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...
