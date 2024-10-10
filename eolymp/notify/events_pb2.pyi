from eolymp.acl import acl_service_pb2 as _acl_service_pb2
from eolymp.notify import notification_pb2 as _notification_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationEvent(_message.Message):
    __slots__ = ["notification"]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    notification: _notification_pb2.Notification
    def __init__(self, notification: _Optional[_Union[_notification_pb2.Notification, _Mapping]] = ...) -> None: ...
