from eolymp.runtime import language_pb2 as _language_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Runtime(_message.Message):
    __slots__ = ["deprecated", "id", "lang", "name", "type", "version"]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    deprecated: bool
    id: str
    lang: str
    name: str
    type: _language_pb2.Language.Type
    version: str
    def __init__(self, id: _Optional[str] = ..., lang: _Optional[str] = ..., version: _Optional[str] = ..., type: _Optional[_Union[_language_pb2.Language.Type, str]] = ..., name: _Optional[str] = ..., deprecated: bool = ...) -> None: ...
