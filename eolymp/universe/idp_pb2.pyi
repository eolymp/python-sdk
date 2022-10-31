from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IdentityProvider(_message.Message):
    __slots__ = []
    class OIDC(_message.Message):
        __slots__ = ["authorize_endpoint", "client_id", "client_secret", "keys_endpoint", "token_endpoint", "userinfo_endpoint"]
        AUTHORIZE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        KEYS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        USERINFO_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        authorize_endpoint: str
        client_id: str
        client_secret: str
        keys_endpoint: str
        token_endpoint: str
        userinfo_endpoint: str
        def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., authorize_endpoint: _Optional[str] = ..., token_endpoint: _Optional[str] = ..., keys_endpoint: _Optional[str] = ..., userinfo_endpoint: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
