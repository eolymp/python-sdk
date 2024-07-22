from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignmentV2(_message.Message):
    __slots__ = ["all_modules", "complete_at", "due_at", "group_id", "id", "member_id", "modules", "start_at"]
    class Item(_message.Message):
        __slots__ = ["id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Module(_message.Message):
        __slots__ = ["all_items", "id", "items"]
        ALL_ITEMS_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        all_items: bool
        id: str
        items: _containers.RepeatedCompositeFieldContainer[AssignmentV2.Item]
        def __init__(self, id: _Optional[str] = ..., all_items: bool = ..., items: _Optional[_Iterable[_Union[AssignmentV2.Item, _Mapping]]] = ...) -> None: ...
    ALL_MODULES_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
    DUE_AT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MODULES_FIELD_NUMBER: _ClassVar[int]
    START_AT_FIELD_NUMBER: _ClassVar[int]
    all_modules: bool
    complete_at: _timestamp_pb2.Timestamp
    due_at: _timestamp_pb2.Timestamp
    group_id: str
    id: str
    member_id: str
    modules: _containers.RepeatedCompositeFieldContainer[AssignmentV2.Module]
    start_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., group_id: _Optional[str] = ..., all_modules: bool = ..., modules: _Optional[_Iterable[_Union[AssignmentV2.Module, _Mapping]]] = ..., due_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
