from eolymp.universe import space_appearance_config_pb2 as _space_appearance_config_pb2
from eolymp.universe import space_user_config_pb2 as _space_user_config_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Space(_message.Message):
    __slots__ = ["appearance_config", "home_url", "id", "image", "issuer_url", "key", "name", "plan", "type", "url", "user_config", "visibility"]
    class Membership(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Quota(_message.Message):
        __slots__ = ["active_contests_per_space", "attributes_per_space", "contests_per_space", "courses_per_space", "members_per_space", "participants_per_contest", "permissions_per_space", "problems_per_contest", "problems_per_space", "scoreboards_per_space"]
        ACTIVE_CONTESTS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
        CONTESTS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
        COURSES_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
        MEMBERS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANTS_PER_CONTEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
        PROBLEMS_PER_CONTEST_FIELD_NUMBER: _ClassVar[int]
        PROBLEMS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
        SCOREBOARDS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
        active_contests_per_space: int
        attributes_per_space: int
        contests_per_space: int
        courses_per_space: int
        members_per_space: int
        participants_per_contest: int
        permissions_per_space: int
        problems_per_contest: int
        problems_per_space: int
        scoreboards_per_space: int
        def __init__(self, problems_per_space: _Optional[int] = ..., members_per_space: _Optional[int] = ..., contests_per_space: _Optional[int] = ..., active_contests_per_space: _Optional[int] = ..., scoreboards_per_space: _Optional[int] = ..., permissions_per_space: _Optional[int] = ..., attributes_per_space: _Optional[int] = ..., courses_per_space: _Optional[int] = ..., problems_per_contest: _Optional[int] = ..., participants_per_contest: _Optional[int] = ...) -> None: ...
    APPEARANCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLASSROOM: Space.Type
    COMPETITION: Space.Type
    HOME_URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUAL: Space.Membership
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OTHER: Space.Type
    PLAN_FIELD_NUMBER: _ClassVar[int]
    PRIVATE: Space.Visibility
    PUBLIC: Space.Visibility
    TEAM: Space.Membership
    TEAMROOM: Space.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MEMBERSHIP: Space.Membership
    UNKNOWN_TYPE: Space.Type
    UNKNOWN_VISIBILITY: Space.Visibility
    URL_FIELD_NUMBER: _ClassVar[int]
    USER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    appearance_config: _space_appearance_config_pb2.AppearanceConfig
    home_url: str
    id: str
    image: str
    issuer_url: str
    key: str
    name: str
    plan: str
    type: Space.Type
    url: str
    user_config: _space_user_config_pb2.UserConfig
    visibility: Space.Visibility
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., type: _Optional[_Union[Space.Type, str]] = ..., plan: _Optional[str] = ..., visibility: _Optional[_Union[Space.Visibility, str]] = ..., home_url: _Optional[str] = ..., issuer_url: _Optional[str] = ..., user_config: _Optional[_Union[_space_user_config_pb2.UserConfig, _Mapping]] = ..., appearance_config: _Optional[_Union[_space_appearance_config_pb2.AppearanceConfig, _Mapping]] = ...) -> None: ...
