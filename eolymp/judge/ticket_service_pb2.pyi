from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.judge import ticket_pb2 as _ticket_pb2
from eolymp.judge import ticket_reply_pb2 as _ticket_reply_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TicketChangedEvent(_message.Message):
    __slots__ = ("scope", "before", "after")
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    scope: str
    before: _ticket_pb2.Ticket
    after: _ticket_pb2.Ticket
    def __init__(self, scope: _Optional[str] = ..., before: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ..., after: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class ReplyChangedEvent(_message.Message):
    __slots__ = ("ticket_id", "before", "after")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    before: _ticket_reply_pb2.Reply
    after: _ticket_reply_pb2.Reply
    def __init__(self, ticket_id: _Optional[str] = ..., before: _Optional[_Union[_ticket_reply_pb2.Reply, _Mapping]] = ..., after: _Optional[_Union[_ticket_reply_pb2.Reply, _Mapping]] = ...) -> None: ...

class CreateTicketInput(_message.Message):
    __slots__ = ("contest_id", "subject", "message", "raw_message")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RAW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    subject: str
    message: _content_pb2.Content
    raw_message: str
    def __init__(self, contest_id: _Optional[str] = ..., subject: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., raw_message: _Optional[str] = ...) -> None: ...

class CreateTicketOutput(_message.Message):
    __slots__ = ("ticket_id",)
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ...) -> None: ...

class UpdateTicketInput(_message.Message):
    __slots__ = ("patch", "ticket_id", "ticket")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateTicketInput.Patch]
        STATUS: _ClassVar[UpdateTicketInput.Patch]
        SUBJECT: _ClassVar[UpdateTicketInput.Patch]
    ALL: UpdateTicketInput.Patch
    STATUS: UpdateTicketInput.Patch
    SUBJECT: UpdateTicketInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateTicketInput.Patch]
    ticket_id: str
    ticket: _ticket_pb2.Ticket
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateTicketInput.Patch, str]]] = ..., ticket_id: _Optional[str] = ..., ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class UpdateTicketOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadTicketInput(_message.Message):
    __slots__ = ("contest_id", "ticket_id", "timestamp")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    ticket_id: str
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, contest_id: _Optional[str] = ..., ticket_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReadTicketOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTicketInput(_message.Message):
    __slots__ = ("contest_id", "ticket_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    ticket_id: str
    def __init__(self, contest_id: _Optional[str] = ..., ticket_id: _Optional[str] = ...) -> None: ...

class DeleteTicketOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeTicketInput(_message.Message):
    __slots__ = ("contest_id", "ticket_id", "extra")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    ticket_id: str
    extra: _containers.RepeatedScalarFieldContainer[_ticket_pb2.Ticket.Extra]
    def __init__(self, contest_id: _Optional[str] = ..., ticket_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_ticket_pb2.Ticket.Extra, str]]] = ...) -> None: ...

class DescribeTicketOutput(_message.Message):
    __slots__ = ("ticket",)
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: _ticket_pb2.Ticket
    def __init__(self, ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class ListTicketsInput(_message.Message):
    __slots__ = ("after", "offset", "size", "filters", "sort", "order", "extra")
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CREATED_AT: _ClassVar[ListTicketsInput.Sort]
        UPDATED_AT: _ClassVar[ListTicketsInput.Sort]
    CREATED_AT: ListTicketsInput.Sort
    UPDATED_AT: ListTicketsInput.Sort
    class Filter(_message.Message):
        __slots__ = ("id", "contest_id", "participant_id", "member_id", "is_read", "is_open", "own", "status")
        ID_FIELD_NUMBER: _ClassVar[int]
        CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        IS_READ_FIELD_NUMBER: _ClassVar[int]
        IS_OPEN_FIELD_NUMBER: _ClassVar[int]
        OWN_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        contest_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        participant_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        is_read: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        is_open: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        own: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., contest_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., participant_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., is_read: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., is_open: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., own: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    after: str
    offset: int
    size: int
    filters: ListTicketsInput.Filter
    sort: ListTicketsInput.Sort
    order: _direction_pb2.Direction
    extra: _containers.RepeatedScalarFieldContainer[_ticket_pb2.Ticket.Extra]
    def __init__(self, after: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTicketsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListTicketsInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_ticket_pb2.Ticket.Extra, str]]] = ...) -> None: ...

class ListTicketsOutput(_message.Message):
    __slots__ = ("total", "items", "next_page_cursor")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_ticket_pb2.Ticket]
    next_page_cursor: str
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_ticket_pb2.Ticket, _Mapping]]] = ..., next_page_cursor: _Optional[str] = ...) -> None: ...

class ReplyTicketInput(_message.Message):
    __slots__ = ("ticket_id", "message", "change_status_to")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_STATUS_TO_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    message: _content_pb2.Content
    change_status_to: _ticket_pb2.Ticket.Status
    def __init__(self, ticket_id: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., change_status_to: _Optional[_Union[_ticket_pb2.Ticket.Status, str]] = ...) -> None: ...

class ReplyTicketOutput(_message.Message):
    __slots__ = ("reply_id",)
    REPLY_ID_FIELD_NUMBER: _ClassVar[int]
    reply_id: str
    def __init__(self, reply_id: _Optional[str] = ...) -> None: ...

class WatchTicketInput(_message.Message):
    __slots__ = ("ticket_id", "extra")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    extra: _containers.RepeatedScalarFieldContainer[_ticket_pb2.Ticket.Extra]
    def __init__(self, ticket_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_ticket_pb2.Ticket.Extra, str]]] = ...) -> None: ...

class WatchTicketOutput(_message.Message):
    __slots__ = ("ticket",)
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: _ticket_pb2.Ticket
    def __init__(self, ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class WatchTicketsInput(_message.Message):
    __slots__ = ("contest_id", "member_id", "status", "extra")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    member_id: str
    status: str
    extra: _containers.RepeatedScalarFieldContainer[_ticket_pb2.Ticket.Extra]
    def __init__(self, contest_id: _Optional[str] = ..., member_id: _Optional[str] = ..., status: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_ticket_pb2.Ticket.Extra, str]]] = ...) -> None: ...

class WatchTicketsOutput(_message.Message):
    __slots__ = ("event", "ticket")
    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EVENT: _ClassVar[WatchTicketsOutput.Event]
        CREATED: _ClassVar[WatchTicketsOutput.Event]
        UPDATED: _ClassVar[WatchTicketsOutput.Event]
        DELETED: _ClassVar[WatchTicketsOutput.Event]
    UNKNOWN_EVENT: WatchTicketsOutput.Event
    CREATED: WatchTicketsOutput.Event
    UPDATED: WatchTicketsOutput.Event
    DELETED: WatchTicketsOutput.Event
    EVENT_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    event: WatchTicketsOutput.Event
    ticket: _ticket_pb2.Ticket
    def __init__(self, event: _Optional[_Union[WatchTicketsOutput.Event, str]] = ..., ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class WatchTicketSummaryInput(_message.Message):
    __slots__ = ("contest_id", "member_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    member_id: str
    def __init__(self, contest_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class WatchTicketSummaryOutput(_message.Message):
    __slots__ = ("unread_count", "unresolved_count")
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNRESOLVED_COUNT_FIELD_NUMBER: _ClassVar[int]
    unread_count: int
    unresolved_count: int
    def __init__(self, unread_count: _Optional[int] = ..., unresolved_count: _Optional[int] = ...) -> None: ...

class ListRepliesInput(_message.Message):
    __slots__ = ("ticket_id", "offset", "size", "extra")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    offset: int
    size: int
    extra: _containers.RepeatedScalarFieldContainer[_ticket_reply_pb2.Reply.Extra]
    def __init__(self, ticket_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., extra: _Optional[_Iterable[_Union[_ticket_reply_pb2.Reply.Extra, str]]] = ...) -> None: ...

class ListRepliesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_ticket_reply_pb2.Reply]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_ticket_reply_pb2.Reply, _Mapping]]] = ...) -> None: ...

class DescribeReplyInput(_message.Message):
    __slots__ = ("ticket_id", "reply_id", "extra")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    reply_id: str
    extra: _containers.RepeatedScalarFieldContainer[_ticket_reply_pb2.Reply.Extra]
    def __init__(self, ticket_id: _Optional[str] = ..., reply_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_ticket_reply_pb2.Reply.Extra, str]]] = ...) -> None: ...

class DescribeReplyOutput(_message.Message):
    __slots__ = ("reply",)
    REPLY_FIELD_NUMBER: _ClassVar[int]
    reply: _ticket_reply_pb2.Reply
    def __init__(self, reply: _Optional[_Union[_ticket_reply_pb2.Reply, _Mapping]] = ...) -> None: ...

class DeleteReplyInput(_message.Message):
    __slots__ = ("ticket_id", "reply_id")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    reply_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., reply_id: _Optional[str] = ...) -> None: ...

class DeleteReplyOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateReplyInput(_message.Message):
    __slots__ = ("ticket_id", "reply_id", "message")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    reply_id: str
    message: _content_pb2.Content
    def __init__(self, ticket_id: _Optional[str] = ..., reply_id: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class UpdateReplyOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WatchRepliesInput(_message.Message):
    __slots__ = ("ticket_id", "cursor", "extra")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    cursor: str
    extra: _containers.RepeatedScalarFieldContainer[_ticket_reply_pb2.Reply.Extra]
    def __init__(self, ticket_id: _Optional[str] = ..., cursor: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_ticket_reply_pb2.Reply.Extra, str]]] = ...) -> None: ...

class WatchRepliesOutput(_message.Message):
    __slots__ = ("event", "reply")
    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EVENT: _ClassVar[WatchRepliesOutput.Event]
        CREATED: _ClassVar[WatchRepliesOutput.Event]
        UPDATED: _ClassVar[WatchRepliesOutput.Event]
        DELETED: _ClassVar[WatchRepliesOutput.Event]
    UNKNOWN_EVENT: WatchRepliesOutput.Event
    CREATED: WatchRepliesOutput.Event
    UPDATED: WatchRepliesOutput.Event
    DELETED: WatchRepliesOutput.Event
    EVENT_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    event: WatchRepliesOutput.Event
    reply: _ticket_reply_pb2.Reply
    def __init__(self, event: _Optional[_Union[WatchRepliesOutput.Event, str]] = ..., reply: _Optional[_Union[_ticket_reply_pb2.Reply, _Mapping]] = ...) -> None: ...
