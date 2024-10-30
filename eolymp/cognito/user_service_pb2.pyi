from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
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

class IntrospectUserInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectUserOutput(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

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

class ResendEmailVerificationInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ResendEmailVerificationOutput(_message.Message):
    __slots__ = ["email_confirmation_hint"]
    EMAIL_CONFIRMATION_HINT_FIELD_NUMBER: _ClassVar[int]
    email_confirmation_hint: str
    def __init__(self, email_confirmation_hint: _Optional[str] = ...) -> None: ...

class SelfDestructInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SelfDestructOutput(_message.Message):
    __slots__ = ["delete_on"]
    DELETE_ON_FIELD_NUMBER: _ClassVar[int]
    delete_on: _timestamp_pb2.Timestamp
    def __init__(self, delete_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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

class UserChangedEvent(_message.Message):
    __slots__ = ["after", "before"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    after: _user_pb2.User
    before: _user_pb2.User
    def __init__(self, before: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., after: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

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
