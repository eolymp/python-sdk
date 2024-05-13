from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.universe import quota_pb2 as _quota_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Plan(_message.Message):
    __slots__ = ["description", "id", "labels", "max_seats", "min_seats", "name", "quota", "variants"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Recurrence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Variant(_message.Message):
        __slots__ = ["currency", "id", "recurrence", "unit_amount"]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        RECURRENCE_FIELD_NUMBER: _ClassVar[int]
        UNIT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        currency: str
        id: str
        recurrence: Plan.Recurrence
        unit_amount: int
        def __init__(self, id: _Optional[str] = ..., recurrence: _Optional[_Union[Plan.Recurrence, str]] = ..., currency: _Optional[str] = ..., unit_amount: _Optional[int] = ...) -> None: ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_RENDER: Plan.Extra
    DESCRIPTION_VALUE: Plan.Extra
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    MAX_SEATS_FIELD_NUMBER: _ClassVar[int]
    MIN_SEATS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY: Plan.Recurrence
    NAME_FIELD_NUMBER: _ClassVar[int]
    NO_EXTRA: Plan.Extra
    ONETIME: Plan.Recurrence
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_RECURRENCE: Plan.Recurrence
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    YEARLY: Plan.Recurrence
    description: _content_pb2.Content
    id: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    max_seats: int
    min_seats: int
    name: str
    quota: _quota_pb2.Quota
    variants: _containers.RepeatedCompositeFieldContainer[Plan.Variant]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., quota: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ..., min_seats: _Optional[int] = ..., max_seats: _Optional[int] = ..., variants: _Optional[_Iterable[_Union[Plan.Variant, _Mapping]]] = ...) -> None: ...
