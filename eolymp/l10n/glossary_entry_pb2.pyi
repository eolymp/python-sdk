from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GlossaryEntry(_message.Message):
    __slots__ = ("id", "term", "translation", "locale")
    class Patch(_message.Message):
        __slots__ = ("term", "translation", "locale")
        TERM_FIELD_NUMBER: _ClassVar[int]
        TRANSLATION_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        term: str
        translation: str
        locale: str
        def __init__(self, term: _Optional[str] = ..., translation: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    id: str
    term: str
    translation: str
    locale: str
    def __init__(self, id: _Optional[str] = ..., term: _Optional[str] = ..., translation: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...
