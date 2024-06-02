from eolymp.mailing import email_type_pb2 as _email_type_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["birthday", "city", "country", "email", "email_subscriptions", "email_verified", "issuer", "name", "nickname", "nickname_change_timeout", "password", "password_age", "picture", "preferences", "subject", "team_id"]
    class Preferences(_message.Message):
        __slots__ = ["locale", "runtime", "timezone"]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        TIMEZONE_FIELD_NUMBER: _ClassVar[int]
        locale: str
        runtime: str
        timezone: str
        def __init__(self, locale: _Optional[str] = ..., timezone: _Optional[str] = ..., runtime: _Optional[str] = ...) -> None: ...
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_CHANGE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_AGE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    birthday: _timestamp_pb2.Timestamp
    city: str
    country: str
    email: str
    email_subscriptions: _containers.RepeatedScalarFieldContainer[_email_type_pb2.EmailType]
    email_verified: bool
    issuer: str
    name: str
    nickname: str
    nickname_change_timeout: int
    password: str
    password_age: int
    picture: str
    preferences: User.Preferences
    subject: str
    team_id: str
    def __init__(self, issuer: _Optional[str] = ..., subject: _Optional[str] = ..., nickname: _Optional[str] = ..., nickname_change_timeout: _Optional[int] = ..., email: _Optional[str] = ..., email_verified: bool = ..., email_subscriptions: _Optional[_Iterable[_Union[_email_type_pb2.EmailType, str]]] = ..., password: _Optional[str] = ..., password_age: _Optional[int] = ..., name: _Optional[str] = ..., picture: _Optional[str] = ..., birthday: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., country: _Optional[str] = ..., city: _Optional[str] = ..., team_id: _Optional[str] = ..., preferences: _Optional[_Union[User.Preferences, _Mapping]] = ...) -> None: ...
