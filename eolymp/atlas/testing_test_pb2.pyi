from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Test(_message.Message):
    __slots__ = ["answer_object_id", "answer_url", "example", "id", "index", "input_object_id", "input_url", "score", "secret", "testset_id"]
    ANSWER_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    INPUT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    answer_object_id: str
    answer_url: str
    example: bool
    id: str
    index: int
    input_object_id: str
    input_url: str
    score: float
    secret: bool
    testset_id: str
    def __init__(self, id: _Optional[str] = ..., testset_id: _Optional[str] = ..., index: _Optional[int] = ..., example: bool = ..., secret: bool = ..., score: _Optional[float] = ..., input_object_id: _Optional[str] = ..., input_url: _Optional[str] = ..., answer_object_id: _Optional[str] = ..., answer_url: _Optional[str] = ...) -> None: ...
