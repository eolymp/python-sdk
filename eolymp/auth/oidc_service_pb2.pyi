from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteLoginInput(_message.Message):
    __slots__ = ["code", "state"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str
    def __init__(self, code: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class CompleteLoginOutput(_message.Message):
    __slots__ = ["access_token", "expires_in", "id_token", "refresh_token", "scope", "token_type"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    expires_in: int
    id_token: str
    refresh_token: str
    scope: str
    token_type: str
    def __init__(self, access_token: _Optional[str] = ..., token_type: _Optional[str] = ..., expires_in: _Optional[int] = ..., refresh_token: _Optional[str] = ..., scope: _Optional[str] = ..., id_token: _Optional[str] = ...) -> None: ...

class InitiateLoginInput(_message.Message):
    __slots__ = ["scope", "state"]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    scope: str
    state: str
    def __init__(self, scope: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class InitiateLoginOutput(_message.Message):
    __slots__ = ["login_url"]
    LOGIN_URL_FIELD_NUMBER: _ClassVar[int]
    login_url: str
    def __init__(self, login_url: _Optional[str] = ...) -> None: ...
