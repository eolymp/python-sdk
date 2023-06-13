from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.discussion import discussion_pb2 as _discussion_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDiscussionInput(_message.Message):
    __slots__ = ["discussion"]
    DISCUSSION_FIELD_NUMBER: _ClassVar[int]
    discussion: _discussion_pb2.Discussion
    def __init__(self, discussion: _Optional[_Union[_discussion_pb2.Discussion, _Mapping]] = ...) -> None: ...

class CreateDiscussionOutput(_message.Message):
    __slots__ = ["discussion_id"]
    DISCUSSION_ID_FIELD_NUMBER: _ClassVar[int]
    discussion_id: str
    def __init__(self, discussion_id: _Optional[str] = ...) -> None: ...

class DeleteDiscussionInput(_message.Message):
    __slots__ = ["discussion_id"]
    DISCUSSION_ID_FIELD_NUMBER: _ClassVar[int]
    discussion_id: str
    def __init__(self, discussion_id: _Optional[str] = ...) -> None: ...

class DeleteDiscussionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeDiscussionInput(_message.Message):
    __slots__ = ["discussion_id", "render"]
    DISCUSSION_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    discussion_id: str
    render: bool
    def __init__(self, discussion_id: _Optional[str] = ..., render: bool = ...) -> None: ...

class DescribeDiscussionOutput(_message.Message):
    __slots__ = ["discussion"]
    DISCUSSION_FIELD_NUMBER: _ClassVar[int]
    discussion: _discussion_pb2.Discussion
    def __init__(self, discussion: _Optional[_Union[_discussion_pb2.Discussion, _Mapping]] = ...) -> None: ...

class ListDiscussionsInput(_message.Message):
    __slots__ = ["filters", "offset", "render", "size"]
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
    filters: ListDiscussionsInput.Filter
    offset: int
    render: bool
    size: int
    def __init__(self, render: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListDiscussionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListDiscussionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_discussion_pb2.Discussion]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_discussion_pb2.Discussion, _Mapping]]] = ...) -> None: ...

class UpdateDiscussionInput(_message.Message):
    __slots__ = ["discussion", "discussion_id"]
    DISCUSSION_FIELD_NUMBER: _ClassVar[int]
    DISCUSSION_ID_FIELD_NUMBER: _ClassVar[int]
    discussion: _discussion_pb2.Discussion
    discussion_id: str
    def __init__(self, discussion_id: _Optional[str] = ..., discussion: _Optional[_Union[_discussion_pb2.Discussion, _Mapping]] = ...) -> None: ...

class UpdateDiscussionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VoteDiscussionInput(_message.Message):
    __slots__ = ["discussion_id", "vote"]
    DISCUSSION_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    discussion_id: str
    vote: int
    def __init__(self, discussion_id: _Optional[str] = ..., vote: _Optional[int] = ...) -> None: ...

class VoteDiscussionOutput(_message.Message):
    __slots__ = ["vote_count"]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    vote_count: int
    def __init__(self, vote_count: _Optional[int] = ...) -> None: ...
