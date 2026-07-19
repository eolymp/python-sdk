from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.automation import rule_pb2 as _rule_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListRulesInput(_message.Message):
    __slots__ = ("offset", "size", "search", "filters", "sort", "order")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListRulesInput.Sortable]
        NAME: _ClassVar[ListRulesInput.Sortable]
        CREATED_AT: _ClassVar[ListRulesInput.Sortable]
        TRIGGER_COUNT: _ClassVar[ListRulesInput.Sortable]
    DEFAULT: ListRulesInput.Sortable
    NAME: ListRulesInput.Sortable
    CREATED_AT: ListRulesInput.Sortable
    TRIGGER_COUNT: ListRulesInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "name", "trigger", "inactive")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        INACTIVE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        trigger: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        inactive: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., trigger: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., inactive: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    search: str
    filters: ListRulesInput.Filter
    sort: ListRulesInput.Sortable
    order: _direction_pb2.Direction
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListRulesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListRulesInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListRulesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_rule_pb2.Rule]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_rule_pb2.Rule, _Mapping]]] = ...) -> None: ...

class CreateRuleInput(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: _rule_pb2.Rule
    def __init__(self, rule: _Optional[_Union[_rule_pb2.Rule, _Mapping]] = ...) -> None: ...

class CreateRuleOutput(_message.Message):
    __slots__ = ("rule_id",)
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    def __init__(self, rule_id: _Optional[str] = ...) -> None: ...

class DescribeRuleInput(_message.Message):
    __slots__ = ("rule_id",)
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    def __init__(self, rule_id: _Optional[str] = ...) -> None: ...

class DescribeRuleOutput(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: _rule_pb2.Rule
    def __init__(self, rule: _Optional[_Union[_rule_pb2.Rule, _Mapping]] = ...) -> None: ...

class UpdateRuleInput(_message.Message):
    __slots__ = ("patch", "rule_id", "rule")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_rule_pb2.Rule.Patch.Field]
    rule_id: str
    rule: _rule_pb2.Rule
    def __init__(self, patch: _Optional[_Iterable[_Union[_rule_pb2.Rule.Patch.Field, str]]] = ..., rule_id: _Optional[str] = ..., rule: _Optional[_Union[_rule_pb2.Rule, _Mapping]] = ...) -> None: ...

class UpdateRuleOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRuleInput(_message.Message):
    __slots__ = ("rule_id",)
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    def __init__(self, rule_id: _Optional[str] = ...) -> None: ...

class DeleteRuleOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
