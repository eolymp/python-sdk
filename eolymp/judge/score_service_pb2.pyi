from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import result_pb2 as _result_pb2
from eolymp.judge import score_pb2 as _score_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeScoreInput(_message.Message):
    __slots__ = ["contest_id", "mode", "participant_id", "time_offset"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    mode: _score_pb2.Score.FetchingMode
    participant_id: str
    time_offset: int
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., mode: _Optional[_Union[_score_pb2.Score.FetchingMode, str]] = ..., time_offset: _Optional[int] = ...) -> None: ...

class DescribeScoreOutput(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _score_pb2.Score
    def __init__(self, score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class ExportResultInput(_message.Message):
    __slots__ = ["contest_id", "mode", "time_offset"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    mode: _score_pb2.Score.FetchingMode
    time_offset: int
    def __init__(self, contest_id: _Optional[str] = ..., mode: _Optional[_Union[_score_pb2.Score.FetchingMode, str]] = ..., time_offset: _Optional[int] = ...) -> None: ...

class ExportResultOutput(_message.Message):
    __slots__ = ["export_url"]
    EXPORT_URL_FIELD_NUMBER: _ClassVar[int]
    export_url: str
    def __init__(self, export_url: _Optional[str] = ...) -> None: ...

class ExportScoreInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class ExportScoreOutput(_message.Message):
    __slots__ = ["scores"]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    scores: _containers.RepeatedCompositeFieldContainer[_score_pb2.Score]
    def __init__(self, scores: _Optional[_Iterable[_Union[_score_pb2.Score, _Mapping]]] = ...) -> None: ...

class ImportScoreInput(_message.Message):
    __slots__ = ["contest_id", "participant_id", "scores"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    scores: _containers.RepeatedCompositeFieldContainer[_score_pb2.Score]
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., scores: _Optional[_Iterable[_Union[_score_pb2.Score, _Mapping]]] = ...) -> None: ...

class ImportScoreOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectScoreInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class IntrospectScoreOutput(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _score_pb2.Score
    def __init__(self, score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class ListResultInput(_message.Message):
    __slots__ = ["contest_id", "mode", "offset", "size", "time_offset"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    mode: _score_pb2.Score.FetchingMode
    offset: int
    size: int
    time_offset: int
    def __init__(self, contest_id: _Optional[str] = ..., mode: _Optional[_Union[_score_pb2.Score.FetchingMode, str]] = ..., time_offset: _Optional[int] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListResultOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_result_pb2.Result]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_result_pb2.Result, _Mapping]]] = ...) -> None: ...

class RebuildScoreInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class RebuildScoreOutput(_message.Message):
    __slots__ = ["activity_id"]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    def __init__(self, activity_id: _Optional[str] = ...) -> None: ...

class WatchScoreInput(_message.Message):
    __slots__ = ["contest_id", "mode", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    mode: _score_pb2.Score.FetchingMode
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., mode: _Optional[_Union[_score_pb2.Score.FetchingMode, str]] = ...) -> None: ...

class WatchScoreOutput(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _score_pb2.Score
    def __init__(self, score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...
