from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Claims(_message.Message):
    __slots__ = ["business_title", "city", "company", "country", "email", "email_verified", "issuer", "locale", "minor", "name", "nickname", "picture", "preferred_runtime", "subject", "timezone"]
    BUSINESS_TITLE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    business_title: str
    city: str
    company: str
    country: str
    email: str
    email_verified: bool
    issuer: str
    locale: str
    minor: bool
    name: str
    nickname: str
    picture: str
    preferred_runtime: str
    subject: str
    timezone: str
    def __init__(self, issuer: _Optional[str] = ..., subject: _Optional[str] = ..., email: _Optional[str] = ..., email_verified: bool = ..., name: _Optional[str] = ..., nickname: _Optional[str] = ..., picture: _Optional[str] = ..., locale: _Optional[str] = ..., timezone: _Optional[str] = ..., minor: bool = ..., country: _Optional[str] = ..., city: _Optional[str] = ..., company: _Optional[str] = ..., business_title: _Optional[str] = ..., preferred_runtime: _Optional[str] = ...) -> None: ...
