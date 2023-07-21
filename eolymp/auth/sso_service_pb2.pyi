from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AuthorizeCallbackInput(_message.Message):
    __slots__ = ["code", "state"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str
    def __init__(self, code: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class AuthorizeCallbackOutput(_message.Message):
    __slots__ = ["redirect_uri"]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    redirect_uri: str
    def __init__(self, redirect_uri: _Optional[str] = ...) -> None: ...

class AuthorizeRequestInput(_message.Message):
    __slots__ = ["client_id", "code_challenge", "code_challenge_method", "redirect_uri", "response_type", "scope", "state"]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    CODE_CHALLENGE_METHOD_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    code_challenge: str
    code_challenge_method: str
    redirect_uri: str
    response_type: str
    scope: str
    state: str
    def __init__(self, client_id: _Optional[str] = ..., code_challenge: _Optional[str] = ..., code_challenge_method: _Optional[str] = ..., redirect_uri: _Optional[str] = ..., response_type: _Optional[str] = ..., scope: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class AuthorizeRequestOutput(_message.Message):
    __slots__ = ["redirect_uri"]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    redirect_uri: str
    def __init__(self, redirect_uri: _Optional[str] = ...) -> None: ...
