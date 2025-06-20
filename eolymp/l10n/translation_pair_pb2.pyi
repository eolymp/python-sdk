from eolymp.l10n import term_pb2 as _term_pb2
from eolymp.l10n import translation_pb2 as _translation_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TranslationPair(_message.Message):
    __slots__ = ("term", "source", "translation", "suggestion")
    TERM_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    term: _term_pb2.Term
    source: _translation_pb2.Translation
    translation: _translation_pb2.Translation
    suggestion: _translation_pb2.Translation
    def __init__(self, term: _Optional[_Union[_term_pb2.Term, _Mapping]] = ..., source: _Optional[_Union[_translation_pb2.Translation, _Mapping]] = ..., translation: _Optional[_Union[_translation_pb2.Translation, _Mapping]] = ..., suggestion: _Optional[_Union[_translation_pb2.Translation, _Mapping]] = ...) -> None: ...
