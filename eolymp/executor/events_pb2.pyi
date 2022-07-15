from eolymp.executor import status_pb2 as _status_pb2
from eolymp.executor import status_v2_pb2 as _status_v2_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatusUpdatedEvent(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status
    def __init__(self, status: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class StatusV2UpdatedEvent(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _status_v2_pb2.StatusV2
    def __init__(self, status: _Optional[_Union[_status_v2_pb2.StatusV2, _Mapping]] = ...) -> None: ...
