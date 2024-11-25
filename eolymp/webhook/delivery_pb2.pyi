from eolymp.webhook import webhook_pb2 as _webhook_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Delivery(_message.Message):
    __slots__ = ["event", "id", "payload", "timestamp", "webhook_id"]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_ID_FIELD_NUMBER: _ClassVar[int]
    event: _webhook_pb2.Webhook.Event
    id: str
    payload: _any_pb2.Any
    timestamp: _timestamp_pb2.Timestamp
    webhook_id: str
    def __init__(self, id: _Optional[str] = ..., webhook_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., event: _Optional[_Union[_webhook_pb2.Webhook.Event, str]] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
