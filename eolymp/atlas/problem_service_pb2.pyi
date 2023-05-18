from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import library_service_pb2 as _library_service_pb2
from eolymp.atlas import version_pb2 as _version_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListVersionsInput(_message.Message):
    __slots__ = ["filters", "offset", "problem_id", "size"]
    class Filter(_message.Message):
        __slots__ = ["change_op", "change_path", "created_at", "created_by", "number"]
        CHANGE_OP_FIELD_NUMBER: _ClassVar[int]
        CHANGE_PATH_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        CREATED_BY_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        change_op: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        change_path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        created_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        created_by: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        number: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        def __init__(self, number: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., created_by: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., created_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., change_op: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., change_path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListVersionsInput.Filter
    offset: int
    problem_id: str
    size: int
    def __init__(self, problem_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListVersionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListVersionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_version_pb2.Version]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_version_pb2.Version, _Mapping]]] = ...) -> None: ...
