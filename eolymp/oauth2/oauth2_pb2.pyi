from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthCodeInput(_message.Message):
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

class AuthCodeOutput(_message.Message):
    __slots__ = ["authorization_code", "redirect_uri"]
    AUTHORIZATION_CODE_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    authorization_code: str
    redirect_uri: str
    def __init__(self, authorization_code: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...

class AuthorizeInput(_message.Message):
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

class AuthorizeOutput(_message.Message):
    __slots__ = ["redirect_uri"]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    redirect_uri: str
    def __init__(self, redirect_uri: _Optional[str] = ...) -> None: ...

class CallbackInput(_message.Message):
    __slots__ = ["code", "state"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str
    def __init__(self, code: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class CallbackOutput(_message.Message):
    __slots__ = ["redirect_uri"]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    redirect_uri: str
    def __init__(self, redirect_uri: _Optional[str] = ...) -> None: ...

class IntrospectInput(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class IntrospectOutput(_message.Message):
    __slots__ = ["active", "audience", "email", "email_verified", "expire", "issuer", "locale", "name", "nickname", "picture", "scope", "subject"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    active: bool
    audience: str
    email: str
    email_verified: bool
    expire: _timestamp_pb2.Timestamp
    issuer: str
    locale: str
    name: str
    nickname: str
    picture: str
    scope: str
    subject: str
    def __init__(self, active: bool = ..., scope: _Optional[str] = ..., expire: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., subject: _Optional[str] = ..., audience: _Optional[str] = ..., issuer: _Optional[str] = ..., name: _Optional[str] = ..., nickname: _Optional[str] = ..., picture: _Optional[str] = ..., email: _Optional[str] = ..., email_verified: bool = ..., locale: _Optional[str] = ...) -> None: ...

class RevokeInput(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class RevokeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TokenInput(_message.Message):
    __slots__ = ["client_id", "client_secret", "code", "code_verifier", "grant_type", "password", "redirect_uri", "refresh_token", "scope", "username"]
    class GrantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHORIZATION_CODE: TokenInput.GrantType
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CODE: TokenInput.GrantType
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NONE: TokenInput.GrantType
    PASSWORD: TokenInput.GrantType
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN: TokenInput.GrantType
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    code: str
    code_verifier: str
    grant_type: TokenInput.GrantType
    password: str
    redirect_uri: str
    refresh_token: str
    scope: str
    username: str
    def __init__(self, grant_type: _Optional[_Union[TokenInput.GrantType, str]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., code: _Optional[str] = ..., code_verifier: _Optional[str] = ..., scope: _Optional[str] = ..., refresh_token: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...

class TokenOutput(_message.Message):
    __slots__ = ["access_token", "email", "email_verified", "expires_in", "id_token", "issuer", "name", "nickname", "picture", "refresh_token", "scope", "subject", "token_type"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    email: str
    email_verified: bool
    expires_in: int
    id_token: str
    issuer: str
    name: str
    nickname: str
    picture: str
    refresh_token: str
    scope: str
    subject: str
    token_type: str
    def __init__(self, access_token: _Optional[str] = ..., token_type: _Optional[str] = ..., expires_in: _Optional[int] = ..., refresh_token: _Optional[str] = ..., scope: _Optional[str] = ..., id_token: _Optional[str] = ..., subject: _Optional[str] = ..., issuer: _Optional[str] = ..., name: _Optional[str] = ..., nickname: _Optional[str] = ..., picture: _Optional[str] = ..., email: _Optional[str] = ..., email_verified: bool = ...) -> None: ...

class UserInfoInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UserInfoOutput(_message.Message):
    __slots__ = ["email", "email_verified", "family_name", "given_name", "issuer", "locale", "middle_name", "name", "nickname", "picture", "profile", "subject"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    GIVEN_NAME_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    email: str
    email_verified: bool
    family_name: str
    given_name: str
    issuer: str
    locale: str
    middle_name: str
    name: str
    nickname: str
    picture: str
    profile: str
    subject: str
    def __init__(self, issuer: _Optional[str] = ..., subject: _Optional[str] = ..., name: _Optional[str] = ..., given_name: _Optional[str] = ..., family_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., nickname: _Optional[str] = ..., picture: _Optional[str] = ..., email: _Optional[str] = ..., email_verified: bool = ..., locale: _Optional[str] = ..., profile: _Optional[str] = ...) -> None: ...
