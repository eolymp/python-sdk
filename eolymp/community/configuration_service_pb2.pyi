from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import configuration_identity_pb2 as _configuration_identity_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigureIdentityConfigInput(_message.Message):
    __slots__ = ["config"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _configuration_identity_pb2.IdentityConfig
    def __init__(self, config: _Optional[_Union[_configuration_identity_pb2.IdentityConfig, _Mapping]] = ...) -> None: ...

class ConfigureIdentityConfigOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeIdentityConfigInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeIdentityConfigOutput(_message.Message):
    __slots__ = ["config"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _configuration_identity_pb2.IdentityConfig
    def __init__(self, config: _Optional[_Union[_configuration_identity_pb2.IdentityConfig, _Mapping]] = ...) -> None: ...
