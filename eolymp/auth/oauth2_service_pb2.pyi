from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.auth import claims_pb2 as _claims_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IssueTokenInput(_message.Message):
    __slots__ = ("grant_type", "username", "password", "client_id", "client_secret", "code", "code_verifier", "scope", "refresh_token", "redirect_uri")
    class GrantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[IssueTokenInput.GrantType]
        PASSWORD: _ClassVar[IssueTokenInput.GrantType]
        AUTHORIZATION_CODE: _ClassVar[IssueTokenInput.GrantType]
        REFRESH_TOKEN: _ClassVar[IssueTokenInput.GrantType]
        EOLYMP_SIGNIN: _ClassVar[IssueTokenInput.GrantType]
    NONE: IssueTokenInput.GrantType
    PASSWORD: IssueTokenInput.GrantType
    AUTHORIZATION_CODE: IssueTokenInput.GrantType
    REFRESH_TOKEN: IssueTokenInput.GrantType
    EOLYMP_SIGNIN: IssueTokenInput.GrantType
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    grant_type: IssueTokenInput.GrantType
    username: str
    password: str
    client_id: str
    client_secret: str
    code: str
    code_verifier: str
    scope: str
    refresh_token: str
    redirect_uri: str
    def __init__(self, grant_type: _Optional[_Union[IssueTokenInput.GrantType, str]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., code: _Optional[str] = ..., code_verifier: _Optional[str] = ..., scope: _Optional[str] = ..., refresh_token: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...

class IssueTokenOutput(_message.Message):
    __slots__ = ("access_token", "token_type", "expires_in", "refresh_token", "scope", "claims", "id_token")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    ID_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str
    claims: _claims_pb2.Claims
    id_token: str
    def __init__(self, access_token: _Optional[str] = ..., token_type: _Optional[str] = ..., expires_in: _Optional[int] = ..., refresh_token: _Optional[str] = ..., scope: _Optional[str] = ..., claims: _Optional[_Union[_claims_pb2.Claims, _Mapping]] = ..., id_token: _Optional[str] = ...) -> None: ...

class IntrospectTokenInput(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class IntrospectTokenOutput(_message.Message):
    __slots__ = ("active", "scope", "expire", "claims")
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_FIELD_NUMBER: _ClassVar[int]
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    active: bool
    scope: str
    expire: _timestamp_pb2.Timestamp
    claims: _claims_pb2.Claims
    def __init__(self, active: bool = ..., scope: _Optional[str] = ..., expire: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., claims: _Optional[_Union[_claims_pb2.Claims, _Mapping]] = ...) -> None: ...

class RevokeTokenInput(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class RevokeTokenOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestAuthInput(_message.Message):
    __slots__ = ("client_id", "code_challenge", "code_challenge_method", "redirect_uri", "response_type", "scope", "state")
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

class RequestAuthOutput(_message.Message):
    __slots__ = ("authorization_code", "redirect_uri")
    AUTHORIZATION_CODE_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    authorization_code: str
    redirect_uri: str
    def __init__(self, authorization_code: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...

class UserInfoInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UserInfoOutput(_message.Message):
    __slots__ = ("claims",)
    CLAIMS_FIELD_NUMBER: _ClassVar[int]
    claims: _claims_pb2.Claims
    def __init__(self, claims: _Optional[_Union[_claims_pb2.Claims, _Mapping]] = ...) -> None: ...
