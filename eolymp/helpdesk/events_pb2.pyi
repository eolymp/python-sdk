from eolymp.helpdesk import ticket_pb2 as _ticket_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommentChangedEvent(_message.Message):
    __slots__ = ["after", "before", "ticket_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    after: _ticket_pb2.Ticket.Comment
    before: _ticket_pb2.Ticket.Comment
    ticket_id: str
    def __init__(self, ticket_id: _Optional[str] = ..., before: _Optional[_Union[_ticket_pb2.Ticket.Comment, _Mapping]] = ..., after: _Optional[_Union[_ticket_pb2.Ticket.Comment, _Mapping]] = ...) -> None: ...

class TicketChangedEvent(_message.Message):
    __slots__ = ["after", "before", "scope"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    after: _ticket_pb2.Ticket
    before: _ticket_pb2.Ticket
    scope: str
    def __init__(self, scope: _Optional[str] = ..., before: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ..., after: _Optional[_Union[_ticket_pb2.Ticket, _Mapping]] = ...) -> None: ...
