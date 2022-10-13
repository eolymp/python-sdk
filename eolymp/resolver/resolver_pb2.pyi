from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Record(_message.Message):
    __slots__ = ["auth", "key", "space_id", "summary", "target"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Auth(_message.Message):
        __slots__ = ["authorize_url", "client_id", "client_secret", "scopes", "token_url"]
        AUTHORIZE_URL_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        SCOPES_FIELD_NUMBER: _ClassVar[int]
        TOKEN_URL_FIELD_NUMBER: _ClassVar[int]
        authorize_url: str
        client_id: str
        client_secret: str
        scopes: str
        token_url: str
        def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., scopes: _Optional[str] = ..., token_url: _Optional[str] = ..., authorize_url: _Optional[str] = ...) -> None: ...
    class Target(_message.Message):
        __slots__ = ["type", "url"]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        type: Record.Type
        url: str
        def __init__(self, type: _Optional[_Union[Record.Type, str]] = ..., url: _Optional[str] = ...) -> None: ...
    AUTH_FIELD_NUMBER: _ClassVar[int]
    CONTEST: Record.Type
    KEY_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD: Record.Type
    SPACE: Record.Type
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    UNSPECIFIED: Record.Type
    auth: Record.Auth
    key: str
    space_id: str
    summary: str
    target: Record.Target
    def __init__(self, key: _Optional[str] = ..., space_id: _Optional[str] = ..., summary: _Optional[str] = ..., auth: _Optional[_Union[Record.Auth, _Mapping]] = ..., target: _Optional[_Union[Record.Target, _Mapping]] = ...) -> None: ...

class ResolveNameInput(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ResolveNameOutput(_message.Message):
    __slots__ = ["auth", "target"]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    auth: Record.Auth
    target: Record.Target
    def __init__(self, auth: _Optional[_Union[Record.Auth, _Mapping]] = ..., target: _Optional[_Union[Record.Target, _Mapping]] = ...) -> None: ...
