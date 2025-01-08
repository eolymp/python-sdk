from eolymp.printer import printer_pb2 as _printer_pb2
from eolymp.printer import printer_job_pb2 as _printer_job_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrinterConnectorClientMessage(_message.Message):
    __slots__ = ["id", "authenticate", "status", "report"]
    class Authenticate(_message.Message):
        __slots__ = ["secret"]
        SECRET_FIELD_NUMBER: _ClassVar[int]
        secret: str
        def __init__(self, secret: _Optional[str] = ...) -> None: ...
    class Report(_message.Message):
        __slots__ = ["status"]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: _printer_job_pb2.Job.Status
        def __init__(self, status: _Optional[_Union[_printer_job_pb2.Job.Status, str]] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ["status"]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: _printer_pb2.Printer.Status
        def __init__(self, status: _Optional[_Union[_printer_pb2.Printer.Status, str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    id: str
    authenticate: PrinterConnectorClientMessage.Authenticate
    status: PrinterConnectorClientMessage.Status
    report: PrinterConnectorClientMessage.Report
    def __init__(self, id: _Optional[str] = ..., authenticate: _Optional[_Union[PrinterConnectorClientMessage.Authenticate, _Mapping]] = ..., status: _Optional[_Union[PrinterConnectorClientMessage.Status, _Mapping]] = ..., report: _Optional[_Union[PrinterConnectorClientMessage.Report, _Mapping]] = ...) -> None: ...

class PrinterConnectorServerMessage(_message.Message):
    __slots__ = ["id", "hello", "print"]
    class Hello(_message.Message):
        __slots__ = ["comment"]
        COMMENT_FIELD_NUMBER: _ClassVar[int]
        comment: str
        def __init__(self, comment: _Optional[str] = ...) -> None: ...
    class Print(_message.Message):
        __slots__ = ["job"]
        JOB_FIELD_NUMBER: _ClassVar[int]
        job: _printer_job_pb2.Job
        def __init__(self, job: _Optional[_Union[_printer_job_pb2.Job, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    HELLO_FIELD_NUMBER: _ClassVar[int]
    PRINT_FIELD_NUMBER: _ClassVar[int]
    id: str
    hello: PrinterConnectorServerMessage.Hello
    print: PrinterConnectorServerMessage.Print
    def __init__(self, id: _Optional[str] = ..., hello: _Optional[_Union[PrinterConnectorServerMessage.Hello, _Mapping]] = ..., print: _Optional[_Union[PrinterConnectorServerMessage.Print, _Mapping]] = ...) -> None: ...
