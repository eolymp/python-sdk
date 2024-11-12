from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import penalty_pb2 as _penalty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CancelPenaltyInput(_message.Message):
    __slots__ = ["penalty_id"]
    PENALTY_ID_FIELD_NUMBER: _ClassVar[int]
    penalty_id: str
    def __init__(self, penalty_id: _Optional[str] = ...) -> None: ...

class CancelPenaltyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreatePenaltyInput(_message.Message):
    __slots__ = ["dont_notify", "penalty"]
    DONT_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    PENALTY_FIELD_NUMBER: _ClassVar[int]
    dont_notify: bool
    penalty: _penalty_pb2.Penalty
    def __init__(self, penalty: _Optional[_Union[_penalty_pb2.Penalty, _Mapping]] = ..., dont_notify: bool = ...) -> None: ...

class CreatePenaltyOutput(_message.Message):
    __slots__ = ["penalty_id"]
    PENALTY_ID_FIELD_NUMBER: _ClassVar[int]
    penalty_id: str
    def __init__(self, penalty_id: _Optional[str] = ...) -> None: ...

class DescribePenaltyInput(_message.Message):
    __slots__ = ["penalty_id"]
    PENALTY_ID_FIELD_NUMBER: _ClassVar[int]
    penalty_id: str
    def __init__(self, penalty_id: _Optional[str] = ...) -> None: ...

class DescribePenaltyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListPenaltiesInput(_message.Message):
    __slots__ = ["offset", "size"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListPenaltiesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_penalty_pb2.Penalty]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_penalty_pb2.Penalty, _Mapping]]] = ...) -> None: ...
