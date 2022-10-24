from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Authentication(_message.Message):
    __slots__ = []
    class OAuth2(_message.Message):
        __slots__ = ["authorize_url", "client_id", "client_secret", "introspect_url", "scopes", "signout_url", "token_url"]
        AUTHORIZE_URL_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        INTROSPECT_URL_FIELD_NUMBER: _ClassVar[int]
        SCOPES_FIELD_NUMBER: _ClassVar[int]
        SIGNOUT_URL_FIELD_NUMBER: _ClassVar[int]
        TOKEN_URL_FIELD_NUMBER: _ClassVar[int]
        authorize_url: str
        client_id: str
        client_secret: str
        introspect_url: str
        scopes: str
        signout_url: str
        token_url: str
        def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., scopes: _Optional[str] = ..., authorize_url: _Optional[str] = ..., token_url: _Optional[str] = ..., introspect_url: _Optional[str] = ..., signout_url: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
