from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import notebook_pb2 as _notebook_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadNotebookInput(_message.Message):
    __slots__ = ("member_id", "name", "type", "content_url")
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    name: str
    type: str
    content_url: str
    def __init__(self, member_id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., content_url: _Optional[str] = ...) -> None: ...

class UploadNotebookOutput(_message.Message):
    __slots__ = ("notebook_id",)
    NOTEBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    notebook_id: str
    def __init__(self, notebook_id: _Optional[str] = ...) -> None: ...

class ReviewNotebookInput(_message.Message):
    __slots__ = ("notebook_id", "status")
    NOTEBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    notebook_id: str
    status: _notebook_pb2.Notebook.Status
    def __init__(self, notebook_id: _Optional[str] = ..., status: _Optional[_Union[_notebook_pb2.Notebook.Status, str]] = ...) -> None: ...

class ReviewNotebookOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteNotebookInput(_message.Message):
    __slots__ = ("notebook_id",)
    NOTEBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    notebook_id: str
    def __init__(self, notebook_id: _Optional[str] = ...) -> None: ...

class DeleteNotebookOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeNotebookInput(_message.Message):
    __slots__ = ("notebook_id",)
    NOTEBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    notebook_id: str
    def __init__(self, notebook_id: _Optional[str] = ...) -> None: ...

class DescribeNotebookOutput(_message.Message):
    __slots__ = ("notebook",)
    NOTEBOOK_FIELD_NUMBER: _ClassVar[int]
    notebook: _notebook_pb2.Notebook
    def __init__(self, notebook: _Optional[_Union[_notebook_pb2.Notebook, _Mapping]] = ...) -> None: ...

class ListNotebooksInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "member_id", "status")
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListNotebooksInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListNotebooksInput.Filter, _Mapping]] = ...) -> None: ...

class ListNotebooksOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_notebook_pb2.Notebook]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_notebook_pb2.Notebook, _Mapping]]] = ...) -> None: ...
