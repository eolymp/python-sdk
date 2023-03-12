from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Blob(_message.Message):
    __slots__ = ["data", "ern", "hash", "key", "size"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERN_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    ern: str
    hash: str
    key: str
    size: int
    def __init__(self, ern: _Optional[str] = ..., key: _Optional[str] = ..., hash: _Optional[str] = ..., size: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
