import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Connection(_message.Message):
    __slots__ = ("token_set", "guild_id", "guild_name", "bot_username", "connected_at")
    class Patch(_message.Message):
        __slots__ = ("bot_token", "guild_id")
        BOT_TOKEN_FIELD_NUMBER: _ClassVar[int]
        GUILD_ID_FIELD_NUMBER: _ClassVar[int]
        bot_token: str
        guild_id: str
        def __init__(self, bot_token: _Optional[str] = ..., guild_id: _Optional[str] = ...) -> None: ...
    TOKEN_SET_FIELD_NUMBER: _ClassVar[int]
    GUILD_ID_FIELD_NUMBER: _ClassVar[int]
    GUILD_NAME_FIELD_NUMBER: _ClassVar[int]
    BOT_USERNAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_AT_FIELD_NUMBER: _ClassVar[int]
    token_set: bool
    guild_id: str
    guild_name: str
    bot_username: str
    connected_at: _timestamp_pb2.Timestamp
    def __init__(self, token_set: _Optional[bool] = ..., guild_id: _Optional[str] = ..., guild_name: _Optional[str] = ..., bot_username: _Optional[str] = ..., connected_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Channel(_message.Message):
    __slots__ = ("id", "name", "writable")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WRITABLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    writable: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., writable: _Optional[bool] = ...) -> None: ...
