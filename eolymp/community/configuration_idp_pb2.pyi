from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IdentityProvider(_message.Message):
    __slots__ = []
    class Basecamp(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Local(_message.Message):
        __slots__ = ["allow_modify_basics", "allow_modify_email", "allow_modify_nickname", "allow_modify_password"]
        ALLOW_MODIFY_BASICS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_MODIFY_EMAIL_FIELD_NUMBER: _ClassVar[int]
        ALLOW_MODIFY_NICKNAME_FIELD_NUMBER: _ClassVar[int]
        ALLOW_MODIFY_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        allow_modify_basics: bool
        allow_modify_email: bool
        allow_modify_nickname: bool
        allow_modify_password: bool
        def __init__(self, allow_modify_nickname: bool = ..., allow_modify_basics: bool = ..., allow_modify_email: bool = ..., allow_modify_password: bool = ...) -> None: ...
    class OIDC(_message.Message):
        __slots__ = ["authorize_endpoint", "client_id", "client_secret", "issuer", "keys_endpoint", "redirect_uri", "token_endpoint", "userinfo_endpoint"]
        AUTHORIZE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        ISSUER_FIELD_NUMBER: _ClassVar[int]
        KEYS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
        TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        USERINFO_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        authorize_endpoint: str
        client_id: str
        client_secret: str
        issuer: str
        keys_endpoint: str
        redirect_uri: str
        token_endpoint: str
        userinfo_endpoint: str
        def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., issuer: _Optional[str] = ..., authorize_endpoint: _Optional[str] = ..., token_endpoint: _Optional[str] = ..., keys_endpoint: _Optional[str] = ..., userinfo_endpoint: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...
