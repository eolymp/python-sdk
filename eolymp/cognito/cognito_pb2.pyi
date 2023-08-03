from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.cognito import access_key_pb2 as _access_key_pb2
from eolymp.cognito import quota_pb2 as _quota_pb2
from eolymp.cognito import user_pb2 as _user_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteRecoverInput(_message.Message):
    __slots__ = ["password", "secret", "user_id"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    password: str
    secret: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., secret: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class CompleteRecoverOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateAccessKeyInput(_message.Message):
    __slots__ = ["expires_in", "name", "scope"]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    expires_in: int
    name: str
    scope: str
    def __init__(self, name: _Optional[str] = ..., scope: _Optional[str] = ..., expires_in: _Optional[int] = ...) -> None: ...

class CreateAccessKeyOutput(_message.Message):
    __slots__ = ["key_id", "secret"]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    secret: str
    def __init__(self, key_id: _Optional[str] = ..., secret: _Optional[str] = ...) -> None: ...

class CreateAuthorizationInput(_message.Message):
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

class CreateAuthorizationOutput(_message.Message):
    __slots__ = ["authorization_code", "redirect_uri"]
    AUTHORIZATION_CODE_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    authorization_code: str
    redirect_uri: str
    def __init__(self, authorization_code: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...

class CreateTokenInput(_message.Message):
    __slots__ = ["client_id", "client_secret", "code", "code_verifier", "grant_type", "password", "refresh_token", "scope", "username"]
    class GrantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHORIZATION_CODE: CreateTokenInput.GrantType
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CODE: CreateTokenInput.GrantType
    GRANT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NONE: CreateTokenInput.GrantType
    PASSWORD: CreateTokenInput.GrantType
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN: CreateTokenInput.GrantType
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    code: str
    code_verifier: str
    grant_type: CreateTokenInput.GrantType
    password: str
    refresh_token: str
    scope: str
    username: str
    def __init__(self, grant_type: _Optional[_Union[CreateTokenInput.GrantType, str]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., code: _Optional[str] = ..., code_verifier: _Optional[str] = ..., scope: _Optional[str] = ..., refresh_token: _Optional[str] = ...) -> None: ...

class CreateTokenOutput(_message.Message):
    __slots__ = ["expires_at", "refresh_token", "scopes", "token", "type", "user_id", "username"]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    expires_at: _timestamp_pb2.Timestamp
    refresh_token: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    token: str
    type: str
    user_id: str
    username: str
    def __init__(self, token: _Optional[str] = ..., type: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., scopes: _Optional[_Iterable[str]] = ..., refresh_token: _Optional[str] = ..., user_id: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class CreateUserInput(_message.Message):
    __slots__ = ["birthday", "captcha", "country", "email", "full_name", "locale", "password", "username"]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    CAPTCHA_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    birthday: str
    captcha: str
    country: str
    email: str
    full_name: str
    locale: str
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., full_name: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., country: _Optional[str] = ..., birthday: _Optional[str] = ..., captcha: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class CreateUserOutput(_message.Message):
    __slots__ = ["email_confirmation_hint", "user_id"]
    EMAIL_CONFIRMATION_HINT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    email_confirmation_hint: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., email_confirmation_hint: _Optional[str] = ...) -> None: ...

class DeleteAccessKeyInput(_message.Message):
    __slots__ = ["key_id"]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    def __init__(self, key_id: _Optional[str] = ...) -> None: ...

class DeleteAccessKeyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeUserInput(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class DescribeUserOutput(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class IntrospectQuotaInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectQuotaOutput(_message.Message):
    __slots__ = ["contests_per_user", "participants_per_contest", "problems_per_contest", "problems_per_user"]
    CONTESTS_PER_USER_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_PER_CONTEST_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_PER_CONTEST_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_PER_USER_FIELD_NUMBER: _ClassVar[int]
    contests_per_user: _quota_pb2.Quota
    participants_per_contest: _quota_pb2.Quota
    problems_per_contest: _quota_pb2.Quota
    problems_per_user: _quota_pb2.Quota
    def __init__(self, contests_per_user: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ..., problems_per_contest: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ..., participants_per_contest: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ..., problems_per_user: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ...) -> None: ...

class IntrospectRolesInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectRolesOutput(_message.Message):
    __slots__ = ["roles"]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, roles: _Optional[_Iterable[str]] = ...) -> None: ...

class IntrospectTokenInput(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class IntrospectTokenOutput(_message.Message):
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

class IntrospectUserInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectUserOutput(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class ListAccessKeysInput(_message.Message):
    __slots__ = ["offset", "size"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListAccessKeysOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_access_key_pb2.AccessKey]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_access_key_pb2.AccessKey, _Mapping]]] = ...) -> None: ...

class ListRolesInput(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ListRolesOutput(_message.Message):
    __slots__ = ["roles"]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, roles: _Optional[_Iterable[str]] = ...) -> None: ...

class ListUsersInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "username"]
        ID_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        username: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., username: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListUsersInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListUsersInput.Filter, _Mapping]] = ...) -> None: ...

class ListUsersOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ...) -> None: ...

class NotifyUserInput(_message.Message):
    __slots__ = ["parameters", "template", "user_id"]
    class ParametersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.ScalarMap[str, str]
    template: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., template: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class NotifyUserOutput(_message.Message):
    __slots__ = ["notification_id"]
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    notification_id: str
    def __init__(self, notification_id: _Optional[str] = ...) -> None: ...

class ResendEmailVerificationInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ResendEmailVerificationOutput(_message.Message):
    __slots__ = ["email_confirmation_hint"]
    EMAIL_CONFIRMATION_HINT_FIELD_NUMBER: _ClassVar[int]
    email_confirmation_hint: str
    def __init__(self, email_confirmation_hint: _Optional[str] = ...) -> None: ...

class RevokeTokenInput(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class RevokeTokenOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SelfDestructInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SelfDestructOutput(_message.Message):
    __slots__ = ["delete_on"]
    DELETE_ON_FIELD_NUMBER: _ClassVar[int]
    delete_on: _timestamp_pb2.Timestamp
    def __init__(self, delete_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SigninInput(_message.Message):
    __slots__ = ["password", "username"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class SigninOutput(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class SignoutInput(_message.Message):
    __slots__ = ["everywhere"]
    EVERYWHERE_FIELD_NUMBER: _ClassVar[int]
    everywhere: bool
    def __init__(self, everywhere: bool = ...) -> None: ...

class SignoutOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StartRecoveryInput(_message.Message):
    __slots__ = ["captcha", "email", "locale"]
    CAPTCHA_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    captcha: str
    email: str
    locale: str
    def __init__(self, email: _Optional[str] = ..., captcha: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class StartRecoveryOutput(_message.Message):
    __slots__ = ["email_recovery_hint"]
    EMAIL_RECOVERY_HINT_FIELD_NUMBER: _ClassVar[int]
    email_recovery_hint: str
    def __init__(self, email_recovery_hint: _Optional[str] = ...) -> None: ...

class UpdateEmailInput(_message.Message):
    __slots__ = ["email"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class UpdateEmailOutput(_message.Message):
    __slots__ = ["email_confirmation_hint"]
    EMAIL_CONFIRMATION_HINT_FIELD_NUMBER: _ClassVar[int]
    email_confirmation_hint: str
    def __init__(self, email_confirmation_hint: _Optional[str] = ...) -> None: ...

class UpdatePasswordInput(_message.Message):
    __slots__ = ["current_password", "new_password"]
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    current_password: str
    new_password: str
    def __init__(self, current_password: _Optional[str] = ..., new_password: _Optional[str] = ...) -> None: ...

class UpdatePasswordOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdatePictureInput(_message.Message):
    __slots__ = ["data", "filename", "offset_x", "offset_y", "size"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_X_FIELD_NUMBER: _ClassVar[int]
    OFFSET_Y_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    filename: str
    offset_x: int
    offset_y: int
    size: int
    def __init__(self, filename: _Optional[str] = ..., data: _Optional[bytes] = ..., offset_x: _Optional[int] = ..., offset_y: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class UpdatePictureOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateProfileInput(_message.Message):
    __slots__ = ["birthday", "city", "company", "country", "email", "locale", "name", "occupation", "patch", "username"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BIRTHDAY: UpdateProfileInput.Patch
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    CITY: UpdateProfileInput.Patch
    CITY_FIELD_NUMBER: _ClassVar[int]
    COMPANY: UpdateProfileInput.Patch
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY: UpdateProfileInput.Patch
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    EMAIL: UpdateProfileInput.Patch
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE: UpdateProfileInput.Patch
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME: UpdateProfileInput.Patch
    NAME_FIELD_NUMBER: _ClassVar[int]
    OCCUPATION: UpdateProfileInput.Patch
    OCCUPATION_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    USERNAME: UpdateProfileInput.Patch
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    birthday: str
    city: str
    company: str
    country: str
    email: str
    locale: str
    name: str
    occupation: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateProfileInput.Patch]
    username: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateProfileInput.Patch, str]]] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., name: _Optional[str] = ..., company: _Optional[str] = ..., occupation: _Optional[str] = ..., country: _Optional[str] = ..., city: _Optional[str] = ..., birthday: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class UpdateProfileOutput(_message.Message):
    __slots__ = ["email_confirmation_hint"]
    EMAIL_CONFIRMATION_HINT_FIELD_NUMBER: _ClassVar[int]
    email_confirmation_hint: str
    def __init__(self, email_confirmation_hint: _Optional[str] = ...) -> None: ...

class UpdateRolesInput(_message.Message):
    __slots__ = ["roles", "user_id"]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedScalarFieldContainer[str]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateRolesOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VerifyEmailInput(_message.Message):
    __slots__ = ["secret", "user_id"]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    secret: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., secret: _Optional[str] = ...) -> None: ...

class VerifyEmailOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
