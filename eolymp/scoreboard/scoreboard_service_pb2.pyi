from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.scoreboard import scoreboard_pb2 as _scoreboard_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateScoreboardInput(_message.Message):
    __slots__ = ("scoreboard",)
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    scoreboard: _scoreboard_pb2.Scoreboard
    def __init__(self, scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ...) -> None: ...

class CreateScoreboardOutput(_message.Message):
    __slots__ = ("scoreboard_id",)
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class UpdateScoreboardInput(_message.Message):
    __slots__ = ("scoreboard_id", "scoreboard")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    scoreboard: _scoreboard_pb2.Scoreboard.Patch
    def __init__(self, scoreboard_id: _Optional[str] = ..., scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard.Patch, _Mapping]] = ...) -> None: ...

class UpdateScoreboardOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteScoreboardInput(_message.Message):
    __slots__ = ("scoreboard_id",)
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class DeleteScoreboardOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeScoreboardInput(_message.Message):
    __slots__ = ("scoreboard_id",)
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class DescribeScoreboardOutput(_message.Message):
    __slots__ = ("scoreboard",)
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    scoreboard: _scoreboard_pb2.Scoreboard
    def __init__(self, scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ...) -> None: ...

class ListScoreboardsInput(_message.Message):
    __slots__ = ("offset", "size", "search", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "slug", "contest_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        SLUG_FIELD_NUMBER: _ClassVar[int]
        CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        slug: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        contest_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., slug: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., contest_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    search: str
    filters: ListScoreboardsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListScoreboardsInput.Filter, _Mapping]] = ...) -> None: ...

class ListScoreboardsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Scoreboard]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard, _Mapping]]] = ...) -> None: ...

class AddScoreboardContestInput(_message.Message):
    __slots__ = ("scoreboard_id", "contest_id", "index")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    contest_id: str
    index: int
    def __init__(self, scoreboard_id: _Optional[str] = ..., contest_id: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...

class AddScoreboardContestOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveScoreboardContestInput(_message.Message):
    __slots__ = ("scoreboard_id", "contest_id")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    contest_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., contest_id: _Optional[str] = ...) -> None: ...

class RemoveScoreboardContestOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddScoreboardAttributeInput(_message.Message):
    __slots__ = ("scoreboard_id", "attribute_key", "index", "label")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    attribute_key: str
    index: int
    label: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., attribute_key: _Optional[str] = ..., index: _Optional[int] = ..., label: _Optional[str] = ...) -> None: ...

class AddScoreboardAttributeOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveScoreboardAttributeInput(_message.Message):
    __slots__ = ("scoreboard_id", "attribute_key")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    attribute_key: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., attribute_key: _Optional[str] = ...) -> None: ...

class RemoveScoreboardAttributeOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListScoreboardRowsInput(_message.Message):
    __slots__ = ("scoreboard_id", "mode", "offset", "size", "filters", "order", "sort_contest_id", "sort_attribute_key")
    class ExpressionAttribute(_message.Message):
        __slots__ = ("attribute_key", "number", "string")
        ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        STRING_FIELD_NUMBER: _ClassVar[int]
        attribute_key: str
        number: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        string: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, attribute_key: _Optional[str] = ..., number: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., string: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    class Filter(_message.Message):
        __slots__ = ("unofficial", "disqualified", "attributes")
        UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
        DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        unofficial: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        disqualified: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        attributes: _containers.RepeatedCompositeFieldContainer[ListScoreboardRowsInput.ExpressionAttribute]
        def __init__(self, unofficial: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., disqualified: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., attributes: _Optional[_Iterable[_Union[ListScoreboardRowsInput.ExpressionAttribute, _Mapping]]] = ...) -> None: ...
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SORT_CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SORT_ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    mode: _scoreboard_pb2.Scoreboard.Mode
    offset: int
    size: int
    filters: ListScoreboardRowsInput.Filter
    order: _direction_pb2.Direction
    sort_contest_id: str
    sort_attribute_key: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., mode: _Optional[_Union[_scoreboard_pb2.Scoreboard.Mode, str]] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListScoreboardRowsInput.Filter, _Mapping]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., sort_contest_id: _Optional[str] = ..., sort_attribute_key: _Optional[str] = ...) -> None: ...

class ListScoreboardRowsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Row]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Row, _Mapping]]] = ...) -> None: ...

class DescribeScoreboardRowInput(_message.Message):
    __slots__ = ("scoreboard_id", "member_id", "mode")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    member_id: str
    mode: _scoreboard_pb2.Scoreboard.Mode
    def __init__(self, scoreboard_id: _Optional[str] = ..., member_id: _Optional[str] = ..., mode: _Optional[_Union[_scoreboard_pb2.Scoreboard.Mode, str]] = ...) -> None: ...

class DescribeScoreboardRowOutput(_message.Message):
    __slots__ = ("row",)
    ROW_FIELD_NUMBER: _ClassVar[int]
    row: _scoreboard_pb2.Row
    def __init__(self, row: _Optional[_Union[_scoreboard_pb2.Row, _Mapping]] = ...) -> None: ...

class RebuildScoreboardInput(_message.Message):
    __slots__ = ("scoreboard_id",)
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class RebuildScoreboardOutput(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...
