from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import generation_pb2 as _generation_pb2
from eolymp.wellknown import watch_pb2 as _watch_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeGenerationInput(_message.Message):
    __slots__ = ("problem_id", "generation_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    generation_id: str
    def __init__(self, problem_id: _Optional[str] = ..., generation_id: _Optional[str] = ...) -> None: ...

class DescribeGenerationOutput(_message.Message):
    __slots__ = ("generation",)
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    generation: _generation_pb2.Generation
    def __init__(self, generation: _Optional[_Union[_generation_pb2.Generation, _Mapping]] = ...) -> None: ...

class ListGenerationsInput(_message.Message):
    __slots__ = ("problem_id", "offset", "size")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    offset: int
    size: int
    def __init__(self, problem_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListGenerationsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_generation_pb2.Generation]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_generation_pb2.Generation, _Mapping]]] = ...) -> None: ...

class WatchGenerationInput(_message.Message):
    __slots__ = ("problem_id", "generation_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    generation_id: str
    def __init__(self, problem_id: _Optional[str] = ..., generation_id: _Optional[str] = ...) -> None: ...

class WatchGenerationOutput(_message.Message):
    __slots__ = ("generation", "event")
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    generation: _generation_pb2.Generation
    event: _watch_pb2.WatchEventType
    def __init__(self, generation: _Optional[_Union[_generation_pb2.Generation, _Mapping]] = ..., event: _Optional[_Union[_watch_pb2.WatchEventType, str]] = ...) -> None: ...
