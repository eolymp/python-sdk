from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import configuration_pb2 as _configuration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeConfigInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeConfigOutput(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _configuration_pb2.Config
    def __init__(self, config: _Optional[_Union[_configuration_pb2.Config, _Mapping]] = ...) -> None: ...

class UpdateConfigInput(_message.Message):
    __slots__ = ("patch", "config")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_configuration_pb2.Config.Patch.Field]
    config: _configuration_pb2.Config
    def __init__(self, patch: _Optional[_Iterable[_Union[_configuration_pb2.Config.Patch.Field, str]]] = ..., config: _Optional[_Union[_configuration_pb2.Config, _Mapping]] = ...) -> None: ...

class UpdateConfigOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
