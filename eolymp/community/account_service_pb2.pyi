from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.community import attribute_pb2 as _attribute_pb2
from eolymp.community import member_user_pb2 as _member_user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteRecoverInput(_message.Message):
    __slots__ = ["code", "password", "subject"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    code: str
    password: str
    subject: str
    def __init__(self, code: _Optional[str] = ..., password: _Optional[str] = ..., subject: _Optional[str] = ...) -> None: ...

class CompleteRecoverOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CompleteVerificationInput(_message.Message):
    __slots__ = ["code", "subject"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    code: str
    subject: str
    def __init__(self, code: _Optional[str] = ..., subject: _Optional[str] = ...) -> None: ...

class CompleteVerificationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateAccountInput(_message.Message):
    __slots__ = ["account", "attributes", "captcha"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CAPTCHA_FIELD_NUMBER: _ClassVar[int]
    account: _member_user_pb2.User
    attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute.Value]
    captcha: str
    def __init__(self, account: _Optional[_Union[_member_user_pb2.User, _Mapping]] = ..., attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute.Value, _Mapping]]] = ..., captcha: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["account", "attributes"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    account: _member_user_pb2.User
    attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute.Value]
    def __init__(self, account: _Optional[_Union[_member_user_pb2.User, _Mapping]] = ..., attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute.Value, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ["account", "attributes", "current_password", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ALL: UpdateAccountInput.Patch
    ATTRIBUTES: UpdateAccountInput.Patch
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
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
    account: _member_user_pb2.User
    attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute.Value]
    current_password: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateAccountInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateAccountInput.Patch, str]]] = ..., current_password: _Optional[str] = ..., account: _Optional[_Union[_member_user_pb2.User, _Mapping]] = ..., attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute.Value, _Mapping]]] = ...) -> None: ...

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
    __slots__ = []
    def __init__(self) -> None: ...
