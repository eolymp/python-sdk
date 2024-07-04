from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import attribute_pb2 as _attribute_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeRegistrationInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DescribeRegistrationOutput(_message.Message):
    __slots__ = ["attributes", "values"]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute]
    values: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute.Value]
    def __init__(self, attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute, _Mapping]]] = ..., values: _Optional[_Iterable[_Union[_attribute_pb2.Attribute.Value, _Mapping]]] = ...) -> None: ...

class SubmitRegistrationInput(_message.Message):
    __slots__ = ["contest_id", "values"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    values: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute.Value]
    def __init__(self, contest_id: _Optional[str] = ..., values: _Optional[_Iterable[_Union[_attribute_pb2.Attribute.Value, _Mapping]]] = ...) -> None: ...

class SubmitRegistrationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
