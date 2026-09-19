import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ("id", "title", "content", "channel_ids", "status", "deliveries", "reference", "created_at", "scheduled_at", "sent_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Message.Status]
        DRAFT: _ClassVar[Message.Status]
        SCHEDULED: _ClassVar[Message.Status]
        SENDING: _ClassVar[Message.Status]
        SENT: _ClassVar[Message.Status]
        FAILED: _ClassVar[Message.Status]
    UNKNOWN_STATUS: Message.Status
    DRAFT: Message.Status
    SCHEDULED: Message.Status
    SENDING: Message.Status
    SENT: Message.Status
    FAILED: Message.Status
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Message.Extra.Field]
            CONTENT_VALUE: _ClassVar[Message.Extra.Field]
            CONTENT_RENDER: _ClassVar[Message.Extra.Field]
        UNKNOWN_EXTRA: Message.Extra.Field
        CONTENT_VALUE: Message.Extra.Field
        CONTENT_RENDER: Message.Extra.Field
        def __init__(self) -> None: ...
    class Delivery(_message.Message):
        __slots__ = ("channel_id", "channel_name", "status", "error", "url", "delivered_at")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_STATUS: _ClassVar[Message.Delivery.Status]
            PENDING: _ClassVar[Message.Delivery.Status]
            SENT: _ClassVar[Message.Delivery.Status]
            FAILED: _ClassVar[Message.Delivery.Status]
        UNKNOWN_STATUS: Message.Delivery.Status
        PENDING: Message.Delivery.Status
        SENT: Message.Delivery.Status
        FAILED: Message.Delivery.Status
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        DELIVERED_AT_FIELD_NUMBER: _ClassVar[int]
        channel_id: str
        channel_name: str
        status: Message.Delivery.Status
        error: str
        url: str
        delivered_at: _timestamp_pb2.Timestamp
        def __init__(self, channel_id: _Optional[str] = ..., channel_name: _Optional[str] = ..., status: _Optional[_Union[Message.Delivery.Status, str]] = ..., error: _Optional[str] = ..., url: _Optional[str] = ..., delivered_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Patch(_message.Message):
        __slots__ = ("title", "content", "channel_ids", "clear_channel_ids", "scheduled_at", "unschedule", "reference")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
        CLEAR_CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
        SCHEDULED_AT_FIELD_NUMBER: _ClassVar[int]
        UNSCHEDULE_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        title: str
        content: _content_pb2.Content
        channel_ids: _containers.RepeatedScalarFieldContainer[str]
        clear_channel_ids: bool
        scheduled_at: _timestamp_pb2.Timestamp
        unschedule: bool
        reference: str
        def __init__(self, title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., channel_ids: _Optional[_Iterable[str]] = ..., clear_channel_ids: _Optional[bool] = ..., scheduled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., unschedule: _Optional[bool] = ..., reference: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DELIVERIES_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_AT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    content: _content_pb2.Content
    channel_ids: _containers.RepeatedScalarFieldContainer[str]
    status: Message.Status
    deliveries: _containers.RepeatedCompositeFieldContainer[Message.Delivery]
    reference: str
    created_at: _timestamp_pb2.Timestamp
    scheduled_at: _timestamp_pb2.Timestamp
    sent_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., channel_ids: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[Message.Status, str]] = ..., deliveries: _Optional[_Iterable[_Union[Message.Delivery, _Mapping]]] = ..., reference: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., scheduled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sent_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
