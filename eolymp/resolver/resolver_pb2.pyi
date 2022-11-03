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
    __slots__ = []
    class OAuth2(_message.Message):
        __slots__ = ["authorize_endpoint", "client_id", "signout_endpoint", "token_endpoint", "userinfo_endpoint"]
        AUTHORIZE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        SIGNOUT_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        USERINFO_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        authorize_endpoint: str
        client_id: str
        signout_endpoint: str
        token_endpoint: str
        userinfo_endpoint: str
        def __init__(self, client_id: _Optional[str] = ..., token_endpoint: _Optional[str] = ..., authorize_endpoint: _Optional[str] = ..., userinfo_endpoint: _Optional[str] = ..., signout_endpoint: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class Record(_message.Message):
    __slots__ = ["target"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Target(_message.Message):
        __slots__ = ["type", "url"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        type: Record.Type
        url: str
        def __init__(self, type: _Optional[_Union[Record.Type, str]] = ..., url: _Optional[str] = ...) -> None: ...
    CONTEST: Record.Type
    SCOREBOARD: Record.Type
    SPACE: Record.Type
    TARGET_FIELD_NUMBER: _ClassVar[int]
    UNSPECIFIED: Record.Type
    target: Record.Target
    def __init__(self, target: _Optional[_Union[Record.Target, _Mapping]] = ...) -> None: ...

class ResolveNameInput(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResolveNameOutput(_message.Message):
    __slots__ = ["contest", "oauth2", "scoreboard", "space", "target"]
    CONTEST_FIELD_NUMBER: _ClassVar[int]
    OAUTH2_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    contest: _contest_pb2.Contest
    oauth2: Authorization.OAuth2
    scoreboard: _scoreboard_pb2.Scoreboard
    space: _space_pb2.Space
    target: Record.Target
    def __init__(self, target: _Optional[_Union[Record.Target, _Mapping]] = ..., space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., contest: _Optional[_Union[_contest_pb2.Contest, _Mapping]] = ..., scoreboard: _Optional[_Union[_scoreboard_pb2.Scoreboard, _Mapping]] = ..., oauth2: _Optional[_Union[Authorization.OAuth2, _Mapping]] = ...) -> None: ...
