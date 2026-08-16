from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.copilot import chat_pb2 as _chat_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartChatInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartChatOutput(_message.Message):
    __slots__ = ("chat_id",)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    def __init__(self, chat_id: _Optional[str] = ...) -> None: ...

class DescribeChatInput(_message.Message):
    __slots__ = ("chat_id",)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    def __init__(self, chat_id: _Optional[str] = ...) -> None: ...

class DescribeChatOutput(_message.Message):
    __slots__ = ("chat",)
    CHAT_FIELD_NUMBER: _ClassVar[int]
    chat: _chat_pb2.Chat
    def __init__(self, chat: _Optional[_Union[_chat_pb2.Chat, _Mapping]] = ...) -> None: ...

class ListChatsInput(_message.Message):
    __slots__ = ("offset", "size", "query", "filters", "sort", "order")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListChatsInput.Sortable]
        CREATED_AT: _ClassVar[ListChatsInput.Sortable]
        UPDATED_AT: _ClassVar[ListChatsInput.Sortable]
    DEFAULT: ListChatsInput.Sortable
    CREATED_AT: ListChatsInput.Sortable
    UPDATED_AT: ListChatsInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "archived")
        ID_FIELD_NUMBER: _ClassVar[int]
        ARCHIVED_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        archived: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., archived: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    query: str
    filters: ListChatsInput.Filter
    sort: ListChatsInput.Sortable
    order: _direction_pb2.Direction
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., query: _Optional[str] = ..., filters: _Optional[_Union[ListChatsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListChatsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListChatsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_chat_pb2.Chat]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_chat_pb2.Chat, _Mapping]]] = ...) -> None: ...

class ArchiveChatInput(_message.Message):
    __slots__ = ("chat_id", "unarchive")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    UNARCHIVE_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    unarchive: bool
    def __init__(self, chat_id: _Optional[str] = ..., unarchive: _Optional[bool] = ...) -> None: ...

class ArchiveChatOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteChatInput(_message.Message):
    __slots__ = ("chat_id",)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    def __init__(self, chat_id: _Optional[str] = ...) -> None: ...

class DeleteChatOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendMessageInput(_message.Message):
    __slots__ = ("chat_id", "model", "message", "approval")
    class Message(_message.Message):
        __slots__ = ("text",)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        def __init__(self, text: _Optional[str] = ...) -> None: ...
    class Approval(_message.Message):
        __slots__ = ("allow", "reject")
        ALLOW_FIELD_NUMBER: _ClassVar[int]
        REJECT_FIELD_NUMBER: _ClassVar[int]
        allow: _containers.RepeatedScalarFieldContainer[str]
        reject: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, allow: _Optional[_Iterable[str]] = ..., reject: _Optional[_Iterable[str]] = ...) -> None: ...
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    model: str
    message: SendMessageInput.Message
    approval: SendMessageInput.Approval
    def __init__(self, chat_id: _Optional[str] = ..., model: _Optional[str] = ..., message: _Optional[_Union[SendMessageInput.Message, _Mapping]] = ..., approval: _Optional[_Union[SendMessageInput.Approval, _Mapping]] = ...) -> None: ...

class SendMessageOutput(_message.Message):
    __slots__ = ("chat", "message", "status")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[SendMessageOutput.Status]
        THINKING: _ClassVar[SendMessageOutput.Status]
        STREAMING: _ClassVar[SendMessageOutput.Status]
        CALLING: _ClassVar[SendMessageOutput.Status]
    UNKNOWN_STATUS: SendMessageOutput.Status
    THINKING: SendMessageOutput.Status
    STREAMING: SendMessageOutput.Status
    CALLING: SendMessageOutput.Status
    CHAT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    chat: _chat_pb2.Chat
    message: _chat_pb2.Message
    status: SendMessageOutput.Status
    def __init__(self, chat: _Optional[_Union[_chat_pb2.Chat, _Mapping]] = ..., message: _Optional[_Union[_chat_pb2.Message, _Mapping]] = ..., status: _Optional[_Union[SendMessageOutput.Status, str]] = ...) -> None: ...

class ListMessagesInput(_message.Message):
    __slots__ = ("chat_id", "offset", "size", "filters", "sort", "order")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListMessagesInput.Sortable]
        TIMESTAMP: _ClassVar[ListMessagesInput.Sortable]
    DEFAULT: ListMessagesInput.Sortable
    TIMESTAMP: ListMessagesInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    offset: int
    size: int
    filters: ListMessagesInput.Filter
    sort: ListMessagesInput.Sortable
    order: _direction_pb2.Direction
    def __init__(self, chat_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListMessagesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListMessagesInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListMessagesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_chat_pb2.Message]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_chat_pb2.Message, _Mapping]]] = ...) -> None: ...

class DescribeChatOptionsInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeChatOptionsOutput(_message.Message):
    __slots__ = ("models",)
    class Model(_message.Message):
        __slots__ = ("id", "name")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[DescribeChatOptionsOutput.Model]
    def __init__(self, models: _Optional[_Iterable[_Union[DescribeChatOptionsOutput.Model, _Mapping]]] = ...) -> None: ...
