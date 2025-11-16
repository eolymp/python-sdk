import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.universe import quota_pb2 as _quota_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Space(_message.Message):
    __slots__ = ("id", "url", "home_url", "issuer_url", "graphql_url", "key", "name", "image", "visibility", "status", "features", "subscription", "affiliation", "discord_guild_id", "locales")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Space.Status]
        TRIAL: _ClassVar[Space.Status]
        ACTIVE: _ClassVar[Space.Status]
        SUSPENDED: _ClassVar[Space.Status]
    UNKNOWN_STATUS: Space.Status
    TRIAL: Space.Status
    ACTIVE: Space.Status
    SUSPENDED: Space.Status
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_VISIBILITY: _ClassVar[Space.Visibility]
        PUBLIC: _ClassVar[Space.Visibility]
        PRIVATE: _ClassVar[Space.Visibility]
    UNKNOWN_VISIBILITY: Space.Visibility
    PUBLIC: Space.Visibility
    PRIVATE: Space.Visibility
    class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_FEATURE: _ClassVar[Space.Feature]
        PRINTERS: _ClassVar[Space.Feature]
        NEWSLETTERS: _ClassVar[Space.Feature]
        MEMBER_CREDITS: _ClassVar[Space.Feature]
        MERCHANDISE_STORE: _ClassVar[Space.Feature]
        RATING: _ClassVar[Space.Feature]
    UNKNOWN_FEATURE: Space.Feature
    PRINTERS: Space.Feature
    NEWSLETTERS: Space.Feature
    MEMBER_CREDITS: Space.Feature
    MERCHANDISE_STORE: Space.Feature
    RATING: Space.Feature
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Space.Extra.Field]
            SUBSCRIPTION: _ClassVar[Space.Extra.Field]
        UNKNOWN_EXTRA: Space.Extra.Field
        SUBSCRIPTION: Space.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_PATCH: _ClassVar[Space.Patch.Field]
            KEY: _ClassVar[Space.Patch.Field]
            NAME: _ClassVar[Space.Patch.Field]
            IMAGE: _ClassVar[Space.Patch.Field]
            VISIBILITY: _ClassVar[Space.Patch.Field]
            LOCALES: _ClassVar[Space.Patch.Field]
        UNKNOWN_PATCH: Space.Patch.Field
        KEY: Space.Patch.Field
        NAME: Space.Patch.Field
        IMAGE: Space.Patch.Field
        VISIBILITY: Space.Patch.Field
        LOCALES: Space.Patch.Field
        def __init__(self) -> None: ...
    class Subscription(_message.Message):
        __slots__ = ("plan", "seats", "quota", "billing_period_start", "billing_period_end", "quota_period_start", "quota_period_end")
        PLAN_FIELD_NUMBER: _ClassVar[int]
        SEATS_FIELD_NUMBER: _ClassVar[int]
        QUOTA_FIELD_NUMBER: _ClassVar[int]
        BILLING_PERIOD_START_FIELD_NUMBER: _ClassVar[int]
        BILLING_PERIOD_END_FIELD_NUMBER: _ClassVar[int]
        QUOTA_PERIOD_START_FIELD_NUMBER: _ClassVar[int]
        QUOTA_PERIOD_END_FIELD_NUMBER: _ClassVar[int]
        plan: str
        seats: int
        quota: _quota_pb2.Quota
        billing_period_start: _timestamp_pb2.Timestamp
        billing_period_end: _timestamp_pb2.Timestamp
        quota_period_start: _timestamp_pb2.Timestamp
        quota_period_end: _timestamp_pb2.Timestamp
        def __init__(self, plan: _Optional[str] = ..., seats: _Optional[int] = ..., quota: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ..., billing_period_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., billing_period_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., quota_period_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., quota_period_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HOME_URL_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    GRAPHQL_URL_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AFFILIATION_FIELD_NUMBER: _ClassVar[int]
    DISCORD_GUILD_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALES_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    home_url: str
    issuer_url: str
    graphql_url: str
    key: str
    name: str
    image: str
    visibility: Space.Visibility
    status: Space.Status
    features: _containers.RepeatedScalarFieldContainer[Space.Feature]
    subscription: Space.Subscription
    affiliation: str
    discord_guild_id: str
    locales: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., home_url: _Optional[str] = ..., issuer_url: _Optional[str] = ..., graphql_url: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., visibility: _Optional[_Union[Space.Visibility, str]] = ..., status: _Optional[_Union[Space.Status, str]] = ..., features: _Optional[_Iterable[_Union[Space.Feature, str]]] = ..., subscription: _Optional[_Union[Space.Subscription, _Mapping]] = ..., affiliation: _Optional[str] = ..., discord_guild_id: _Optional[str] = ..., locales: _Optional[_Iterable[str]] = ...) -> None: ...
