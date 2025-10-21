from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import credit_pb2 as _credit_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeBalanceInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeBalanceOutput(_message.Message):
    __slots__ = ("balance",)
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    balance: int
    def __init__(self, balance: _Optional[int] = ...) -> None: ...

class GrantCreditInput(_message.Message):
    __slots__ = ("grant",)
    GRANT_FIELD_NUMBER: _ClassVar[int]
    grant: _credit_pb2.Credit.Grant
    def __init__(self, grant: _Optional[_Union[_credit_pb2.Credit.Grant, _Mapping]] = ...) -> None: ...

class GrantCreditOutput(_message.Message):
    __slots__ = ("grant_id", "transaction_id")
    GRANT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    grant_id: str
    transaction_id: str
    def __init__(self, grant_id: _Optional[str] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class CancelCreditInput(_message.Message):
    __slots__ = ("grant_id",)
    GRANT_ID_FIELD_NUMBER: _ClassVar[int]
    grant_id: str
    def __init__(self, grant_id: _Optional[str] = ...) -> None: ...

class CancelCreditOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCreditGrantsInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "reference", "note", "amount", "active")
        ID_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        NOTE_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        reference: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        note: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        amount: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        active: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., reference: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., note: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., amount: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., active: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListCreditGrantsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListCreditGrantsInput.Filter, _Mapping]] = ...) -> None: ...

class ListCreditGrantsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_credit_pb2.Credit.Grant]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_credit_pb2.Credit.Grant, _Mapping]]] = ...) -> None: ...

class RedeemCreditInput(_message.Message):
    __slots__ = ("amount", "reference", "note")
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    amount: int
    reference: str
    note: str
    def __init__(self, amount: _Optional[int] = ..., reference: _Optional[str] = ..., note: _Optional[str] = ...) -> None: ...

class RedeemCreditOutput(_message.Message):
    __slots__ = ("transaction_id",)
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    def __init__(self, transaction_id: _Optional[str] = ...) -> None: ...

class ListCreditTransactionsInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListCreditTransactionsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListCreditTransactionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListCreditTransactionsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_credit_pb2.Credit.Transaction]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_credit_pb2.Credit.Transaction, _Mapping]]] = ...) -> None: ...

class RefundCreditInput(_message.Message):
    __slots__ = ("transaction_id", "amount")
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    amount: int
    def __init__(self, transaction_id: _Optional[str] = ..., amount: _Optional[int] = ...) -> None: ...

class RefundCreditOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
