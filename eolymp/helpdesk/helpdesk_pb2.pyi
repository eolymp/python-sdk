from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.helpdesk import document_pb2 as _document_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDocumentInput(_message.Message):
    __slots__ = ["document"]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document
    def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ...) -> None: ...

class CreateDocumentOutput(_message.Message):
    __slots__ = ["document_id"]
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    document_id: str
    def __init__(self, document_id: _Optional[str] = ...) -> None: ...

class DeleteDocumentInput(_message.Message):
    __slots__ = ["document_id"]
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    document_id: str
    def __init__(self, document_id: _Optional[str] = ...) -> None: ...

class DeleteDocumentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeDocumentInput(_message.Message):
    __slots__ = ["document_id", "render"]
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    document_id: str
    render: bool
    def __init__(self, document_id: _Optional[str] = ..., render: bool = ...) -> None: ...

class DescribeDocumentOutput(_message.Message):
    __slots__ = ["document"]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document
    def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ...) -> None: ...

class DescribePathInput(_message.Message):
    __slots__ = ["locale", "path", "render"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    locale: str
    path: str
    render: bool
    def __init__(self, path: _Optional[str] = ..., render: bool = ..., locale: _Optional[str] = ...) -> None: ...

class DescribePathOutput(_message.Message):
    __slots__ = ["document"]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document
    def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ...) -> None: ...

class ListDocumentsInput(_message.Message):
    __slots__ = ["filters", "offset", "render", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "locale", "path", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListDocumentsInput.Filter
    offset: int
    render: bool
    size: int
    def __init__(self, render: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListDocumentsInput.Filter, _Mapping]] = ...) -> None: ...

class ListDocumentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_document_pb2.Document]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_document_pb2.Document, _Mapping]]] = ...) -> None: ...

class ListParentsInput(_message.Message):
    __slots__ = ["locale", "path", "render"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    locale: str
    path: str
    render: bool
    def __init__(self, path: _Optional[str] = ..., locale: _Optional[str] = ..., render: bool = ...) -> None: ...

class ListParentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_document_pb2.Document]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_document_pb2.Document, _Mapping]]] = ...) -> None: ...

class ListPathsInput(_message.Message):
    __slots__ = ["filters", "locale", "offset", "render", "size"]
    class Filter(_message.Message):
        __slots__ = ["label", "path", "query"]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        label: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        def __init__(self, query: _Optional[str] = ..., path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., label: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListPathsInput.Filter
    locale: str
    offset: int
    render: bool
    size: int
    def __init__(self, locale: _Optional[str] = ..., render: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListPathsInput.Filter, _Mapping]] = ...) -> None: ...

class ListPathsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_document_pb2.Document]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_document_pb2.Document, _Mapping]]] = ...) -> None: ...

class UpdateDocumentInput(_message.Message):
    __slots__ = ["document", "document_id"]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document
    document_id: str
    def __init__(self, document_id: _Optional[str] = ..., document: _Optional[_Union[_document_pb2.Document, _Mapping]] = ...) -> None: ...

class UpdateDocumentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
