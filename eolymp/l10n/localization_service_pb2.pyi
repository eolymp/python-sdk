from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.l10n import term_pb2 as _term_pb2
from eolymp.l10n import translation_pb2 as _translation_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApproveTermInput(_message.Message):
    __slots__ = ["term_id"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    def __init__(self, term_id: _Optional[str] = ...) -> None: ...

class ApproveTermOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ApproveTranslationInput(_message.Message):
    __slots__ = ["term_id", "translation_id"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    translation_id: str
    def __init__(self, term_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class ApproveTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateTermInput(_message.Message):
    __slots__ = ["term"]
    TERM_FIELD_NUMBER: _ClassVar[int]
    term: _term_pb2.Term
    def __init__(self, term: _Optional[_Union[_term_pb2.Term, _Mapping]] = ...) -> None: ...

class CreateTermOutput(_message.Message):
    __slots__ = ["term_id"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    def __init__(self, term_id: _Optional[str] = ...) -> None: ...

class DeleteTermInput(_message.Message):
    __slots__ = ["term_id"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    def __init__(self, term_id: _Optional[str] = ...) -> None: ...

class DeleteTermOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteTranslationInput(_message.Message):
    __slots__ = ["term_id", "translation_id"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    translation_id: str
    def __init__(self, term_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class DeleteTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeprecateTermInput(_message.Message):
    __slots__ = ["term_id"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    def __init__(self, term_id: _Optional[str] = ...) -> None: ...

class DeprecateTermOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeTermInput(_message.Message):
    __slots__ = ["term_id"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    def __init__(self, term_id: _Optional[str] = ...) -> None: ...

class DescribeTermOutput(_message.Message):
    __slots__ = ["term"]
    TERM_FIELD_NUMBER: _ClassVar[int]
    term: _term_pb2.Term
    def __init__(self, term: _Optional[_Union[_term_pb2.Term, _Mapping]] = ...) -> None: ...

class DescribeTranslationInput(_message.Message):
    __slots__ = ["term_id"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    def __init__(self, term_id: _Optional[str] = ...) -> None: ...

class DescribeTranslationOutput(_message.Message):
    __slots__ = ["term"]
    TERM_FIELD_NUMBER: _ClassVar[int]
    term: _term_pb2.Term
    def __init__(self, term: _Optional[_Union[_term_pb2.Term, _Mapping]] = ...) -> None: ...

class ExportTranslationsInput(_message.Message):
    __slots__ = ["locale"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    locale: str
    def __init__(self, locale: _Optional[str] = ...) -> None: ...

class ExportTranslationsOutput(_message.Message):
    __slots__ = ["translations"]
    class TranslationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TRANSLATIONS_FIELD_NUMBER: _ClassVar[int]
    translations: _containers.ScalarMap[str, str]
    def __init__(self, translations: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ImportTermsInput(_message.Message):
    __slots__ = ["set_deprecation", "set_outdated", "terms"]
    SET_DEPRECATION_FIELD_NUMBER: _ClassVar[int]
    SET_OUTDATED_FIELD_NUMBER: _ClassVar[int]
    TERMS_FIELD_NUMBER: _ClassVar[int]
    set_deprecation: bool
    set_outdated: bool
    terms: _containers.RepeatedCompositeFieldContainer[_term_pb2.Term]
    def __init__(self, terms: _Optional[_Iterable[_Union[_term_pb2.Term, _Mapping]]] = ..., set_deprecation: bool = ..., set_outdated: bool = ...) -> None: ...

class ImportTermsOutput(_message.Message):
    __slots__ = ["deprecated_count", "imported_count"]
    DEPRECATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    deprecated_count: int
    imported_count: int
    def __init__(self, imported_count: _Optional[int] = ..., deprecated_count: _Optional[int] = ...) -> None: ...

class ImportTranslationsInput(_message.Message):
    __slots__ = ["locale", "translations"]
    class TranslationsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TRANSLATIONS_FIELD_NUMBER: _ClassVar[int]
    locale: str
    translations: _containers.ScalarMap[str, str]
    def __init__(self, locale: _Optional[str] = ..., translations: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ImportTranslationsOutput(_message.Message):
    __slots__ = ["deprecated_count", "imported_count"]
    DEPRECATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    deprecated_count: int
    imported_count: int
    def __init__(self, imported_count: _Optional[int] = ..., deprecated_count: _Optional[int] = ...) -> None: ...

class ListTermsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["has_suggestions", "id", "message", "status"]
        HAS_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        has_suggestions: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        message: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., message: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., has_suggestions: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListTermsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTermsInput.Filter, _Mapping]] = ...) -> None: ...

class ListTermsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_term_pb2.Term]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_term_pb2.Term, _Mapping]]] = ...) -> None: ...

class ListTranslationsInput(_message.Message):
    __slots__ = ["filters", "offset", "size", "term_id"]
    class Filter(_message.Message):
        __slots__ = ["id", "locale", "message", "status"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        message: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., message: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    filters: ListTranslationsInput.Filter
    offset: int
    size: int
    term_id: str
    def __init__(self, term_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTranslationsInput.Filter, _Mapping]] = ...) -> None: ...

class ListTranslationsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_translation_pb2.Translation]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_translation_pb2.Translation, _Mapping]]] = ...) -> None: ...

class RejectTranslationInput(_message.Message):
    __slots__ = ["term_id", "translation_id"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    translation_id: str
    def __init__(self, term_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class RejectTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TranslateTermInput(_message.Message):
    __slots__ = ["term_id", "translation"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    translation: _translation_pb2.Translation
    def __init__(self, term_id: _Optional[str] = ..., translation: _Optional[_Union[_translation_pb2.Translation, _Mapping]] = ...) -> None: ...

class TranslateTermOutput(_message.Message):
    __slots__ = ["translation_id"]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    translation_id: str
    def __init__(self, translation_id: _Optional[str] = ...) -> None: ...

class UpdateTermInput(_message.Message):
    __slots__ = ["term", "term_id"]
    TERM_FIELD_NUMBER: _ClassVar[int]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    term: _term_pb2.Term
    term_id: str
    def __init__(self, term_id: _Optional[str] = ..., term: _Optional[_Union[_term_pb2.Term, _Mapping]] = ...) -> None: ...

class UpdateTermOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateTranslationInput(_message.Message):
    __slots__ = ["term_id", "translation", "translation_id"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    translation: _translation_pb2.Translation
    translation_id: str
    def __init__(self, term_id: _Optional[str] = ..., translation_id: _Optional[str] = ..., translation: _Optional[_Union[_translation_pb2.Translation, _Mapping]] = ...) -> None: ...

class UpdateTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
