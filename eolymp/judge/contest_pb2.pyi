from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Contest(_message.Message):
    __slots__ = ("id", "url", "name", "logo_url", "starts_at", "starts_in", "ends_at", "ends_in", "duration", "status", "visibility", "join_unofficially", "participation_mode", "format", "key", "problem_count", "problem_count_hidden", "participant_count", "participant_count_hidden", "featured_until", "printer_id", "taxonomy", "appearance", "environment", "upsolve", "scoreboard")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNKNOWN: _ClassVar[Contest.Status]
        SCHEDULED: _ClassVar[Contest.Status]
        OPEN: _ClassVar[Contest.Status]
        COMPLETE: _ClassVar[Contest.Status]
        SUSPENDED: _ClassVar[Contest.Status]
        FROZEN: _ClassVar[Contest.Status]
    STATUS_UNKNOWN: Contest.Status
    SCHEDULED: Contest.Status
    OPEN: Contest.Status
    COMPLETE: Contest.Status
    SUSPENDED: Contest.Status
    FROZEN: Contest.Status
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VISIBILITY_UNKNOWN: _ClassVar[Contest.Visibility]
        PUBLIC: _ClassVar[Contest.Visibility]
        UNLISTED: _ClassVar[Contest.Visibility]
        PRIVATE: _ClassVar[Contest.Visibility]
    VISIBILITY_UNKNOWN: Contest.Visibility
    PUBLIC: Contest.Visibility
    UNLISTED: Contest.Visibility
    PRIVATE: Contest.Visibility
    class ParticipationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARTICIPATION_MODE_UNKNOWN: _ClassVar[Contest.ParticipationMode]
        ONLINE: _ClassVar[Contest.ParticipationMode]
        VIRTUAL: _ClassVar[Contest.ParticipationMode]
    PARTICIPATION_MODE_UNKNOWN: Contest.ParticipationMode
    ONLINE: Contest.ParticipationMode
    VIRTUAL: Contest.ParticipationMode
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_UNKNOWN: _ClassVar[Contest.Format]
        IOI: _ClassVar[Contest.Format]
        ICPC: _ClassVar[Contest.Format]
    FORMAT_UNKNOWN: Contest.Format
    IOI: Contest.Format
    ICPC: Contest.Format
    class Appearance(_message.Message):
        __slots__ = ("title", "description", "logo_url")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LOGO_URL_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        logo_url: str
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., logo_url: _Optional[str] = ...) -> None: ...
    class Taxonomy(_message.Message):
        __slots__ = ("year", "series", "scale", "difficulty", "country", "region", "city")
        class Scale(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_SCALE: _ClassVar[Contest.Taxonomy.Scale]
            LOCAL: _ClassVar[Contest.Taxonomy.Scale]
            REGIONAL: _ClassVar[Contest.Taxonomy.Scale]
            NATIONAL: _ClassVar[Contest.Taxonomy.Scale]
            INTERNATIONAL: _ClassVar[Contest.Taxonomy.Scale]
        UNKNOWN_SCALE: Contest.Taxonomy.Scale
        LOCAL: Contest.Taxonomy.Scale
        REGIONAL: Contest.Taxonomy.Scale
        NATIONAL: Contest.Taxonomy.Scale
        INTERNATIONAL: Contest.Taxonomy.Scale
        YEAR_FIELD_NUMBER: _ClassVar[int]
        SERIES_FIELD_NUMBER: _ClassVar[int]
        SCALE_FIELD_NUMBER: _ClassVar[int]
        DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        CITY_FIELD_NUMBER: _ClassVar[int]
        year: int
        series: str
        scale: Contest.Taxonomy.Scale
        difficulty: int
        country: str
        region: str
        city: str
        def __init__(self, year: _Optional[int] = ..., series: _Optional[str] = ..., scale: _Optional[_Union[Contest.Taxonomy.Scale, str]] = ..., difficulty: _Optional[int] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...
    class Environment(_message.Message):
        __slots__ = ("allowed_runtimes",)
        ALLOWED_RUNTIMES_FIELD_NUMBER: _ClassVar[int]
        allowed_runtimes: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, allowed_runtimes: _Optional[_Iterable[str]] = ...) -> None: ...
    class Upsolve(_message.Message):
        __slots__ = ("free_upsolve", "virtual_upsolve")
        FREE_UPSOLVE_FIELD_NUMBER: _ClassVar[int]
        VIRTUAL_UPSOLVE_FIELD_NUMBER: _ClassVar[int]
        free_upsolve: bool
        virtual_upsolve: bool
        def __init__(self, free_upsolve: bool = ..., virtual_upsolve: bool = ...) -> None: ...
    class Scoreboard(_message.Message):
        __slots__ = ("visibility", "freezing_time", "unfreeze_delay", "attempt_penalty", "tie_breaker", "no_spoiler_ui", "share_key")
        class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_VISIBILITY: _ClassVar[Contest.Scoreboard.Visibility]
            INVISIBLE: _ClassVar[Contest.Scoreboard.Visibility]
            INTERNAL: _ClassVar[Contest.Scoreboard.Visibility]
            PUBLIC: _ClassVar[Contest.Scoreboard.Visibility]
        UNKNOWN_VISIBILITY: Contest.Scoreboard.Visibility
        INVISIBLE: Contest.Scoreboard.Visibility
        INTERNAL: Contest.Scoreboard.Visibility
        PUBLIC: Contest.Scoreboard.Visibility
        VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        FREEZING_TIME_FIELD_NUMBER: _ClassVar[int]
        UNFREEZE_DELAY_FIELD_NUMBER: _ClassVar[int]
        ATTEMPT_PENALTY_FIELD_NUMBER: _ClassVar[int]
        TIE_BREAKER_FIELD_NUMBER: _ClassVar[int]
        NO_SPOILER_UI_FIELD_NUMBER: _ClassVar[int]
        SHARE_KEY_FIELD_NUMBER: _ClassVar[int]
        visibility: Contest.Scoreboard.Visibility
        freezing_time: int
        unfreeze_delay: int
        attempt_penalty: int
        tie_breaker: str
        no_spoiler_ui: bool
        share_key: str
        def __init__(self, visibility: _Optional[_Union[Contest.Scoreboard.Visibility, str]] = ..., freezing_time: _Optional[int] = ..., unfreeze_delay: _Optional[int] = ..., attempt_penalty: _Optional[int] = ..., tie_breaker: _Optional[str] = ..., no_spoiler_ui: bool = ..., share_key: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    STARTS_IN_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_IN_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    JOIN_UNOFFICIALLY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPATION_MODE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_COUNT_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_COUNT_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    FEATURED_UNTIL_FIELD_NUMBER: _ClassVar[int]
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    UPSOLVE_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    logo_url: str
    starts_at: _timestamp_pb2.Timestamp
    starts_in: int
    ends_at: _timestamp_pb2.Timestamp
    ends_in: int
    duration: int
    status: Contest.Status
    visibility: Contest.Visibility
    join_unofficially: bool
    participation_mode: Contest.ParticipationMode
    format: Contest.Format
    key: str
    problem_count: int
    problem_count_hidden: bool
    participant_count: int
    participant_count_hidden: bool
    featured_until: _timestamp_pb2.Timestamp
    printer_id: str
    taxonomy: Contest.Taxonomy
    appearance: Contest.Appearance
    environment: Contest.Environment
    upsolve: Contest.Upsolve
    scoreboard: Contest.Scoreboard
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., logo_url: _Optional[str] = ..., starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., starts_in: _Optional[int] = ..., ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ends_in: _Optional[int] = ..., duration: _Optional[int] = ..., status: _Optional[_Union[Contest.Status, str]] = ..., visibility: _Optional[_Union[Contest.Visibility, str]] = ..., join_unofficially: bool = ..., participation_mode: _Optional[_Union[Contest.ParticipationMode, str]] = ..., format: _Optional[_Union[Contest.Format, str]] = ..., key: _Optional[str] = ..., problem_count: _Optional[int] = ..., problem_count_hidden: bool = ..., participant_count: _Optional[int] = ..., participant_count_hidden: bool = ..., featured_until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., printer_id: _Optional[str] = ..., taxonomy: _Optional[_Union[Contest.Taxonomy, _Mapping]] = ..., appearance: _Optional[_Union[Contest.Appearance, _Mapping]] = ..., environment: _Optional[_Union[Contest.Environment, _Mapping]] = ..., upsolve: _Optional[_Union[Contest.Upsolve, _Mapping]] = ..., scoreboard: _Optional[_Union[Contest.Scoreboard, _Mapping]] = ...) -> None: ...
