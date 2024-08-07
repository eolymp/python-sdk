from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import assignment_item_v2_pb2 as _assignment_item_v2_pb2
from eolymp.course import assignment_v2_pb2 as _assignment_v2_pb2
from eolymp.course import module_item_pb2 as _module_item_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAssignmentV2Input(_message.Message):
    __slots__ = ["complete_before", "duration", "module_id", "start_after"]
    COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    START_AFTER_FIELD_NUMBER: _ClassVar[int]
    complete_before: _timestamp_pb2.Timestamp
    duration: int
    module_id: str
    start_after: _timestamp_pb2.Timestamp
    def __init__(self, module_id: _Optional[str] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ...) -> None: ...

class CreateAssignmentV2Output(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteAssignmentV2Input(_message.Message):
    __slots__ = ["module_id"]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    module_id: str
    def __init__(self, module_id: _Optional[str] = ...) -> None: ...

class DeleteAssignmentV2Output(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeAssignmentItemV2Input(_message.Message):
    __slots__ = ["extra", "item_id", "module_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_module_item_pb2.ModuleItem.Extra]
    item_id: str
    module_id: str
    def __init__(self, module_id: _Optional[str] = ..., item_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_module_item_pb2.ModuleItem.Extra, str]]] = ...) -> None: ...

class DescribeAssignmentItemV2Output(_message.Message):
    __slots__ = ["item"]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _assignment_item_v2_pb2.AssignmentItemV2
    def __init__(self, item: _Optional[_Union[_assignment_item_v2_pb2.AssignmentItemV2, _Mapping]] = ...) -> None: ...

class ListAssignmentItemsV2Input(_message.Message):
    __slots__ = ["module_id"]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    module_id: str
    def __init__(self, module_id: _Optional[str] = ...) -> None: ...

class ListAssignmentItemsV2Output(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_assignment_item_v2_pb2.AssignmentItemV2]
    def __init__(self, items: _Optional[_Iterable[_Union[_assignment_item_v2_pb2.AssignmentItemV2, _Mapping]]] = ...) -> None: ...

class ListAssignmentsV2Input(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListAssignmentsV2Output(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_assignment_v2_pb2.AssignmentV2]
    def __init__(self, items: _Optional[_Iterable[_Union[_assignment_v2_pb2.AssignmentV2, _Mapping]]] = ...) -> None: ...

class StartAssignmentV2Input(_message.Message):
    __slots__ = ["module_id"]
    MODULE_ID_FIELD_NUMBER: _ClassVar[int]
    module_id: str
    def __init__(self, module_id: _Optional[str] = ...) -> None: ...

class StartAssignmentV2Output(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
