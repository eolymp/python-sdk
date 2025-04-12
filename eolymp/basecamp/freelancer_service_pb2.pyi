from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeFreelancerStatusInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeFreelancerStatusOutput(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[DescribeFreelancerStatusOutput.Status]
        UNSIGNED: _ClassVar[DescribeFreelancerStatusOutput.Status]
        PENDING: _ClassVar[DescribeFreelancerStatusOutput.Status]
        COMPLETE: _ClassVar[DescribeFreelancerStatusOutput.Status]
    UNKNOWN_STATUS: DescribeFreelancerStatusOutput.Status
    UNSIGNED: DescribeFreelancerStatusOutput.Status
    PENDING: DescribeFreelancerStatusOutput.Status
    COMPLETE: DescribeFreelancerStatusOutput.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: DescribeFreelancerStatusOutput.Status
    def __init__(self, status: _Optional[_Union[DescribeFreelancerStatusOutput.Status, str]] = ...) -> None: ...

class UpdateFreelancerStatusInput(_message.Message):
    __slots__ = ("first_name", "last_name", "address")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    address: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...

class UpdateFreelancerStatusOutput(_message.Message):
    __slots__ = ("sign_url",)
    SIGN_URL_FIELD_NUMBER: _ClassVar[int]
    sign_url: str
    def __init__(self, sign_url: _Optional[str] = ...) -> None: ...
