from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.taxonomy import topic_pb2 as _topic_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTopicInput(_message.Message):
    __slots__ = ["topic"]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: _topic_pb2.Topic
    def __init__(self, topic: _Optional[_Union[_topic_pb2.Topic, _Mapping]] = ...) -> None: ...

class CreateTopicOutput(_message.Message):
    __slots__ = ["topic_id"]
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    def __init__(self, topic_id: _Optional[str] = ...) -> None: ...

class DeleteTopicInput(_message.Message):
    __slots__ = ["topic_id"]
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    def __init__(self, topic_id: _Optional[str] = ...) -> None: ...

class DeleteTopicOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteTranslationInput(_message.Message):
    __slots__ = ["locale", "topic_id"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    locale: str
    topic_id: str
    def __init__(self, topic_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class DeleteTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeTopicInput(_message.Message):
    __slots__ = ["locale", "topic_id"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    locale: str
    topic_id: str
    def __init__(self, topic_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class DescribeTopicOutput(_message.Message):
    __slots__ = ["topic"]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: _topic_pb2.Topic
    def __init__(self, topic: _Optional[_Union[_topic_pb2.Topic, _Mapping]] = ...) -> None: ...

class ListTopicsInput(_message.Message):
    __slots__ = ["filters", "locale", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "name", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListTopicsInput.Filter
    locale: str
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTopicsInput.Filter, _Mapping]] = ..., locale: _Optional[str] = ...) -> None: ...

class ListTopicsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_topic_pb2.Topic]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_topic_pb2.Topic, _Mapping]]] = ...) -> None: ...

class ListTranslationsInput(_message.Message):
    __slots__ = ["filters", "offset", "size", "topic_id"]
    class Filter(_message.Message):
        __slots__ = ["locale"]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    filters: ListTranslationsInput.Filter
    offset: int
    size: int
    topic_id: str
    def __init__(self, topic_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTranslationsInput.Filter, _Mapping]] = ...) -> None: ...

class ListTranslationsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_topic_pb2.Topic.Translation]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_topic_pb2.Topic.Translation, _Mapping]]] = ...) -> None: ...

class TranslateTopicInput(_message.Message):
    __slots__ = ["locale", "topic_id", "translation"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    locale: str
    topic_id: str
    translation: _topic_pb2.Topic.Translation
    def __init__(self, topic_id: _Optional[str] = ..., locale: _Optional[str] = ..., translation: _Optional[_Union[_topic_pb2.Topic.Translation, _Mapping]] = ...) -> None: ...

class TranslateTopicOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateTopicInput(_message.Message):
    __slots__ = ["patch", "topic", "topic_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateTopicInput.Patch
    KEYWORDS: UpdateTopicInput.Patch
    NAME: UpdateTopicInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SUMMARY: UpdateTopicInput.Patch
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateTopicInput.Patch]
    topic: _topic_pb2.Topic
    topic_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateTopicInput.Patch, str]]] = ..., topic_id: _Optional[str] = ..., topic: _Optional[_Union[_topic_pb2.Topic, _Mapping]] = ...) -> None: ...

class UpdateTopicOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
