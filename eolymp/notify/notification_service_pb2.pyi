from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.notify import notification_pb2 as _notification_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateNotificationInput(_message.Message):
    __slots__ = ["notification"]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    notification: _notification_pb2.Notification
    def __init__(self, notification: _Optional[_Union[_notification_pb2.Notification, _Mapping]] = ...) -> None: ...

class CreateNotificationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteNotificationInput(_message.Message):
    __slots__ = ["notification_id"]
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    notification_id: str
    def __init__(self, notification_id: _Optional[str] = ...) -> None: ...

class DeleteNotificationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeNotificationConfigInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeNotificationConfigOutput(_message.Message):
    __slots__ = ["email_subscriptions"]
    EMAIL_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    email_subscriptions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, email_subscriptions: _Optional[_Iterable[str]] = ...) -> None: ...

class DescribeNotificationInput(_message.Message):
    __slots__ = ["notification_id"]
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    notification_id: str
    def __init__(self, notification_id: _Optional[str] = ...) -> None: ...

class DescribeNotificationOutput(_message.Message):
    __slots__ = ["notification"]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    notification: _notification_pb2.Notification
    def __init__(self, notification: _Optional[_Union[_notification_pb2.Notification, _Mapping]] = ...) -> None: ...

class ListNotificationsInput(_message.Message):
    __slots__ = ["after", "size"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    after: str
    size: int
    def __init__(self, size: _Optional[int] = ..., after: _Optional[str] = ...) -> None: ...

class ListNotificationsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_notification_pb2.Notification]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_notification_pb2.Notification, _Mapping]]] = ...) -> None: ...

class NotificationEvent(_message.Message):
    __slots__ = ["notification"]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    notification: _notification_pb2.Notification
    def __init__(self, notification: _Optional[_Union[_notification_pb2.Notification, _Mapping]] = ...) -> None: ...

class ReadNotificationInput(_message.Message):
    __slots__ = ["notification_id"]
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    notification_id: str
    def __init__(self, notification_id: _Optional[str] = ...) -> None: ...

class ReadNotificationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateNotificationConfigInput(_message.Message):
    __slots__ = ["email_subscriptions"]
    EMAIL_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    email_subscriptions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, email_subscriptions: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateNotificationConfigOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
