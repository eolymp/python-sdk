from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Contest(_message.Message):
    __slots__ = ["domain", "duration", "ends_at", "ends_in", "ern", "format", "id", "name", "participation_mode", "space_id", "starts_at", "starts_in", "status", "url", "visibility"]
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ParticipationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Appearance(_message.Message):
        __slots__ = ["logo_image", "primary_color", "secondary_color", "tagline", "title"]
        LOGO_IMAGE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
        TAGLINE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        logo_image: str
        primary_color: str
        secondary_color: str
        tagline: str
        title: str
        def __init__(self, title: _Optional[str] = ..., tagline: _Optional[str] = ..., logo_image: _Optional[str] = ..., primary_color: _Optional[str] = ..., secondary_color: _Optional[str] = ...) -> None: ...
    class Scoring(_message.Message):
        __slots__ = ["allow_upsolving", "attempt_penalty", "freezing_time", "show_scoreboard"]
        ALLOW_UPSOLVING_FIELD_NUMBER: _ClassVar[int]
        ATTEMPT_PENALTY_FIELD_NUMBER: _ClassVar[int]
        FREEZING_TIME_FIELD_NUMBER: _ClassVar[int]
        SHOW_SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
        allow_upsolving: bool
        attempt_penalty: int
        freezing_time: int
        show_scoreboard: bool
        def __init__(self, show_scoreboard: bool = ..., attempt_penalty: _Optional[int] = ..., freezing_time: _Optional[int] = ..., allow_upsolving: bool = ...) -> None: ...
    COMPLETE: Contest.Status
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_IN_FIELD_NUMBER: _ClassVar[int]
    ERN_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    ICPC: Contest.Format
    ID_FIELD_NUMBER: _ClassVar[int]
    IOI: Contest.Format
    NAME_FIELD_NUMBER: _ClassVar[int]
    NO_FORMAT: Contest.Format
    NO_PARTICIPATION: Contest.ParticipationMode
    NO_STATUS: Contest.Status
    NO_VISIBILITY: Contest.Visibility
    ONLINE: Contest.ParticipationMode
    OPEN: Contest.Status
    PARTICIPATION_MODE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE: Contest.Visibility
    PUBLIC: Contest.Visibility
    SCHEDULED: Contest.Status
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    STARTS_IN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNLISTED: Contest.Visibility
    URL_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL: Contest.ParticipationMode
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    duration: int
    ends_at: _timestamp_pb2.Timestamp
    ends_in: int
    ern: str
    format: Contest.Format
    id: str
    name: str
    participation_mode: Contest.ParticipationMode
    space_id: str
    starts_at: _timestamp_pb2.Timestamp
    starts_in: int
    status: Contest.Status
    url: str
    visibility: Contest.Visibility
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., ern: _Optional[str] = ..., name: _Optional[str] = ..., starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., starts_in: _Optional[int] = ..., ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ends_in: _Optional[int] = ..., duration: _Optional[int] = ..., status: _Optional[_Union[Contest.Status, str]] = ..., visibility: _Optional[_Union[Contest.Visibility, str]] = ..., participation_mode: _Optional[_Union[Contest.ParticipationMode, str]] = ..., format: _Optional[_Union[Contest.Format, str]] = ..., domain: _Optional[str] = ..., space_id: _Optional[str] = ...) -> None: ...
