from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.discussion import message_pb2 as _message_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteMessageInput(_message.Message):
    __slots__ = ["message_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class DeleteMessageOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeMessageInput(_message.Message):
    __slots__ = ["message_id", "render"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    render: bool
    def __init__(self, message_id: _Optional[str] = ..., render: bool = ...) -> None: ...

class DescribeMessageOutput(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class ListMessagesInput(_message.Message):
    __slots__ = ["filters", "offset", "render", "size", "thread_id"]
    class Filter(_message.Message):
        __slots__ = ["id", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    filters: ListMessagesInput.Filter
    offset: int
    render: bool
    size: int
    thread_id: str
    def __init__(self, render: bool = ..., thread_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListMessagesInput.Filter, _Mapping]] = ...) -> None: ...

class ListMessagesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_message_pb2.Message]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_message_pb2.Message, _Mapping]]] = ...) -> None: ...

class PostMessageInput(_message.Message):
    __slots__ = ["message", "reply_to"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    reply_to: str
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ..., reply_to: _Optional[str] = ...) -> None: ...

class PostMessageOutput(_message.Message):
    __slots__ = ["message_id"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class UpdateMessageInput(_message.Message):
    __slots__ = ["message", "message_id"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    message_id: str
    def __init__(self, message_id: _Optional[str] = ..., message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class UpdateMessageOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VoteMessageInput(_message.Message):
    __slots__ = ["message_id", "vote"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    vote: int
    def __init__(self, message_id: _Optional[str] = ..., vote: _Optional[int] = ...) -> None: ...

class VoteMessageOutput(_message.Message):
    __slots__ = ["vote_count"]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    vote_count: int
    def __init__(self, vote_count: _Optional[int] = ...) -> None: ...
