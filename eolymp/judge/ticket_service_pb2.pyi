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

class CreateTicketInput(_message.Message):
    __slots__ = ["contest_id", "message", "raw_message", "subject"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RAW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    message: _content_pb2.Content
    raw_message: str
    subject: str
    def __init__(self, contest_id: _Optional[str] = ..., subject: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., raw_message: _Optional[str] = ...) -> None: ...

class CreateTicketOutput(_message.Message):
    __slots__ = ["ticket_id"]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ...) -> None: ...

class DeleteReplyInput(_message.Message):
    __slots__ = ["reply_id", "ticket_id"]
    REPLY_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    reply_id: str
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., reply_id: _Optional[str] = ...) -> None: ...

class DeleteReplyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteTicketInput(_message.Message):
    __slots__ = ["contest_id", "ticket_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    ticket_id: str
    def __init__(self, contest_id: _Optional[str] = ..., ticket_id: _Optional[str] = ...) -> None: ...

class DeleteTicketOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeTicketInput(_message.Message):
    __slots__ = ["contest_id", "extra", "ticket_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    extra: _containers.RepeatedScalarFieldContainer[_ticket_pb2.Ticket.Extra]
    ticket_id: str
    def __init__(self, contest_id: _Optional[str] = ..., ticket_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_ticket_pb2.Ticket.Extra, str]]] = ...) -> None: ...

class DescribeTicketOutput(_message.Message):
    __slots__ = ["ticket"]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: _ticket_pb2.Ticket
    def __init__(self, ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class ListRepliesInput(_message.Message):
    __slots__ = ["extra", "offset", "size", "ticket_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_ticket_reply_pb2.Reply.Extra]
    offset: int
    size: int
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., extra: _Optional[_Iterable[_Union[_ticket_reply_pb2.Reply.Extra, str]]] = ...) -> None: ...

class ListRepliesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_ticket_reply_pb2.Reply]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_ticket_reply_pb2.Reply, _Mapping]]] = ...) -> None: ...

class ListTicketsInput(_message.Message):
    __slots__ = ["after", "extra", "filters", "offset", "order", "size", "sort"]
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["contest_id", "id", "is_open", "is_read", "member_id", "own", "participant_id", "status"]
        CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        IS_OPEN_FIELD_NUMBER: _ClassVar[int]
        IS_READ_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        OWN_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        contest_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        is_open: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        is_read: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        own: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        participant_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., contest_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., participant_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., is_read: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., is_open: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., own: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT: ListTicketsInput.Sort
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT: ListTicketsInput.Sort
    after: str
    extra: _containers.RepeatedScalarFieldContainer[_ticket_pb2.Ticket.Extra]
    filters: ListTicketsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListTicketsInput.Sort
    def __init__(self, after: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTicketsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListTicketsInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_ticket_pb2.Ticket.Extra, str]]] = ...) -> None: ...

class ListTicketsOutput(_message.Message):
    __slots__ = ["items", "next_page_cursor", "prev_page_cursor", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_ticket_pb2.Ticket]
    next_page_cursor: str
    prev_page_cursor: str
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_ticket_pb2.Ticket, _Mapping]]] = ..., next_page_cursor: _Optional[str] = ..., prev_page_cursor: _Optional[str] = ...) -> None: ...

class ReadTicketInput(_message.Message):
    __slots__ = ["contest_id", "ticket_id", "timestamp"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    ticket_id: str
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, contest_id: _Optional[str] = ..., ticket_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReadTicketOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReplyTicketInput(_message.Message):
    __slots__ = ["change_status_to", "message", "ticket_id"]
    CHANGE_STATUS_TO_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    change_status_to: _ticket_pb2.Ticket.Status
    message: _content_pb2.Content
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., change_status_to: _Optional[_Union[_ticket_pb2.Ticket.Status, str]] = ...) -> None: ...

class ReplyTicketOutput(_message.Message):
    __slots__ = ["reply_id"]
    REPLY_ID_FIELD_NUMBER: _ClassVar[int]
    reply_id: str
    def __init__(self, reply_id: _Optional[str] = ...) -> None: ...

class UpdateReplyInput(_message.Message):
    __slots__ = ["message", "reply_id", "ticket_id"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPLY_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    message: _content_pb2.Content
    reply_id: str
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., reply_id: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class UpdateReplyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateTicketInput(_message.Message):
    __slots__ = ["patch", "ticket", "ticket_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateTicketInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    STATUS: UpdateTicketInput.Patch
    SUBJECT: UpdateTicketInput.Patch
    TICKET_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateTicketInput.Patch]
    ticket: _ticket_pb2.Ticket
    ticket_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateTicketInput.Patch, str]]] = ..., ticket_id: _Optional[str] = ..., ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class UpdateTicketOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class WatchRepliesInput(_message.Message):
    __slots__ = ["cursor", "extra", "ticket_id"]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    cursor: str
    extra: _containers.RepeatedScalarFieldContainer[_ticket_reply_pb2.Reply.Extra]
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., cursor: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_ticket_reply_pb2.Reply.Extra, str]]] = ...) -> None: ...

class WatchRepliesOutput(_message.Message):
    __slots__ = ["event", "reply"]
    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CREATED: WatchRepliesOutput.Event
    DELETED: WatchRepliesOutput.Event
    EVENT_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EVENT: WatchRepliesOutput.Event
    UPDATED: WatchRepliesOutput.Event
    event: WatchRepliesOutput.Event
    reply: _ticket_reply_pb2.Reply
    def __init__(self, event: _Optional[_Union[WatchRepliesOutput.Event, str]] = ..., reply: _Optional[_Union[_ticket_reply_pb2.Reply, _Mapping]] = ...) -> None: ...

class WatchTicketInput(_message.Message):
    __slots__ = ["extra", "ticket_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_ticket_pb2.Ticket.Extra]
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_ticket_pb2.Ticket.Extra, str]]] = ...) -> None: ...

class WatchTicketOutput(_message.Message):
    __slots__ = ["ticket"]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: _ticket_pb2.Ticket
    def __init__(self, ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class WatchTicketSummaryInput(_message.Message):
    __slots__ = ["contest_id", "member_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    member_id: str
    def __init__(self, contest_id: _Optional[str] = ..., member_id: _Optional[str] = ...) -> None: ...

class WatchTicketSummaryOutput(_message.Message):
    __slots__ = ["unread_count", "unresolved_count"]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNRESOLVED_COUNT_FIELD_NUMBER: _ClassVar[int]
    unread_count: int
    unresolved_count: int
    def __init__(self, unread_count: _Optional[int] = ..., unresolved_count: _Optional[int] = ...) -> None: ...

class WatchTicketsInput(_message.Message):
    __slots__ = ["contest_id", "extra", "member_id", "status"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    extra: _containers.RepeatedScalarFieldContainer[_ticket_pb2.Ticket.Extra]
    member_id: str
    status: str
    def __init__(self, contest_id: _Optional[str] = ..., member_id: _Optional[str] = ..., status: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_ticket_pb2.Ticket.Extra, str]]] = ...) -> None: ...

class WatchTicketsOutput(_message.Message):
    __slots__ = ["event", "ticket"]
    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CREATED: WatchTicketsOutput.Event
    DELETED: WatchTicketsOutput.Event
    EVENT_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EVENT: WatchTicketsOutput.Event
    UPDATED: WatchTicketsOutput.Event
    event: WatchTicketsOutput.Event
    ticket: _ticket_pb2.Ticket
    def __init__(self, event: _Optional[_Union[WatchTicketsOutput.Event, str]] = ..., ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...
