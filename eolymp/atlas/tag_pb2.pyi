from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tag(_message.Message):
    __slots__ = ["descriptions", "id", "visible"]
    class Description(_message.Message):
        __slots__ = ["locale", "name", "summary"]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        locale: str
        name: str
        summary: str
        def __init__(self, locale: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[str] = ...) -> None: ...
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    descriptions: _containers.RepeatedCompositeFieldContainer[Tag.Description]
    id: str
    visible: bool
    def __init__(self, id: _Optional[str] = ..., visible: bool = ..., descriptions: _Optional[_Iterable[_Union[Tag.Description, _Mapping]]] = ...) -> None: ...
