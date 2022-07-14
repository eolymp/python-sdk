from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Test(_message.Message):
    __slots__ = ["answer_object_id", "example", "id", "index", "input_object_id", "score", "testset_id"]
    ANSWER_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    INPUT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    answer_object_id: str
    example: bool
    id: str
    index: int
    input_object_id: str
    score: float
    testset_id: str
    def __init__(self, id: _Optional[str] = ..., testset_id: _Optional[str] = ..., index: _Optional[int] = ..., example: bool = ..., score: _Optional[float] = ..., input_object_id: _Optional[str] = ..., answer_object_id: _Optional[str] = ...) -> None: ...
