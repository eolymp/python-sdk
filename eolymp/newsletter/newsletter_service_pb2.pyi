from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.newsletter import newsletter_pb2 as _newsletter_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateNewsletterInput(_message.Message):
    __slots__ = ["newsletter"]
    NEWSLETTER_FIELD_NUMBER: _ClassVar[int]
    newsletter: _newsletter_pb2.Newsletter
    def __init__(self, newsletter: _Optional[_Union[_newsletter_pb2.Newsletter, _Mapping]] = ...) -> None: ...

class CreateNewsletterOutput(_message.Message):
    __slots__ = ["newsletter_id"]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    def __init__(self, newsletter_id: _Optional[str] = ...) -> None: ...

class CreateNewsletterTranslationInput(_message.Message):
    __slots__ = ["newsletter_id", "translation"]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    translation: _newsletter_pb2.Newsletter.Translation
    def __init__(self, newsletter_id: _Optional[str] = ..., translation: _Optional[_Union[_newsletter_pb2.Newsletter.Translation, _Mapping]] = ...) -> None: ...

class CreateNewsletterTranslationOutput(_message.Message):
    __slots__ = ["translation_id"]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    translation_id: str
    def __init__(self, translation_id: _Optional[str] = ...) -> None: ...

class DeleteNewsletterInput(_message.Message):
    __slots__ = ["newsletter_id"]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    def __init__(self, newsletter_id: _Optional[str] = ...) -> None: ...

class DeleteNewsletterOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteNewsletterTranslationInput(_message.Message):
    __slots__ = ["newsletter_id", "translation_id"]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    translation_id: str
    def __init__(self, newsletter_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class DeleteNewsletterTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeNewsletterInput(_message.Message):
    __slots__ = ["newsletter_id"]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    def __init__(self, newsletter_id: _Optional[str] = ...) -> None: ...

class DescribeNewsletterOutput(_message.Message):
    __slots__ = ["newsletter"]
    NEWSLETTER_FIELD_NUMBER: _ClassVar[int]
    newsletter: _newsletter_pb2.Newsletter
    def __init__(self, newsletter: _Optional[_Union[_newsletter_pb2.Newsletter, _Mapping]] = ...) -> None: ...

class DescribeNewsletterTranslationInput(_message.Message):
    __slots__ = ["newsletter_id", "translation_id"]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    translation_id: str
    def __init__(self, newsletter_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class DescribeNewsletterTranslationOutput(_message.Message):
    __slots__ = ["translation"]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    translation: _newsletter_pb2.Newsletter.Translation
    def __init__(self, translation: _Optional[_Union[_newsletter_pb2.Newsletter.Translation, _Mapping]] = ...) -> None: ...

class ListNewsletterTranslationsInput(_message.Message):
    __slots__ = ["filters", "newsletter_id", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "locale", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListNewsletterTranslationsInput.Filter
    newsletter_id: str
    offset: int
    size: int
    def __init__(self, newsletter_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListNewsletterTranslationsInput.Filter, _Mapping]] = ...) -> None: ...

class ListNewsletterTranslationsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_newsletter_pb2.Newsletter.Translation]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_newsletter_pb2.Newsletter.Translation, _Mapping]]] = ...) -> None: ...

class ListNewslettersInput(_message.Message):
    __slots__ = ["offset", "size"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListNewslettersOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_newsletter_pb2.Newsletter]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_newsletter_pb2.Newsletter, _Mapping]]] = ...) -> None: ...

class SendNewsletterInput(_message.Message):
    __slots__ = ["newsletter_id"]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    def __init__(self, newsletter_id: _Optional[str] = ...) -> None: ...

class SendNewsletterOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TestNewsletterInput(_message.Message):
    __slots__ = ["email", "locale", "newsletter_id"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    locale: str
    newsletter_id: str
    def __init__(self, newsletter_id: _Optional[str] = ..., email: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class TestNewsletterOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateNewsletterInput(_message.Message):
    __slots__ = ["newsletter", "newsletter_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateNewsletterInput.Patch
    CONTENT: UpdateNewsletterInput.Patch
    NEWSLETTER_FIELD_NUMBER: _ClassVar[int]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SUBJECT: UpdateNewsletterInput.Patch
    TYPE: UpdateNewsletterInput.Patch
    newsletter: _newsletter_pb2.Newsletter
    newsletter_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateNewsletterInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateNewsletterInput.Patch, str]]] = ..., newsletter_id: _Optional[str] = ..., newsletter: _Optional[_Union[_newsletter_pb2.Newsletter, _Mapping]] = ...) -> None: ...

class UpdateNewsletterOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateNewsletterTranslationInput(_message.Message):
    __slots__ = ["newsletter_id", "patch", "translation", "translation_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateNewsletterTranslationInput.Patch
    CONTENT: UpdateNewsletterTranslationInput.Patch
    LOCALE: UpdateNewsletterTranslationInput.Patch
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SUBJECT: UpdateNewsletterTranslationInput.Patch
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateNewsletterTranslationInput.Patch]
    translation: _newsletter_pb2.Newsletter.Translation
    translation_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateNewsletterTranslationInput.Patch, str]]] = ..., newsletter_id: _Optional[str] = ..., translation_id: _Optional[str] = ..., translation: _Optional[_Union[_newsletter_pb2.Newsletter.Translation, _Mapping]] = ...) -> None: ...

class UpdateNewsletterTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
