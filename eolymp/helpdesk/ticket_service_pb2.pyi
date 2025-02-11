from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.helpdesk import ticket_pb2 as _ticket_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTicketInput(_message.Message):
    __slots__ = ("ticket", "captcha")
    TICKET_FIELD_NUMBER: _ClassVar[int]
    CAPTCHA_FIELD_NUMBER: _ClassVar[int]
    ticket: _ticket_pb2.Ticket
    captcha: str
    def __init__(self, ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ..., captcha: _Optional[str] = ...) -> None: ...

class CreateTicketOutput(_message.Message):
    __slots__ = ("ticket_id",)
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ...) -> None: ...

class UpdateTicketInput(_message.Message):
    __slots__ = ("ticket_id", "ticket")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    ticket: _ticket_pb2.Ticket
    def __init__(self, ticket_id: _Optional[str] = ..., ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class UpdateTicketOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTicketInput(_message.Message):
    __slots__ = ("ticket_id",)
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ...) -> None: ...

class DeleteTicketOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeTicketInput(_message.Message):
    __slots__ = ("ticket_id", "render")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    render: bool
    def __init__(self, ticket_id: _Optional[str] = ..., render: bool = ...) -> None: ...

class DescribeTicketOutput(_message.Message):
    __slots__ = ("ticket",)
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: _ticket_pb2.Ticket
    def __init__(self, ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class ListTicketsInput(_message.Message):
    __slots__ = ("render", "offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("query", "id", "user_id", "user_email", "status", "type", "created_at", "updated_at", "locale")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        user_email: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        created_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        updated_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_email: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., created_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., updated_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    RENDER_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    render: bool
    offset: int
    size: int
    filters: ListTicketsInput.Filter
    def __init__(self, render: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTicketsInput.Filter, _Mapping]] = ...) -> None: ...

class ListTicketsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_ticket_pb2.Ticket]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_ticket_pb2.Ticket, _Mapping]]] = ...) -> None: ...

class ApproveTicketInput(_message.Message):
    __slots__ = ("ticket_id", "comment")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    comment: str
    def __init__(self, ticket_id: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class ApproveTicketOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RejectTicketInput(_message.Message):
    __slots__ = ("ticket_id", "comment")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    comment: str
    def __init__(self, ticket_id: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class RejectTicketOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloseTicketInput(_message.Message):
    __slots__ = ("ticket_id", "comment")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    comment: str
    def __init__(self, ticket_id: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class CloseTicketOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddCommentInput(_message.Message):
    __slots__ = ("ticket_id", "comment")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    comment: _ticket_pb2.Ticket.Comment
    def __init__(self, ticket_id: _Optional[str] = ..., comment: _Optional[_Union[_ticket_pb2.Ticket.Comment, _Mapping]] = ...) -> None: ...

class AddCommentOutput(_message.Message):
    __slots__ = ("comment_id",)
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    def __init__(self, comment_id: _Optional[str] = ...) -> None: ...

class UpdateCommentInput(_message.Message):
    __slots__ = ("ticket_id", "comment_id", "comment")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    comment_id: str
    comment: _ticket_pb2.Ticket.Comment
    def __init__(self, ticket_id: _Optional[str] = ..., comment_id: _Optional[str] = ..., comment: _Optional[_Union[_ticket_pb2.Ticket.Comment, _Mapping]] = ...) -> None: ...

class UpdateCommentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCommentInput(_message.Message):
    __slots__ = ("ticket_id", "comment_id")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    comment_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., comment_id: _Optional[str] = ...) -> None: ...

class DeleteCommentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCommentsInput(_message.Message):
    __slots__ = ("ticket_id", "render", "offset", "size")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    render: bool
    offset: int
    size: int
    def __init__(self, ticket_id: _Optional[str] = ..., render: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListCommentsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_ticket_pb2.Ticket.Comment]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_ticket_pb2.Ticket.Comment, _Mapping]]] = ...) -> None: ...

class DescribeCommentInput(_message.Message):
    __slots__ = ("ticket_id", "comment_id", "render")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    comment_id: str
    render: bool
    def __init__(self, ticket_id: _Optional[str] = ..., comment_id: _Optional[str] = ..., render: bool = ...) -> None: ...

class DescribeCommentOutput(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: _ticket_pb2.Ticket.Comment
    def __init__(self, comment: _Optional[_Union[_ticket_pb2.Ticket.Comment, _Mapping]] = ...) -> None: ...

class UploadAttachmentInput(_message.Message):
    __slots__ = ("name", "type", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    data: bytes
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadAttachmentOutput(_message.Message):
    __slots__ = ("attachment_url",)
    ATTACHMENT_URL_FIELD_NUMBER: _ClassVar[int]
    attachment_url: str
    def __init__(self, attachment_url: _Optional[str] = ...) -> None: ...
