from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.discord import connection_pb2 as _connection_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeConnectionInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeConnectionOutput(_message.Message):
    __slots__ = ("connection",)
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    connection: _connection_pb2.Connection
    def __init__(self, connection: _Optional[_Union[_connection_pb2.Connection, _Mapping]] = ...) -> None: ...

class UpdateConnectionInput(_message.Message):
    __slots__ = ("connection",)
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    connection: _connection_pb2.Connection.Patch
    def __init__(self, connection: _Optional[_Union[_connection_pb2.Connection.Patch, _Mapping]] = ...) -> None: ...

class UpdateConnectionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteConnectionInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteConnectionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListChannelsInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListChannelsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_connection_pb2.Channel]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_connection_pb2.Channel, _Mapping]]] = ...) -> None: ...

class PostMessageInput(_message.Message):
    __slots__ = ("channel_id", "title", "content", "validate_only")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    title: str
    content: _content_pb2.Content
    validate_only: bool
    def __init__(self, channel_id: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., validate_only: _Optional[bool] = ...) -> None: ...

class PostMessageOutput(_message.Message):
    __slots__ = ("message_id", "url")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    url: str
    def __init__(self, message_id: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
