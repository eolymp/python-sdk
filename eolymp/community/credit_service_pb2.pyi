from eolymp.annotations import http_pb2 as _http_pb2
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

class CreateCreditInput(_message.Message):
    __slots__ = ("credit",)
    CREDIT_FIELD_NUMBER: _ClassVar[int]
    credit: _credit_pb2.Credit
    def __init__(self, credit: _Optional[_Union[_credit_pb2.Credit, _Mapping]] = ...) -> None: ...

class CreateCreditOutput(_message.Message):
    __slots__ = ("credit_id",)
    CREDIT_ID_FIELD_NUMBER: _ClassVar[int]
    credit_id: str
    def __init__(self, credit_id: _Optional[str] = ...) -> None: ...

class DeleteCreditInput(_message.Message):
    __slots__ = ("credit_id",)
    CREDIT_ID_FIELD_NUMBER: _ClassVar[int]
    credit_id: str
    def __init__(self, credit_id: _Optional[str] = ...) -> None: ...

class DeleteCreditOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCreditsInput(_message.Message):
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
    filters: ListCreditsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListCreditsInput.Filter, _Mapping]] = ...) -> None: ...

class ListCreditsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_credit_pb2.Credit]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_credit_pb2.Credit, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeCreditBalanceInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeCreditBalanceOutput(_message.Message):
    __slots__ = ("balance",)
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    balance: int
    def __init__(self, balance: _Optional[int] = ...) -> None: ...
