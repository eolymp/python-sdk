from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import member_pb2 as _member_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignMemberInput(_message.Message):
    __slots__ = ["member_id", "team_id"]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    team_id: str
    def __init__(self, team_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class AssignMemberOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateMemberInput(_message.Message):
    __slots__ = ["member"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _member_pb2.Member
    def __init__(self, member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class CreateMemberOutput(_message.Message):
    __slots__ = ["member_id"]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    def __init__(self, member_id: _Optional[str] = ...) -> None: ...

class DeleteMemberInput(_message.Message):
    __slots__ = ["force_delete", "member_id"]
    FORCE_DELETE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    force_delete: bool
    member_id: str
    def __init__(self, member_id: _Optional[str] = ..., force_delete: bool = ...) -> None: ...

class DeleteMemberOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeMemberInput(_message.Message):
    __slots__ = ["extra", "member_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_member_pb2.Member.Extra]
    member_id: str
    def __init__(self, member_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_member_pb2.Member.Extra, str]]] = ...) -> None: ...

class DescribeMemberOutput(_message.Message):
    __slots__ = ["member"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _member_pb2.Member
    def __init__(self, member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class DescribeMemberUsageInput(_message.Message):
    __slots__ = ["period_end", "period_start"]
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    period_end: _timestamp_pb2.Timestamp
    period_start: _timestamp_pb2.Timestamp
    def __init__(self, period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DescribeMemberUsageOutput(_message.Message):
    __slots__ = ["active_members", "new_members", "total_members"]
    ACTIVE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NEW_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    active_members: int
    new_members: int
    total_members: int
    def __init__(self, total_members: _Optional[int] = ..., active_members: _Optional[int] = ..., new_members: _Optional[int] = ...) -> None: ...

class ListMembersInput(_message.Message):
    __slots__ = ["extra", "filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["group_id", "id", "inactive", "incomplete", "name", "query", "score", "seated", "team_id", "type", "unofficial", "user_email", "user_issuer", "user_name", "user_nickname", "user_subject"]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        INACTIVE_FIELD_NUMBER: _ClassVar[int]
        INCOMPLETE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SEATED_FIELD_NUMBER: _ClassVar[int]
        TEAM_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
        USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        USER_ISSUER_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        USER_NICKNAME_FIELD_NUMBER: _ClassVar[int]
        USER_SUBJECT_FIELD_NUMBER: _ClassVar[int]
        group_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        inactive: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        incomplete: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        score: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        seated: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        team_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        unofficial: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        user_email: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        user_issuer: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        user_name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        user_nickname: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        user_subject: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., inactive: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., incomplete: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., unofficial: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., seated: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., team_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., group_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_issuer: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., user_subject: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., user_email: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., user_name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., user_nickname: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., score: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ...) -> None: ...
    CREATED_AT: ListMembersInput.Sortable
    DEFAULT: ListMembersInput.Sortable
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    NAME: ListMembersInput.Sortable
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SCORE: ListMembersInput.Sortable
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    TYPE: ListMembersInput.Sortable
    extra: _containers.RepeatedScalarFieldContainer[_member_pb2.Member.Extra]
    filters: ListMembersInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListMembersInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListMembersInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListMembersInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_member_pb2.Member.Extra, str]]] = ...) -> None: ...

class ListMembersOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_member_pb2.Member]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_member_pb2.Member, _Mapping]]] = ...) -> None: ...

class RestoreMemberInput(_message.Message):
    __slots__ = ["member_id"]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    def __init__(self, member_id: _Optional[str] = ...) -> None: ...

class RestoreMemberOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UnassignMemberInput(_message.Message):
    __slots__ = ["member_id", "team_id"]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    team_id: str
    def __init__(self, team_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class UnassignMemberOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateMemberInput(_message.Message):
    __slots__ = ["member", "member_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACCOUNT: UpdateMemberInput.Patch
    ALL: UpdateMemberInput.Patch
    ATTRIBUTES: UpdateMemberInput.Patch
    GHOST_NAME: UpdateMemberInput.Patch
    GROUPS: UpdateMemberInput.Patch
    GROUPS_ADD: UpdateMemberInput.Patch
    GROUPS_REMOVE: UpdateMemberInput.Patch
    INACTIVE: UpdateMemberInput.Patch
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    RATING: UpdateMemberInput.Patch
    TEAM_NAME: UpdateMemberInput.Patch
    UNOFFICIAL: UpdateMemberInput.Patch
    USER_BIRTHDAY: UpdateMemberInput.Patch
    USER_CITY: UpdateMemberInput.Patch
    USER_COUNTRY: UpdateMemberInput.Patch
    USER_EMAIL: UpdateMemberInput.Patch
    USER_EMAIL_SUBSCRIPTIONS: UpdateMemberInput.Patch
    USER_NAME: UpdateMemberInput.Patch
    USER_NICKNAME: UpdateMemberInput.Patch
    USER_PASSWORD: UpdateMemberInput.Patch
    USER_PICTURE: UpdateMemberInput.Patch
    USER_PREFERENCES: UpdateMemberInput.Patch
    USER_PREFERENCES_LOCALE: UpdateMemberInput.Patch
    USER_PREFERENCES_RUNTIME: UpdateMemberInput.Patch
    USER_PREFERENCES_TIMEZONE: UpdateMemberInput.Patch
    member: _member_pb2.Member
    member_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateMemberInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateMemberInput.Patch, str]]] = ..., member_id: _Optional[str] = ..., member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class UpdateMemberOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
