from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.notify import notification_pb2 as _notification_pb2
from eolymp.notify import preferences_pb2 as _preferences_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
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

class DescribePreferencesInput(_message.Message):
    __slots__ = ["space_id"]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: _Optional[str] = ...) -> None: ...

class DescribePreferencesOutput(_message.Message):
    __slots__ = ["preferences"]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: _preferences_pb2.Preferences
    def __init__(self, preferences: _Optional[_Union[_preferences_pb2.Preferences, _Mapping]] = ...) -> None: ...

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

class UpdatePreferencesInput(_message.Message):
    __slots__ = ["patch", "preferences", "space_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdatePreferencesInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS: UpdatePreferencesInput.Patch
    SUBSCRIPTIONS_ADD: UpdatePreferencesInput.Patch
    SUBSCRIPTIONS_REMOVE: UpdatePreferencesInput.Patch
    patch: _containers.RepeatedScalarFieldContainer[UpdatePreferencesInput.Patch]
    preferences: _preferences_pb2.Preferences
    space_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdatePreferencesInput.Patch, str]]] = ..., space_id: _Optional[str] = ..., preferences: _Optional[_Union[_preferences_pb2.Preferences, _Mapping]] = ...) -> None: ...

class UpdatePreferencesOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
