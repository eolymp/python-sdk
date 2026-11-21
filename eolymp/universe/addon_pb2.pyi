from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.universe import plan_pb2 as _plan_pb2
from eolymp.universe import quota_pb2 as _quota_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Addon(_message.Message):
    __slots__ = ("id", "name", "description", "quota", "variants")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Addon.Extra]
        DESCRIPTION_RENDER: _ClassVar[Addon.Extra]
        DESCRIPTION_VALUE: _ClassVar[Addon.Extra]
    UNKNOWN_EXTRA: Addon.Extra
    DESCRIPTION_RENDER: Addon.Extra
    DESCRIPTION_VALUE: Addon.Extra
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: _content_pb2.Content
    quota: _quota_pb2.Quota
    variants: _containers.RepeatedCompositeFieldContainer[_plan_pb2.Plan.Variant]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., quota: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ..., variants: _Optional[_Iterable[_Union[_plan_pb2.Plan.Variant, _Mapping]]] = ...) -> None: ...
