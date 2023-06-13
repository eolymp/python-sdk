from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.discussion import forum_pb2 as _forum_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateForumInput(_message.Message):
    __slots__ = ["forum"]
    FORUM_FIELD_NUMBER: _ClassVar[int]
    forum: _forum_pb2.Forum
    def __init__(self, forum: _Optional[_Union[_forum_pb2.Forum, _Mapping]] = ...) -> None: ...

class CreateForumOutput(_message.Message):
    __slots__ = ["forum_id"]
    FORUM_ID_FIELD_NUMBER: _ClassVar[int]
    forum_id: str
    def __init__(self, forum_id: _Optional[str] = ...) -> None: ...

class DeleteForumInput(_message.Message):
    __slots__ = ["forum_id"]
    FORUM_ID_FIELD_NUMBER: _ClassVar[int]
    forum_id: str
    def __init__(self, forum_id: _Optional[str] = ...) -> None: ...

class DeleteForumOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeForumInput(_message.Message):
    __slots__ = ["forum_id", "render"]
    FORUM_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    forum_id: str
    render: bool
    def __init__(self, forum_id: _Optional[str] = ..., render: bool = ...) -> None: ...

class DescribeForumOutput(_message.Message):
    __slots__ = ["forum"]
    FORUM_FIELD_NUMBER: _ClassVar[int]
    forum: _forum_pb2.Forum
    def __init__(self, forum: _Optional[_Union[_forum_pb2.Forum, _Mapping]] = ...) -> None: ...

class ListForumsInput(_message.Message):
    __slots__ = ["filters", "offset", "render", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "parent_id", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        PARENT_ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        parent_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., parent_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListForumsInput.Filter
    offset: int
    render: bool
    size: int
    def __init__(self, render: bool = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListForumsInput.Filter, _Mapping]] = ...) -> None: ...

class ListForumsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_forum_pb2.Forum]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_forum_pb2.Forum, _Mapping]]] = ...) -> None: ...

class UpdateForumInput(_message.Message):
    __slots__ = ["forum", "forum_id"]
    FORUM_FIELD_NUMBER: _ClassVar[int]
    FORUM_ID_FIELD_NUMBER: _ClassVar[int]
    forum: _forum_pb2.Forum
    forum_id: str
    def __init__(self, forum_id: _Optional[str] = ..., forum: _Optional[_Union[_forum_pb2.Forum, _Mapping]] = ...) -> None: ...

class UpdateForumOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
