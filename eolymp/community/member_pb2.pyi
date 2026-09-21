import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.community import attribute_pb2 as _attribute_pb2
from eolymp.community import member_ghost_pb2 as _member_ghost_pb2
from eolymp.community import member_team_pb2 as _member_team_pb2
from eolymp.community import member_user_pb2 as _member_user_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Member(_message.Message):
    __slots__ = ("id", "url", "resource_link", "space_link", "console_link", "external_ref", "display_name", "rank", "rank_lower", "rating", "level", "inactive", "incomplete", "unofficial", "secret", "active_period_start", "active_period_end", "created_at", "seated_at", "active_at", "user", "team", "ghost", "restrictions", "stats", "groups", "attributes", "metadata")
    class Reference(_message.Message):
        __slots__ = ("id", "display_name", "email")
        ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        id: str
        display_name: str
        email: str
        def __init__(self, id: _Optional[str] = ..., display_name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Member.Extra.Field]
            RANK: _ClassVar[Member.Extra.Field]
            STATS: _ClassVar[Member.Extra.Field]
            GROUPS: _ClassVar[Member.Extra.Field]
            ATTRIBUTES: _ClassVar[Member.Extra.Field]
            METADATA: _ClassVar[Member.Extra.Field]
            RESTRICTIONS: _ClassVar[Member.Extra.Field]
            PRIVATE_DATA: _ClassVar[Member.Extra.Field]
        UNKNOWN_EXTRA: Member.Extra.Field
        RANK: Member.Extra.Field
        STATS: Member.Extra.Field
        GROUPS: Member.Extra.Field
        ATTRIBUTES: Member.Extra.Field
        METADATA: Member.Extra.Field
        RESTRICTIONS: Member.Extra.Field
        PRIVATE_DATA: Member.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ("inactive", "unofficial", "active_period_start", "active_period_end", "groups", "unset_groups", "remove_groups", "add_groups", "attributes", "user", "team", "ghost")
        INACTIVE_FIELD_NUMBER: _ClassVar[int]
        UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PERIOD_START_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PERIOD_END_FIELD_NUMBER: _ClassVar[int]
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        UNSET_GROUPS_FIELD_NUMBER: _ClassVar[int]
        REMOVE_GROUPS_FIELD_NUMBER: _ClassVar[int]
        ADD_GROUPS_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        USER_FIELD_NUMBER: _ClassVar[int]
        TEAM_FIELD_NUMBER: _ClassVar[int]
        GHOST_FIELD_NUMBER: _ClassVar[int]
        inactive: bool
        unofficial: bool
        active_period_start: _timestamp_pb2.Timestamp
        active_period_end: _timestamp_pb2.Timestamp
        groups: _containers.RepeatedScalarFieldContainer[str]
        unset_groups: bool
        remove_groups: _containers.RepeatedScalarFieldContainer[str]
        add_groups: _containers.RepeatedScalarFieldContainer[str]
        attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute.Value]
        user: _member_user_pb2.User.Patch
        team: _member_team_pb2.Team.Patch
        ghost: _member_ghost_pb2.Ghost.Patch
        def __init__(self, inactive: _Optional[bool] = ..., unofficial: _Optional[bool] = ..., active_period_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., active_period_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., groups: _Optional[_Iterable[str]] = ..., unset_groups: _Optional[bool] = ..., remove_groups: _Optional[_Iterable[str]] = ..., add_groups: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute.Value, _Mapping]]] = ..., user: _Optional[_Union[_member_user_pb2.User.Patch, _Mapping]] = ..., team: _Optional[_Union[_member_team_pb2.Team.Patch, _Mapping]] = ..., ghost: _Optional[_Union[_member_ghost_pb2.Ghost.Patch, _Mapping]] = ...) -> None: ...
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
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LINK_FIELD_NUMBER: _ClassVar[int]
    SPACE_LINK_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_LINK_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REF_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    RANK_LOWER_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    INCOMPLETE_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SEATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    resource_link: str
    space_link: str
    console_link: str
    external_ref: str
    display_name: str
    rank: int
    rank_lower: int
    rating: int
    level: int
    inactive: bool
    incomplete: bool
    unofficial: bool
    secret: bool
    active_period_start: _timestamp_pb2.Timestamp
    active_period_end: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    seated_at: _timestamp_pb2.Timestamp
    active_at: _timestamp_pb2.Timestamp
    user: _member_user_pb2.User
    team: _member_team_pb2.Team
    ghost: _member_ghost_pb2.Ghost
    restrictions: _containers.RepeatedScalarFieldContainer[str]
    stats: Member.Stats
    groups: _containers.RepeatedScalarFieldContainer[str]
    attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute.Value]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., resource_link: _Optional[str] = ..., space_link: _Optional[str] = ..., console_link: _Optional[str] = ..., external_ref: _Optional[str] = ..., display_name: _Optional[str] = ..., rank: _Optional[int] = ..., rank_lower: _Optional[int] = ..., rating: _Optional[int] = ..., level: _Optional[int] = ..., inactive: _Optional[bool] = ..., incomplete: _Optional[bool] = ..., unofficial: _Optional[bool] = ..., secret: _Optional[bool] = ..., active_period_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., active_period_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., seated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., active_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user: _Optional[_Union[_member_user_pb2.User, _Mapping]] = ..., team: _Optional[_Union[_member_team_pb2.Team, _Mapping]] = ..., ghost: _Optional[_Union[_member_ghost_pb2.Ghost, _Mapping]] = ..., restrictions: _Optional[_Iterable[str]] = ..., stats: _Optional[_Union[Member.Stats, _Mapping]] = ..., groups: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute.Value, _Mapping]]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
