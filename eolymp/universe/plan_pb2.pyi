from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.universe import quota_pb2 as _quota_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Plan(_message.Message):
    __slots__ = ("id", "name", "description", "quota", "labels", "requires_approval", "min_seats", "max_seats", "variants")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Plan.Extra]
        DESCRIPTION_RENDER: _ClassVar[Plan.Extra]
        DESCRIPTION_VALUE: _ClassVar[Plan.Extra]
    NO_EXTRA: Plan.Extra
    DESCRIPTION_RENDER: Plan.Extra
    DESCRIPTION_VALUE: Plan.Extra
    class Recurrence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_RECURRENCE: _ClassVar[Plan.Recurrence]
        ONETIME: _ClassVar[Plan.Recurrence]
        MONTHLY: _ClassVar[Plan.Recurrence]
        YEARLY: _ClassVar[Plan.Recurrence]
    UNKNOWN_RECURRENCE: Plan.Recurrence
    ONETIME: Plan.Recurrence
    MONTHLY: Plan.Recurrence
    YEARLY: Plan.Recurrence
    class Variant(_message.Message):
        __slots__ = ("id", "recurrence", "currency", "unit_amount")
        ID_FIELD_NUMBER: _ClassVar[int]
        RECURRENCE_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        UNIT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        id: str
        recurrence: Plan.Recurrence
        currency: str
        unit_amount: int
        def __init__(self, id: _Optional[str] = ..., recurrence: _Optional[_Union[Plan.Recurrence, str]] = ..., currency: _Optional[str] = ..., unit_amount: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    MIN_SEATS_FIELD_NUMBER: _ClassVar[int]
    MAX_SEATS_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: _content_pb2.Content
    quota: _quota_pb2.Quota
    labels: _containers.RepeatedScalarFieldContainer[str]
    requires_approval: bool
    min_seats: int
    max_seats: int
    variants: _containers.RepeatedCompositeFieldContainer[Plan.Variant]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., quota: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ..., requires_approval: bool = ..., min_seats: _Optional[int] = ..., max_seats: _Optional[int] = ..., variants: _Optional[_Iterable[_Union[Plan.Variant, _Mapping]]] = ...) -> None: ...
