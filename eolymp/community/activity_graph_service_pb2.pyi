from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeActivityGraphInput(_message.Message):
    __slots__ = ["after", "before", "metric"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    after: _timestamp_pb2.Timestamp
    before: _timestamp_pb2.Timestamp
    metric: str
    def __init__(self, after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metric: _Optional[str] = ...) -> None: ...

class DescribeActivityGraphOutput(_message.Message):
    __slots__ = ["max_value", "values"]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    max_value: int
    values: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[int]] = ..., max_value: _Optional[int] = ...) -> None: ...
