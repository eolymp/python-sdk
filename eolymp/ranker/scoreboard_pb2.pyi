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
    __slots__ = ("id", "key", "name", "historical", "frozen", "freeze_at", "freeze_in", "unfreeze_at", "unfreeze_in", "default_sort_column", "default_sort_order", "format")
    class FetchingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LATEST: _ClassVar[Scoreboard.FetchingMode]
        PUNCTUAL: _ClassVar[Scoreboard.FetchingMode]
        FROZEN: _ClassVar[Scoreboard.FetchingMode]
        UPSOLVE: _ClassVar[Scoreboard.FetchingMode]
    LATEST: Scoreboard.FetchingMode
    PUNCTUAL: Scoreboard.FetchingMode
    FROZEN: Scoreboard.FetchingMode
    UPSOLVE: Scoreboard.FetchingMode
    class Row(_message.Message):
        __slots__ = ("id", "name", "member_id", "score", "penalty", "ghost", "unofficial", "rank", "rank_lower", "values")
        class Value(_message.Message):
            __slots__ = ("id", "column_id", "valid_after", "valid_until", "score", "penalty", "percentage", "attempts", "solved_in", "upsolve", "value_string", "value_number")
            ID_FIELD_NUMBER: _ClassVar[int]
            COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
            VALID_AFTER_FIELD_NUMBER: _ClassVar[int]
            VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
            SCORE_FIELD_NUMBER: _ClassVar[int]
            PENALTY_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
            SOLVED_IN_FIELD_NUMBER: _ClassVar[int]
            UPSOLVE_FIELD_NUMBER: _ClassVar[int]
            VALUE_STRING_FIELD_NUMBER: _ClassVar[int]
            VALUE_NUMBER_FIELD_NUMBER: _ClassVar[int]
            id: str
            column_id: str
            valid_after: int
            valid_until: int
            score: float
            penalty: float
            percentage: float
            attempts: int
            solved_in: int
            upsolve: bool
            value_string: str
            value_number: int
            def __init__(self, id: _Optional[str] = ..., column_id: _Optional[str] = ..., valid_after: _Optional[int] = ..., valid_until: _Optional[int] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., percentage: _Optional[float] = ..., attempts: _Optional[int] = ..., solved_in: _Optional[int] = ..., upsolve: bool = ..., value_string: _Optional[str] = ..., value_number: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        GHOST_FIELD_NUMBER: _ClassVar[int]
        UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        RANK_LOWER_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        member_id: str
        score: float
        penalty: float
        ghost: bool
        unofficial: bool
        rank: int
        rank_lower: int
        values: _containers.RepeatedCompositeFieldContainer[Scoreboard.Row.Value]
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., member_id: _Optional[str] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., ghost: bool = ..., unofficial: bool = ..., rank: _Optional[int] = ..., rank_lower: _Optional[int] = ..., values: _Optional[_Iterable[_Union[Scoreboard.Row.Value, _Mapping]]] = ...) -> None: ...
    class Column(_message.Message):
        __slots__ = ("id", "parent_id", "key", "name", "short_name", "type", "index", "visible", "filterable", "sortable", "judge_contest_id", "judge_problem_id", "community_attribute_key", "community_attribute_type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NONE: _ClassVar[Scoreboard.Column.Type]
            CONTEST: _ClassVar[Scoreboard.Column.Type]
            PROBLEM: _ClassVar[Scoreboard.Column.Type]
            ATTRIBUTE: _ClassVar[Scoreboard.Column.Type]
            NAME: _ClassVar[Scoreboard.Column.Type]
            TOTAL: _ClassVar[Scoreboard.Column.Type]
        NONE: Scoreboard.Column.Type
        CONTEST: Scoreboard.Column.Type
        PROBLEM: Scoreboard.Column.Type
        ATTRIBUTE: Scoreboard.Column.Type
        NAME: Scoreboard.Column.Type
        TOTAL: Scoreboard.Column.Type
        ID_FIELD_NUMBER: _ClassVar[int]
        PARENT_ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        VISIBLE_FIELD_NUMBER: _ClassVar[int]
        FILTERABLE_FIELD_NUMBER: _ClassVar[int]
        SORTABLE_FIELD_NUMBER: _ClassVar[int]
        JUDGE_CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
        JUDGE_PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        COMMUNITY_ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
        COMMUNITY_ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        parent_id: str
        key: str
        name: str
        short_name: str
        type: Scoreboard.Column.Type
        index: int
        visible: bool
        filterable: bool
        sortable: bool
        judge_contest_id: str
        judge_problem_id: str
        community_attribute_key: str
        community_attribute_type: str
        def __init__(self, id: _Optional[str] = ..., parent_id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., short_name: _Optional[str] = ..., type: _Optional[_Union[Scoreboard.Column.Type, str]] = ..., index: _Optional[int] = ..., visible: bool = ..., filterable: bool = ..., sortable: bool = ..., judge_contest_id: _Optional[str] = ..., judge_problem_id: _Optional[str] = ..., community_attribute_key: _Optional[str] = ..., community_attribute_type: _Optional[str] = ...) -> None: ...
    class Action(_message.Message):
        __slots__ = ("id", "execute_at", "type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NONE: _ClassVar[Scoreboard.Action.Type]
            FREEZE: _ClassVar[Scoreboard.Action.Type]
            UNFREEZE: _ClassVar[Scoreboard.Action.Type]
        NONE: Scoreboard.Action.Type
        FREEZE: Scoreboard.Action.Type
        UNFREEZE: Scoreboard.Action.Type
        ID_FIELD_NUMBER: _ClassVar[int]
        EXECUTE_AT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        execute_at: _timestamp_pb2.Timestamp
        type: Scoreboard.Action.Type
        def __init__(self, id: _Optional[str] = ..., execute_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[_Union[Scoreboard.Action.Type, str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HISTORICAL_FIELD_NUMBER: _ClassVar[int]
    FROZEN_FIELD_NUMBER: _ClassVar[int]
    FREEZE_AT_FIELD_NUMBER: _ClassVar[int]
    FREEZE_IN_FIELD_NUMBER: _ClassVar[int]
    UNFREEZE_AT_FIELD_NUMBER: _ClassVar[int]
    UNFREEZE_IN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SORT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    name: str
    historical: bool
    frozen: bool
    freeze_at: _timestamp_pb2.Timestamp
    freeze_in: int
    unfreeze_at: _timestamp_pb2.Timestamp
    unfreeze_in: int
    default_sort_column: str
    default_sort_order: _direction_pb2.Direction
    format: _format_pb2.Format
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., historical: bool = ..., frozen: bool = ..., freeze_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., freeze_in: _Optional[int] = ..., unfreeze_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., unfreeze_in: _Optional[int] = ..., default_sort_column: _Optional[str] = ..., default_sort_order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., format: _Optional[_Union[_format_pb2.Format, str]] = ...) -> None: ...
