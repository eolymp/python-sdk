from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Plan(_message.Message):
    __slots__ = ["id", "name", "variants"]
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
    DESCRIPTION_RENDER: Plan.Extra
    DESCRIPTION_VALUE: Plan.Extra
    ID_FIELD_NUMBER: _ClassVar[int]
    MONTHLY: Plan.Recurrence
    NAME_FIELD_NUMBER: _ClassVar[int]
    NO_EXTRA: Plan.Extra
    ONETIME: Plan.Recurrence
    UNKNOWN_RECURRENCE: Plan.Recurrence
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    YEARLY: Plan.Recurrence
    id: str
    name: str
    variants: _containers.RepeatedCompositeFieldContainer[Plan.Variant]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., variants: _Optional[_Iterable[_Union[Plan.Variant, _Mapping]]] = ...) -> None: ...
