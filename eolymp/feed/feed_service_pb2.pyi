from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.feed import entry_pb2 as _entry_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListEntriesInput(_message.Message):
    __slots__ = ["after", "size"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    after: str
    size: int
    def __init__(self, size: _Optional[int] = ..., after: _Optional[str] = ...) -> None: ...

class ListEntriesOutput(_message.Message):
    __slots__ = ["items", "next_page_cursor", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_entry_pb2.Entry]
    next_page_cursor: str
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_entry_pb2.Entry, _Mapping]]] = ..., next_page_cursor: _Optional[str] = ...) -> None: ...
