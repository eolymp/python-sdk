from eolymp.annotations import resource_pb2 as _resource_pb2
from eolymp.atlas import attachment_pb2 as _attachment_pb2
from eolymp.atlas import permission_pb2 as _permission_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from eolymp.atlas import template_pb2 as _template_pb2
from eolymp.atlas import test_pb2 as _test_pb2
from eolymp.atlas import testset_pb2 as _testset_pb2
from eolymp.executor import interactor_pb2 as _interactor_pb2
from eolymp.executor import verifier_pb2 as _verifier_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Version(_message.Message):
    __slots__ = ["change_op", "change_path", "created_at", "created_by", "number"]
    CHANGE_OP_FIELD_NUMBER: _ClassVar[int]
    CHANGE_PATH_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    change_op: str
    change_path: str
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    number: int
    def __init__(self, number: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., change_op: _Optional[str] = ..., change_path: _Optional[str] = ...) -> None: ...
