from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["active", "birthday", "city", "company", "country", "email", "email_status", "id", "last_activity", "locale", "name", "occupation", "password_changed_on", "picture", "rank", "rank_trend", "registered_on", "username", "username_changed_on"]
    class RankTrend(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DOWN: User.RankTrend
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NONE: User.RankTrend
    OCCUPATION_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_CHANGED_ON_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    RANK_TREND_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ON_FIELD_NUMBER: _ClassVar[int]
    UP: User.RankTrend
    USERNAME_CHANGED_ON_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    active: bool
    birthday: str
    city: str
    company: str
    country: str
    email: str
    email_status: str
    id: str
    last_activity: _timestamp_pb2.Timestamp
    locale: str
    name: str
    occupation: str
    password_changed_on: _timestamp_pb2.Timestamp
    picture: str
    rank: int
    rank_trend: User.RankTrend
    registered_on: _timestamp_pb2.Timestamp
    username: str
    username_changed_on: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., active: bool = ..., rank: _Optional[int] = ..., rank_trend: _Optional[_Union[User.RankTrend, str]] = ..., name: _Optional[str] = ..., picture: _Optional[str] = ..., company: _Optional[str] = ..., occupation: _Optional[str] = ..., country: _Optional[str] = ..., city: _Optional[str] = ..., email_status: _Optional[str] = ..., birthday: _Optional[str] = ..., registered_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_activity: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., username_changed_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., password_changed_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., locale: _Optional[str] = ...) -> None: ...
