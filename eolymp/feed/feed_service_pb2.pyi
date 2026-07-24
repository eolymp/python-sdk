from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.feed import entry_pb2 as _entry_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListEntriesInput(_message.Message):
    __slots__ = ("size", "after", "filters")
    class Filter(_message.Message):
        __slots__ = ("member_id", "type")
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    SIZE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    size: int
    after: str
    filters: ListEntriesInput.Filter
    def __init__(self, size: _Optional[int] = ..., after: _Optional[str] = ..., filters: _Optional[_Union[ListEntriesInput.Filter, _Mapping]] = ...) -> None: ...

class ListEntriesOutput(_message.Message):
    __slots__ = ("total", "items", "next_page_cursor")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_entry_pb2.Entry]
    next_page_cursor: str
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_entry_pb2.Entry, _Mapping]]] = ..., next_page_cursor: _Optional[str] = ...) -> None: ...
