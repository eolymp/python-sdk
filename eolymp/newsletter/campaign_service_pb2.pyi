from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.newsletter import campaign_pb2 as _campaign_pb2
from eolymp.newsletter import recipient_pb2 as _recipient_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCampaignInput(_message.Message):
    __slots__ = ("campaign",)
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign: _campaign_pb2.Campaign
    def __init__(self, campaign: _Optional[_Union[_campaign_pb2.Campaign, _Mapping]] = ...) -> None: ...

class CreateCampaignOutput(_message.Message):
    __slots__ = ("campaign_id",)
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    def __init__(self, campaign_id: _Optional[str] = ...) -> None: ...

class UpdateCampaignInput(_message.Message):
    __slots__ = ("patch", "campaign_id", "campaign")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_campaign_pb2.Campaign.Patch]
    campaign_id: str
    campaign: _campaign_pb2.Campaign
    def __init__(self, patch: _Optional[_Iterable[_Union[_campaign_pb2.Campaign.Patch, str]]] = ..., campaign_id: _Optional[str] = ..., campaign: _Optional[_Union[_campaign_pb2.Campaign, _Mapping]] = ...) -> None: ...

class UpdateCampaignOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCampaignInput(_message.Message):
    __slots__ = ("campaign_id",)
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    def __init__(self, campaign_id: _Optional[str] = ...) -> None: ...

class DeleteCampaignOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeCampaignInput(_message.Message):
    __slots__ = ("campaign_id", "extra")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    extra: _containers.RepeatedScalarFieldContainer[_campaign_pb2.Campaign.Extra]
    def __init__(self, campaign_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_campaign_pb2.Campaign.Extra, str]]] = ...) -> None: ...

class DescribeCampaignOutput(_message.Message):
    __slots__ = ("campaign",)
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    campaign: _campaign_pb2.Campaign
    def __init__(self, campaign: _Optional[_Union[_campaign_pb2.Campaign, _Mapping]] = ...) -> None: ...

class ListCampaignsInput(_message.Message):
    __slots__ = ("offset", "size", "filters", "search", "sort", "order", "locale", "extra")
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CREATED_AT: _ClassVar[ListCampaignsInput.Sort]
    CREATED_AT: ListCampaignsInput.Sort
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
    filters: ListCampaignsInput.Filter
    search: str
    sort: ListCampaignsInput.Sort
    order: _direction_pb2.Direction
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_campaign_pb2.Campaign.Extra]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListCampaignsInput.Filter, _Mapping]] = ..., search: _Optional[str] = ..., sort: _Optional[_Union[ListCampaignsInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_campaign_pb2.Campaign.Extra, str]]] = ...) -> None: ...

class ListCampaignsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_campaign_pb2.Campaign]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_campaign_pb2.Campaign, _Mapping]]] = ...) -> None: ...

class TestCampaignInput(_message.Message):
    __slots__ = ("campaign_id", "email", "locale", "member_id", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    email: str
    locale: str
    member_id: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, campaign_id: _Optional[str] = ..., email: _Optional[str] = ..., locale: _Optional[str] = ..., member_id: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TestCampaignOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendCampaignInput(_message.Message):
    __slots__ = ("campaign_id", "recipient_id")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    recipient_id: str
    def __init__(self, campaign_id: _Optional[str] = ..., recipient_id: _Optional[str] = ...) -> None: ...

class SendCampaignOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TranslateCampaignInput(_message.Message):
    __slots__ = ("campaign_id", "source", "target", "target_automatic", "override_manual")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_MANUAL_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    source: str
    target: _containers.RepeatedScalarFieldContainer[str]
    target_automatic: bool
    override_manual: bool
    def __init__(self, campaign_id: _Optional[str] = ..., source: _Optional[str] = ..., target: _Optional[_Iterable[str]] = ..., target_automatic: bool = ..., override_manual: bool = ...) -> None: ...

class TranslateCampaignOutput(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class CreateTranslationInput(_message.Message):
    __slots__ = ("campaign_id", "translation")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    translation: _campaign_pb2.Campaign.Translation
    def __init__(self, campaign_id: _Optional[str] = ..., translation: _Optional[_Union[_campaign_pb2.Campaign.Translation, _Mapping]] = ...) -> None: ...

class CreateTranslationOutput(_message.Message):
    __slots__ = ("translation_id",)
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    translation_id: str
    def __init__(self, translation_id: _Optional[str] = ...) -> None: ...

class UpdateTranslationInput(_message.Message):
    __slots__ = ("patch", "campaign_id", "translation_id", "translation")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_campaign_pb2.Campaign.Patch]
    campaign_id: str
    translation_id: str
    translation: _campaign_pb2.Campaign.Translation
    def __init__(self, patch: _Optional[_Iterable[_Union[_campaign_pb2.Campaign.Patch, str]]] = ..., campaign_id: _Optional[str] = ..., translation_id: _Optional[str] = ..., translation: _Optional[_Union[_campaign_pb2.Campaign.Translation, _Mapping]] = ...) -> None: ...

class UpdateTranslationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTranslationInput(_message.Message):
    __slots__ = ("campaign_id", "translation_id")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    translation_id: str
    def __init__(self, campaign_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class DeleteTranslationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeTranslationInput(_message.Message):
    __slots__ = ("campaign_id", "translation_id")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    translation_id: str
    def __init__(self, campaign_id: _Optional[str] = ..., translation_id: _Optional[str] = ...) -> None: ...

class DescribeTranslationOutput(_message.Message):
    __slots__ = ("translation",)
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    translation: _campaign_pb2.Campaign.Translation
    def __init__(self, translation: _Optional[_Union[_campaign_pb2.Campaign.Translation, _Mapping]] = ...) -> None: ...

class ListTranslationsInput(_message.Message):
    __slots__ = ("campaign_id", "offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "locale")
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    offset: int
    size: int
    filters: ListTranslationsInput.Filter
    def __init__(self, campaign_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTranslationsInput.Filter, _Mapping]] = ...) -> None: ...

class ListTranslationsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_campaign_pb2.Campaign.Translation]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_campaign_pb2.Campaign.Translation, _Mapping]]] = ...) -> None: ...

class CreateRecipientInput(_message.Message):
    __slots__ = ("campaign_id", "member_id", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    member_id: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, campaign_id: _Optional[str] = ..., member_id: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateRecipientOutput(_message.Message):
    __slots__ = ("recipient_id",)
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    recipient_id: str
    def __init__(self, recipient_id: _Optional[str] = ...) -> None: ...

class ImportRecipientInput(_message.Message):
    __slots__ = ("campaign_id", "all_members", "group_id", "contest_id", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    ALL_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    all_members: bool
    group_id: str
    contest_id: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, campaign_id: _Optional[str] = ..., all_members: bool = ..., group_id: _Optional[str] = ..., contest_id: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ImportRecipientOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteRecipientInput(_message.Message):
    __slots__ = ("campaign_id", "recipient_id")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    recipient_id: str
    def __init__(self, campaign_id: _Optional[str] = ..., recipient_id: _Optional[str] = ...) -> None: ...

class DeleteRecipientOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRecipientsInput(_message.Message):
    __slots__ = ("campaign_id", "offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "status", "member_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    offset: int
    size: int
    filters: ListRecipientsInput.Filter
    def __init__(self, campaign_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListRecipientsInput.Filter, _Mapping]] = ...) -> None: ...

class ListRecipientsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_recipient_pb2.Recipient]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_recipient_pb2.Recipient, _Mapping]]] = ...) -> None: ...

class DescribeRecipientInput(_message.Message):
    __slots__ = ("campaign_id", "recipient_id")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    recipient_id: str
    def __init__(self, campaign_id: _Optional[str] = ..., recipient_id: _Optional[str] = ...) -> None: ...

class DescribeRecipientOutput(_message.Message):
    __slots__ = ("recipient",)
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    recipient: _recipient_pb2.Recipient
    def __init__(self, recipient: _Optional[_Union[_recipient_pb2.Recipient, _Mapping]] = ...) -> None: ...
