from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.l10n import term_pb2 as _term_pb2
from eolymp.l10n import translation_pb2 as _translation_pb2
from eolymp.l10n import translation_pair_pb2 as _translation_pair_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddLocaleInput(_message.Message):
    __slots__ = ["locale_code"]
    LOCALE_CODE_FIELD_NUMBER: _ClassVar[int]
    locale_code: str
    def __init__(self, locale_code: _Optional[str] = ...) -> None: ...

class AddLocaleOutput(_message.Message):
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
    __slots__ = ["terms"]
    TERMS_FIELD_NUMBER: _ClassVar[int]
    terms: _containers.RepeatedCompositeFieldContainer[_term_pb2.Term]
    def __init__(self, terms: _Optional[_Iterable[_Union[_term_pb2.Term, _Mapping]]] = ...) -> None: ...

class ImportTermsOutput(_message.Message):
    __slots__ = ["created_count", "deprecated_count", "updated_count"]
    CREATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    created_count: int
    deprecated_count: int
    updated_count: int
    def __init__(self, created_count: _Optional[int] = ..., updated_count: _Optional[int] = ..., deprecated_count: _Optional[int] = ...) -> None: ...

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
    __slots__ = ["created_count"]
    CREATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    created_count: int
    def __init__(self, created_count: _Optional[int] = ...) -> None: ...

class ListLocalesInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["code", "ready"]
        CODE_FIELD_NUMBER: _ClassVar[int]
        READY_FIELD_NUMBER: _ClassVar[int]
        code: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        ready: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, code: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., ready: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListLocalesInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListLocalesInput.Filter, _Mapping]] = ...) -> None: ...

class ListLocalesOutput(_message.Message):
    __slots__ = ["items", "total"]
    class Locale(_message.Message):
        __slots__ = ["code", "missing_terms", "ready", "total_terms", "translated_terms"]
        CODE_FIELD_NUMBER: _ClassVar[int]
        MISSING_TERMS_FIELD_NUMBER: _ClassVar[int]
        READY_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TERMS_FIELD_NUMBER: _ClassVar[int]
        TRANSLATED_TERMS_FIELD_NUMBER: _ClassVar[int]
        code: str
        missing_terms: int
        ready: bool
        total_terms: int
        translated_terms: int
        def __init__(self, code: _Optional[str] = ..., ready: bool = ..., translated_terms: _Optional[int] = ..., missing_terms: _Optional[int] = ..., total_terms: _Optional[int] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ListLocalesOutput.Locale]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[ListLocalesOutput.Locale, _Mapping]]] = ...) -> None: ...

class ListTermsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class ExpressionTranslation(_message.Message):
        __slots__ = ["locale", "status"]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        locale: str
        status: _expression_pb2.ExpressionEnum
        def __init__(self, locale: _Optional[str] = ..., status: _Optional[_Union[_expression_pb2.ExpressionEnum, _Mapping]] = ...) -> None: ...
    class Filter(_message.Message):
        __slots__ = ["id", "key", "message", "query", "status", "translation"]
        ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TRANSLATION_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        key: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        message: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        translation: _containers.RepeatedCompositeFieldContainer[ListTermsInput.ExpressionTranslation]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., key: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., message: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., translation: _Optional[_Iterable[_Union[ListTermsInput.ExpressionTranslation, _Mapping]]] = ...) -> None: ...
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

class ListTranslationPairsInput(_message.Message):
    __slots__ = ["after", "before", "filters", "locale", "offset", "size", "source"]
    class Filter(_message.Message):
        __slots__ = ["query", "source_message", "term_key", "term_status", "translation_message", "translation_status"]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        SOURCE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        TERM_KEY_FIELD_NUMBER: _ClassVar[int]
        TERM_STATUS_FIELD_NUMBER: _ClassVar[int]
        TRANSLATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        TRANSLATION_STATUS_FIELD_NUMBER: _ClassVar[int]
        query: str
        source_message: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        term_key: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        term_status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        translation_message: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        translation_status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, query: _Optional[str] = ..., term_key: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., term_status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., source_message: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., translation_status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., translation_message: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    after: str
    before: str
    filters: ListTranslationPairsInput.Filter
    locale: str
    offset: int
    size: int
    source: str
    def __init__(self, locale: _Optional[str] = ..., source: _Optional[str] = ..., size: _Optional[int] = ..., offset: _Optional[int] = ..., after: _Optional[str] = ..., before: _Optional[str] = ..., filters: _Optional[_Union[ListTranslationPairsInput.Filter, _Mapping]] = ...) -> None: ...

class ListTranslationPairsOutput(_message.Message):
    __slots__ = ["has_more", "items", "total"]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    has_more: bool
    items: _containers.RepeatedCompositeFieldContainer[_translation_pair_pb2.TranslationPair]
    total: int
    def __init__(self, total: _Optional[int] = ..., has_more: bool = ..., items: _Optional[_Iterable[_Union[_translation_pair_pb2.TranslationPair, _Mapping]]] = ...) -> None: ...

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

class RemoveLocaleInput(_message.Message):
    __slots__ = ["locale_code"]
    LOCALE_CODE_FIELD_NUMBER: _ClassVar[int]
    locale_code: str
    def __init__(self, locale_code: _Optional[str] = ...) -> None: ...

class RemoveLocaleOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RestoreTermInput(_message.Message):
    __slots__ = ["term_id"]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    term_id: str
    def __init__(self, term_id: _Optional[str] = ...) -> None: ...

class RestoreTermOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SuggestTranslationInput(_message.Message):
    __slots__ = ["locale", "term_id"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    locale: str
    term_id: str
    def __init__(self, term_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class SuggestTranslationOutput(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, messages: _Optional[_Iterable[str]] = ...) -> None: ...

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
