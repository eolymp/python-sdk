from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
ENDPOINT_FIELD_NUMBER: _ClassVar[int]
endpoint: _descriptor.FieldDescriptor

class Endpoint(_message.Message):
    __slots__ = ["field", "service"]
    class Service(_message.Message):
        __slots__ = ["name"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    FIELD_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    field: str
    service: _containers.RepeatedCompositeFieldContainer[Endpoint.Service]
    def __init__(self, field: _Optional[str] = ..., service: _Optional[_Iterable[_Union[Endpoint.Service, _Mapping]]] = ...) -> None: ...
