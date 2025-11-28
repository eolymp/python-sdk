from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.mail import newsletter_pb2 as _newsletter_pb2
from eolymp.mail import newsletter_recipient_pb2 as _newsletter_recipient_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateNewsletterInput(_message.Message):
    __slots__ = ("newsletter",)
    NEWSLETTER_FIELD_NUMBER: _ClassVar[int]
    newsletter: _newsletter_pb2.Newsletter
    def __init__(self, newsletter: _Optional[_Union[_newsletter_pb2.Newsletter, _Mapping]] = ...) -> None: ...

class CreateNewsletterOutput(_message.Message):
    __slots__ = ("newsletter_id",)
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    def __init__(self, newsletter_id: _Optional[str] = ...) -> None: ...

class UpdateNewsletterInput(_message.Message):
    __slots__ = ("patch", "newsletter_id", "newsletter")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    NEWSLETTER_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_newsletter_pb2.Newsletter.Patch.Field]
    newsletter_id: str
    newsletter: _newsletter_pb2.Newsletter
    def __init__(self, patch: _Optional[_Iterable[_Union[_newsletter_pb2.Newsletter.Patch.Field, str]]] = ..., newsletter_id: _Optional[str] = ..., newsletter: _Optional[_Union[_newsletter_pb2.Newsletter, _Mapping]] = ...) -> None: ...

class UpdateNewsletterOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteNewsletterInput(_message.Message):
    __slots__ = ("newsletter_id",)
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    def __init__(self, newsletter_id: _Optional[str] = ...) -> None: ...

class DeleteNewsletterOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeNewsletterInput(_message.Message):
    __slots__ = ("newsletter_id", "extra")
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    extra: _containers.RepeatedScalarFieldContainer[_newsletter_pb2.Newsletter.Extra.Field]
    def __init__(self, newsletter_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_newsletter_pb2.Newsletter.Extra.Field, str]]] = ...) -> None: ...

class DescribeNewsletterOutput(_message.Message):
    __slots__ = ("newsletter",)
    NEWSLETTER_FIELD_NUMBER: _ClassVar[int]
    newsletter: _newsletter_pb2.Newsletter
    def __init__(self, newsletter: _Optional[_Union[_newsletter_pb2.Newsletter, _Mapping]] = ...) -> None: ...

class ListNewslettersInput(_message.Message):
    __slots__ = ("offset", "size", "filters", "search", "sort", "order", "locale", "extra")
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CREATED_AT: _ClassVar[ListNewslettersInput.Sort]
    CREATED_AT: ListNewslettersInput.Sort
    class Filter(_message.Message):
        __slots__ = ("id", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListNewslettersInput.Filter
    search: str
    sort: ListNewslettersInput.Sort
    order: _direction_pb2.Direction
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_newsletter_pb2.Newsletter.Extra.Field]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListNewslettersInput.Filter, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[ListNewslettersInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_newsletter_pb2.Newsletter.Extra.Field, str]]] = ...) -> None: ...

class ListNewslettersOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_newsletter_pb2.Newsletter]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_newsletter_pb2.Newsletter, _Mapping]]] = ...) -> None: ...

class TestNewsletterInput(_message.Message):
    __slots__ = ("newsletter_id", "email", "locale", "member_id", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    email: str
    locale: str
    member_id: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, newsletter_id: _Optional[str] = ..., email: _Optional[str] = ..., locale: _Optional[str] = ..., member_id: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TestNewsletterOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendNewsletterInput(_message.Message):
    __slots__ = ("newsletter_id", "recipient_id")
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    recipient_id: str
    def __init__(self, newsletter_id: _Optional[str] = ..., recipient_id: _Optional[str] = ...) -> None: ...

class SendNewsletterOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TranslateNewsletterInput(_message.Message):
    __slots__ = ("newsletter_id", "source", "target", "target_automatic", "override_manual")
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_MANUAL_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    source: str
    target: _containers.RepeatedScalarFieldContainer[str]
    target_automatic: bool
    override_manual: bool
    def __init__(self, newsletter_id: _Optional[str] = ..., source: _Optional[str] = ..., target: _Optional[_Iterable[str]] = ..., target_automatic: bool = ..., override_manual: bool = ...) -> None: ...

class TranslateNewsletterOutput(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class CreateTranslationInput(_message.Message):
    __slots__ = ("newsletter_id", "translation")
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    translation: _newsletter_pb2.Newsletter.Translation
    def __init__(self, newsletter_id: _Optional[str] = ..., translation: _Optional[_Union[_newsletter_pb2.Newsletter.Translation, _Mapping]] = ...) -> None: ...

class CreateTranslationOutput(_message.Message):
    __slots__ = ("translation_id",)
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    translation_id: str
    def __init__(self, translation_id: _Optional[str] = ...) -> None: ...

class UpdateTranslationInput(_message.Message):
    __slots__ = ("patch", "newsletter_id", "translation_id", "translation")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_newsletter_pb2.Newsletter.Patch.Field]
    newsletter_id: str
    translation_id: str
    translation: _newsletter_pb2.Newsletter.Translation
    def __init__(self, patch: _Optional[_Iterable[_Union[_newsletter_pb2.Newsletter.Patch.Field, str]]] = ..., newsletter_id: _Optional[str] = ..., translation_id: _Optional[str] = ..., translation: _Optional[_Union[_newsletter_pb2.Newsletter.Translation, _Mapping]] = ...) -> None: ...

class UpdateTranslationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTranslationInput(_message.Message):
    __slots__ = ("newsletter_id", "translation_id")
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    translation_id: str
    def __init__(self, newsletter_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class DeleteTranslationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeTranslationInput(_message.Message):
    __slots__ = ("newsletter_id", "translation_id")
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    translation_id: str
    def __init__(self, newsletter_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class DescribeTranslationOutput(_message.Message):
    __slots__ = ("translation",)
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    translation: _newsletter_pb2.Newsletter.Translation
    def __init__(self, translation: _Optional[_Union[_newsletter_pb2.Newsletter.Translation, _Mapping]] = ...) -> None: ...

class ListTranslationsInput(_message.Message):
    __slots__ = ("newsletter_id", "offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "locale")
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    offset: int
    size: int
    filters: ListTranslationsInput.Filter
    def __init__(self, newsletter_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTranslationsInput.Filter, _Mapping]] = ...) -> None: ...

class ListTranslationsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_newsletter_pb2.Newsletter.Translation]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_newsletter_pb2.Newsletter.Translation, _Mapping]]] = ...) -> None: ...

class CreateRecipientInput(_message.Message):
    __slots__ = ("newsletter_id", "member_id", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    member_id: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, newsletter_id: _Optional[str] = ..., member_id: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateRecipientOutput(_message.Message):
    __slots__ = ("recipient_id",)
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    recipient_id: str
    def __init__(self, recipient_id: _Optional[str] = ...) -> None: ...

class ImportRecipientInput(_message.Message):
    __slots__ = ("newsletter_id", "all_members", "group_id", "contest_id", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    ALL_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    all_members: bool
    group_id: str
    contest_id: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, newsletter_id: _Optional[str] = ..., all_members: bool = ..., group_id: _Optional[str] = ..., contest_id: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ImportRecipientOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRecipientInput(_message.Message):
    __slots__ = ("newsletter_id", "recipient_id")
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    recipient_id: str
    def __init__(self, newsletter_id: _Optional[str] = ..., recipient_id: _Optional[str] = ...) -> None: ...

class DeleteRecipientOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRecipientsInput(_message.Message):
    __slots__ = ("newsletter_id", "offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "status", "member_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    offset: int
    size: int
    filters: ListRecipientsInput.Filter
    def __init__(self, newsletter_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListRecipientsInput.Filter, _Mapping]] = ...) -> None: ...

class ListRecipientsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_newsletter_recipient_pb2.Recipient]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_newsletter_recipient_pb2.Recipient, _Mapping]]] = ...) -> None: ...

class DescribeRecipientInput(_message.Message):
    __slots__ = ("newsletter_id", "recipient_id")
    NEWSLETTER_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    newsletter_id: str
    recipient_id: str
    def __init__(self, newsletter_id: _Optional[str] = ..., recipient_id: _Optional[str] = ...) -> None: ...

class DescribeRecipientOutput(_message.Message):
    __slots__ = ("recipient",)
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    recipient: _newsletter_recipient_pb2.Recipient
    def __init__(self, recipient: _Optional[_Union[_newsletter_recipient_pb2.Recipient, _Mapping]] = ...) -> None: ...
