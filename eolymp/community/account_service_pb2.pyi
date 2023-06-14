from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.community import member_pb2 as _member_pb2
from google.protobuf.internal import containers as _containers
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
    __slots__ = ["captcha", "email", "locale", "nickname", "password", "values"]
    CAPTCHA_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    captcha: str
    email: str
    locale: str
    nickname: str
    password: str
    values: _containers.RepeatedCompositeFieldContainer[_member_pb2.Member.Value]
    def __init__(self, nickname: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., locale: _Optional[str] = ..., values: _Optional[_Iterable[_Union[_member_pb2.Member.Value, _Mapping]]] = ..., captcha: _Optional[str] = ...) -> None: ...

class CreateAccountOutput(_message.Message):
    __slots__ = ["hint", "identity_issuer", "identity_subject", "member_id"]
    HINT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_ISSUER_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    hint: str
    identity_issuer: str
    identity_subject: str
    member_id: str
    def __init__(self, member_id: _Optional[str] = ..., identity_issuer: _Optional[str] = ..., identity_subject: _Optional[str] = ..., hint: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["email", "email_verified", "locale", "nickname", "nickname_change_timeout", "password_age", "values"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_CHANGE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_AGE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    email: str
    email_verified: bool
    locale: str
    nickname: str
    nickname_change_timeout: int
    password_age: int
    values: _containers.RepeatedCompositeFieldContainer[_member_pb2.Member.Value]
    def __init__(self, nickname: _Optional[str] = ..., nickname_change_timeout: _Optional[int] = ..., email: _Optional[str] = ..., email_verified: bool = ..., password_age: _Optional[int] = ..., locale: _Optional[str] = ..., values: _Optional[_Iterable[_Union[_member_pb2.Member.Value, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ["current_password", "email", "locale", "nickname", "password", "patch", "values"]
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    current_password: str
    email: str
    locale: str
    nickname: str
    password: str
    patch: _containers.RepeatedScalarFieldContainer[str]
    values: _containers.RepeatedCompositeFieldContainer[_member_pb2.Member.Value]
    def __init__(self, patch: _Optional[_Iterable[str]] = ..., current_password: _Optional[str] = ..., nickname: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., locale: _Optional[str] = ..., values: _Optional[_Iterable[_Union[_member_pb2.Member.Value, _Mapping]]] = ...) -> None: ...

class UpdateAccountOutput(_message.Message):
    __slots__ = ["hint"]
    HINT_FIELD_NUMBER: _ClassVar[int]
    hint: str
    def __init__(self, hint: _Optional[str] = ...) -> None: ...
