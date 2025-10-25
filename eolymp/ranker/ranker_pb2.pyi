from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.ranker import activity_pb2 as _activity_pb2
from eolymp.ranker import scoreboard_pb2 as _scoreboard_pb2
from eolymp.ranker import scoreboard_service_pb2 as _scoreboard_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListActivitiesInput(_message.Message):
    __slots__ = ("scoreboard_id", "offset", "size")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    offset: int
    size: int
    def __init__(self, scoreboard_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListActivitiesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_activity_pb2.Activity]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_activity_pb2.Activity, _Mapping]]] = ...) -> None: ...

class ScheduleActionInput(_message.Message):
    __slots__ = ("scoreboard_id", "action")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    action: _scoreboard_pb2.Scoreboard.Action
    def __init__(self, scoreboard_id: _Optional[str] = ..., action: _Optional[_Union[_scoreboard_pb2.Scoreboard.Action, _Mapping]] = ...) -> None: ...

class ScheduleActionOutput(_message.Message):
    __slots__ = ("action_id",)
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    action_id: str
    def __init__(self, action_id: _Optional[str] = ...) -> None: ...

class UnscheduleActionInput(_message.Message):
    __slots__ = ("scoreboard_id", "action_id")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    action_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., action_id: _Optional[str] = ...) -> None: ...

class UnscheduleActionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListScheduledActionsInput(_message.Message):
    __slots__ = ("scoreboard_id",)
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...

class ListScheduledActionsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_scoreboard_pb2.Scoreboard.Action]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_scoreboard_pb2.Scoreboard.Action, _Mapping]]] = ...) -> None: ...
