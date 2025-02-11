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
    __slots__ = ("id", "display_name", "url", "rank", "rank_lower", "rating", "level", "inactive", "incomplete", "unofficial", "secret", "tier_id", "fallback_tier_id", "created_at", "seated_at", "active_at", "user", "team", "ghost", "stats", "groups", "attributes")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Member.Extra]
        TIER: _ClassVar[Member.Extra]
        STATS: _ClassVar[Member.Extra]
        GROUPS: _ClassVar[Member.Extra]
        ATTRIBUTES: _ClassVar[Member.Extra]
    NO_EXTRA: Member.Extra
    TIER: Member.Extra
    STATS: Member.Extra
    GROUPS: Member.Extra
    ATTRIBUTES: Member.Extra
    class Stats(_message.Message):
        __slots__ = ("streak", "problems_solved", "submissions_accepted", "submissions_total")
        STREAK_FIELD_NUMBER: _ClassVar[int]
        PROBLEMS_SOLVED_FIELD_NUMBER: _ClassVar[int]
        SUBMISSIONS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
        SUBMISSIONS_TOTAL_FIELD_NUMBER: _ClassVar[int]
        streak: int
        problems_solved: int
        submissions_accepted: int
        submissions_total: int
        def __init__(self, streak: _Optional[int] = ..., problems_solved: _Optional[int] = ..., submissions_accepted: _Optional[int] = ..., submissions_total: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    RANK_LOWER_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    INCOMPLETE_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    TIER_ID_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_TIER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SEATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    url: str
    rank: int
    rank_lower: int
    rating: int
    level: int
    inactive: bool
    incomplete: bool
    unofficial: bool
    secret: bool
    tier_id: str
    fallback_tier_id: str
    created_at: _timestamp_pb2.Timestamp
    seated_at: _timestamp_pb2.Timestamp
    active_at: _timestamp_pb2.Timestamp
    user: _member_user_pb2.User
    team: _member_team_pb2.Team
    ghost: _member_ghost_pb2.Ghost
    stats: Member.Stats
    groups: _containers.RepeatedScalarFieldContainer[str]
    attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute.Value]
    def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., url: _Optional[str] = ..., rank: _Optional[int] = ..., rank_lower: _Optional[int] = ..., rating: _Optional[int] = ..., level: _Optional[int] = ..., inactive: bool = ..., incomplete: bool = ..., unofficial: bool = ..., secret: bool = ..., tier_id: _Optional[str] = ..., fallback_tier_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., seated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., active_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., user: _Optional[_Union[_member_user_pb2.User, _Mapping]] = ..., team: _Optional[_Union[_member_team_pb2.Team, _Mapping]] = ..., ghost: _Optional[_Union[_member_ghost_pb2.Ghost, _Mapping]] = ..., stats: _Optional[_Union[Member.Stats, _Mapping]] = ..., groups: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute.Value, _Mapping]]] = ...) -> None: ...
