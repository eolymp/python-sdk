from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import scoreboard_pb2 as _scoreboard_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeScoreboardInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeScoreboardOutput(_message.Message):
    __slots__ = ["scoreboard"]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    scoreboard: _scoreboard_pb2.Scoreboard
    def __init__(self, scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ...) -> None: ...

class ListScoreboardRowsInput(_message.Message):
    __slots__ = ["after", "filters", "mode", "order", "problem_id", "round_id", "size"]
    class Filter(_message.Message):
        __slots__ = ["disqualified", "unofficial"]
        DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
        UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
        disqualified: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        unofficial: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, unofficial: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., disqualified: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    ROUND_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    after: str
    filters: ListScoreboardRowsInput.Filter
    mode: _scoreboard_pb2.Scoreboard.Mode
    order: _direction_pb2.Direction
    problem_id: str
    round_id: str
    size: int
    def __init__(self, mode: _Optional[_Union[_scoreboard_pb2.Scoreboard.Mode, str]] = ..., size: _Optional[int] = ..., after: _Optional[str] = ..., filters: _Optional[_Union[ListScoreboardRowsInput.Filter, _Mapping]] = ..., round_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListScoreboardRowsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Scoreboard.Row]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard.Row, _Mapping]]] = ...) -> None: ...
