from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.annotations import service_pb2 as _service_pb2
from eolymp.ranker import activity_pb2 as _activity_pb2
from eolymp.ranker import scoreboard_pb2 as _scoreboard_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
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
    __slots__ = ["scoreboard"]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    scoreboard: _scoreboard_pb2.Scoreboard
    def __init__(self, scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ...) -> None: ...

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
    __slots__ = ["member_id", "scoreboard_id"]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class DescribeScoreboardRowOutput(_message.Message):
    __slots__ = ["row"]
    ROW_FIELD_NUMBER: _ClassVar[int]
    row: _scoreboard_pb2.Scoreboard.Row
    def __init__(self, row: _Optional[_Union[_scoreboard_pb2.Scoreboard.Row, _Mapping]] = ...) -> None: ...

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
    __slots__ = ["filters", "offset", "scoreboard_id", "size"]
    class Filter(_message.Message):
        __slots__ = ["member_id"]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListScoreboardRowsInput.Filter
    offset: int
    scoreboard_id: str
    size: int
    def __init__(self, scoreboard_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListScoreboardRowsInput.Filter, _Mapping]] = ...) -> None: ...

class ListScoreboardRowsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Scoreboard.Row]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard.Row, _Mapping]]] = ...) -> None: ...

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

class UpdateScoreboardInput(_message.Message):
    __slots__ = ["scoreboard", "scoreboard_id"]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard: _scoreboard_pb2.Scoreboard
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ...) -> None: ...

class UpdateScoreboardOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
