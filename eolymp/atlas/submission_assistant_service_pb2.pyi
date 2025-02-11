from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.ecm import node_pb2 as _node_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DebugAssistanceMessage(_message.Message):
    __slots__ = ("id", "locale", "message", "rating")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    id: str
    locale: str
    message: _node_pb2.Node
    rating: int
    def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., message: _Optional[_Union[_node_pb2.Node, _Mapping]] = ..., rating: _Optional[int] = ...) -> None: ...

class RequestDebugAssistanceInput(_message.Message):
    __slots__ = ("submission_id", "locale")
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    locale: str
    def __init__(self, submission_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class RequestDebugAssistanceOutput(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: DebugAssistanceMessage
    def __init__(self, message: _Optional[_Union[DebugAssistanceMessage, _Mapping]] = ...) -> None: ...

class DescribeDebugAssistanceInput(_message.Message):
    __slots__ = ("submission_id",)
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    def __init__(self, submission_id: _Optional[str] = ...) -> None: ...

class DescribeDebugAssistanceOutput(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: DebugAssistanceMessage
    def __init__(self, message: _Optional[_Union[DebugAssistanceMessage, _Mapping]] = ...) -> None: ...

class RateDebugAssistanceInput(_message.Message):
    __slots__ = ("submission_id", "rating")
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    rating: int
    def __init__(self, submission_id: _Optional[str] = ..., rating: _Optional[int] = ...) -> None: ...

class RateDebugAssistanceOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
