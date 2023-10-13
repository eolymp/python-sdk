from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Contest(_message.Message):
    __slots__ = ["appearance", "domain", "duration", "ends_at", "ends_in", "environment", "format", "id", "join_unofficially", "name", "participation_mode", "scoreboard", "space_id", "starts_at", "starts_in", "status", "taxonomy", "upsolve", "url", "visibility"]
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ParticipationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Appearance(_message.Message):
        __slots__ = ["description", "logo_image", "primary_color", "secondary_color", "tagline", "title"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LOGO_IMAGE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
        TAGLINE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        description: str
        logo_image: str
        primary_color: str
        secondary_color: str
        tagline: str
        title: str
        def __init__(self, title: _Optional[str] = ..., tagline: _Optional[str] = ..., description: _Optional[str] = ..., logo_image: _Optional[str] = ..., primary_color: _Optional[str] = ..., secondary_color: _Optional[str] = ...) -> None: ...
    class Environment(_message.Message):
        __slots__ = ["allowed_runtimes"]
        ALLOWED_RUNTIMES_FIELD_NUMBER: _ClassVar[int]
        allowed_runtimes: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, allowed_runtimes: _Optional[_Iterable[str]] = ...) -> None: ...
    class Scoreboard(_message.Message):
        __slots__ = ["attempt_penalty", "freezing_time", "unfreeze_delay", "use_name_in_scoreboard", "visibility"]
        class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ATTEMPT_PENALTY_FIELD_NUMBER: _ClassVar[int]
        FREEZING_TIME_FIELD_NUMBER: _ClassVar[int]
        INTERNAL: Contest.Scoreboard.Visibility
        INVISIBLE: Contest.Scoreboard.Visibility
        PUBLIC: Contest.Scoreboard.Visibility
        UNFREEZE_DELAY_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_VISIBILITY: Contest.Scoreboard.Visibility
        USE_NAME_IN_SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
        VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        attempt_penalty: int
        freezing_time: int
        unfreeze_delay: int
        use_name_in_scoreboard: bool
        visibility: Contest.Scoreboard.Visibility
        def __init__(self, visibility: _Optional[_Union[Contest.Scoreboard.Visibility, str]] = ..., freezing_time: _Optional[int] = ..., unfreeze_delay: _Optional[int] = ..., attempt_penalty: _Optional[int] = ..., use_name_in_scoreboard: bool = ...) -> None: ...
    class Taxonomy(_message.Message):
        __slots__ = ["city", "country", "difficulty", "region", "scale", "series", "year"]
        class Scale(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        CITY_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
        INTERNATIONAL: Contest.Taxonomy.Scale
        LOCAL: Contest.Taxonomy.Scale
        NATIONAL: Contest.Taxonomy.Scale
        REGIONAL: Contest.Taxonomy.Scale
        REGION_FIELD_NUMBER: _ClassVar[int]
        SCALE_FIELD_NUMBER: _ClassVar[int]
        SERIES_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_SCALE: Contest.Taxonomy.Scale
        YEAR_FIELD_NUMBER: _ClassVar[int]
        city: str
        country: str
        difficulty: int
        region: str
        scale: Contest.Taxonomy.Scale
        series: str
        year: int
        def __init__(self, year: _Optional[int] = ..., series: _Optional[str] = ..., scale: _Optional[_Union[Contest.Taxonomy.Scale, str]] = ..., difficulty: _Optional[int] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...
    class Upsolve(_message.Message):
        __slots__ = ["free_upsolve", "virtual_upsolve"]
        FREE_UPSOLVE_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_UPSOLVE_FIELD_NUMBER: _ClassVar[int]
        free_upsolve: bool
        virtual_upsolve: bool
        def __init__(self, free_upsolve: bool = ..., virtual_upsolve: bool = ...) -> None: ...
    APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: Contest.Status
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_IN_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_UNKNOWN: Contest.Format
    FROZEN: Contest.Status
    ICPC: Contest.Format
    ID_FIELD_NUMBER: _ClassVar[int]
    IOI: Contest.Format
    JOIN_UNOFFICIALLY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ONLINE: Contest.ParticipationMode
    OPEN: Contest.Status
    PARTICIPATION_MODE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPATION_MODE_UNKNOWN: Contest.ParticipationMode
    PRIVATE: Contest.Visibility
    PUBLIC: Contest.Visibility
    SCHEDULED: Contest.Status
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    STARTS_IN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_UNKNOWN: Contest.Status
    SUSPENDED: Contest.Status
    TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    UNLISTED: Contest.Visibility
    UPSOLVE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL: Contest.ParticipationMode
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_UNKNOWN: Contest.Visibility
    appearance: Contest.Appearance
    domain: str
    duration: int
    ends_at: _timestamp_pb2.Timestamp
    ends_in: int
    environment: Contest.Environment
    format: Contest.Format
    id: str
    join_unofficially: bool
    name: str
    participation_mode: Contest.ParticipationMode
    scoreboard: Contest.Scoreboard
    space_id: str
    starts_at: _timestamp_pb2.Timestamp
    starts_in: int
    status: Contest.Status
    taxonomy: Contest.Taxonomy
    upsolve: Contest.Upsolve
    url: str
    visibility: Contest.Visibility
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., starts_in: _Optional[int] = ..., ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ends_in: _Optional[int] = ..., duration: _Optional[int] = ..., status: _Optional[_Union[Contest.Status, str]] = ..., visibility: _Optional[_Union[Contest.Visibility, str]] = ..., join_unofficially: bool = ..., participation_mode: _Optional[_Union[Contest.ParticipationMode, str]] = ..., format: _Optional[_Union[Contest.Format, str]] = ..., domain: _Optional[str] = ..., space_id: _Optional[str] = ..., taxonomy: _Optional[_Union[Contest.Taxonomy, _Mapping]] = ..., appearance: _Optional[_Union[Contest.Appearance, _Mapping]] = ..., environment: _Optional[_Union[Contest.Environment, _Mapping]] = ..., upsolve: _Optional[_Union[Contest.Upsolve, _Mapping]] = ..., scoreboard: _Optional[_Union[Contest.Scoreboard, _Mapping]] = ...) -> None: ...
