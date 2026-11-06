from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.team import team_pb2 as _team_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTeamInput(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: _team_pb2.Team
    def __init__(self, team: _Optional[_Union[_team_pb2.Team, _Mapping]] = ...) -> None: ...

class CreateTeamOutput(_message.Message):
    __slots__ = ("team_id",)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    def __init__(self, team_id: _Optional[str] = ...) -> None: ...

class UpdateTeamInput(_message.Message):
    __slots__ = ("team_id", "team")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    team: _team_pb2.Team.Patch
    def __init__(self, team_id: _Optional[str] = ..., team: _Optional[_Union[_team_pb2.Team.Patch, _Mapping]] = ...) -> None: ...

class UpdateTeamOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TransferCaptainInput(_message.Message):
    __slots__ = ("team_id", "member_id")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    member_id: str
    def __init__(self, team_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class TransferCaptainOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DisbandTeamInput(_message.Message):
    __slots__ = ("team_id",)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    def __init__(self, team_id: _Optional[str] = ...) -> None: ...

class DisbandTeamOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeTeamInput(_message.Message):
    __slots__ = ("team_id",)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    def __init__(self, team_id: _Optional[str] = ...) -> None: ...

class DescribeTeamOutput(_message.Message):
    __slots__ = ("team",)
    TEAM_FIELD_NUMBER: _ClassVar[int]
    team: _team_pb2.Team
    def __init__(self, team: _Optional[_Union[_team_pb2.Team, _Mapping]] = ...) -> None: ...

class ListTeamsInput(_message.Message):
    __slots__ = ("offset", "size", "search", "filters", "sort", "order")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListTeamsInput.Sortable]
        NAME: _ClassVar[ListTeamsInput.Sortable]
        CREATED_AT: _ClassVar[ListTeamsInput.Sortable]
    DEFAULT: ListTeamsInput.Sortable
    NAME: ListTeamsInput.Sortable
    CREATED_AT: ListTeamsInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "member_id", "captain_id", "disbanded")
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        CAPTAIN_ID_FIELD_NUMBER: _ClassVar[int]
        DISBANDED_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        captain_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        disbanded: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., captain_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., disbanded: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    search: str
    filters: ListTeamsInput.Filter
    sort: ListTeamsInput.Sortable
    order: _direction_pb2.Direction
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListTeamsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListTeamsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListTeamsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_team_pb2.Team]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_team_pb2.Team, _Mapping]]] = ...) -> None: ...

class AddTeamMemberInput(_message.Message):
    __slots__ = ("team_id", "member_id")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    member_id: str
    def __init__(self, team_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class AddTeamMemberOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveTeamMemberInput(_message.Message):
    __slots__ = ("team_id", "member_id")
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    member_id: str
    def __init__(self, team_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class RemoveTeamMemberOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LeaveTeamInput(_message.Message):
    __slots__ = ("team_id",)
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    team_id: str
    def __init__(self, team_id: _Optional[str] = ...) -> None: ...

class LeaveTeamOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
