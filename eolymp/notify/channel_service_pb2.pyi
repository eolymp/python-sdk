from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.notify import channel_pb2 as _channel_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateChannelInput(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: _channel_pb2.Channel
    def __init__(self, channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]] = ...) -> None: ...

class CreateChannelOutput(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class UpdateChannelInput(_message.Message):
    __slots__ = ("channel_id", "channel")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    channel: _channel_pb2.Channel.Patch
    def __init__(self, channel_id: _Optional[str] = ..., channel: _Optional[_Union[_channel_pb2.Channel.Patch, _Mapping]] = ...) -> None: ...

class UpdateChannelOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteChannelInput(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class DeleteChannelOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeChannelInput(_message.Message):
    __slots__ = ("channel_id",)
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    def __init__(self, channel_id: _Optional[str] = ...) -> None: ...

class DescribeChannelOutput(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: _channel_pb2.Channel
    def __init__(self, channel: _Optional[_Union[_channel_pb2.Channel, _Mapping]] = ...) -> None: ...

class ListChannelsInput(_message.Message):
    __slots__ = ("offset", "size", "search", "filters")
    class Filter(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    search: str
    filters: ListChannelsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListChannelsInput.Filter, _Mapping]] = ...) -> None: ...

class ListChannelsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_channel_pb2.Channel]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_channel_pb2.Channel, _Mapping]]] = ...) -> None: ...
