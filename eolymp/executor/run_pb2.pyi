from eolymp.executor import execution_report_pb2 as _execution_report_pb2
from eolymp.executor import stats_pb2 as _stats_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Run(_message.Message):
    __slots__ = ("id", "status", "outcome", "error", "stats", "interactor_stats", "interaction_url")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_STATS_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: _execution_report_pb2.ExecutionReport.Status
    outcome: _execution_report_pb2.ExecutionReport.Outcome
    error: str
    stats: _stats_pb2.Stats
    interactor_stats: _stats_pb2.Stats
    interaction_url: str
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[_execution_report_pb2.ExecutionReport.Status, str]] = ..., outcome: _Optional[_Union[_execution_report_pb2.ExecutionReport.Outcome, str]] = ..., error: _Optional[str] = ..., stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., interactor_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., interaction_url: _Optional[str] = ...) -> None: ...
