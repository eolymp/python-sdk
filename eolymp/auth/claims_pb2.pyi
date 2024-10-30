from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Claims(_message.Message):
    __slots__ = ["birthday", "country", "email", "email_restricted", "email_verified", "id", "issuer", "locale", "minor", "name", "nickname", "picture", "preferred_runtime", "session_id", "subject", "timezone"]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_RESTRICTED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    birthday: str
    country: str
    email: str
    email_restricted: bool
    email_verified: bool
    id: str
    issuer: str
    locale: str
    minor: bool
    name: str
    nickname: str
    picture: str
    preferred_runtime: str
    session_id: str
    subject: str
    timezone: str
    def __init__(self, id: _Optional[str] = ..., issuer: _Optional[str] = ..., subject: _Optional[str] = ..., session_id: _Optional[str] = ..., email: _Optional[str] = ..., email_verified: bool = ..., email_restricted: bool = ..., name: _Optional[str] = ..., nickname: _Optional[str] = ..., picture: _Optional[str] = ..., locale: _Optional[str] = ..., timezone: _Optional[str] = ..., birthday: _Optional[str] = ..., minor: bool = ..., country: _Optional[str] = ..., preferred_runtime: _Optional[str] = ...) -> None: ...
