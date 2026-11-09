from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.content import sitemap_pb2 as _sitemap_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListSitemapChunksInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSitemapChunksOutput(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_sitemap_pb2.Sitemap.Chunk]
    def __init__(self, items: _Optional[_Iterable[_Union[_sitemap_pb2.Sitemap.Chunk, _Mapping]]] = ...) -> None: ...

class DescribeSitemapChunkInput(_message.Message):
    __slots__ = ("chunk_id",)
    CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    chunk_id: str
    def __init__(self, chunk_id: _Optional[str] = ...) -> None: ...

class DescribeSitemapChunkOutput(_message.Message):
    __slots__ = ("chunk", "entries")
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    chunk: _sitemap_pb2.Sitemap.Chunk
    entries: _containers.RepeatedCompositeFieldContainer[_sitemap_pb2.Sitemap.Entry]
    def __init__(self, chunk: _Optional[_Union[_sitemap_pb2.Sitemap.Chunk, _Mapping]] = ..., entries: _Optional[_Iterable[_Union[_sitemap_pb2.Sitemap.Entry, _Mapping]]] = ...) -> None: ...
