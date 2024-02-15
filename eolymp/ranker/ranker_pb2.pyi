from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.ranker import activity_pb2 as _activity_pb2
from eolymp.ranker import scoreboard_pb2 as _scoreboard_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddScoreboardColumnInput(_message.Message):
    __slots__ = ["column", "scoreboard_id"]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    column: _scoreboard_pb2.Scoreboard.Column
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., column: _Optional[_Union[_scoreboard_pb2.Scoreboard.Column, _Mapping]] = ...) -> None: ...

class AddScoreboardColumnOutput(_message.Message):
    __slots__ = ["column_id"]
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    column_id: str
    def __init__(self, column_id: _Optional[str] = ...) -> None: ...

class CreateScoreboardInput(_message.Message):
    __slots__ = ["add_default_columns", "duplicate_scoreboard_id", "scoreboard"]
    ADD_DEFAULT_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    add_default_columns: bool
    duplicate_scoreboard_id: str
    scoreboard: _scoreboard_pb2.Scoreboard
    def __init__(self, scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ..., add_default_columns: bool = ..., duplicate_scoreboard_id: _Optional[str] = ...) -> None: ...

class CreateScoreboardOutput(_message.Message):
    __slots__ = ["scoreboard_id"]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class DeleteScoreboardColumnInput(_message.Message):
    __slots__ = ["column_id", "scoreboard_id"]
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    column_id: str
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., column_id: _Optional[str] = ...) -> None: ...

class DeleteScoreboardColumnOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteScoreboardInput(_message.Message):
    __slots__ = ["scoreboard_id"]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class DeleteScoreboardOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeScoreboardColumnInput(_message.Message):
    __slots__ = ["column_id", "scoreboard_id"]
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    column_id: str
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., column_id: _Optional[str] = ...) -> None: ...

class DescribeScoreboardColumnOutput(_message.Message):
    __slots__ = ["column"]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    column: _scoreboard_pb2.Scoreboard.Column
    def __init__(self, column: _Optional[_Union[_scoreboard_pb2.Scoreboard.Column, _Mapping]] = ...) -> None: ...

class DescribeScoreboardInput(_message.Message):
    __slots__ = ["scoreboard_id", "scoreboard_key"]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_KEY_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    scoreboard_key: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., scoreboard_key: _Optional[str] = ...) -> None: ...

class DescribeScoreboardOutput(_message.Message):
    __slots__ = ["scoreboard"]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    scoreboard: _scoreboard_pb2.Scoreboard
    def __init__(self, scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ...) -> None: ...

class DescribeScoreboardRowInput(_message.Message):
    __slots__ = ["member_id", "mode", "punctual_time", "scoreboard_id"]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    PUNCTUAL_TIME_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    mode: _scoreboard_pb2.Scoreboard.FetchingMode
    punctual_time: int
    scoreboard_id: str
    def __init__(self, mode: _Optional[_Union[_scoreboard_pb2.Scoreboard.FetchingMode, str]] = ..., punctual_time: _Optional[int] = ..., scoreboard_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class DescribeScoreboardRowOutput(_message.Message):
    __slots__ = ["frozen", "row"]
    FROZEN_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    frozen: bool
    row: _scoreboard_pb2.Scoreboard.Row
    def __init__(self, row: _Optional[_Union[_scoreboard_pb2.Scoreboard.Row, _Mapping]] = ..., frozen: bool = ...) -> None: ...

class ListActivitiesInput(_message.Message):
    __slots__ = ["offset", "scoreboard_id", "size"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    scoreboard_id: str
    size: int
    def __init__(self, scoreboard_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListActivitiesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_activity_pb2.Activity]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_activity_pb2.Activity, _Mapping]]] = ...) -> None: ...

class ListScheduledActionsInput(_message.Message):
    __slots__ = ["scoreboard_id"]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class ListScheduledActionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Scoreboard.Action]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard.Action, _Mapping]]] = ...) -> None: ...

class ListScoreboardColumnsInput(_message.Message):
    __slots__ = ["scoreboard_id"]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class ListScoreboardColumnsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Scoreboard.Column]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard.Column, _Mapping]]] = ...) -> None: ...

class ListScoreboardRowsInput(_message.Message):
    __slots__ = ["filters", "mode", "offset", "order", "punctual_time", "scoreboard_id", "size", "sort"]
    class ExpressionColumn(_message.Message):
        __slots__ = ["enum", "key", "number", "string"]
        ENUM_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        STRING_FIELD_NUMBER: _ClassVar[int]
        enum: _expression_pb2.ExpressionEnum
        key: str
        number: _expression_pb2.ExpressionInt
        string: _expression_pb2.ExpressionString
        def __init__(self, key: _Optional[str] = ..., string: _Optional[_Union[_expression_pb2.ExpressionString, _Mapping]] = ..., number: _Optional[_Union[_expression_pb2.ExpressionInt, _Mapping]] = ..., enum: _Optional[_Union[_expression_pb2.ExpressionEnum, _Mapping]] = ...) -> None: ...
    class Filter(_message.Message):
        __slots__ = ["column", "member_id"]
        COLUMN_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        column: _containers.RepeatedCompositeFieldContainer[ListScoreboardRowsInput.ExpressionColumn]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., column: _Optional[_Iterable[_Union[ListScoreboardRowsInput.ExpressionColumn, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PUNCTUAL_TIME_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    filters: ListScoreboardRowsInput.Filter
    mode: _scoreboard_pb2.Scoreboard.FetchingMode
    offset: int
    order: _direction_pb2.Direction
    punctual_time: int
    scoreboard_id: str
    size: int
    sort: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., mode: _Optional[_Union[_scoreboard_pb2.Scoreboard.FetchingMode, str]] = ..., punctual_time: _Optional[int] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListScoreboardRowsInput.Filter, _Mapping]] = ..., sort: _Optional[str] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListScoreboardRowsOutput(_message.Message):
    __slots__ = ["frozen", "items", "total"]
    FROZEN_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    frozen: bool
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Scoreboard.Row]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard.Row, _Mapping]]] = ..., frozen: bool = ...) -> None: ...

class ListScoreboardsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListScoreboardsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListScoreboardsInput.Filter, _Mapping]] = ...) -> None: ...

class ListScoreboardsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Scoreboard]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard, _Mapping]]] = ...) -> None: ...

class RebuildScoreboardInput(_message.Message):
    __slots__ = ["scoreboard_id"]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class RebuildScoreboardOutput(_message.Message):
    __slots__ = ["activity_id"]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    def __init__(self, activity_id: _Optional[str] = ...) -> None: ...

class ScheduleActionInput(_message.Message):
    __slots__ = ["action", "scoreboard_id"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    action: _scoreboard_pb2.Scoreboard.Action
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., action: _Optional[_Union[_scoreboard_pb2.Scoreboard.Action, _Mapping]] = ...) -> None: ...

class ScheduleActionOutput(_message.Message):
    __slots__ = ["action_id"]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    def __init__(self, action_id: _Optional[str] = ...) -> None: ...

class UnscheduleActionInput(_message.Message):
    __slots__ = ["action_id", "scoreboard_id"]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., action_id: _Optional[str] = ...) -> None: ...

class UnscheduleActionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateScoreboardColumnInput(_message.Message):
    __slots__ = ["column", "column_id", "patch", "scoreboard_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateScoreboardColumnInput.Patch
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    FILTERABLE: UpdateScoreboardColumnInput.Patch
    INDEX: UpdateScoreboardColumnInput.Patch
    KEY: UpdateScoreboardColumnInput.Patch
    NAME: UpdateScoreboardColumnInput.Patch
    PARENT_ID: UpdateScoreboardColumnInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SHORT_NAME: UpdateScoreboardColumnInput.Patch
    SORTABLE: UpdateScoreboardColumnInput.Patch
    VISIBLE: UpdateScoreboardColumnInput.Patch
    column: _scoreboard_pb2.Scoreboard.Column
    column_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateScoreboardColumnInput.Patch]
    scoreboard_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateScoreboardColumnInput.Patch, str]]] = ..., scoreboard_id: _Optional[str] = ..., column_id: _Optional[str] = ..., column: _Optional[_Union[_scoreboard_pb2.Scoreboard.Column, _Mapping]] = ...) -> None: ...

class UpdateScoreboardColumnOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateScoreboardInput(_message.Message):
    __slots__ = ["patch", "scoreboard", "scoreboard_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateScoreboardInput.Patch
    DEFAULT_SORT: UpdateScoreboardInput.Patch
    HISTORICAL: UpdateScoreboardInput.Patch
    KEY: UpdateScoreboardInput.Patch
    NAME: UpdateScoreboardInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateScoreboardInput.Patch]
    scoreboard: _scoreboard_pb2.Scoreboard
    scoreboard_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateScoreboardInput.Patch, str]]] = ..., scoreboard_id: _Optional[str] = ..., scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ...) -> None: ...

class UpdateScoreboardOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
