from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.judge import participant_pb2 as _participant_pb2
from eolymp.judge import result_pb2 as _result_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParticipantChangedEvent(_message.Message):
    __slots__ = ("contest_id", "before", "after")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    before: _participant_pb2.Participant
    after: _participant_pb2.Participant
    def __init__(self, contest_id: _Optional[str] = ..., before: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ..., after: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class ParticipantJoinedEvent(_message.Message):
    __slots__ = ("contest_id", "participant")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant: _participant_pb2.Participant
    def __init__(self, contest_id: _Optional[str] = ..., participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class ParticipantFinalizedEvent(_message.Message):
    __slots__ = ("contest_id", "participant", "result")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant: _participant_pb2.Participant
    result: _result_pb2.Result
    def __init__(self, contest_id: _Optional[str] = ..., participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ..., result: _Optional[_Union[_result_pb2.Result, _Mapping]] = ...) -> None: ...

class AssignParticipantInput(_message.Message):
    __slots__ = ("contest_id", "member_id", "group_id", "ghost", "unofficial", "inactive", "role")
    class Ghost(_message.Message):
        __slots__ = ("display_name",)
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        def __init__(self, display_name: _Optional[str] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    member_id: str
    group_id: str
    ghost: AssignParticipantInput.Ghost
    unofficial: bool
    inactive: bool
    role: _participant_pb2.Participant.Role
    def __init__(self, contest_id: _Optional[str] = ..., member_id: _Optional[str] = ..., group_id: _Optional[str] = ..., ghost: _Optional[_Union[AssignParticipantInput.Ghost, _Mapping]] = ..., unofficial: bool = ..., inactive: bool = ..., role: _Optional[_Union[_participant_pb2.Participant.Role, str]] = ...) -> None: ...

class AssignParticipantOutput(_message.Message):
    __slots__ = ("participant_id",)
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    participant_id: str
    def __init__(self, participant_id: _Optional[str] = ...) -> None: ...

class EnableParticipantInput(_message.Message):
    __slots__ = ("contest_id", "participant_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class EnableParticipantOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisableParticipantInput(_message.Message):
    __slots__ = ("contest_id", "participant_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class DisableParticipantOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateParticipantInput(_message.Message):
    __slots__ = ("patch", "contest_id", "participant_id", "participant")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_participant_pb2.Participant.Patch.Field]
    contest_id: str
    participant_id: str
    participant: _participant_pb2.Participant
    def __init__(self, patch: _Optional[_Iterable[_Union[_participant_pb2.Participant.Patch.Field, str]]] = ..., contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class UpdateParticipantOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisqualifyParticipantInput(_message.Message):
    __slots__ = ("contest_id", "participant_id", "disqualify", "reason")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    DISQUALIFY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    disqualify: bool
    reason: _content_pb2.Content
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., disqualify: bool = ..., reason: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class DisqualifyParticipantOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteParticipantInput(_message.Message):
    __slots__ = ("contest_id", "participant_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class DeleteParticipantOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeParticipantInput(_message.Message):
    __slots__ = ("contest_id", "participant_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class DescribeParticipantOutput(_message.Message):
    __slots__ = ("participant",)
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    participant: _participant_pb2.Participant
    def __init__(self, participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class ListParticipantsInput(_message.Message):
    __slots__ = ("contest_id", "offset", "size", "search", "filters", "sort", "order")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListParticipantsInput.Sortable]
        DISPLAY_NAME: _ClassVar[ListParticipantsInput.Sortable]
        STARTED_AT: _ClassVar[ListParticipantsInput.Sortable]
    DEFAULT: ListParticipantsInput.Sortable
    DISPLAY_NAME: ListParticipantsInput.Sortable
    STARTED_AT: ListParticipantsInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "member_id", "group_id", "status", "started_at", "unofficial", "disqualified", "inactive", "role", "staff", "has_violations")
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
        DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
        INACTIVE_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        STAFF_FIELD_NUMBER: _ClassVar[int]
        HAS_VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        group_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        started_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        unofficial: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        disqualified: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        inactive: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        role: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        staff: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        has_violations: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., group_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., started_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., unofficial: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., disqualified: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., inactive: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., role: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., staff: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., has_violations: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    offset: int
    size: int
    search: str
    filters: ListParticipantsInput.Filter
    sort: ListParticipantsInput.Sortable
    order: _direction_pb2.Direction
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListParticipantsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListParticipantsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListParticipantsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_participant_pb2.Participant]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_participant_pb2.Participant, _Mapping]]] = ...) -> None: ...

class WatchParticipantInput(_message.Message):
    __slots__ = ("contest_id", "participant_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class WatchParticipantOutput(_message.Message):
    __slots__ = ("participant",)
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    participant: _participant_pb2.Participant
    def __init__(self, participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class DescribeViewerInput(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DescribeViewerOutput(_message.Message):
    __slots__ = ("participant",)
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    participant: _participant_pb2.Participant
    def __init__(self, participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class JoinContestInput(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class JoinContestOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartContestInput(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class StartContestOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PauseContestInput(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class PauseContestOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FinishContestInput(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class FinishContestOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
