from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.helpdesk import document_pb2 as _document_pb2
from eolymp.helpdesk import ticket_pb2 as _ticket_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApproveTicketInput(_message.Message):
    __slots__ = ["comment", "ticket_id"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    comment: str
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class ApproveTicketOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CloseTicketInput(_message.Message):
    __slots__ = ["comment", "ticket_id"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    comment: str
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class CloseTicketOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateTicketInput(_message.Message):
    __slots__ = ["ticket"]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: _ticket_pb2.Ticket
    def __init__(self, ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class CreateTicketOutput(_message.Message):
    __slots__ = ["ticket_id"]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ...) -> None: ...

class DeleteTicketInput(_message.Message):
    __slots__ = ["ticket_id"]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ...) -> None: ...

class DeleteTicketOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeTicketInput(_message.Message):
    __slots__ = ["ticket_id"]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ...) -> None: ...

class DescribeTicketOutput(_message.Message):
    __slots__ = ["ticket"]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: _ticket_pb2.Ticket
    def __init__(self, ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class ListTicketsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["author", "id", "query", "status", "type"]
        AUTHOR_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        author: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        query: str
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., author: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListTicketsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTicketsInput.Filter, _Mapping]] = ...) -> None: ...

class ListTicketsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_ticket_pb2.Ticket]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_ticket_pb2.Ticket, _Mapping]]] = ...) -> None: ...

class RejectTicketInput(_message.Message):
    __slots__ = ["comment", "ticket_id"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    comment: str
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class RejectTicketOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateTicketInput(_message.Message):
    __slots__ = ["ticket", "ticket_id"]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    ticket: _ticket_pb2.Ticket
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., ticket: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...

class UpdateTicketOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
