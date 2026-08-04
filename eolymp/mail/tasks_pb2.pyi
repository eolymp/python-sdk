from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TranslateNewsletterTask(_message.Message):
    __slots__ = ("newsletter_id", "source_locale", "target_locales", "override_manual")
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOCALE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LOCALES_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_MANUAL_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    source_locale: str
    target_locales: _containers.RepeatedScalarFieldContainer[str]
    override_manual: bool
    def __init__(self, newsletter_id: _Optional[str] = ..., source_locale: _Optional[str] = ..., target_locales: _Optional[_Iterable[str]] = ..., override_manual: _Optional[bool] = ...) -> None: ...
