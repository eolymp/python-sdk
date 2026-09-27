from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import topic_pb2 as _topic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeTopicInput(_message.Message):
    __slots__ = ("topic_id", "locale", "extra")
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_topic_pb2.Topic.Extra]
    def __init__(self, topic_id: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_topic_pb2.Topic.Extra, str]]] = ...) -> None: ...

class DescribeTopicOutput(_message.Message):
    __slots__ = ("topic",)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: _topic_pb2.Topic
    def __init__(self, topic: _Optional[_Union[_topic_pb2.Topic, _Mapping]] = ...) -> None: ...

class ListTopicsInput(_message.Message):
    __slots__ = ("offset", "size", "locale", "search", "extra")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    locale: str
    search: str
    extra: _containers.RepeatedScalarFieldContainer[_topic_pb2.Topic.Extra]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., locale: _Optional[str] = ..., search: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_topic_pb2.Topic.Extra, str]]] = ...) -> None: ...

class ListTopicsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_topic_pb2.Topic]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_topic_pb2.Topic, _Mapping]]] = ...) -> None: ...

class CreateTopicInput(_message.Message):
    __slots__ = ("topic",)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: _topic_pb2.Topic
    def __init__(self, topic: _Optional[_Union[_topic_pb2.Topic, _Mapping]] = ...) -> None: ...

class CreateTopicOutput(_message.Message):
    __slots__ = ("topic_id",)
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    def __init__(self, topic_id: _Optional[str] = ...) -> None: ...

class UpdateTopicInput(_message.Message):
    __slots__ = ("topic_id", "topic")
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    topic: _topic_pb2.Topic
    def __init__(self, topic_id: _Optional[str] = ..., topic: _Optional[_Union[_topic_pb2.Topic, _Mapping]] = ...) -> None: ...

class UpdateTopicOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTopicInput(_message.Message):
    __slots__ = ("topic_id",)
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    def __init__(self, topic_id: _Optional[str] = ...) -> None: ...

class DeleteTopicOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
