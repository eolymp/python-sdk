from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.helpdesk import auto_reply_pb2 as _auto_reply_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAutoReplyInput(_message.Message):
    __slots__ = ["reply"]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    reply: _auto_reply_pb2.AutoReply
    def __init__(self, reply: _Optional[_Union[_auto_reply_pb2.AutoReply, _Mapping]] = ...) -> None: ...

class CreateAutoReplyOutput(_message.Message):
    __slots__ = ["reply_id"]
    REPLY_ID_FIELD_NUMBER: _ClassVar[int]
    reply_id: str
    def __init__(self, reply_id: _Optional[str] = ...) -> None: ...

class DeleteAutoReplyInput(_message.Message):
    __slots__ = ["reply_id"]
    REPLY_ID_FIELD_NUMBER: _ClassVar[int]
    reply_id: str
    def __init__(self, reply_id: _Optional[str] = ...) -> None: ...

class DeleteAutoReplyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeAutoReplyInput(_message.Message):
    __slots__ = ["render", "reply_id"]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    REPLY_ID_FIELD_NUMBER: _ClassVar[int]
    render: bool
    reply_id: str
    def __init__(self, reply_id: _Optional[str] = ..., render: bool = ...) -> None: ...

class DescribeAutoReplyOutput(_message.Message):
    __slots__ = ["reply"]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    reply: _auto_reply_pb2.AutoReply
    def __init__(self, reply: _Optional[_Union[_auto_reply_pb2.AutoReply, _Mapping]] = ...) -> None: ...

class ListAutoRepliesInput(_message.Message):
    __slots__ = ["filters", "offset", "render", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "locale", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListAutoRepliesInput.Filter
    offset: int
    render: bool
    size: int
    def __init__(self, render: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListAutoRepliesInput.Filter, _Mapping]] = ...) -> None: ...

class ListAutoRepliesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_auto_reply_pb2.AutoReply]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_auto_reply_pb2.AutoReply, _Mapping]]] = ...) -> None: ...

class UpdateAutoReplyInput(_message.Message):
    __slots__ = ["reply", "reply_id"]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    REPLY_ID_FIELD_NUMBER: _ClassVar[int]
    reply: _auto_reply_pb2.AutoReply
    reply_id: str
    def __init__(self, reply_id: _Optional[str] = ..., reply: _Optional[_Union[_auto_reply_pb2.AutoReply, _Mapping]] = ...) -> None: ...

class UpdateAutoReplyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
