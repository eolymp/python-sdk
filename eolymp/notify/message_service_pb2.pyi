from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.notify import message_pb2 as _message_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateMessageInput(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class CreateMessageOutput(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class UpdateMessageInput(_message.Message):
    __slots__ = ("message_id", "message")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    message: _message_pb2.Message.Patch
    def __init__(self, message_id: _Optional[str] = ..., message: _Optional[_Union[_message_pb2.Message.Patch, _Mapping]] = ...) -> None: ...

class UpdateMessageOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteMessageInput(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class DeleteMessageOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeMessageInput(_message.Message):
    __slots__ = ("message_id", "extra")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    extra: _containers.RepeatedScalarFieldContainer[_message_pb2.Message.Extra.Field]
    def __init__(self, message_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_message_pb2.Message.Extra.Field, str]]] = ...) -> None: ...

class DescribeMessageOutput(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class ListMessagesInput(_message.Message):
    __slots__ = ("offset", "size", "search", "filters", "sort", "order", "extra")
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_SORT: _ClassVar[ListMessagesInput.Sort]
        CREATED_AT: _ClassVar[ListMessagesInput.Sort]
        SCHEDULED_AT: _ClassVar[ListMessagesInput.Sort]
    UNKNOWN_SORT: ListMessagesInput.Sort
    CREATED_AT: ListMessagesInput.Sort
    SCHEDULED_AT: ListMessagesInput.Sort
    class Filter(_message.Message):
        __slots__ = ("id", "status", "reference", "channel_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        reference: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        channel_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., reference: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., channel_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    search: str
    filters: ListMessagesInput.Filter
    sort: ListMessagesInput.Sort
    order: _direction_pb2.Direction
    extra: _containers.RepeatedScalarFieldContainer[_message_pb2.Message.Extra.Field]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListMessagesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListMessagesInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_message_pb2.Message.Extra.Field, str]]] = ...) -> None: ...

class ListMessagesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_message_pb2.Message]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_message_pb2.Message, _Mapping]]] = ...) -> None: ...

class PublishMessageInput(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class PublishMessageOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
