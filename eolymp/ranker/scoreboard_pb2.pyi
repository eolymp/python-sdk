from eolymp.ranker import format_pb2 as _format_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Scoreboard(_message.Message):
    __slots__ = ["format", "frozen", "id", "key", "name", "timeline"]
    class FetchingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Column(_message.Message):
        __slots__ = ["columns", "community_attribute_key", "community_attribute_type", "filterable", "id", "index", "judge_contest_id", "judge_problem_id", "key", "name", "parent_id", "short_name", "timeline_duration", "timeline_enabled", "timeline_freeze_time", "timeline_offset", "type", "visible"]
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ATTRIBUTE: Scoreboard.Column.Type
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        COMMUNITY_ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
        COMMUNITY_ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTEST: Scoreboard.Column.Type
        FILTERABLE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        JUDGE_CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
        JUDGE_PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        NAME: Scoreboard.Column.Type
        NAME_FIELD_NUMBER: _ClassVar[int]
        NONE: Scoreboard.Column.Type
        PARENT_ID_FIELD_NUMBER: _ClassVar[int]
        PROBLEM: Scoreboard.Column.Type
        SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
        TIMELINE_DURATION_FIELD_NUMBER: _ClassVar[int]
        TIMELINE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        TIMELINE_FREEZE_TIME_FIELD_NUMBER: _ClassVar[int]
        TIMELINE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VISIBLE_FIELD_NUMBER: _ClassVar[int]
        columns: _containers.RepeatedCompositeFieldContainer[Scoreboard.Column]
        community_attribute_key: str
        community_attribute_type: str
        filterable: bool
        id: str
        index: int
        judge_contest_id: str
        judge_problem_id: str
        key: str
        name: str
        parent_id: str
        short_name: str
        timeline_duration: int
        timeline_enabled: bool
        timeline_freeze_time: int
        timeline_offset: int
        type: Scoreboard.Column.Type
        visible: bool
        def __init__(self, id: _Optional[str] = ..., parent_id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., short_name: _Optional[str] = ..., type: _Optional[_Union[Scoreboard.Column.Type, str]] = ..., index: _Optional[int] = ..., visible: bool = ..., filterable: bool = ..., timeline_enabled: bool = ..., timeline_offset: _Optional[int] = ..., timeline_duration: _Optional[int] = ..., timeline_freeze_time: _Optional[int] = ..., judge_contest_id: _Optional[str] = ..., judge_problem_id: _Optional[str] = ..., community_attribute_key: _Optional[str] = ..., community_attribute_type: _Optional[str] = ..., columns: _Optional[_Iterable[_Union[Scoreboard.Column, _Mapping]]] = ...) -> None: ...
    class Row(_message.Message):
        __slots__ = ["ghost", "id", "member_id", "name", "out_of_competition", "penalty", "rank", "rank_lower", "score", "values"]
        class Value(_message.Message):
            __slots__ = ["attempts", "column_id", "id", "penalty", "percentage", "score", "solved_in", "timeline_latest", "timeline_offset_end", "timeline_offset_start", "timeline_set", "value_number", "value_string"]
            ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
            COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            PENALTY_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            SCORE_FIELD_NUMBER: _ClassVar[int]
            SOLVED_IN_FIELD_NUMBER: _ClassVar[int]
            TIMELINE_LATEST_FIELD_NUMBER: _ClassVar[int]
            TIMELINE_OFFSET_END_FIELD_NUMBER: _ClassVar[int]
            TIMELINE_OFFSET_START_FIELD_NUMBER: _ClassVar[int]
            TIMELINE_SET_FIELD_NUMBER: _ClassVar[int]
            VALUE_NUMBER_FIELD_NUMBER: _ClassVar[int]
            VALUE_STRING_FIELD_NUMBER: _ClassVar[int]
            attempts: int
            column_id: str
            id: str
            penalty: float
            percentage: float
            score: float
            solved_in: int
            timeline_latest: bool
            timeline_offset_end: int
            timeline_offset_start: int
            timeline_set: bool
            value_number: int
            value_string: str
            def __init__(self, id: _Optional[str] = ..., column_id: _Optional[str] = ..., timeline_set: bool = ..., timeline_latest: bool = ..., timeline_offset_start: _Optional[int] = ..., timeline_offset_end: _Optional[int] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., percentage: _Optional[float] = ..., attempts: _Optional[int] = ..., solved_in: _Optional[int] = ..., value_string: _Optional[str] = ..., value_number: _Optional[int] = ...) -> None: ...
        GHOST_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OUT_OF_COMPETITION_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        RANK_LOWER_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        ghost: bool
        id: str
        member_id: str
        name: str
        out_of_competition: bool
        penalty: float
        rank: int
        rank_lower: int
        score: float
        values: _containers.RepeatedCompositeFieldContainer[Scoreboard.Row.Value]
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., member_id: _Optional[str] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., ghost: bool = ..., out_of_competition: bool = ..., rank: _Optional[int] = ..., rank_lower: _Optional[int] = ..., values: _Optional[_Iterable[_Union[Scoreboard.Row.Value, _Mapping]]] = ...) -> None: ...
    class Timeline(_message.Message):
        __slots__ = ["duration", "freeze_time", "starts_at"]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        FREEZE_TIME_FIELD_NUMBER: _ClassVar[int]
        STARTS_AT_FIELD_NUMBER: _ClassVar[int]
        duration: int
        freeze_time: int
        starts_at: _timestamp_pb2.Timestamp
        def __init__(self, starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., freeze_time: _Optional[int] = ...) -> None: ...
    ACTUAL: Scoreboard.FetchingMode
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FROZEN: Scoreboard.FetchingMode
    FROZEN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LATEST: Scoreboard.FetchingMode
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUNCTUAL: Scoreboard.FetchingMode
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    format: _format_pb2.Format
    frozen: bool
    id: str
    key: str
    name: str
    timeline: _containers.RepeatedCompositeFieldContainer[Scoreboard.Timeline]
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., frozen: bool = ..., timeline: _Optional[_Iterable[_Union[Scoreboard.Timeline, _Mapping]]] = ..., format: _Optional[_Union[_format_pb2.Format, str]] = ...) -> None: ...
