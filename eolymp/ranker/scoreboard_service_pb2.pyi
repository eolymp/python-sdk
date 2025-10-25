from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.ranker import scoreboard_pb2 as _scoreboard_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateScoreboardInput(_message.Message):
    __slots__ = ("scoreboard", "add_default_columns", "duplicate_scoreboard_id")
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    ADD_DEFAULT_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard: _scoreboard_pb2.Scoreboard
    add_default_columns: bool
    duplicate_scoreboard_id: str
    def __init__(self, scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ..., add_default_columns: bool = ..., duplicate_scoreboard_id: _Optional[str] = ...) -> None: ...

class CreateScoreboardOutput(_message.Message):
    __slots__ = ("scoreboard_id",)
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class UpdateScoreboardInput(_message.Message):
    __slots__ = ("patch", "scoreboard_id", "scoreboard")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateScoreboardInput.Patch]
        KEY: _ClassVar[UpdateScoreboardInput.Patch]
        NAME: _ClassVar[UpdateScoreboardInput.Patch]
        DEFAULT_SORT: _ClassVar[UpdateScoreboardInput.Patch]
        HISTORICAL: _ClassVar[UpdateScoreboardInput.Patch]
    ALL: UpdateScoreboardInput.Patch
    KEY: UpdateScoreboardInput.Patch
    NAME: UpdateScoreboardInput.Patch
    DEFAULT_SORT: UpdateScoreboardInput.Patch
    HISTORICAL: UpdateScoreboardInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateScoreboardInput.Patch]
    scoreboard_id: str
    scoreboard: _scoreboard_pb2.Scoreboard
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateScoreboardInput.Patch, str]]] = ..., scoreboard_id: _Optional[str] = ..., scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ...) -> None: ...

class UpdateScoreboardOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RebuildScoreboardInput(_message.Message):
    __slots__ = ("scoreboard_id",)
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class RebuildScoreboardOutput(_message.Message):
    __slots__ = ("activity_id",)
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    def __init__(self, activity_id: _Optional[str] = ...) -> None: ...

class DeleteScoreboardInput(_message.Message):
    __slots__ = ("scoreboard_id",)
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class DeleteScoreboardOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeScoreboardInput(_message.Message):
    __slots__ = ("scoreboard_id", "scoreboard_key", "extra")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_KEY_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    scoreboard_key: str
    extra: _containers.RepeatedScalarFieldContainer[_scoreboard_pb2.Scoreboard.Extra]
    def __init__(self, scoreboard_id: _Optional[str] = ..., scoreboard_key: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard.Extra, str]]] = ...) -> None: ...

class DescribeScoreboardOutput(_message.Message):
    __slots__ = ("scoreboard",)
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    scoreboard: _scoreboard_pb2.Scoreboard
    def __init__(self, scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ...) -> None: ...

class LookupScoreboardInput(_message.Message):
    __slots__ = ("scoreboard_key", "extra")
    SCOREBOARD_KEY_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    scoreboard_key: str
    extra: _containers.RepeatedScalarFieldContainer[_scoreboard_pb2.Scoreboard.Extra]
    def __init__(self, scoreboard_key: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard.Extra, str]]] = ...) -> None: ...

class LookupScoreboardOutput(_message.Message):
    __slots__ = ("scoreboard",)
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    scoreboard: _scoreboard_pb2.Scoreboard
    def __init__(self, scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ...) -> None: ...

class ListScoreboardsInput(_message.Message):
    __slots__ = ("offset", "size", "filters", "extra")
    class Filter(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListScoreboardsInput.Filter
    extra: _containers.RepeatedScalarFieldContainer[_scoreboard_pb2.Scoreboard.Extra]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListScoreboardsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard.Extra, str]]] = ...) -> None: ...

class ListScoreboardsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Scoreboard]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard, _Mapping]]] = ...) -> None: ...

class DescribeScoreboardRowInput(_message.Message):
    __slots__ = ("mode", "punctual_time", "scoreboard_id", "member_id")
    MODE_FIELD_NUMBER: _ClassVar[int]
    PUNCTUAL_TIME_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    mode: _scoreboard_pb2.Scoreboard.FetchingMode
    punctual_time: int
    scoreboard_id: str
    member_id: str
    def __init__(self, mode: _Optional[_Union[_scoreboard_pb2.Scoreboard.FetchingMode, str]] = ..., punctual_time: _Optional[int] = ..., scoreboard_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class DescribeScoreboardRowOutput(_message.Message):
    __slots__ = ("row", "frozen")
    ROW_FIELD_NUMBER: _ClassVar[int]
    FROZEN_FIELD_NUMBER: _ClassVar[int]
    row: _scoreboard_pb2.Scoreboard.Row
    frozen: bool
    def __init__(self, row: _Optional[_Union[_scoreboard_pb2.Scoreboard.Row, _Mapping]] = ..., frozen: bool = ...) -> None: ...

class ListScoreboardRowsInput(_message.Message):
    __slots__ = ("scoreboard_id", "mode", "punctual_time", "offset", "size", "filters", "sort", "order")
    class ExpressionColumn(_message.Message):
        __slots__ = ("key", "string", "number", "enum")
        KEY_FIELD_NUMBER: _ClassVar[int]
        STRING_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        ENUM_FIELD_NUMBER: _ClassVar[int]
        key: str
        string: _expression_pb2.ExpressionString
        number: _expression_pb2.ExpressionInt
        enum: _expression_pb2.ExpressionEnum
        def __init__(self, key: _Optional[str] = ..., string: _Optional[_Union[_expression_pb2.ExpressionString, _Mapping]] = ..., number: _Optional[_Union[_expression_pb2.ExpressionInt, _Mapping]] = ..., enum: _Optional[_Union[_expression_pb2.ExpressionEnum, _Mapping]] = ...) -> None: ...
    class Filter(_message.Message):
        __slots__ = ("member_id", "column")
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        COLUMN_FIELD_NUMBER: _ClassVar[int]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        column: _containers.RepeatedCompositeFieldContainer[ListScoreboardRowsInput.ExpressionColumn]
        def __init__(self, member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., column: _Optional[_Iterable[_Union[ListScoreboardRowsInput.ExpressionColumn, _Mapping]]] = ...) -> None: ...
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    PUNCTUAL_TIME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    mode: _scoreboard_pb2.Scoreboard.FetchingMode
    punctual_time: int
    offset: int
    size: int
    filters: ListScoreboardRowsInput.Filter
    sort: str
    order: _direction_pb2.Direction
    def __init__(self, scoreboard_id: _Optional[str] = ..., mode: _Optional[_Union[_scoreboard_pb2.Scoreboard.FetchingMode, str]] = ..., punctual_time: _Optional[int] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListScoreboardRowsInput.Filter, _Mapping]] = ..., sort: _Optional[str] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListScoreboardRowsOutput(_message.Message):
    __slots__ = ("total", "items", "frozen")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    FROZEN_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Scoreboard.Row]
    frozen: bool
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard.Row, _Mapping]]] = ..., frozen: bool = ...) -> None: ...

class AddScoreboardColumnInput(_message.Message):
    __slots__ = ("scoreboard_id", "column")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    column: _scoreboard_pb2.Scoreboard.Column
    def __init__(self, scoreboard_id: _Optional[str] = ..., column: _Optional[_Union[_scoreboard_pb2.Scoreboard.Column, _Mapping]] = ...) -> None: ...

class AddScoreboardColumnOutput(_message.Message):
    __slots__ = ("column_id",)
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    column_id: str
    def __init__(self, column_id: _Optional[str] = ...) -> None: ...

class UpdateScoreboardColumnInput(_message.Message):
    __slots__ = ("patch", "scoreboard_id", "column_id", "column")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateScoreboardColumnInput.Patch]
        PARENT_ID: _ClassVar[UpdateScoreboardColumnInput.Patch]
        KEY: _ClassVar[UpdateScoreboardColumnInput.Patch]
        NAME: _ClassVar[UpdateScoreboardColumnInput.Patch]
        SHORT_NAME: _ClassVar[UpdateScoreboardColumnInput.Patch]
        INDEX: _ClassVar[UpdateScoreboardColumnInput.Patch]
        VISIBLE: _ClassVar[UpdateScoreboardColumnInput.Patch]
        FILTERABLE: _ClassVar[UpdateScoreboardColumnInput.Patch]
        SORTABLE: _ClassVar[UpdateScoreboardColumnInput.Patch]
    ALL: UpdateScoreboardColumnInput.Patch
    PARENT_ID: UpdateScoreboardColumnInput.Patch
    KEY: UpdateScoreboardColumnInput.Patch
    NAME: UpdateScoreboardColumnInput.Patch
    SHORT_NAME: UpdateScoreboardColumnInput.Patch
    INDEX: UpdateScoreboardColumnInput.Patch
    VISIBLE: UpdateScoreboardColumnInput.Patch
    FILTERABLE: UpdateScoreboardColumnInput.Patch
    SORTABLE: UpdateScoreboardColumnInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateScoreboardColumnInput.Patch]
    scoreboard_id: str
    column_id: str
    column: _scoreboard_pb2.Scoreboard.Column
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateScoreboardColumnInput.Patch, str]]] = ..., scoreboard_id: _Optional[str] = ..., column_id: _Optional[str] = ..., column: _Optional[_Union[_scoreboard_pb2.Scoreboard.Column, _Mapping]] = ...) -> None: ...

class UpdateScoreboardColumnOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteScoreboardColumnInput(_message.Message):
    __slots__ = ("scoreboard_id", "column_id")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    column_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., column_id: _Optional[str] = ...) -> None: ...

class DeleteScoreboardColumnOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeScoreboardColumnInput(_message.Message):
    __slots__ = ("scoreboard_id", "column_id")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    column_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., column_id: _Optional[str] = ...) -> None: ...

class DescribeScoreboardColumnOutput(_message.Message):
    __slots__ = ("column",)
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    column: _scoreboard_pb2.Scoreboard.Column
    def __init__(self, column: _Optional[_Union[_scoreboard_pb2.Scoreboard.Column, _Mapping]] = ...) -> None: ...

class ListScoreboardColumnsInput(_message.Message):
    __slots__ = ("scoreboard_id",)
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class ListScoreboardColumnsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Scoreboard.Column]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard.Column, _Mapping]]] = ...) -> None: ...
