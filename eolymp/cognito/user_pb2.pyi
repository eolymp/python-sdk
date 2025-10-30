import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("id", "username", "email", "active", "rating", "name", "picture", "company", "occupation", "country", "city", "email_status", "email_verified", "birthday", "registered_on", "last_activity", "username_changed_on", "password_changed_on", "locale", "aliases", "discord_user_id")
    class Alias(_message.Message):
        __slots__ = ("nickname", "changed_at")
        NICKNAME_FIELD_NUMBER: _ClassVar[int]
        CHANGED_AT_FIELD_NUMBER: _ClassVar[int]
        nickname: str
        changed_at: _timestamp_pb2.Timestamp
        def __init__(self, nickname: _Optional[str] = ..., changed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    OCCUPATION_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_STATUS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ON_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    USERNAME_CHANGED_ON_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_CHANGED_ON_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    DISCORD_USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    username: str
    email: str
    active: bool
    rating: int
    name: str
    picture: str
    company: str
    occupation: str
    country: str
    city: str
    email_status: str
    email_verified: bool
    birthday: str
    registered_on: _timestamp_pb2.Timestamp
    last_activity: _timestamp_pb2.Timestamp
    username_changed_on: _timestamp_pb2.Timestamp
    password_changed_on: _timestamp_pb2.Timestamp
    locale: str
    aliases: _containers.RepeatedCompositeFieldContainer[User.Alias]
    discord_user_id: str
    def __init__(self, id: _Optional[str] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., active: bool = ..., rating: _Optional[int] = ..., name: _Optional[str] = ..., picture: _Optional[str] = ..., company: _Optional[str] = ..., occupation: _Optional[str] = ..., country: _Optional[str] = ..., city: _Optional[str] = ..., email_status: _Optional[str] = ..., email_verified: bool = ..., birthday: _Optional[str] = ..., registered_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_activity: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., username_changed_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., password_changed_on: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., locale: _Optional[str] = ..., aliases: _Optional[_Iterable[_Union[User.Alias, _Mapping]]] = ..., discord_user_id: _Optional[str] = ...) -> None: ...
