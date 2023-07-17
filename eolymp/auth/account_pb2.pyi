from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ["active", "birthday", "business_title", "city", "company", "country", "created_at", "email", "email_verified", "id", "locale", "name", "nickname", "nickname_change_timeout", "password", "password_age", "picture"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_TITLE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_CHANGE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_AGE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    birthday: _timestamp_pb2.Timestamp
    business_title: str
    city: str
    company: str
    country: str
    created_at: _timestamp_pb2.Timestamp
    email: str
    email_verified: bool
    id: str
    locale: str
    name: str
    nickname: str
    nickname_change_timeout: int
    password: str
    password_age: int
    picture: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., active: bool = ..., email: _Optional[str] = ..., email_verified: bool = ..., password: _Optional[str] = ..., password_age: _Optional[int] = ..., name: _Optional[str] = ..., nickname: _Optional[str] = ..., nickname_change_timeout: _Optional[int] = ..., picture: _Optional[str] = ..., locale: _Optional[str] = ..., birthday: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., country: _Optional[str] = ..., city: _Optional[str] = ..., company: _Optional[str] = ..., business_title: _Optional[str] = ...) -> None: ...
