from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.auth import linked_account_pb2 as _linked_account_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestLinkedAccountInput(_message.Message):
    __slots__ = ("type", "callback_uri")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_URI_FIELD_NUMBER: _ClassVar[int]
    type: _linked_account_pb2.LinkedAccount.Type
    callback_uri: str
    def __init__(self, type: _Optional[_Union[_linked_account_pb2.LinkedAccount.Type, str]] = ..., callback_uri: _Optional[str] = ...) -> None: ...

class RequestLinkedAccountOutput(_message.Message):
    __slots__ = ("redirect_uri",)
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    redirect_uri: str
    def __init__(self, redirect_uri: _Optional[str] = ...) -> None: ...

class CreateLinkedAccountInput(_message.Message):
    __slots__ = ("code", "state")
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str
    def __init__(self, code: _Optional[str] = ..., state: _Optional[str] = ...) -> None: ...

class CreateLinkedAccountOutput(_message.Message):
    __slots__ = ("link_id",)
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    def __init__(self, link_id: _Optional[str] = ...) -> None: ...

class DeleteLinkedAccountInput(_message.Message):
    __slots__ = ("link_id",)
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    def __init__(self, link_id: _Optional[str] = ...) -> None: ...

class DeleteLinkedAccountOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeLinkedAccountInput(_message.Message):
    __slots__ = ("link_id",)
    LINK_ID_FIELD_NUMBER: _ClassVar[int]
    link_id: str
    def __init__(self, link_id: _Optional[str] = ...) -> None: ...

class DescribeLinkedAccountOutput(_message.Message):
    __slots__ = ("link",)
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: _linked_account_pb2.LinkedAccount
    def __init__(self, link: _Optional[_Union[_linked_account_pb2.LinkedAccount, _Mapping]] = ...) -> None: ...

class ListLinkedAccountsInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListLinkedAccountsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListLinkedAccountsInput.Filter, _Mapping]] = ...) -> None: ...

class ListLinkedAccountsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_linked_account_pb2.LinkedAccount]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_linked_account_pb2.LinkedAccount, _Mapping]]] = ...) -> None: ...
