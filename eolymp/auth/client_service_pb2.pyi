import datetime

from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.auth import client_pb2 as _client_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListClientsInput(_message.Message):
    __slots__ = ("offset", "size")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListClientsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_client_pb2.Client]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_client_pb2.Client, _Mapping]]] = ...) -> None: ...

class DescribeClientInput(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class DescribeClientOutput(_message.Message):
    __slots__ = ("client",)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: _client_pb2.Client
    def __init__(self, client: _Optional[_Union[_client_pb2.Client, _Mapping]] = ...) -> None: ...

class CreateClientInput(_message.Message):
    __slots__ = ("client",)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: _client_pb2.Client
    def __init__(self, client: _Optional[_Union[_client_pb2.Client, _Mapping]] = ...) -> None: ...

class CreateClientOutput(_message.Message):
    __slots__ = ("client_id", "secret")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    secret: str
    def __init__(self, client_id: _Optional[str] = ..., secret: _Optional[str] = ...) -> None: ...

class UpdateClientInput(_message.Message):
    __slots__ = ("patch", "client_id", "client")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_client_pb2.Client.Patch.Field]
    client_id: str
    client: _client_pb2.Client
    def __init__(self, patch: _Optional[_Iterable[_Union[_client_pb2.Client.Patch.Field, str]]] = ..., client_id: _Optional[str] = ..., client: _Optional[_Union[_client_pb2.Client, _Mapping]] = ...) -> None: ...

class UpdateClientOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteClientInput(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class DeleteClientOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetClientSecretInput(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class ResetClientSecretOutput(_message.Message):
    __slots__ = ("secret",)
    SECRET_FIELD_NUMBER: _ClassVar[int]
    secret: str
    def __init__(self, secret: _Optional[str] = ...) -> None: ...

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
