import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Profile(_message.Message):
    __slots__ = ("id", "status", "status_reason", "first_name", "last_name", "company_name", "birthday", "email", "phone", "tax_id", "country", "state", "postal_code", "city", "line1", "line2", "created_at", "updated_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Profile.Status]
        DRAFT: _ClassVar[Profile.Status]
        REVIEW: _ClassVar[Profile.Status]
        APPROVED: _ClassVar[Profile.Status]
        REJECTED: _ClassVar[Profile.Status]
    UNKNOWN_STATUS: Profile.Status
    DRAFT: Profile.Status
    REVIEW: Profile.Status
    APPROVED: Profile.Status
    REJECTED: Profile.Status
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNONWN_FIELD: _ClassVar[Profile.Patch.Field]
            FIRST_NAME: _ClassVar[Profile.Patch.Field]
            LAST_NAME: _ClassVar[Profile.Patch.Field]
            COMPANY_NAME: _ClassVar[Profile.Patch.Field]
            BIRTHDAY: _ClassVar[Profile.Patch.Field]
            EMAIL: _ClassVar[Profile.Patch.Field]
            PHONE: _ClassVar[Profile.Patch.Field]
            TAX_ID: _ClassVar[Profile.Patch.Field]
            ADDRESS: _ClassVar[Profile.Patch.Field]
        UNKNONWN_FIELD: Profile.Patch.Field
        FIRST_NAME: Profile.Patch.Field
        LAST_NAME: Profile.Patch.Field
        COMPANY_NAME: Profile.Patch.Field
        BIRTHDAY: Profile.Patch.Field
        EMAIL: Profile.Patch.Field
        PHONE: Profile.Patch.Field
        TAX_ID: Profile.Patch.Field
        ADDRESS: Profile.Patch.Field
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_REASON_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    TAX_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    LINE1_FIELD_NUMBER: _ClassVar[int]
    LINE2_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: Profile.Status
    status_reason: str
    first_name: str
    last_name: str
    company_name: str
    birthday: _timestamp_pb2.Timestamp
    email: str
    phone: str
    tax_id: str
    country: str
    state: str
    postal_code: str
    city: str
    line1: str
    line2: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Profile.Status, str]] = ..., status_reason: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., company_name: _Optional[str] = ..., birthday: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., tax_id: _Optional[str] = ..., country: _Optional[str] = ..., state: _Optional[str] = ..., postal_code: _Optional[str] = ..., city: _Optional[str] = ..., line1: _Optional[str] = ..., line2: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
