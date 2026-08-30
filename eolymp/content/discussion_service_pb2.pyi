import datetime

from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.discussion import message_pb2 as _message_pb2
from eolymp.discussion import subscription_pb2 as _subscription_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeMessageInput(_message.Message):
    __slots__ = ("post_id", "message_id", "render", "extra")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    message_id: str
    render: bool
    extra: _containers.RepeatedScalarFieldContainer[_message_pb2.Message.Extra]
    def __init__(self, post_id: _Optional[str] = ..., message_id: _Optional[str] = ..., render: _Optional[bool] = ..., extra: _Optional[_Iterable[_Union[_message_pb2.Message.Extra, str]]] = ...) -> None: ...

class DescribeMessageOutput(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class ListMessagesInput(_message.Message):
    __slots__ = ("post_id", "render", "after", "size", "sort", "order", "filters", "extra")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListMessagesInput.Sortable]
        POSTED_AT: _ClassVar[ListMessagesInput.Sortable]
        VOTE_COUNT: _ClassVar[ListMessagesInput.Sortable]
        REPLY_COUNT: _ClassVar[ListMessagesInput.Sortable]
    DEFAULT: ListMessagesInput.Sortable
    POSTED_AT: ListMessagesInput.Sortable
    VOTE_COUNT: ListMessagesInput.Sortable
    REPLY_COUNT: ListMessagesInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("query", "id", "reply_to", "member_id", "thread_id", "vote_count", "reply_count", "posted_at")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        REPLY_TO_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        THREAD_ID_FIELD_NUMBER: _ClassVar[int]
        VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
        REPLY_COUNT_FIELD_NUMBER: _ClassVar[int]
        POSTED_AT_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        reply_to: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        thread_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        vote_count: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        reply_count: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        posted_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., reply_to: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., thread_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., vote_count: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., reply_count: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., posted_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ...) -> None: ...
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    render: bool
    after: str
    size: int
    sort: ListMessagesInput.Sortable
    order: _direction_pb2.Direction
    filters: ListMessagesInput.Filter
    extra: _containers.RepeatedScalarFieldContainer[_message_pb2.Message.Extra]
    def __init__(self, post_id: _Optional[str] = ..., render: _Optional[bool] = ..., after: _Optional[str] = ..., size: _Optional[int] = ..., sort: _Optional[_Union[ListMessagesInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., filters: _Optional[_Union[ListMessagesInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_message_pb2.Message.Extra, str]]] = ...) -> None: ...

class ListMessagesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_message_pb2.Message]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_message_pb2.Message, _Mapping]]] = ...) -> None: ...

class PostMessageInput(_message.Message):
    __slots__ = ("post_id", "message", "reply_to")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    message: _message_pb2.Message
    reply_to: str
    def __init__(self, post_id: _Optional[str] = ..., message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ..., reply_to: _Optional[str] = ...) -> None: ...

class PostMessageOutput(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class UpdateMessageInput(_message.Message):
    __slots__ = ("post_id", "message_id", "message")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    message_id: str
    message: _message_pb2.Message
    def __init__(self, post_id: _Optional[str] = ..., message_id: _Optional[str] = ..., message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class UpdateMessageOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteMessageInput(_message.Message):
    __slots__ = ("post_id", "message_id", "reason")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    message_id: str
    reason: str
    def __init__(self, post_id: _Optional[str] = ..., message_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class DeleteMessageOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VoteMessageInput(_message.Message):
    __slots__ = ("post_id", "message_id", "vote")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    message_id: str
    vote: int
    def __init__(self, post_id: _Optional[str] = ..., message_id: _Optional[str] = ..., vote: _Optional[int] = ...) -> None: ...

class VoteMessageOutput(_message.Message):
    __slots__ = ("vote_count",)
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    vote_count: int
    def __init__(self, vote_count: _Optional[int] = ...) -> None: ...

class ListMessageChangesInput(_message.Message):
    __slots__ = ("post_id", "message_id")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    message_id: str
    def __init__(self, post_id: _Optional[str] = ..., message_id: _Optional[str] = ...) -> None: ...

class ListMessageChangesOutput(_message.Message):
    __slots__ = ("items",)
    class Record(_message.Message):
        __slots__ = ("revision", "timestamp", "message")
        REVISION_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        revision: int
        timestamp: _timestamp_pb2.Timestamp
        message: _content_pb2.Content
        def __init__(self, revision: _Optional[int] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ListMessageChangesOutput.Record]
    def __init__(self, items: _Optional[_Iterable[_Union[ListMessageChangesOutput.Record, _Mapping]]] = ...) -> None: ...

class DescribeSubscriptionInput(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class DescribeSubscriptionOutput(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: _subscription_pb2.Subscription
    def __init__(self, subscription: _Optional[_Union[_subscription_pb2.Subscription, _Mapping]] = ...) -> None: ...

class UpdateSubscriptionInput(_message.Message):
    __slots__ = ("post_id", "subscription")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    subscription: _subscription_pb2.Subscription
    def __init__(self, post_id: _Optional[str] = ..., subscription: _Optional[_Union[_subscription_pb2.Subscription, _Mapping]] = ...) -> None: ...

class UpdateSubscriptionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
