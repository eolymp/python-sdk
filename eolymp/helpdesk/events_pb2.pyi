from eolymp.helpdesk import ticket_pb2 as _ticket_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

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

class CommentChangedEvent(_message.Message):
    __slots__ = ("ticket_id", "before", "after")
    TICKET_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    ticket_id: str
    before: _ticket_pb2.Ticket.Comment
    after: _ticket_pb2.Ticket.Comment
    def __init__(self, ticket_id: _Optional[str] = ..., before: _Optional[_Union[_ticket_pb2.Ticket.Comment, _Mapping]] = ..., after: _Optional[_Union[_ticket_pb2.Ticket.Comment, _Mapping]] = ...) -> None: ...
