from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.community import account_pb2 as _account_pb2
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
    __slots__ = ["account", "captcha"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CAPTCHA_FIELD_NUMBER: _ClassVar[int]
    account: _account_pb2.Account
    captcha: str
    def __init__(self, account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., captcha: _Optional[str] = ...) -> None: ...

class CreateAccountOutput(_message.Message):
    __slots__ = ["hint"]
    HINT_FIELD_NUMBER: _ClassVar[int]
    hint: str
    def __init__(self, hint: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["account"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: _account_pb2.Account
    def __init__(self, account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ...) -> None: ...

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
    __slots__ = ["account", "current_password", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ALL: UpdateAccountInput.Patch
    BIRTHDAY: UpdateAccountInput.Patch
    COUNTRY: UpdateAccountInput.Patch
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EMAIL: UpdateAccountInput.Patch
    LOCALE: UpdateAccountInput.Patch
    NAME: UpdateAccountInput.Patch
    NICKNAME: UpdateAccountInput.Patch
    PASSWORD: UpdateAccountInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PICTURE: UpdateAccountInput.Patch
    account: _account_pb2.Account
    current_password: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateAccountInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateAccountInput.Patch, str]]] = ..., current_password: _Optional[str] = ..., account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ...) -> None: ...

class UpdateAccountOutput(_message.Message):
    __slots__ = ["hint"]
    HINT_FIELD_NUMBER: _ClassVar[int]
    hint: str
    def __init__(self, hint: _Optional[str] = ...) -> None: ...
