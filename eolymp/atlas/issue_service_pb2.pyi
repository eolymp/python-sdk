from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import issue_pb2 as _issue_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListIssuesInput(_message.Message):
    __slots__ = ("offset", "size", "filters", "sort", "order", "extra")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListIssuesInput.Sortable]
        CREATED_AT: _ClassVar[ListIssuesInput.Sortable]
        UPDATED_AT: _ClassVar[ListIssuesInput.Sortable]
    DEFAULT: ListIssuesInput.Sortable
    CREATED_AT: ListIssuesInput.Sortable
    UPDATED_AT: ListIssuesInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "status", "user_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListIssuesInput.Filter
    sort: ListIssuesInput.Sortable
    order: _direction_pb2.Direction
    extra: _containers.RepeatedScalarFieldContainer[_issue_pb2.Issue.Extra.Field]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListIssuesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListIssuesInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_issue_pb2.Issue.Extra.Field, str]]] = ...) -> None: ...

class ListIssuesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_issue_pb2.Issue]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_issue_pb2.Issue, _Mapping]]] = ...) -> None: ...

class DescribeIssueInput(_message.Message):
    __slots__ = ("issue_id", "extra")
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    issue_id: str
    extra: _containers.RepeatedScalarFieldContainer[_issue_pb2.Issue.Extra.Field]
    def __init__(self, issue_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_issue_pb2.Issue.Extra.Field, str]]] = ...) -> None: ...

class DescribeIssueOutput(_message.Message):
    __slots__ = ("issue",)
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    issue: _issue_pb2.Issue
    def __init__(self, issue: _Optional[_Union[_issue_pb2.Issue, _Mapping]] = ...) -> None: ...

class CreateIssueInput(_message.Message):
    __slots__ = ("issue",)
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    issue: _issue_pb2.Issue
    def __init__(self, issue: _Optional[_Union[_issue_pb2.Issue, _Mapping]] = ...) -> None: ...

class CreateIssueOutput(_message.Message):
    __slots__ = ("issue_id",)
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    issue_id: str
    def __init__(self, issue_id: _Optional[str] = ...) -> None: ...

class UpdateIssueInput(_message.Message):
    __slots__ = ("patch", "issue_id", "issue")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_issue_pb2.Issue.Patch.Field]
    issue_id: str
    issue: _issue_pb2.Issue
    def __init__(self, patch: _Optional[_Iterable[_Union[_issue_pb2.Issue.Patch.Field, str]]] = ..., issue_id: _Optional[str] = ..., issue: _Optional[_Union[_issue_pb2.Issue, _Mapping]] = ...) -> None: ...

class UpdateIssueOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteIssueInput(_message.Message):
    __slots__ = ("issue_id",)
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    issue_id: str
    def __init__(self, issue_id: _Optional[str] = ...) -> None: ...

class DeleteIssueOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
