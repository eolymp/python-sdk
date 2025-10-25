import datetime

from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.auth import certificate_pb2 as _certificate_pb2
from eolymp.auth import claims_pb2 as _claims_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

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
    def __init__(self, active: bool = ..., scope: _Optional[str] = ..., expire: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., claims: _Optional[_Union[_claims_pb2.Claims, _Mapping]] = ...) -> None: ...

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

class ListCertificatesInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCertificatesOutput(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_certificate_pb2.Certificate]
    def __init__(self, items: _Optional[_Iterable[_Union[_certificate_pb2.Certificate, _Mapping]]] = ...) -> None: ...

class RegisterClientInput(_message.Message):
    __slots__ = ("redirect_uris", "token_endpoint_auth_method", "grant_types", "response_types", "client_name", "client_uri", "logo_uri", "scope", "contacts", "tos_uri", "policy_uri", "jwks_uri", "software_id", "software_version", "software_statement")
    REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ENDPOINT_AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_URI_FIELD_NUMBER: _ClassVar[int]
    LOGO_URI_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    TOS_URI_FIELD_NUMBER: _ClassVar[int]
    POLICY_URI_FIELD_NUMBER: _ClassVar[int]
    JWKS_URI_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_ID_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    token_endpoint_auth_method: str
    grant_types: _containers.RepeatedScalarFieldContainer[str]
    response_types: _containers.RepeatedScalarFieldContainer[str]
    client_name: str
    client_uri: str
    logo_uri: str
    scope: str
    contacts: _containers.RepeatedScalarFieldContainer[str]
    tos_uri: str
    policy_uri: str
    jwks_uri: str
    software_id: str
    software_version: str
    software_statement: str
    def __init__(self, redirect_uris: _Optional[_Iterable[str]] = ..., token_endpoint_auth_method: _Optional[str] = ..., grant_types: _Optional[_Iterable[str]] = ..., response_types: _Optional[_Iterable[str]] = ..., client_name: _Optional[str] = ..., client_uri: _Optional[str] = ..., logo_uri: _Optional[str] = ..., scope: _Optional[str] = ..., contacts: _Optional[_Iterable[str]] = ..., tos_uri: _Optional[str] = ..., policy_uri: _Optional[str] = ..., jwks_uri: _Optional[str] = ..., software_id: _Optional[str] = ..., software_version: _Optional[str] = ..., software_statement: _Optional[str] = ...) -> None: ...

class RegisterClientOutput(_message.Message):
    __slots__ = ("client_id", "client_secret", "client_id_issued_at", "client_secret_expires_at", "registration_access_token", "registration_client_uri", "token_endpoint_auth_method", "application_type", "redirect_uris", "client_name", "logo_uri", "subject_type", "sector_identifier_uri", "jwks_uri", "userinfo_encrypted_response_alg", "userinfo_encrypted_response_enc", "contacts", "request_uris")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_CLIENT_URI_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ENDPOINT_AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_URI_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SECTOR_IDENTIFIER_URI_FIELD_NUMBER: _ClassVar[int]
    JWKS_URI_FIELD_NUMBER: _ClassVar[int]
    USERINFO_ENCRYPTED_RESPONSE_ALG_FIELD_NUMBER: _ClassVar[int]
    USERINFO_ENCRYPTED_RESPONSE_ENC_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_URIS_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    client_id_issued_at: _timestamp_pb2.Timestamp
    client_secret_expires_at: _timestamp_pb2.Timestamp
    registration_access_token: str
    registration_client_uri: str
    token_endpoint_auth_method: str
    application_type: str
    redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    client_name: str
    logo_uri: str
    subject_type: str
    sector_identifier_uri: str
    jwks_uri: str
    userinfo_encrypted_response_alg: str
    userinfo_encrypted_response_enc: str
    contacts: _containers.RepeatedScalarFieldContainer[str]
    request_uris: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., client_id_issued_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., client_secret_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., registration_access_token: _Optional[str] = ..., registration_client_uri: _Optional[str] = ..., token_endpoint_auth_method: _Optional[str] = ..., application_type: _Optional[str] = ..., redirect_uris: _Optional[_Iterable[str]] = ..., client_name: _Optional[str] = ..., logo_uri: _Optional[str] = ..., subject_type: _Optional[str] = ..., sector_identifier_uri: _Optional[str] = ..., jwks_uri: _Optional[str] = ..., userinfo_encrypted_response_alg: _Optional[str] = ..., userinfo_encrypted_response_enc: _Optional[str] = ..., contacts: _Optional[_Iterable[str]] = ..., request_uris: _Optional[_Iterable[str]] = ...) -> None: ...
