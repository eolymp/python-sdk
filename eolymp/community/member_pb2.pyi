from eolymp.community import attribute_pb2 as _attribute_pb2
from eolymp.community import member_ghost_pb2 as _member_ghost_pb2
from eolymp.community import member_team_pb2 as _member_team_pb2
from eolymp.community import member_user_pb2 as _member_user_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Member(_message.Message):
    __slots__ = ["active", "attributes", "created_at", "fallback_tier_id", "ghost", "groups", "id", "incomplete", "name", "rank", "rank_lower", "score", "secret", "stats", "team", "tier_id", "unofficial", "url", "user"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Stats(_message.Message):
        __slots__ = ["problems_solved", "streak", "submissions_accepted", "submissions_total"]
        PROBLEMS_SOLVED_FIELD_NUMBER: _ClassVar[int]
        STREAK_FIELD_NUMBER: _ClassVar[int]
        SUBMISSIONS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
        SUBMISSIONS_TOTAL_FIELD_NUMBER: _ClassVar[int]
        problems_solved: int
        streak: int
        submissions_accepted: int
        submissions_total: int
        def __init__(self, streak: _Optional[int] = ..., problems_solved: _Optional[int] = ..., submissions_accepted: _Optional[int] = ..., submissions_total: _Optional[int] = ...) -> None: ...
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES: Member.Extra
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_TIER_ID_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    GROUPS: Member.Extra
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INCOMPLETE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NO_EXTRA: Member.Extra
    RANK_FIELD_NUMBER: _ClassVar[int]
    RANK_LOWER_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    STATS: Member.Extra
    STATS_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    TIER: Member.Extra
    TIER_ID_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    active: bool
    attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute.Value]
    created_at: _timestamp_pb2.Timestamp
    fallback_tier_id: str
    ghost: _member_ghost_pb2.Ghost
    groups: _containers.RepeatedScalarFieldContainer[str]
    id: str
    incomplete: bool
    name: str
    rank: int
    rank_lower: int
    score: int
    secret: bool
    stats: Member.Stats
    team: _member_team_pb2.Team
    tier_id: str
    unofficial: bool
    url: str
    user: _member_user_pb2.User
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., url: _Optional[str] = ..., rank: _Optional[int] = ..., rank_lower: _Optional[int] = ..., score: _Optional[int] = ..., active: bool = ..., incomplete: bool = ..., unofficial: bool = ..., secret: bool = ..., tier_id: _Optional[str] = ..., fallback_tier_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user: _Optional[_Union[_member_user_pb2.User, _Mapping]] = ..., team: _Optional[_Union[_member_team_pb2.Team, _Mapping]] = ..., ghost: _Optional[_Union[_member_ghost_pb2.Ghost, _Mapping]] = ..., stats: _Optional[_Union[Member.Stats, _Mapping]] = ..., groups: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute.Value, _Mapping]]] = ...) -> None: ...
