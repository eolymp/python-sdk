from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PostType(_message.Message):
    __slots__ = ["hidden", "id", "name", "order"]
    class Variant(_message.Message):
        __slots__ = ["id", "locale", "name"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: str
        locale: str
        name: str
        def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    hidden: bool
    id: str
    name: str
    order: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., hidden: bool = ..., order: _Optional[int] = ...) -> None: ...
