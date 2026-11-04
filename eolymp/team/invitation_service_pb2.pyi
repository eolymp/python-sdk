from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.team import invitation_pb2 as _invitation_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateInvitationInput(_message.Message):
    __slots__ = ("invitation",)
    INVITATION_FIELD_NUMBER: _ClassVar[int]
    invitation: _invitation_pb2.Invitation
    def __init__(self, invitation: _Optional[_Union[_invitation_pb2.Invitation, _Mapping]] = ...) -> None: ...

class CreateInvitationOutput(_message.Message):
    __slots__ = ("invitation_id",)
    INVITATION_ID_FIELD_NUMBER: _ClassVar[int]
    invitation_id: str
    def __init__(self, invitation_id: _Optional[str] = ...) -> None: ...

class DescribeInvitationInput(_message.Message):
    __slots__ = ("invitation_id",)
    INVITATION_ID_FIELD_NUMBER: _ClassVar[int]
    invitation_id: str
    def __init__(self, invitation_id: _Optional[str] = ...) -> None: ...

class DescribeInvitationOutput(_message.Message):
    __slots__ = ("invitation",)
    INVITATION_FIELD_NUMBER: _ClassVar[int]
    invitation: _invitation_pb2.Invitation
    def __init__(self, invitation: _Optional[_Union[_invitation_pb2.Invitation, _Mapping]] = ...) -> None: ...

class ListInvitationsInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "team_id", "member_id", "status")
        ID_FIELD_NUMBER: _ClassVar[int]
        TEAM_ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        team_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., team_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListInvitationsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListInvitationsInput.Filter, _Mapping]] = ...) -> None: ...

class ListInvitationsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_invitation_pb2.Invitation]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_invitation_pb2.Invitation, _Mapping]]] = ...) -> None: ...

class AcceptInvitationInput(_message.Message):
    __slots__ = ("invitation_id",)
    INVITATION_ID_FIELD_NUMBER: _ClassVar[int]
    invitation_id: str
    def __init__(self, invitation_id: _Optional[str] = ...) -> None: ...

class AcceptInvitationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeclineInvitationInput(_message.Message):
    __slots__ = ("invitation_id",)
    INVITATION_ID_FIELD_NUMBER: _ClassVar[int]
    invitation_id: str
    def __init__(self, invitation_id: _Optional[str] = ...) -> None: ...

class DeclineInvitationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RevokeInvitationInput(_message.Message):
    __slots__ = ("invitation_id",)
    INVITATION_ID_FIELD_NUMBER: _ClassVar[int]
    invitation_id: str
    def __init__(self, invitation_id: _Optional[str] = ...) -> None: ...

class RevokeInvitationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResendInvitationInput(_message.Message):
    __slots__ = ("invitation_id",)
    INVITATION_ID_FIELD_NUMBER: _ClassVar[int]
    invitation_id: str
    def __init__(self, invitation_id: _Optional[str] = ...) -> None: ...

class ResendInvitationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
