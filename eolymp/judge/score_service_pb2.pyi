from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import score_pb2 as _score_pb2
from eolymp.judge import score_timeline_pb2 as _score_timeline_pb2
from eolymp.judge import scoreboard_pb2 as _scoreboard_pb2
from eolymp.wellknown import watch_pb2 as _watch_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RebuildScoreInput(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class RebuildScoreOutput(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...

class DescribeViewerScoreInput(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DescribeViewerScoreOutput(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _score_pb2.Score
    def __init__(self, score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class WatchScoreInput(_message.Message):
    __slots__ = ("contest_id", "participant_id", "mode")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    mode: _scoreboard_pb2.Scoreboard.Mode
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., mode: _Optional[_Union[_scoreboard_pb2.Scoreboard.Mode, str]] = ...) -> None: ...

class WatchScoreOutput(_message.Message):
    __slots__ = ("score", "event")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    score: _score_pb2.Score
    event: _watch_pb2.WatchEventType
    def __init__(self, score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ..., event: _Optional[_Union[_watch_pb2.WatchEventType, str]] = ...) -> None: ...

class DescribeScoreInput(_message.Message):
    __slots__ = ("contest_id", "participant_id", "mode")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    mode: _scoreboard_pb2.Scoreboard.Mode
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., mode: _Optional[_Union[_scoreboard_pb2.Scoreboard.Mode, str]] = ...) -> None: ...

class DescribeScoreOutput(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _score_pb2.Score
    def __init__(self, score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class ImportScoreInput(_message.Message):
    __slots__ = ("contest_id", "participant_id", "scores")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    scores: _containers.RepeatedCompositeFieldContainer[_score_pb2.Score]
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., scores: _Optional[_Iterable[_Union[_score_pb2.Score, _Mapping]]] = ...) -> None: ...

class ImportScoreOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportScoreInput(_message.Message):
    __slots__ = ("contest_id", "participant_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class ExportScoreOutput(_message.Message):
    __slots__ = ("scores",)
    SCORES_FIELD_NUMBER: _ClassVar[int]
    scores: _containers.RepeatedCompositeFieldContainer[_score_pb2.Score]
    def __init__(self, scores: _Optional[_Iterable[_Union[_score_pb2.Score, _Mapping]]] = ...) -> None: ...

class ListScoreTimelineInput(_message.Message):
    __slots__ = ("contest_id", "participant_id", "mode")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    mode: _scoreboard_pb2.Scoreboard.Mode
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., mode: _Optional[_Union[_scoreboard_pb2.Scoreboard.Mode, str]] = ...) -> None: ...

class ListScoreTimelineOutput(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_score_timeline_pb2.ScoreTimelinePoint]
    def __init__(self, items: _Optional[_Iterable[_Union[_score_timeline_pb2.ScoreTimelinePoint, _Mapping]]] = ...) -> None: ...
