from eolymp.discussion import message_pb2 as _message_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageChangedEvent(_message.Message):
    __slots__ = ["after", "before"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    after: _message_pb2.Message
    before: _message_pb2.Message
    def __init__(self, before: _Optional[_Union[_message_pb2.Message, _Mapping]] = ..., after: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...
