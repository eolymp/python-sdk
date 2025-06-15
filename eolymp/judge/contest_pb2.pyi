from eolymp.judge import contest_taxonomy_pb2 as _contest_taxonomy_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Contest(_message.Message):
    __slots__ = ("id", "url", "name", "image_url", "starts_at", "starts_in", "ends_at", "ends_in", "duration", "status", "visibility", "join_unofficially", "participation_mode", "require_admission", "allow_pause", "allow_finish_early", "allow_upsolve", "allow_followup", "format", "key", "problem_count", "problem_count_hidden", "participant_count", "participant_count_hidden", "featured_until", "printer_id", "scoreboard", "taxonomy")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[Contest.Patch]
        NAME: _ClassVar[Contest.Patch]
        STARTS_AT: _ClassVar[Contest.Patch]
        ENDS_AT: _ClassVar[Contest.Patch]
        DURATION: _ClassVar[Contest.Patch]
        VISIBILITY: _ClassVar[Contest.Patch]
        JOIN_UNOFFICIALLY: _ClassVar[Contest.Patch]
        REQUIRE_ADMISSION: _ClassVar[Contest.Patch]
        ALLOW_PAUSE: _ClassVar[Contest.Patch]
        ALLOW_FINISH_EARLY: _ClassVar[Contest.Patch]
        ALLOW_UPSOLVE: _ClassVar[Contest.Patch]
        ALLOW_FOLLOWUP: _ClassVar[Contest.Patch]
        PARTICIPATION_MODE: _ClassVar[Contest.Patch]
        FORMAT: _ClassVar[Contest.Patch]
        KEY: _ClassVar[Contest.Patch]
        IMAGE_URL: _ClassVar[Contest.Patch]
        PROBLEM_COUNT_HIDDEN: _ClassVar[Contest.Patch]
        PARTICIPANT_COUNT_HIDDEN: _ClassVar[Contest.Patch]
        FEATURED_UNTIL: _ClassVar[Contest.Patch]
        PRINTER: _ClassVar[Contest.Patch]
        SCOREBOARD: _ClassVar[Contest.Patch]
    ALL: Contest.Patch
    NAME: Contest.Patch
    STARTS_AT: Contest.Patch
    ENDS_AT: Contest.Patch
    DURATION: Contest.Patch
    VISIBILITY: Contest.Patch
    JOIN_UNOFFICIALLY: Contest.Patch
    REQUIRE_ADMISSION: Contest.Patch
    ALLOW_PAUSE: Contest.Patch
    ALLOW_FINISH_EARLY: Contest.Patch
    ALLOW_UPSOLVE: Contest.Patch
    ALLOW_FOLLOWUP: Contest.Patch
    PARTICIPATION_MODE: Contest.Patch
    FORMAT: Contest.Patch
    KEY: Contest.Patch
    IMAGE_URL: Contest.Patch
    PROBLEM_COUNT_HIDDEN: Contest.Patch
    PARTICIPANT_COUNT_HIDDEN: Contest.Patch
    FEATURED_UNTIL: Contest.Patch
    PRINTER: Contest.Patch
    SCOREBOARD: Contest.Patch
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Contest.Extra]
        TAXONOMY: _ClassVar[Contest.Extra]
    UNKNOWN_EXTRA: Contest.Extra
    TAXONOMY: Contest.Extra
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
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    STARTS_IN_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_IN_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    JOIN_UNOFFICIALLY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPATION_MODE_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_ADMISSION_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PAUSE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FINISH_EARLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UPSOLVE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FOLLOWUP_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_COUNT_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_COUNT_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    FEATURED_UNTIL_FIELD_NUMBER: _ClassVar[int]
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    name: str
    image_url: str
    starts_at: _timestamp_pb2.Timestamp
    starts_in: int
    ends_at: _timestamp_pb2.Timestamp
    ends_in: int
    duration: int
    status: Contest.Status
    visibility: Contest.Visibility
    join_unofficially: bool
    participation_mode: Contest.ParticipationMode
    require_admission: bool
    allow_pause: bool
    allow_finish_early: bool
    allow_upsolve: bool
    allow_followup: bool
    format: Contest.Format
    key: str
    problem_count: int
    problem_count_hidden: bool
    participant_count: int
    participant_count_hidden: bool
    featured_until: _timestamp_pb2.Timestamp
    printer_id: str
    scoreboard: Contest.Scoreboard
    taxonomy: _contest_taxonomy_pb2.Taxonomy
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., starts_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., starts_in: _Optional[int] = ..., ends_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., ends_in: _Optional[int] = ..., duration: _Optional[int] = ..., status: _Optional[_Union[Contest.Status, str]] = ..., visibility: _Optional[_Union[Contest.Visibility, str]] = ..., join_unofficially: bool = ..., participation_mode: _Optional[_Union[Contest.ParticipationMode, str]] = ..., require_admission: bool = ..., allow_pause: bool = ..., allow_finish_early: bool = ..., allow_upsolve: bool = ..., allow_followup: bool = ..., format: _Optional[_Union[Contest.Format, str]] = ..., key: _Optional[str] = ..., problem_count: _Optional[int] = ..., problem_count_hidden: bool = ..., participant_count: _Optional[int] = ..., participant_count_hidden: bool = ..., featured_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., printer_id: _Optional[str] = ..., scoreboard: _Optional[_Union[Contest.Scoreboard, _Mapping]] = ..., taxonomy: _Optional[_Union[_contest_taxonomy_pb2.Taxonomy, _Mapping]] = ...) -> None: ...
