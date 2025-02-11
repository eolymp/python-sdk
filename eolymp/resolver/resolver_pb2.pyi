from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.judge import contest_pb2 as _contest_pb2
from eolymp.ranker import scoreboard_pb2 as _scoreboard_pb2
from eolymp.universe import space_pb2 as _space_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Authorization(_message.Message):
    __slots__ = ()
    class OAuth2(_message.Message):
        __slots__ = ("client_id", "token_endpoint", "authorize_endpoint", "userinfo_endpoint", "signout_endpoint")
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        AUTHORIZE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        USERINFO_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        SIGNOUT_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        client_id: str
        token_endpoint: str
        authorize_endpoint: str
        userinfo_endpoint: str
        signout_endpoint: str
        def __init__(self, client_id: _Optional[str] = ..., token_endpoint: _Optional[str] = ..., authorize_endpoint: _Optional[str] = ..., userinfo_endpoint: _Optional[str] = ..., signout_endpoint: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class Record(_message.Message):
    __slots__ = ("target",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[Record.Type]
        SPACE: _ClassVar[Record.Type]
        CONTEST: _ClassVar[Record.Type]
        SCOREBOARD: _ClassVar[Record.Type]
    UNSPECIFIED: Record.Type
    SPACE: Record.Type
    CONTEST: Record.Type
    SCOREBOARD: Record.Type
    class Target(_message.Message):
        __slots__ = ("type", "url")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        type: Record.Type
        url: str
        def __init__(self, type: _Optional[_Union[Record.Type, str]] = ..., url: _Optional[str] = ...) -> None: ...
    TARGET_FIELD_NUMBER: _ClassVar[int]
    target: Record.Target
    def __init__(self, target: _Optional[_Union[Record.Target, _Mapping]] = ...) -> None: ...

class ResolveNameInput(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResolveNameOutput(_message.Message):
    __slots__ = ("target", "space", "contest", "scoreboard", "oauth2")
    TARGET_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    CONTEST_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    OAUTH2_FIELD_NUMBER: _ClassVar[int]
    target: Record.Target
    space: _space_pb2.Space
    contest: _contest_pb2.Contest
    scoreboard: _scoreboard_pb2.Scoreboard
    oauth2: Authorization.OAuth2
    def __init__(self, target: _Optional[_Union[Record.Target, _Mapping]] = ..., space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., contest: _Optional[_Union[_contest_pb2.Contest, _Mapping]] = ..., scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ..., oauth2: _Optional[_Union[Authorization.OAuth2, _Mapping]] = ...) -> None: ...
