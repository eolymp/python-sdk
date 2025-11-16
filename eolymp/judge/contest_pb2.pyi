import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.runtime import runtime_pb2 as _runtime_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Contest(_message.Message):
    __slots__ = ("id", "url", "name", "image_url", "starts_at", "ends_at", "duration", "status", "visibility", "participation_mode", "join_unofficially", "require_admission", "allow_pause", "allow_finish_early", "allow_upsolve", "allow_followup", "display_editorials", "format", "key", "problem_count", "problem_count_hidden", "participant_count", "participant_count_hidden", "featured_until", "printer_id", "classification", "scoreboard_config", "environment_config", "certification_config", "plagiarism_config", "rating_config", "staff")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNKNOWN: _ClassVar[Contest.Status]
        SCHEDULED: _ClassVar[Contest.Status]
        OPEN: _ClassVar[Contest.Status]
        COMPLETE: _ClassVar[Contest.Status]
        SUSPENDED: _ClassVar[Contest.Status]
        FROZEN: _ClassVar[Contest.Status]
        FINALIZED: _ClassVar[Contest.Status]
    STATUS_UNKNOWN: Contest.Status
    SCHEDULED: Contest.Status
    OPEN: Contest.Status
    COMPLETE: Contest.Status
    SUSPENDED: Contest.Status
    FROZEN: Contest.Status
    FINALIZED: Contest.Status
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
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[Contest.Patch.Field]
            NAME: _ClassVar[Contest.Patch.Field]
            IMAGE_URL: _ClassVar[Contest.Patch.Field]
            STARTS_AT: _ClassVar[Contest.Patch.Field]
            ENDS_AT: _ClassVar[Contest.Patch.Field]
            DURATION: _ClassVar[Contest.Patch.Field]
            VISIBILITY: _ClassVar[Contest.Patch.Field]
            JOIN_UNOFFICIALLY: _ClassVar[Contest.Patch.Field]
            PARTICIPATION_MODE: _ClassVar[Contest.Patch.Field]
            REQUIRE_ADMISSION: _ClassVar[Contest.Patch.Field]
            ALLOW_PAUSE: _ClassVar[Contest.Patch.Field]
            ALLOW_FINISH_EARLY: _ClassVar[Contest.Patch.Field]
            ALLOW_UPSOLVE: _ClassVar[Contest.Patch.Field]
            ALLOW_FOLLOWUP: _ClassVar[Contest.Patch.Field]
            DISPLAY_EDITORIALS: _ClassVar[Contest.Patch.Field]
            FORMAT: _ClassVar[Contest.Patch.Field]
            KEY: _ClassVar[Contest.Patch.Field]
            PROBLEM_COUNT_HIDDEN: _ClassVar[Contest.Patch.Field]
            PARTICIPANT_COUNT_HIDDEN: _ClassVar[Contest.Patch.Field]
            FEATURED_UNTIL: _ClassVar[Contest.Patch.Field]
            PRINTER: _ClassVar[Contest.Patch.Field]
            CLASSIFICATION: _ClassVar[Contest.Patch.Field]
            SCOREBOARD_CONFIG: _ClassVar[Contest.Patch.Field]
            CERTIFICATION_CONFIG: _ClassVar[Contest.Patch.Field]
            ENVIRONMENT_CONFIG: _ClassVar[Contest.Patch.Field]
            PLAGIARISM_CONFIG: _ClassVar[Contest.Patch.Field]
            RATING_CONFIG: _ClassVar[Contest.Patch.Field]
        UNKNOWN: Contest.Patch.Field
        NAME: Contest.Patch.Field
        IMAGE_URL: Contest.Patch.Field
        STARTS_AT: Contest.Patch.Field
        ENDS_AT: Contest.Patch.Field
        DURATION: Contest.Patch.Field
        VISIBILITY: Contest.Patch.Field
        JOIN_UNOFFICIALLY: Contest.Patch.Field
        PARTICIPATION_MODE: Contest.Patch.Field
        REQUIRE_ADMISSION: Contest.Patch.Field
        ALLOW_PAUSE: Contest.Patch.Field
        ALLOW_FINISH_EARLY: Contest.Patch.Field
        ALLOW_UPSOLVE: Contest.Patch.Field
        ALLOW_FOLLOWUP: Contest.Patch.Field
        DISPLAY_EDITORIALS: Contest.Patch.Field
        FORMAT: Contest.Patch.Field
        KEY: Contest.Patch.Field
        PROBLEM_COUNT_HIDDEN: Contest.Patch.Field
        PARTICIPANT_COUNT_HIDDEN: Contest.Patch.Field
        FEATURED_UNTIL: Contest.Patch.Field
        PRINTER: Contest.Patch.Field
        CLASSIFICATION: Contest.Patch.Field
        SCOREBOARD_CONFIG: Contest.Patch.Field
        CERTIFICATION_CONFIG: Contest.Patch.Field
        ENVIRONMENT_CONFIG: Contest.Patch.Field
        PLAGIARISM_CONFIG: Contest.Patch.Field
        RATING_CONFIG: Contest.Patch.Field
        def __init__(self) -> None: ...
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[Contest.Extra.Field]
            STAFF: _ClassVar[Contest.Extra.Field]
            CLASSIFICATION: _ClassVar[Contest.Extra.Field]
            SCOREBOARD_CONFIG: _ClassVar[Contest.Extra.Field]
            CERTIFICATION_CONFIG: _ClassVar[Contest.Extra.Field]
            ENVIRONMENT_CONFIG: _ClassVar[Contest.Extra.Field]
            PLAGIARISM_CONFIG: _ClassVar[Contest.Extra.Field]
            RATING_CONFIG: _ClassVar[Contest.Extra.Field]
        UNKNOWN: Contest.Extra.Field
        STAFF: Contest.Extra.Field
        CLASSIFICATION: Contest.Extra.Field
        SCOREBOARD_CONFIG: Contest.Extra.Field
        CERTIFICATION_CONFIG: Contest.Extra.Field
        ENVIRONMENT_CONFIG: Contest.Extra.Field
        PLAGIARISM_CONFIG: Contest.Extra.Field
        RATING_CONFIG: Contest.Extra.Field
        def __init__(self) -> None: ...
    class Classification(_message.Message):
        __slots__ = ("year", "series", "scale", "difficulty", "country", "region", "city")
        class Scale(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_SCALE: _ClassVar[Contest.Classification.Scale]
            LOCAL: _ClassVar[Contest.Classification.Scale]
            REGIONAL: _ClassVar[Contest.Classification.Scale]
            NATIONAL: _ClassVar[Contest.Classification.Scale]
            INTERNATIONAL: _ClassVar[Contest.Classification.Scale]
        UNKNOWN_SCALE: Contest.Classification.Scale
        LOCAL: Contest.Classification.Scale
        REGIONAL: Contest.Classification.Scale
        NATIONAL: Contest.Classification.Scale
        INTERNATIONAL: Contest.Classification.Scale
        YEAR_FIELD_NUMBER: _ClassVar[int]
        SERIES_FIELD_NUMBER: _ClassVar[int]
        SCALE_FIELD_NUMBER: _ClassVar[int]
        DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        CITY_FIELD_NUMBER: _ClassVar[int]
        year: int
        series: str
        scale: Contest.Classification.Scale
        difficulty: int
        country: str
        region: str
        city: str
        def __init__(self, year: _Optional[int] = ..., series: _Optional[str] = ..., scale: _Optional[_Union[Contest.Classification.Scale, str]] = ..., difficulty: _Optional[int] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...
    class ScoreboardConfig(_message.Message):
        __slots__ = ("visibility", "freezing_time", "unfreeze_delay", "attempt_penalty", "tie_breaker", "no_spoiler_ui", "share_key")
        class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_VISIBILITY: _ClassVar[Contest.ScoreboardConfig.Visibility]
            INVISIBLE: _ClassVar[Contest.ScoreboardConfig.Visibility]
            INTERNAL: _ClassVar[Contest.ScoreboardConfig.Visibility]
            PUBLIC: _ClassVar[Contest.ScoreboardConfig.Visibility]
        UNKNOWN_VISIBILITY: Contest.ScoreboardConfig.Visibility
        INVISIBLE: Contest.ScoreboardConfig.Visibility
        INTERNAL: Contest.ScoreboardConfig.Visibility
        PUBLIC: Contest.ScoreboardConfig.Visibility
        VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        FREEZING_TIME_FIELD_NUMBER: _ClassVar[int]
        UNFREEZE_DELAY_FIELD_NUMBER: _ClassVar[int]
        ATTEMPT_PENALTY_FIELD_NUMBER: _ClassVar[int]
        TIE_BREAKER_FIELD_NUMBER: _ClassVar[int]
        NO_SPOILER_UI_FIELD_NUMBER: _ClassVar[int]
        SHARE_KEY_FIELD_NUMBER: _ClassVar[int]
        visibility: Contest.ScoreboardConfig.Visibility
        freezing_time: int
        unfreeze_delay: int
        attempt_penalty: int
        tie_breaker: str
        no_spoiler_ui: bool
        share_key: str
        def __init__(self, visibility: _Optional[_Union[Contest.ScoreboardConfig.Visibility, str]] = ..., freezing_time: _Optional[int] = ..., unfreeze_delay: _Optional[int] = ..., attempt_penalty: _Optional[int] = ..., tie_breaker: _Optional[str] = ..., no_spoiler_ui: bool = ..., share_key: _Optional[str] = ...) -> None: ...
    class RatingConfig(_message.Message):
        __slots__ = ("rated", "max_rating")
        RATED_FIELD_NUMBER: _ClassVar[int]
        MAX_RATING_FIELD_NUMBER: _ClassVar[int]
        rated: bool
        max_rating: int
        def __init__(self, rated: bool = ..., max_rating: _Optional[int] = ...) -> None: ...
    class CertificationConfig(_message.Message):
        __slots__ = ("enabled", "affiliation", "signers")
        class Signer(_message.Message):
            __slots__ = ("name", "title")
            NAME_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            name: str
            title: str
            def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        AFFILIATION_FIELD_NUMBER: _ClassVar[int]
        SIGNERS_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        affiliation: str
        signers: _containers.RepeatedCompositeFieldContainer[Contest.CertificationConfig.Signer]
        def __init__(self, enabled: bool = ..., affiliation: _Optional[str] = ..., signers: _Optional[_Iterable[_Union[Contest.CertificationConfig.Signer, _Mapping]]] = ...) -> None: ...
    class EnvironmentConfig(_message.Message):
        __slots__ = ("runtimes",)
        RUNTIMES_FIELD_NUMBER: _ClassVar[int]
        runtimes: _containers.RepeatedCompositeFieldContainer[_runtime_pb2.Runtime]
        def __init__(self, runtimes: _Optional[_Iterable[_Union[_runtime_pb2.Runtime, _Mapping]]] = ...) -> None: ...
    class PlagiarismConfig(_message.Message):
        __slots__ = ("check_genai_use",)
        CHECK_GENAI_USE_FIELD_NUMBER: _ClassVar[int]
        check_genai_use: bool
        def __init__(self, check_genai_use: bool = ...) -> None: ...
    class Staff(_message.Message):
        __slots__ = ("member_id", "display_name", "role")
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        member_id: str
        display_name: str
        role: str
        def __init__(self, member_id: _Optional[str] = ..., display_name: _Optional[str] = ..., role: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPATION_MODE_FIELD_NUMBER: _ClassVar[int]
    JOIN_UNOFFICIALLY_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_ADMISSION_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PAUSE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FINISH_EARLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UPSOLVE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FOLLOWUP_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_EDITORIALS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_COUNT_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_COUNT_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    FEATURED_UNTIL_FIELD_NUMBER: _ClassVar[int]
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PLAGIARISM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RATING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STAFF_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    image_url: str
    starts_at: _timestamp_pb2.Timestamp
    ends_at: _timestamp_pb2.Timestamp
    duration: int
    status: Contest.Status
    visibility: Contest.Visibility
    participation_mode: Contest.ParticipationMode
    join_unofficially: bool
    require_admission: bool
    allow_pause: bool
    allow_finish_early: bool
    allow_upsolve: bool
    allow_followup: bool
    display_editorials: bool
    format: Contest.Format
    key: str
    problem_count: int
    problem_count_hidden: bool
    participant_count: int
    participant_count_hidden: bool
    featured_until: _timestamp_pb2.Timestamp
    printer_id: str
    classification: Contest.Classification
    scoreboard_config: Contest.ScoreboardConfig
    environment_config: Contest.EnvironmentConfig
    certification_config: Contest.CertificationConfig
    plagiarism_config: Contest.PlagiarismConfig
    rating_config: Contest.RatingConfig
    staff: _containers.RepeatedCompositeFieldContainer[Contest.Staff]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., starts_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ends_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., status: _Optional[_Union[Contest.Status, str]] = ..., visibility: _Optional[_Union[Contest.Visibility, str]] = ..., participation_mode: _Optional[_Union[Contest.ParticipationMode, str]] = ..., join_unofficially: bool = ..., require_admission: bool = ..., allow_pause: bool = ..., allow_finish_early: bool = ..., allow_upsolve: bool = ..., allow_followup: bool = ..., display_editorials: bool = ..., format: _Optional[_Union[Contest.Format, str]] = ..., key: _Optional[str] = ..., problem_count: _Optional[int] = ..., problem_count_hidden: bool = ..., participant_count: _Optional[int] = ..., participant_count_hidden: bool = ..., featured_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., printer_id: _Optional[str] = ..., classification: _Optional[_Union[Contest.Classification, _Mapping]] = ..., scoreboard_config: _Optional[_Union[Contest.ScoreboardConfig, _Mapping]] = ..., environment_config: _Optional[_Union[Contest.EnvironmentConfig, _Mapping]] = ..., certification_config: _Optional[_Union[Contest.CertificationConfig, _Mapping]] = ..., plagiarism_config: _Optional[_Union[Contest.PlagiarismConfig, _Mapping]] = ..., rating_config: _Optional[_Union[Contest.RatingConfig, _Mapping]] = ..., staff: _Optional[_Iterable[_Union[Contest.Staff, _Mapping]]] = ...) -> None: ...
