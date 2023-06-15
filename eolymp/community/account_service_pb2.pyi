from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.community import member_pb2 as _member_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteRecoverInput(_message.Message):
    __slots__ = ["code", "password"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    code: str
    password: str
    def __init__(self, code: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class CompleteRecoverOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CompleteVerificationInput(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class CompleteVerificationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateAccountInput(_message.Message):
    __slots__ = ["attributes", "captcha", "email", "locale", "nickname", "password"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CAPTCHA_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[_member_pb2.Member.Value]
    captcha: str
    email: str
    locale: str
    nickname: str
    password: str
    def __init__(self, nickname: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., locale: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[_member_pb2.Member.Value, _Mapping]]] = ..., captcha: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["email", "email_verified", "locale", "nickname", "nickname_change_timeout", "password_age"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_CHANGE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_AGE_FIELD_NUMBER: _ClassVar[int]
    email: str
    email_verified: bool
    locale: str
    nickname: str
    nickname_change_timeout: int
    password_age: int
    def __init__(self, nickname: _Optional[str] = ..., nickname_change_timeout: _Optional[int] = ..., email: _Optional[str] = ..., email_verified: bool = ..., password_age: _Optional[int] = ..., locale: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["hint"]
    HINT_FIELD_NUMBER: _ClassVar[int]
    hint: str
    def __init__(self, hint: _Optional[str] = ...) -> None: ...

class UpdateAccountInput(_message.Message):
    __slots__ = ["attributes", "current_password", "email", "locale", "nickname", "password", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateAccountInput.Patch
    ATTRIBUTES: UpdateAccountInput.Patch
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EMAIL: UpdateAccountInput.Patch
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE: UpdateAccountInput.Patch
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME: UpdateAccountInput.Patch
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD: UpdateAccountInput.Patch
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[_member_pb2.Member.Value]
    current_password: str
    email: str
    locale: str
    nickname: str
    password: str
    patch: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, patch: _Optional[_Iterable[str]] = ..., current_password: _Optional[str] = ..., nickname: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., locale: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[_member_pb2.Member.Value, _Mapping]]] = ...) -> None: ...

class UpdateAccountOutput(_message.Message):
    __slots__ = ["hint"]
    HINT_FIELD_NUMBER: _ClassVar[int]
    hint: str
    def __init__(self, hint: _Optional[str] = ...) -> None: ...
