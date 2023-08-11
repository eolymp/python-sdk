from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import entry_pb2 as _entry_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDocumentInput(_message.Message):
    __slots__ = ["document", "parent_id", "title"]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    document: _content_pb2.Content
    parent_id: str
    title: str
    def __init__(self, parent_id: _Optional[str] = ..., title: _Optional[str] = ..., document: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class CreateDocumentOutput(_message.Message):
    __slots__ = ["entry_id"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    def __init__(self, entry_id: _Optional[str] = ...) -> None: ...

class CreateSectionInput(_message.Message):
    __slots__ = ["description", "parent_id", "title"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    description: _content_pb2.Content
    parent_id: str
    title: str
    def __init__(self, parent_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class CreateSectionOutput(_message.Message):
    __slots__ = ["entry_id"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    def __init__(self, entry_id: _Optional[str] = ...) -> None: ...

class DeleteEntryInput(_message.Message):
    __slots__ = ["entry_id"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    def __init__(self, entry_id: _Optional[str] = ...) -> None: ...

class DeleteEntryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeEntryInput(_message.Message):
    __slots__ = ["entry_id"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    def __init__(self, entry_id: _Optional[str] = ...) -> None: ...

class DescribeEntryOutput(_message.Message):
    __slots__ = ["entry"]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _entry_pb2.Entry
    def __init__(self, entry: _Optional[_Union[_entry_pb2.Entry, _Mapping]] = ...) -> None: ...

class ListEntriesInput(_message.Message):
    __slots__ = ["filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["id", "parent_id", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        PARENT_ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        parent_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., parent_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    DEFAULT: ListEntriesInput.Sortable
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    filters: ListEntriesInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListEntriesInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListEntriesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListEntriesInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListEntriesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_entry_pb2.Entry]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_entry_pb2.Entry, _Mapping]]] = ...) -> None: ...

class RenameEntryInput(_message.Message):
    __slots__ = ["entry_id", "title"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    title: str
    def __init__(self, entry_id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class RenameEntryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateDocumentInput(_message.Message):
    __slots__ = ["document", "entry_id", "parent_id", "title"]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    document: _content_pb2.Content
    entry_id: str
    parent_id: str
    title: str
    def __init__(self, entry_id: _Optional[str] = ..., parent_id: _Optional[str] = ..., title: _Optional[str] = ..., document: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class UpdateDocumentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateSectionInput(_message.Message):
    __slots__ = ["description", "entry_id", "parent_id", "title"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    description: _content_pb2.Content
    entry_id: str
    parent_id: str
    title: str
    def __init__(self, entry_id: _Optional[str] = ..., parent_id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class UpdateSectionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
