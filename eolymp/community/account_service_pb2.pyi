from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.community import member_pb2 as _member_pb2
from eolymp.community import subscription_pb2 as _subscription_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteRecoverInput(_message.Message):
    __slots__ = ["code", "member_id", "password"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    code: str
    member_id: str
    password: str
    def __init__(self, code: _Optional[str] = ..., password: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class CompleteRecoverOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CompleteVerificationInput(_message.Message):
    __slots__ = ["code", "member_id"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    code: str
    member_id: str
    def __init__(self, code: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class CompleteVerificationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ConfigureActiveSubscriptionInput(_message.Message):
    __slots__ = ["price_id", "tier_id"]
    PRICE_ID_FIELD_NUMBER: _ClassVar[int]
    TIER_ID_FIELD_NUMBER: _ClassVar[int]
    price_id: str
    tier_id: str
    def __init__(self, tier_id: _Optional[str] = ..., price_id: _Optional[str] = ...) -> None: ...

class ConfigureActiveSubscriptionOutput(_message.Message):
    __slots__ = ["checkout_url"]
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    def __init__(self, checkout_url: _Optional[str] = ...) -> None: ...

class CreateAccountInput(_message.Message):
    __slots__ = ["captcha", "member"]
    CAPTCHA_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    captcha: str
    member: _member_pb2.Member
    def __init__(self, member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ..., captcha: _Optional[str] = ...) -> None: ...

class CreateAccountOutput(_message.Message):
    __slots__ = ["hint", "member_id"]
    HINT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    hint: str
    member_id: str
    def __init__(self, member_id: _Optional[str] = ..., hint: _Optional[str] = ...) -> None: ...

class DeleteAccountInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteAccountOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeAccountInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeAccountOutput(_message.Message):
    __slots__ = ["extra", "member", "team"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_member_pb2.Member.Extra]
    member: _member_pb2.Member
    team: _member_pb2.Member
    def __init__(self, member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ..., team: _Optional[_Union[_member_pb2.Member, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_member_pb2.Member.Extra, str]]] = ...) -> None: ...

class DescribeActiveSubscriptionInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeActiveSubscriptionOutput(_message.Message):
    __slots__ = ["subscription"]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: _subscription_pb2.Subscription
    def __init__(self, subscription: _Optional[_Union[_subscription_pb2.Subscription, _Mapping]] = ...) -> None: ...

class ResendVerificationInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ResendVerificationOutput(_message.Message):
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
    def __init__(self, email: _Optional[str] = ..., locale: _Optional[str] = ..., captcha: _Optional[str] = ...) -> None: ...

class StartRecoveryOutput(_message.Message):
    __slots__ = ["hint", "member_id"]
    HINT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    hint: str
    member_id: str
    def __init__(self, hint: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class UpdateAccountInput(_message.Message):
    __slots__ = ["current_password", "member", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateAccountInput.Patch
    ATTRIBUTES: UpdateAccountInput.Patch
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    USER_BIRTHDAY: UpdateAccountInput.Patch
    USER_CITY: UpdateAccountInput.Patch
    USER_COUNTRY: UpdateAccountInput.Patch
    USER_EMAIL: UpdateAccountInput.Patch
    USER_NAME: UpdateAccountInput.Patch
    USER_NICKNAME: UpdateAccountInput.Patch
    USER_PASSWORD: UpdateAccountInput.Patch
    USER_PICTURE: UpdateAccountInput.Patch
    USER_PREFERENCES: UpdateAccountInput.Patch
    USER_PREFERENCES_LOCALE: UpdateAccountInput.Patch
    USER_PREFERENCES_RUNTIME: UpdateAccountInput.Patch
    USER_PREFERENCES_TIMEZONE: UpdateAccountInput.Patch
    current_password: str
    member: _member_pb2.Member
    patch: _containers.RepeatedScalarFieldContainer[UpdateAccountInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateAccountInput.Patch, str]]] = ..., current_password: _Optional[str] = ..., member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class UpdateAccountOutput(_message.Message):
    __slots__ = ["hint"]
    HINT_FIELD_NUMBER: _ClassVar[int]
    hint: str
    def __init__(self, hint: _Optional[str] = ...) -> None: ...

class UploadPictureInput(_message.Message):
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

class UploadPictureOutput(_message.Message):
    __slots__ = ["picture_url"]
    PICTURE_URL_FIELD_NUMBER: _ClassVar[int]
    picture_url: str
    def __init__(self, picture_url: _Optional[str] = ...) -> None: ...
