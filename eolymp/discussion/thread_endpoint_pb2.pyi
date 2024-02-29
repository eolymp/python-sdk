from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.discussion import thread_pb2 as _thread_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeThreadInput(_message.Message):
    __slots__ = ["locale"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    locale: str
    def __init__(self, locale: _Optional[str] = ...) -> None: ...

class DescribeThreadOutput(_message.Message):
    __slots__ = ["thread"]
    THREAD_FIELD_NUMBER: _ClassVar[int]
    thread: _thread_pb2.Thread
    def __init__(self, thread: _Optional[_Union[_thread_pb2.Thread, _Mapping]] = ...) -> None: ...

class VoteThreadInput(_message.Message):
    __slots__ = ["message_id", "vote"]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    vote: int
    def __init__(self, message_id: _Optional[str] = ..., vote: _Optional[int] = ...) -> None: ...

class VoteThreadOutput(_message.Message):
    __slots__ = ["vote_count"]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    vote_count: int
    def __init__(self, vote_count: _Optional[int] = ...) -> None: ...
