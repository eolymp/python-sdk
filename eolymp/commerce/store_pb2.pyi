import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Store(_message.Message):
    __slots__ = ("currency", "credit_value", "stripe_live_mode", "stripe_live", "stripe_test", "catalog_synced_at")
    class Patch(_message.Message):
        __slots__ = ("currency", "credit_value", "stripe_live_mode", "stripe_live", "stripe_test")
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        CREDIT_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRIPE_LIVE_MODE_FIELD_NUMBER: _ClassVar[int]
        STRIPE_LIVE_FIELD_NUMBER: _ClassVar[int]
        STRIPE_TEST_FIELD_NUMBER: _ClassVar[int]
        currency: str
        credit_value: int
        stripe_live_mode: bool
        stripe_live: Store.Stripe
        stripe_test: Store.Stripe
        def __init__(self, currency: _Optional[str] = ..., credit_value: _Optional[int] = ..., stripe_live_mode: _Optional[bool] = ..., stripe_live: _Optional[_Union[Store.Stripe, _Mapping]] = ..., stripe_test: _Optional[_Union[Store.Stripe, _Mapping]] = ...) -> None: ...
    class Stripe(_message.Message):
        __slots__ = ("secret_key", "webhook_secret", "configured", "webhook_url")
        SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
        WEBHOOK_SECRET_FIELD_NUMBER: _ClassVar[int]
        CONFIGURED_FIELD_NUMBER: _ClassVar[int]
        WEBHOOK_URL_FIELD_NUMBER: _ClassVar[int]
        secret_key: str
        webhook_secret: str
        configured: bool
        webhook_url: str
        def __init__(self, secret_key: _Optional[str] = ..., webhook_secret: _Optional[str] = ..., configured: _Optional[bool] = ..., webhook_url: _Optional[str] = ...) -> None: ...
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CREDIT_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRIPE_LIVE_MODE_FIELD_NUMBER: _ClassVar[int]
    STRIPE_LIVE_FIELD_NUMBER: _ClassVar[int]
    STRIPE_TEST_FIELD_NUMBER: _ClassVar[int]
    CATALOG_SYNCED_AT_FIELD_NUMBER: _ClassVar[int]
    currency: str
    credit_value: int
    stripe_live_mode: bool
    stripe_live: Store.Stripe
    stripe_test: Store.Stripe
    catalog_synced_at: _timestamp_pb2.Timestamp
    def __init__(self, currency: _Optional[str] = ..., credit_value: _Optional[int] = ..., stripe_live_mode: _Optional[bool] = ..., stripe_live: _Optional[_Union[Store.Stripe, _Mapping]] = ..., stripe_test: _Optional[_Union[Store.Stripe, _Mapping]] = ..., catalog_synced_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
