from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.guardian import policy_pb2 as _policy_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DefinePolicyInput(_message.Message):
    __slots__ = ["id", "policy"]
    ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    id: str
    policy: _policy_pb2.Policy
    def __init__(self, id: _Optional[str] = ..., policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...

class DefinePolicyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribePolicyInput(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DescribePolicyOutput(_message.Message):
    __slots__ = ["policy"]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    policy: _policy_pb2.Policy
    def __init__(self, policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...

class EvaluateInput(_message.Message):
    __slots__ = ["args", "resource"]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    args: _containers.RepeatedScalarFieldContainer[str]
    resource: str
    def __init__(self, resource: _Optional[str] = ..., args: _Optional[_Iterable[str]] = ...) -> None: ...

class EvaluateOutput(_message.Message):
    __slots__ = ["actions"]
    class ActionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _policy_pb2.Statement.Effect
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_policy_pb2.Statement.Effect, str]] = ...) -> None: ...
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.ScalarMap[str, _policy_pb2.Statement.Effect]
    def __init__(self, actions: _Optional[_Mapping[str, _policy_pb2.Statement.Effect]] = ...) -> None: ...

class ListPoliciesInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListPoliciesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_policy_pb2.Policy]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_policy_pb2.Policy, _Mapping]]] = ...) -> None: ...

class RemovePolicyInput(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RemovePolicyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
