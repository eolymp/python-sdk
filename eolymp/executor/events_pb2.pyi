from eolymp.executor import report_pb2 as _report_pb2
from eolymp.executor import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JobReportedEvent(_message.Message):
    __slots__ = ["report"]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: _report_pb2.Report
    def __init__(self, report: _Optional[_Union[_report_pb2.Report, _Mapping]] = ...) -> None: ...

class StatusUpdatedEvent(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status
    def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...
