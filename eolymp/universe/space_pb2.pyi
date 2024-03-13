from eolymp.universe import quota_pb2 as _quota_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Space(_message.Message):
    __slots__ = ["affiliation", "graphql_url", "home_url", "id", "image", "issuer_url", "key", "name", "status", "subscription", "url", "visibility"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Subscription(_message.Message):
        __slots__ = ["billing_period_end", "billing_period_start", "plan", "quota", "quota_period_end", "quota_period_start", "seats"]
        BILLING_PERIOD_END_FIELD_NUMBER: _ClassVar[int]
        BILLING_PERIOD_START_FIELD_NUMBER: _ClassVar[int]
        PLAN_FIELD_NUMBER: _ClassVar[int]
        QUOTA_FIELD_NUMBER: _ClassVar[int]
        QUOTA_PERIOD_END_FIELD_NUMBER: _ClassVar[int]
        QUOTA_PERIOD_START_FIELD_NUMBER: _ClassVar[int]
        SEATS_FIELD_NUMBER: _ClassVar[int]
        billing_period_end: _timestamp_pb2.Timestamp
        billing_period_start: _timestamp_pb2.Timestamp
        plan: str
        quota: _quota_pb2.Quota
        quota_period_end: _timestamp_pb2.Timestamp
        quota_period_start: _timestamp_pb2.Timestamp
        seats: int
        def __init__(self, plan: _Optional[str] = ..., seats: _Optional[int] = ..., quota: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ..., billing_period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., billing_period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., quota_period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., quota_period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ACTIVE: Space.Status
    AFFILIATION_FIELD_NUMBER: _ClassVar[int]
    GRAPHQL_URL_FIELD_NUMBER: _ClassVar[int]
    HOME_URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVATE: Space.Visibility
    PUBLIC: Space.Visibility
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION: Space.Extra
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED: Space.Status
    TRIAL: Space.Status
    UNKNOWN_EXTRA: Space.Extra
    UNKNOWN_STATUS: Space.Status
    UNKNOWN_VISIBILITY: Space.Visibility
    URL_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    affiliation: str
    graphql_url: str
    home_url: str
    id: str
    image: str
    issuer_url: str
    key: str
    name: str
    status: Space.Status
    subscription: Space.Subscription
    url: str
    visibility: Space.Visibility
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., url: _Optional[str] = ..., home_url: _Optional[str] = ..., issuer_url: _Optional[str] = ..., graphql_url: _Optional[str] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., visibility: _Optional[_Union[Space.Visibility, str]] = ..., status: _Optional[_Union[Space.Status, str]] = ..., subscription: _Optional[_Union[Space.Subscription, _Mapping]] = ..., affiliation: _Optional[str] = ...) -> None: ...
