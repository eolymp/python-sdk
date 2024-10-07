from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.judge import participant_pb2 as _participant_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignParticipantInput(_message.Message):
    __slots__ = ["contest_id", "group_id", "inactive", "member_id", "participant", "unofficial"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    group_id: str
    inactive: bool
    member_id: str
    participant: _participant_pb2.Participant
    unofficial: bool
    def __init__(self, contest_id: _Optional[str] = ..., participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ..., member_id: _Optional[str] = ..., group_id: _Optional[str] = ..., unofficial: bool = ..., inactive: bool = ...) -> None: ...

class AssignParticipantOutput(_message.Message):
    __slots__ = ["participant_id"]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    participant_id: str
    def __init__(self, participant_id: _Optional[str] = ...) -> None: ...

class DeleteParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class DeleteParticipantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

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

class DescribeViewerInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DescribeViewerOutput(_message.Message):
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

class DisqualifyParticipantInput(_message.Message):
    __slots__ = ["contest_id", "disqualify", "participant_id", "reason"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    DISQUALIFY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    disqualify: bool
    participant_id: str
    reason: _content_pb2.Content
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., disqualify: bool = ..., reason: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class DisqualifyParticipantOutput(_message.Message):
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
        __slots__ = ["disqualified", "group_id", "id", "inactive", "member_id", "query", "started_at", "status", "unofficial"]
        DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        INACTIVE_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
        disqualified: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        group_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        inactive: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        query: str
        started_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        unofficial: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., group_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., started_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., unofficial: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., disqualified: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., inactive: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT: ListParticipantsInput.Sortable
    DISPLAY_NAME: ListParticipantsInput.Sortable
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
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
    ALL: UpdateParticipantInput.Patch
    BONUS_TIME: UpdateParticipantInput.Patch
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME: UpdateParticipantInput.Patch
    INACTIVE: UpdateParticipantInput.Patch
    MEDAL: UpdateParticipantInput.Patch
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
