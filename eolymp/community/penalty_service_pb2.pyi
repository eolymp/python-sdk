from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import penalty_pb2 as _penalty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class DeletePenaltyInput(_message.Message):
    __slots__ = ["penalty_id"]
    PENALTY_ID_FIELD_NUMBER: _ClassVar[int]
    penalty_id: str
    def __init__(self, penalty_id: _Optional[str] = ...) -> None: ...

class DeletePenaltyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribePenaltyInput(_message.Message):
    __slots__ = ["extra", "penalty_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    PENALTY_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_penalty_pb2.Penalty.Extra]
    penalty_id: str
    def __init__(self, penalty_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_penalty_pb2.Penalty.Extra, str]]] = ...) -> None: ...

class DescribePenaltyOutput(_message.Message):
    __slots__ = ["penalty"]
    PENALTY_FIELD_NUMBER: _ClassVar[int]
    penalty: _penalty_pb2.Penalty
    def __init__(self, penalty: _Optional[_Union[_penalty_pb2.Penalty, _Mapping]] = ...) -> None: ...

class ListPenaltiesInput(_message.Message):
    __slots__ = ["extra", "offset", "size"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_penalty_pb2.Penalty.Extra]
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., extra: _Optional[_Iterable[_Union[_penalty_pb2.Penalty.Extra, str]]] = ...) -> None: ...

class ListPenaltiesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_penalty_pb2.Penalty]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_penalty_pb2.Penalty, _Mapping]]] = ...) -> None: ...

class UpdatePenaltyInput(_message.Message):
    __slots__ = ["patch", "penalty", "penalty_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdatePenaltyInput.Patch
    DESCRIPTION: UpdatePenaltyInput.Patch
    EXPIRES_AT: UpdatePenaltyInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PENALTY_FIELD_NUMBER: _ClassVar[int]
    PENALTY_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE: UpdatePenaltyInput.Patch
    SUMMARY: UpdatePenaltyInput.Patch
    patch: _containers.RepeatedScalarFieldContainer[UpdatePenaltyInput.Patch]
    penalty: _penalty_pb2.Penalty
    penalty_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdatePenaltyInput.Patch, str]]] = ..., penalty_id: _Optional[str] = ..., penalty: _Optional[_Union[_penalty_pb2.Penalty, _Mapping]] = ...) -> None: ...

class UpdatePenaltyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
