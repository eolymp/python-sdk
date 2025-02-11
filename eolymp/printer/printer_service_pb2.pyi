from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.printer import printer_pb2 as _printer_pb2
from eolymp.printer import printer_job_pb2 as _printer_job_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePrinterInput(_message.Message):
    __slots__ = ("printer",)
    PRINTER_FIELD_NUMBER: _ClassVar[int]
    printer: _printer_pb2.Printer
    def __init__(self, printer: _Optional[_Union[_printer_pb2.Printer, _Mapping]] = ...) -> None: ...

class CreatePrinterOutput(_message.Message):
    __slots__ = ("printer_id",)
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    printer_id: str
    def __init__(self, printer_id: _Optional[str] = ...) -> None: ...

class UpdatePrinterInput(_message.Message):
    __slots__ = ("printer_id", "printer")
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    PRINTER_FIELD_NUMBER: _ClassVar[int]
    printer_id: str
    printer: _printer_pb2.Printer
    def __init__(self, printer_id: _Optional[str] = ..., printer: _Optional[_Union[_printer_pb2.Printer, _Mapping]] = ...) -> None: ...

class UpdatePrinterOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeletePrinterInput(_message.Message):
    __slots__ = ("printer_id",)
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    printer_id: str
    def __init__(self, printer_id: _Optional[str] = ...) -> None: ...

class DeletePrinterOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribePrinterInput(_message.Message):
    __slots__ = ("printer_id",)
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    printer_id: str
    def __init__(self, printer_id: _Optional[str] = ...) -> None: ...

class DescribePrinterOutput(_message.Message):
    __slots__ = ("printer",)
    PRINTER_FIELD_NUMBER: _ClassVar[int]
    printer: _printer_pb2.Printer
    def __init__(self, printer: _Optional[_Union[_printer_pb2.Printer, _Mapping]] = ...) -> None: ...

class ListPrintersInput(_message.Message):
    __slots__ = ("size", "offset", "search", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "status", "name")
        ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    size: int
    offset: int
    search: str
    filters: ListPrintersInput.Filter
    def __init__(self, size: _Optional[int] = ..., offset: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListPrintersInput.Filter, _Mapping]] = ...) -> None: ...

class ListPrintersOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_printer_pb2.Printer]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_printer_pb2.Printer, _Mapping]]] = ...) -> None: ...

class CreatePrinterJobInput(_message.Message):
    __slots__ = ("printer_id", "html")
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    HTML_FIELD_NUMBER: _ClassVar[int]
    printer_id: str
    html: str
    def __init__(self, printer_id: _Optional[str] = ..., html: _Optional[str] = ...) -> None: ...

class CreatePrinterJobOutput(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class DescribePrinterJobInput(_message.Message):
    __slots__ = ("printer_id", "job_id")
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    printer_id: str
    job_id: str
    def __init__(self, printer_id: _Optional[str] = ..., job_id: _Optional[str] = ...) -> None: ...

class DescribePrinterJobOutput(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: _printer_job_pb2.Job
    def __init__(self, job: _Optional[_Union[_printer_job_pb2.Job, _Mapping]] = ...) -> None: ...

class ListPrinterJobsInput(_message.Message):
    __slots__ = ("printer_id", "offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "status")
        ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    printer_id: str
    offset: int
    size: int
    filters: ListPrinterJobsInput.Filter
    def __init__(self, printer_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListPrinterJobsInput.Filter, _Mapping]] = ...) -> None: ...

class ListPrinterJobsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_printer_job_pb2.Job]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_printer_job_pb2.Job, _Mapping]]] = ...) -> None: ...

class CancelPrinterJobInput(_message.Message):
    __slots__ = ("printer_id", "job_id")
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    printer_id: str
    job_id: str
    def __init__(self, printer_id: _Optional[str] = ..., job_id: _Optional[str] = ...) -> None: ...

class CancelPrinterJobOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdatePrinterJobInput(_message.Message):
    __slots__ = ("printer_id", "job_id", "job")
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    printer_id: str
    job_id: str
    job: _printer_job_pb2.Job
    def __init__(self, printer_id: _Optional[str] = ..., job_id: _Optional[str] = ..., job: _Optional[_Union[_printer_job_pb2.Job, _Mapping]] = ...) -> None: ...

class UpdatePrinterJobOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeletePrinterJobInput(_message.Message):
    __slots__ = ("printer_id", "job_id")
    PRINTER_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    printer_id: str
    job_id: str
    def __init__(self, printer_id: _Optional[str] = ..., job_id: _Optional[str] = ...) -> None: ...

class DeletePrinterJobOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
