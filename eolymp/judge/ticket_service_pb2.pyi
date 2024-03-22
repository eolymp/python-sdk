from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.judge import activity_pb2 as _activity_pb2
from eolymp.judge import announcement_pb2 as _announcement_pb2
from eolymp.judge import contest_pb2 as _contest_pb2
from eolymp.judge import participant_pb2 as _participant_pb2
from eolymp.judge import problem_pb2 as _problem_pb2
from eolymp.judge import reply_pb2 as _reply_pb2
from eolymp.judge import result_pb2 as _result_pb2
from eolymp.judge import score_pb2 as _score_pb2
from eolymp.judge import submission_pb2 as _submission_pb2
from eolymp.judge import template_pb2 as _template_pb2
from eolymp.judge import ticket_pb2 as _ticket_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloseTicketInput(_message.Message):
    __slots__ = ["contest_id", "ticket_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    ticket_id: str
    def __init__(self, contest_id: _Optional[str] = ..., ticket_id: _Optional[str] = ...) -> None: ...

class CloseTicketOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

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
    extra: _containers.RepeatedScalarFieldContainer[_reply_pb2.Reply.Extra]
    offset: int
    size: int
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., extra: _Optional[_Iterable[_Union[_reply_pb2.Reply.Extra, str]]] = ...) -> None: ...

class ListRepliesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_reply_pb2.Reply]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_reply_pb2.Reply, _Mapping]]] = ...) -> None: ...

class ListTicketsInput(_message.Message):
    __slots__ = ["extra", "filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["contest_id", "id", "is_open", "is_read_by_owner", "is_read_by_participant", "member_id", "own", "participant_id"]
        CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        IS_OPEN_FIELD_NUMBER: _ClassVar[int]
        IS_READ_BY_OWNER_FIELD_NUMBER: _ClassVar[int]
        IS_READ_BY_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        OWN_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
        contest_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        is_open: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        is_read_by_owner: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        is_read_by_participant: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        own: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        participant_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., contest_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., participant_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., is_read_by_participant: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., is_read_by_owner: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., is_open: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., own: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    CREATED_AT: ListTicketsInput.Sortable
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    READ_BY_OWNER: ListTicketsInput.Sortable
    READ_BY_PARTICIPANT: ListTicketsInput.Sortable
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_ticket_pb2.Ticket.Extra]
    filters: ListTicketsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListTicketsInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTicketsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListTicketsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_ticket_pb2.Ticket.Extra, str]]] = ...) -> None: ...

class ListTicketsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_ticket_pb2.Ticket]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_ticket_pb2.Ticket, _Mapping]]] = ...) -> None: ...

class OpenTicketInput(_message.Message):
    __slots__ = ["contest_id", "ticket_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    ticket_id: str
    def __init__(self, contest_id: _Optional[str] = ..., ticket_id: _Optional[str] = ...) -> None: ...

class OpenTicketOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadTicketInput(_message.Message):
    __slots__ = ["contest_id", "ticket_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    ticket_id: str
    def __init__(self, contest_id: _Optional[str] = ..., ticket_id: _Optional[str] = ...) -> None: ...

class ReadTicketOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReplyTicketInput(_message.Message):
    __slots__ = ["close", "message", "ticket_id"]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    close: bool
    message: _content_pb2.Content
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., close: bool = ...) -> None: ...

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

class WatchRepliesInput(_message.Message):
    __slots__ = ["cursor", "extra", "ticket_id"]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    cursor: str
    extra: _containers.RepeatedScalarFieldContainer[_reply_pb2.Reply.Extra]
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., cursor: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_reply_pb2.Reply.Extra, str]]] = ...) -> None: ...

class WatchRepliesOutput(_message.Message):
    __slots__ = ["event", "reply"]
    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CREATED: WatchRepliesOutput.Event
    DELETED: WatchRepliesOutput.Event
    EVENT_FIELD_NUMBER: _ClassVar[int]
    NO_TYPE: WatchRepliesOutput.Event
    REPLY_FIELD_NUMBER: _ClassVar[int]
    UPDATED: WatchRepliesOutput.Event
    event: WatchRepliesOutput.Event
    reply: _reply_pb2.Reply
    def __init__(self, event: _Optional[_Union[WatchRepliesOutput.Event, str]] = ..., reply: _Optional[_Union[_reply_pb2.Reply, _Mapping]] = ...) -> None: ...

class WatchTicketsInput(_message.Message):
    __slots__ = ["extra"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_ticket_pb2.Ticket.Extra]
    def __init__(self, extra: _Optional[_Iterable[_Union[_ticket_pb2.Ticket.Extra, str]]] = ...) -> None: ...

class WatchTicketsOutput(_message.Message):
    __slots__ = ["event", "ticket", "unread_count"]
    class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CREATED: WatchTicketsOutput.Event
    DELETED: WatchTicketsOutput.Event
    EVENT_FIELD_NUMBER: _ClassVar[int]
    NO_OPERATION: WatchTicketsOutput.Event
    REPLIED: WatchTicketsOutput.Event
    TICKET_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATED: WatchTicketsOutput.Event
    event: WatchTicketsOutput.Event
    ticket: _ticket_pb2.Ticket
    unread_count: int
    def __init__(self, event: _Optional[_Union[WatchTicketsOutput.Event, str]] = ..., ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ..., unread_count: _Optional[int] = ...) -> None: ...
