from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.auth import linked_account_pb2 as _linked_account_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignonRequestInput(_message.Message):
    __slots__ = ("provider_id", "client_id", "redirect_uri", "type", "callback_uri")
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_URI_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    client_id: str
    redirect_uri: str
    type: _linked_account_pb2.LinkedAccount.Type
    callback_uri: str
    def __init__(self, provider_id: _Optional[str] = ..., client_id: _Optional[str] = ..., redirect_uri: _Optional[str] = ..., type: _Optional[_Union[_linked_account_pb2.LinkedAccount.Type, str]] = ..., callback_uri: _Optional[str] = ...) -> None: ...

class SignonRequestOutput(_message.Message):
    __slots__ = ("redirect_uri",)
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    redirect_uri: str
    def __init__(self, redirect_uri: _Optional[str] = ...) -> None: ...

class SignonExchangeInput(_message.Message):
    __slots__ = ("code", "state", "client_id", "client_secret")
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str
    client_id: str
    client_secret: str
    def __init__(self, code: _Optional[str] = ..., state: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ...) -> None: ...

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
