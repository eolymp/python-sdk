from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.proctoring import recording_pb2 as _recording_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRecordingInput(_message.Message):
    __slots__ = ("recording",)
    RECORDING_FIELD_NUMBER: _ClassVar[int]
    recording: _recording_pb2.Recording
    def __init__(self, recording: _Optional[_Union[_recording_pb2.Recording, _Mapping]] = ...) -> None: ...

class CreateRecordingOutput(_message.Message):
    __slots__ = ("recording_id",)
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    def __init__(self, recording_id: _Optional[str] = ...) -> None: ...

class UpdateRecordingInput(_message.Message):
    __slots__ = ("recording_id", "recording")
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDING_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    recording: _recording_pb2.Recording.Patch
    def __init__(self, recording_id: _Optional[str] = ..., recording: _Optional[_Union[_recording_pb2.Recording.Patch, _Mapping]] = ...) -> None: ...

class UpdateRecordingOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRecordingInput(_message.Message):
    __slots__ = ("recording_id",)
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    def __init__(self, recording_id: _Optional[str] = ...) -> None: ...

class DeleteRecordingOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeRecordingInput(_message.Message):
    __slots__ = ("recording_id",)
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    def __init__(self, recording_id: _Optional[str] = ...) -> None: ...

class DescribeRecordingOutput(_message.Message):
    __slots__ = ("recording",)
    RECORDING_FIELD_NUMBER: _ClassVar[int]
    recording: _recording_pb2.Recording
    def __init__(self, recording: _Optional[_Union[_recording_pb2.Recording, _Mapping]] = ...) -> None: ...

class ListRecordingsInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "member_id", "status")
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListRecordingsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListRecordingsInput.Filter, _Mapping]] = ...) -> None: ...

class ListRecordingsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_recording_pb2.Recording]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_recording_pb2.Recording, _Mapping]]] = ...) -> None: ...

class RecordingChangedEvent(_message.Message):
    __slots__ = ("before", "after")
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    before: _recording_pb2.Recording
    after: _recording_pb2.Recording
    def __init__(self, before: _Optional[_Union[_recording_pb2.Recording, _Mapping]] = ..., after: _Optional[_Union[_recording_pb2.Recording, _Mapping]] = ...) -> None: ...
