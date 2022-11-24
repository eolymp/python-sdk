from eolymp.ranker import format_pb2 as _format_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Scoreboard(_message.Message):
    __slots__ = ["default_sort_column", "default_sort_order", "format", "historical", "id", "key", "name", "timeline"]
    class FetchingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Column(_message.Message):
        __slots__ = ["community_attribute_key", "community_attribute_type", "filterable", "id", "index", "judge_contest_id", "judge_problem_id", "key", "name", "parent_id", "short_name", "sortable", "type", "visible"]
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ATTRIBUTE: Scoreboard.Column.Type
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
        SORTABLE_FIELD_NUMBER: _ClassVar[int]
        TOTAL: Scoreboard.Column.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VISIBLE_FIELD_NUMBER: _ClassVar[int]
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
        sortable: bool
        type: Scoreboard.Column.Type
        visible: bool
        def __init__(self, id: _Optional[str] = ..., parent_id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., short_name: _Optional[str] = ..., type: _Optional[_Union[Scoreboard.Column.Type, str]] = ..., index: _Optional[int] = ..., visible: bool = ..., filterable: bool = ..., sortable: bool = ..., judge_contest_id: _Optional[str] = ..., judge_problem_id: _Optional[str] = ..., community_attribute_key: _Optional[str] = ..., community_attribute_type: _Optional[str] = ...) -> None: ...
    class Row(_message.Message):
        __slots__ = ["ghost", "id", "member_id", "name", "out_of_competition", "penalty", "rank", "rank_lower", "score", "values"]
        class Value(_message.Message):
            __slots__ = ["attempts", "column_id", "id", "penalty", "percentage", "score", "solved_in", "timeline_end_offset", "timeline_start_offset", "value_number", "value_string"]
            ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
            COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            PENALTY_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            SCORE_FIELD_NUMBER: _ClassVar[int]
            SOLVED_IN_FIELD_NUMBER: _ClassVar[int]
            TIMELINE_END_OFFSET_FIELD_NUMBER: _ClassVar[int]
            TIMELINE_START_OFFSET_FIELD_NUMBER: _ClassVar[int]
            VALUE_NUMBER_FIELD_NUMBER: _ClassVar[int]
            VALUE_STRING_FIELD_NUMBER: _ClassVar[int]
            attempts: int
            column_id: str
            id: str
            penalty: float
            percentage: float
            score: float
            solved_in: int
            timeline_end_offset: int
            timeline_start_offset: int
            value_number: int
            value_string: str
            def __init__(self, id: _Optional[str] = ..., column_id: _Optional[str] = ..., timeline_start_offset: _Optional[int] = ..., timeline_end_offset: _Optional[int] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., percentage: _Optional[float] = ..., attempts: _Optional[int] = ..., solved_in: _Optional[int] = ..., value_string: _Optional[str] = ..., value_number: _Optional[int] = ...) -> None: ...
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
    class Segment(_message.Message):
        __slots__ = ["end_offset", "freeze_time", "start_offset", "starts_at"]
        END_OFFSET_FIELD_NUMBER: _ClassVar[int]
        FREEZE_TIME_FIELD_NUMBER: _ClassVar[int]
        STARTS_AT_FIELD_NUMBER: _ClassVar[int]
        START_OFFSET_FIELD_NUMBER: _ClassVar[int]
        end_offset: int
        freeze_time: int
        start_offset: int
        starts_at: _timestamp_pb2.Timestamp
        def __init__(self, starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ..., freeze_time: _Optional[int] = ...) -> None: ...
    class Timeline(_message.Message):
        __slots__ = ["duration", "freeze_in", "frozen", "position", "segments", "unfreeze_in"]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        FREEZE_IN_FIELD_NUMBER: _ClassVar[int]
        FROZEN_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        UNFREEZE_IN_FIELD_NUMBER: _ClassVar[int]
        duration: int
        freeze_in: int
        frozen: bool
        position: int
        segments: _containers.RepeatedCompositeFieldContainer[Scoreboard.Segment]
        unfreeze_in: int
        def __init__(self, position: _Optional[int] = ..., duration: _Optional[int] = ..., frozen: bool = ..., freeze_in: _Optional[int] = ..., unfreeze_in: _Optional[int] = ..., segments: _Optional[_Iterable[_Union[Scoreboard.Segment, _Mapping]]] = ...) -> None: ...
    ACTUAL: Scoreboard.FetchingMode
    DEFAULT_SORT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FROZEN: Scoreboard.FetchingMode
    HISTORICAL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LATEST: Scoreboard.FetchingMode
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUNCTUAL: Scoreboard.FetchingMode
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    default_sort_column: str
    default_sort_order: _direction_pb2.Direction
    format: _format_pb2.Format
    historical: bool
    id: str
    key: str
    name: str
    timeline: Scoreboard.Timeline
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., historical: bool = ..., timeline: _Optional[_Union[Scoreboard.Timeline, _Mapping]] = ..., default_sort_column: _Optional[str] = ..., default_sort_order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., format: _Optional[_Union[_format_pb2.Format, str]] = ...) -> None: ...
