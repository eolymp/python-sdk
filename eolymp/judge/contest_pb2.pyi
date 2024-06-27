from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Contest(_message.Message):
    __slots__ = ["appearance", "duration", "ends_at", "ends_in", "environment", "featured_until", "format", "id", "join_unofficially", "key", "links", "logo_url", "name", "participant_count", "participant_count_hidden", "participation_mode", "problem_count", "problem_count_hidden", "scoreboard", "starts_at", "starts_in", "status", "taxonomy", "upsolve", "url", "visibility"]
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ParticipationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Appearance(_message.Message):
        __slots__ = ["description", "logo_url", "title"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LOGO_URL_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        description: str
        logo_url: str
        title: str
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., logo_url: _Optional[str] = ...) -> None: ...
    class Environment(_message.Message):
        __slots__ = ["allowed_runtimes"]
        ALLOWED_RUNTIMES_FIELD_NUMBER: _ClassVar[int]
        allowed_runtimes: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, allowed_runtimes: _Optional[_Iterable[str]] = ...) -> None: ...
    class LinksEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Scoreboard(_message.Message):
        __slots__ = ["attempt_penalty", "freezing_time", "no_spoiler_ui", "share_key", "tie_breaker", "unfreeze_delay", "visibility"]
        class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ATTEMPT_PENALTY_FIELD_NUMBER: _ClassVar[int]
        FREEZING_TIME_FIELD_NUMBER: _ClassVar[int]
        INTERNAL: Contest.Scoreboard.Visibility
        INVISIBLE: Contest.Scoreboard.Visibility
        NO_SPOILER_UI_FIELD_NUMBER: _ClassVar[int]
        PUBLIC: Contest.Scoreboard.Visibility
        SHARE_KEY_FIELD_NUMBER: _ClassVar[int]
        TIE_BREAKER_FIELD_NUMBER: _ClassVar[int]
        UNFREEZE_DELAY_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_VISIBILITY: Contest.Scoreboard.Visibility
        VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        attempt_penalty: int
        freezing_time: int
        no_spoiler_ui: bool
        share_key: str
        tie_breaker: str
        unfreeze_delay: int
        visibility: Contest.Scoreboard.Visibility
        def __init__(self, visibility: _Optional[_Union[Contest.Scoreboard.Visibility, str]] = ..., freezing_time: _Optional[int] = ..., unfreeze_delay: _Optional[int] = ..., attempt_penalty: _Optional[int] = ..., tie_breaker: _Optional[str] = ..., no_spoiler_ui: bool = ..., share_key: _Optional[str] = ...) -> None: ...
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
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_IN_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    FEATURED_UNTIL_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_UNKNOWN: Contest.Format
    FROZEN: Contest.Status
    ICPC: Contest.Format
    ID_FIELD_NUMBER: _ClassVar[int]
    IOI: Contest.Format
    JOIN_UNOFFICIALLY_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ONLINE: Contest.ParticipationMode
    OPEN: Contest.Status
    PARTICIPANT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_COUNT_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    PARTICIPATION_MODE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPATION_MODE_UNKNOWN: Contest.ParticipationMode
    PRIVATE: Contest.Visibility
    PROBLEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_COUNT_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    PUBLIC: Contest.Visibility
    SCHEDULED: Contest.Status
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
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
    duration: int
    ends_at: _timestamp_pb2.Timestamp
    ends_in: int
    environment: Contest.Environment
    featured_until: _timestamp_pb2.Timestamp
    format: Contest.Format
    id: str
    join_unofficially: bool
    key: str
    links: _containers.ScalarMap[str, str]
    logo_url: str
    name: str
    participant_count: int
    participant_count_hidden: bool
    participation_mode: Contest.ParticipationMode
    problem_count: int
    problem_count_hidden: bool
    scoreboard: Contest.Scoreboard
    starts_at: _timestamp_pb2.Timestamp
    starts_in: int
    status: Contest.Status
    taxonomy: Contest.Taxonomy
    upsolve: Contest.Upsolve
    url: str
    visibility: Contest.Visibility
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., links: _Optional[_Mapping[str, str]] = ..., name: _Optional[str] = ..., logo_url: _Optional[str] = ..., starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., starts_in: _Optional[int] = ..., ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ends_in: _Optional[int] = ..., duration: _Optional[int] = ..., status: _Optional[_Union[Contest.Status, str]] = ..., visibility: _Optional[_Union[Contest.Visibility, str]] = ..., join_unofficially: bool = ..., participation_mode: _Optional[_Union[Contest.ParticipationMode, str]] = ..., format: _Optional[_Union[Contest.Format, str]] = ..., key: _Optional[str] = ..., problem_count: _Optional[int] = ..., problem_count_hidden: bool = ..., participant_count: _Optional[int] = ..., participant_count_hidden: bool = ..., featured_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., taxonomy: _Optional[_Union[Contest.Taxonomy, _Mapping]] = ..., appearance: _Optional[_Union[Contest.Appearance, _Mapping]] = ..., environment: _Optional[_Union[Contest.Environment, _Mapping]] = ..., upsolve: _Optional[_Union[Contest.Upsolve, _Mapping]] = ..., scoreboard: _Optional[_Union[Contest.Scoreboard, _Mapping]] = ...) -> None: ...
