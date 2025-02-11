from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.webhook import webhook_pb2 as _webhook_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateWebhookInput(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: _webhook_pb2.Webhook
    def __init__(self, webhook: _Optional[_Union[_webhook_pb2.Webhook, _Mapping]] = ...) -> None: ...

class CreateWebhookOutput(_message.Message):
    __slots__ = ("webhook_id",)
    WEBHOOK_ID_FIELD_NUMBER: _ClassVar[int]
    webhook_id: str
    def __init__(self, webhook_id: _Optional[str] = ...) -> None: ...

class UpdateWebhookInput(_message.Message):
    __slots__ = ("patch", "webhook_id", "webhook")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_ID_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_webhook_pb2.Webhook.Patch]
    webhook_id: str
    webhook: _webhook_pb2.Webhook
    def __init__(self, patch: _Optional[_Iterable[_Union[_webhook_pb2.Webhook.Patch, str]]] = ..., webhook_id: _Optional[str] = ..., webhook: _Optional[_Union[_webhook_pb2.Webhook, _Mapping]] = ...) -> None: ...

class UpdateWebhookOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteWebhookInput(_message.Message):
    __slots__ = ("webhook_id",)
    WEBHOOK_ID_FIELD_NUMBER: _ClassVar[int]
    webhook_id: str
    def __init__(self, webhook_id: _Optional[str] = ...) -> None: ...

class DeleteWebhookOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeWebhookInput(_message.Message):
    __slots__ = ("webhook_id",)
    WEBHOOK_ID_FIELD_NUMBER: _ClassVar[int]
    webhook_id: str
    def __init__(self, webhook_id: _Optional[str] = ...) -> None: ...

class DescribeWebhookOutput(_message.Message):
    __slots__ = ("webhook",)
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    webhook: _webhook_pb2.Webhook
    def __init__(self, webhook: _Optional[_Union[_webhook_pb2.Webhook, _Mapping]] = ...) -> None: ...

class ListWebhooksInput(_message.Message):
    __slots__ = ("size", "offset")
    SIZE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    size: int
    offset: int
    def __init__(self, size: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListWebhooksOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_webhook_pb2.Webhook]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_webhook_pb2.Webhook, _Mapping]]] = ...) -> None: ...

class TestWebhookInput(_message.Message):
    __slots__ = ("webhook_id",)
    WEBHOOK_ID_FIELD_NUMBER: _ClassVar[int]
    webhook_id: str
    def __init__(self, webhook_id: _Optional[str] = ...) -> None: ...

class TestWebhookOutput(_message.Message):
    __slots__ = ("status", "response")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    status: int
    response: str
    def __init__(self, status: _Optional[int] = ..., response: _Optional[str] = ...) -> None: ...
