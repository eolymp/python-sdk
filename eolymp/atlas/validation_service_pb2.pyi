from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import testing_validator_pb2 as _testing_validator_pb2
from eolymp.atlas import validation_pb2 as _validation_pb2
from eolymp.wellknown import watch_pb2 as _watch_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunValidationInput(_message.Message):
    __slots__ = ("problem_id", "validator")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    validator: _testing_validator_pb2.Validator
    def __init__(self, problem_id: _Optional[str] = ..., validator: _Optional[_Union[_testing_validator_pb2.Validator, _Mapping]] = ...) -> None: ...

class RunValidationOutput(_message.Message):
    __slots__ = ("validation_id", "validation")
    VALIDATION_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    validation_id: str
    validation: _validation_pb2.Validation
    def __init__(self, validation_id: _Optional[str] = ..., validation: _Optional[_Union[_validation_pb2.Validation, _Mapping]] = ...) -> None: ...

class DescribeValidationInput(_message.Message):
    __slots__ = ("problem_id", "validation_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    validation_id: str
    def __init__(self, problem_id: _Optional[str] = ..., validation_id: _Optional[str] = ...) -> None: ...

class DescribeValidationOutput(_message.Message):
    __slots__ = ("validation",)
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    validation: _validation_pb2.Validation
    def __init__(self, validation: _Optional[_Union[_validation_pb2.Validation, _Mapping]] = ...) -> None: ...

class WatchValidationInput(_message.Message):
    __slots__ = ("problem_id", "validation_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    validation_id: str
    def __init__(self, problem_id: _Optional[str] = ..., validation_id: _Optional[str] = ...) -> None: ...

class WatchValidationOutput(_message.Message):
    __slots__ = ("validation", "event")
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    validation: _validation_pb2.Validation
    event: _watch_pb2.WatchEventType
    def __init__(self, validation: _Optional[_Union[_validation_pb2.Validation, _Mapping]] = ..., event: _Optional[_Union[_watch_pb2.WatchEventType, str]] = ...) -> None: ...
