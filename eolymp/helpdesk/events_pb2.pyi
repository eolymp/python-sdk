from eolymp.helpdesk import document_pb2 as _document_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DocumentCreatedEvent(_message.Message):
    __slots__ = ["document"]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document
    def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ...) -> None: ...

class DocumentDeletedEvent(_message.Message):
    __slots__ = ["document"]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document
    def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ...) -> None: ...

class DocumentUpdatedEvent(_message.Message):
    __slots__ = ["document"]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document
    def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ...) -> None: ...
