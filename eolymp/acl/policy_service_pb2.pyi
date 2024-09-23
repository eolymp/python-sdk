from eolymp.acl import policy_pb2 as _policy_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CopyPoliciesInput(_message.Message):
    __slots__ = ["dst_principal", "dst_resource", "src_principal", "src_resource"]
    DST_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    DST_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SRC_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    SRC_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    dst_principal: str
    dst_resource: str
    src_principal: str
    src_resource: str
    def __init__(self, src_principal: _Optional[str] = ..., dst_principal: _Optional[str] = ..., src_resource: _Optional[str] = ..., dst_resource: _Optional[str] = ...) -> None: ...

class CopyPoliciesOutput(_message.Message):
    __slots__ = ["copies_count"]
    COPIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    copies_count: int
    def __init__(self, copies_count: _Optional[int] = ...) -> None: ...

class CreatePolicyInput(_message.Message):
    __slots__ = ["policy"]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: _policy_pb2.Policy
    def __init__(self, policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...

class CreatePolicyOutput(_message.Message):
    __slots__ = ["policy_id"]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    policy_id: str
    def __init__(self, policy_id: _Optional[str] = ...) -> None: ...

class DeletePolicyInput(_message.Message):
    __slots__ = ["policy_id"]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    policy_id: str
    def __init__(self, policy_id: _Optional[str] = ...) -> None: ...

class DeletePolicyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribePolicyInput(_message.Message):
    __slots__ = ["policy_id"]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    policy_id: str
    def __init__(self, policy_id: _Optional[str] = ...) -> None: ...

class DescribePolicyOutput(_message.Message):
    __slots__ = ["policy"]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: _policy_pb2.Policy
    def __init__(self, policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...

class ListPoliciesInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "name", "principal", "query", "resource"]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        principal: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        query: str
        resource: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., principal: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., resource: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListPoliciesInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListPoliciesInput.Filter, _Mapping]] = ...) -> None: ...

class ListPoliciesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_policy_pb2.Policy]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_policy_pb2.Policy, _Mapping]]] = ...) -> None: ...

class UpdatePolicyInput(_message.Message):
    __slots__ = ["patch", "policy", "policy_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdatePolicyInput.Patch
    ALLOWS: UpdatePolicyInput.Patch
    NAME: UpdatePolicyInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdatePolicyInput.Patch]
    policy: _policy_pb2.Policy
    policy_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdatePolicyInput.Patch, str]]] = ..., policy_id: _Optional[str] = ..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...

class UpdatePolicyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
