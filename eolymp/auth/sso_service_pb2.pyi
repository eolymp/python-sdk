from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.auth import linked_account_pb2 as _linked_account_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignonRequestInput(_message.Message):
    __slots__ = ("type", "callback_uri", "code_challenge", "code_challenge_method")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_URI_FIELD_NUMBER: _ClassVar[int]
    CODE_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    CODE_CHALLENGE_METHOD_FIELD_NUMBER: _ClassVar[int]
    type: _linked_account_pb2.LinkedAccount.Type
    callback_uri: str
    code_challenge: str
    code_challenge_method: str
    def __init__(self, type: _Optional[_Union[_linked_account_pb2.LinkedAccount.Type, str]] = ..., callback_uri: _Optional[str] = ..., code_challenge: _Optional[str] = ..., code_challenge_method: _Optional[str] = ...) -> None: ...

class SignonRequestOutput(_message.Message):
    __slots__ = ("redirect_uri",)
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    redirect_uri: str
    def __init__(self, redirect_uri: _Optional[str] = ...) -> None: ...

class SignonExchangeInput(_message.Message):
    __slots__ = ("state", "code", "code_verifier")
    STATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    state: str
    code: str
    code_verifier: str
    def __init__(self, state: _Optional[str] = ..., code: _Optional[str] = ..., code_verifier: _Optional[str] = ...) -> None: ...

class SignonExchangeOutput(_message.Message):
    __slots__ = ("access_token", "token_type", "expires_in", "refresh_token")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    def __init__(self, access_token: _Optional[str] = ..., token_type: _Optional[str] = ..., expires_in: _Optional[int] = ..., refresh_token: _Optional[str] = ...) -> None: ...
