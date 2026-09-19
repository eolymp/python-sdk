import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Channel(_message.Message):
    __slots__ = ("id", "name", "discord", "created_at")
    class Discord(_message.Message):
        __slots__ = ("channel_id", "channel_name")
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        channel_id: str
        channel_name: str
        def __init__(self, channel_id: _Optional[str] = ..., channel_name: _Optional[str] = ...) -> None: ...
    class Patch(_message.Message):
        __slots__ = ("name", "discord")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISCORD_FIELD_NUMBER: _ClassVar[int]
        name: str
        discord: Channel.Discord
        def __init__(self, name: _Optional[str] = ..., discord: _Optional[_Union[Channel.Discord, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISCORD_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    discord: Channel.Discord
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., discord: _Optional[_Union[Channel.Discord, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
