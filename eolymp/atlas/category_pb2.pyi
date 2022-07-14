from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Category(_message.Message):
    __slots__ = ["descriptions", "id", "image", "index", "parent_id", "visible"]
    class Description(_message.Message):
        __slots__ = ["locale", "summary", "title"]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        locale: str
        summary: str
        title: str
        def __init__(self, locale: _Optional[str] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ...) -> None: ...
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    descriptions: _containers.RepeatedCompositeFieldContainer[Category.Description]
    id: str
    image: str
    index: int
    parent_id: str
    visible: bool
    def __init__(self, id: _Optional[str] = ..., visible: bool = ..., index: _Optional[int] = ..., parent_id: _Optional[str] = ..., image: _Optional[str] = ..., descriptions: _Optional[_Iterable[_Union[Category.Description, _Mapping]]] = ...) -> None: ...
