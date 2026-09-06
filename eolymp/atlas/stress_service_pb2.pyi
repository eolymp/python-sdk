from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import stress_pb2 as _stress_pb2
from eolymp.wellknown import watch_pb2 as _watch_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunStressInput(_message.Message):
    __slots__ = ("problem_id", "stress")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STRESS_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    stress: _stress_pb2.Stress
    def __init__(self, problem_id: _Optional[str] = ..., stress: _Optional[_Union[_stress_pb2.Stress, _Mapping]] = ...) -> None: ...

class RunStressOutput(_message.Message):
    __slots__ = ("stress_id", "stress")
    STRESS_ID_FIELD_NUMBER: _ClassVar[int]
    STRESS_FIELD_NUMBER: _ClassVar[int]
    stress_id: str
    stress: _stress_pb2.Stress
    def __init__(self, stress_id: _Optional[str] = ..., stress: _Optional[_Union[_stress_pb2.Stress, _Mapping]] = ...) -> None: ...

class DescribeStressInput(_message.Message):
    __slots__ = ("problem_id", "stress_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STRESS_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    stress_id: str
    def __init__(self, problem_id: _Optional[str] = ..., stress_id: _Optional[str] = ...) -> None: ...

class DescribeStressOutput(_message.Message):
    __slots__ = ("stress",)
    STRESS_FIELD_NUMBER: _ClassVar[int]
    stress: _stress_pb2.Stress
    def __init__(self, stress: _Optional[_Union[_stress_pb2.Stress, _Mapping]] = ...) -> None: ...

class WatchStressInput(_message.Message):
    __slots__ = ("problem_id", "stress_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STRESS_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    stress_id: str
    def __init__(self, problem_id: _Optional[str] = ..., stress_id: _Optional[str] = ...) -> None: ...

class WatchStressOutput(_message.Message):
    __slots__ = ("event", "stress")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    STRESS_FIELD_NUMBER: _ClassVar[int]
    event: _watch_pb2.WatchEventType
    stress: _stress_pb2.Stress
    def __init__(self, event: _Optional[_Union[_watch_pb2.WatchEventType, str]] = ..., stress: _Optional[_Union[_stress_pb2.Stress, _Mapping]] = ...) -> None: ...

class CancelStressInput(_message.Message):
    __slots__ = ("problem_id", "stress_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STRESS_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    stress_id: str
    def __init__(self, problem_id: _Optional[str] = ..., stress_id: _Optional[str] = ...) -> None: ...

class CancelStressOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
