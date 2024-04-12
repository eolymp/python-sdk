from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import announcement_pb2 as _announcement_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAnnouncementInput(_message.Message):
    __slots__ = ["announcement", "contest_id"]
    ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    announcement: _announcement_pb2.Announcement
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., announcement: _Optional[_Union[_announcement_pb2.Announcement, _Mapping]] = ...) -> None: ...

class CreateAnnouncementOutput(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteAnnouncementInput(_message.Message):
    __slots__ = ["announcement_id", "contest_id"]
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    announcement_id: str
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., announcement_id: _Optional[str] = ...) -> None: ...

class DeleteAnnouncementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeAnnouncementInput(_message.Message):
    __slots__ = ["announcement_id", "contest_id", "extra"]
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    announcement_id: str
    contest_id: str
    extra: _containers.RepeatedScalarFieldContainer[_announcement_pb2.Announcement.Extra]
    def __init__(self, contest_id: _Optional[str] = ..., announcement_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_announcement_pb2.Announcement.Extra, str]]] = ...) -> None: ...

class DescribeAnnouncementOutput(_message.Message):
    __slots__ = ["announcement"]
    ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    announcement: _announcement_pb2.Announcement
    def __init__(self, announcement: _Optional[_Union[_announcement_pb2.Announcement, _Mapping]] = ...) -> None: ...

class DescribeAnnouncementStatusInput(_message.Message):
    __slots__ = ["announcement_id", "contest_id"]
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    announcement_id: str
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., announcement_id: _Optional[str] = ...) -> None: ...

class DescribeAnnouncementStatusOutput(_message.Message):
    __slots__ = ["is_read"]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    is_read: bool
    def __init__(self, is_read: bool = ...) -> None: ...

class ListAnnouncementsInput(_message.Message):
    __slots__ = ["contest_id", "extra", "filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "is_read"]
        ID_FIELD_NUMBER: _ClassVar[int]
        IS_READ_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        is_read: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., is_read: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    extra: _containers.RepeatedScalarFieldContainer[_announcement_pb2.Announcement.Extra]
    filters: ListAnnouncementsInput.Filter
    offset: int
    size: int
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListAnnouncementsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_announcement_pb2.Announcement.Extra, str]]] = ...) -> None: ...

class ListAnnouncementsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_announcement_pb2.Announcement]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_announcement_pb2.Announcement, _Mapping]]] = ...) -> None: ...

class ReadAnnouncementInput(_message.Message):
    __slots__ = ["announcement_id", "contest_id"]
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    announcement_id: str
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., announcement_id: _Optional[str] = ...) -> None: ...

class ReadAnnouncementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAnnouncementInput(_message.Message):
    __slots__ = ["announcement", "announcement_id", "contest_id"]
    ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    announcement: _announcement_pb2.Announcement
    announcement_id: str
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., announcement_id: _Optional[str] = ..., announcement: _Optional[_Union[_announcement_pb2.Announcement, _Mapping]] = ...) -> None: ...

class UpdateAnnouncementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WatchAnnouncementInput(_message.Message):
    __slots__ = ["announcement_id", "extra"]
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    announcement_id: str
    extra: _containers.RepeatedScalarFieldContainer[_announcement_pb2.Announcement.Extra]
    def __init__(self, announcement_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_announcement_pb2.Announcement.Extra, str]]] = ...) -> None: ...

class WatchAnnouncementOutput(_message.Message):
    __slots__ = ["announcement"]
    ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    announcement: _announcement_pb2.Announcement
    def __init__(self, announcement: _Optional[_Union[_announcement_pb2.Announcement, _Mapping]] = ...) -> None: ...

class WatchAnnouncementSummaryInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WatchAnnouncementSummaryOutput(_message.Message):
    __slots__ = ["unread_count"]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    unread_count: int
    def __init__(self, unread_count: _Optional[int] = ...) -> None: ...

class WatchAnnouncementsInput(_message.Message):
    __slots__ = ["extra"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_announcement_pb2.Announcement.Extra]
    def __init__(self, extra: _Optional[_Iterable[_Union[_announcement_pb2.Announcement.Extra, str]]] = ...) -> None: ...

class WatchAnnouncementsOutput(_message.Message):
    __slots__ = ["announcement", "event"]
    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    CREATED: WatchAnnouncementsOutput.Event
    DELETED: WatchAnnouncementsOutput.Event
    EVENT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EVENT: WatchAnnouncementsOutput.Event
    UPDATED: WatchAnnouncementsOutput.Event
    announcement: _announcement_pb2.Announcement
    event: WatchAnnouncementsOutput.Event
    def __init__(self, event: _Optional[_Union[WatchAnnouncementsOutput.Event, str]] = ..., announcement: _Optional[_Union[_announcement_pb2.Announcement, _Mapping]] = ...) -> None: ...
