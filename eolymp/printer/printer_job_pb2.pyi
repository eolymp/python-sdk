from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ["id", "status", "document_url"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN_STATUS: _ClassVar[Job.Status]
        PENDING: _ClassVar[Job.Status]
        PRINTING: _ClassVar[Job.Status]
        COMPLETE: _ClassVar[Job.Status]
        ERROR: _ClassVar[Job.Status]
    UNKNOWN_STATUS: Job.Status
    PENDING: Job.Status
    PRINTING: Job.Status
    COMPLETE: Job.Status
    ERROR: Job.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: Job.Status
    document_url: str
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Job.Status, str]] = ..., document_url: _Optional[str] = ...) -> None: ...
