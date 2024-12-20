from eolymp.content import fragment_pb2 as _fragment_pb2
from eolymp.content import variant_pb2 as _variant_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FragmentChangedEvent(_message.Message):
    __slots__ = ["after", "before", "scope"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    after: _fragment_pb2.Fragment
    before: _fragment_pb2.Fragment
    scope: str
    def __init__(self, scope: _Optional[str] = ..., before: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ..., after: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class VariantChangedEvent(_message.Message):
    __slots__ = ["after", "before", "fragment_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    after: _variant_pb2.Variant
    before: _variant_pb2.Variant
    fragment_id: str
    def __init__(self, fragment_id: _Optional[str] = ..., before: _Optional[_Union[_variant_pb2.Variant, _Mapping]] = ..., after: _Optional[_Union[_variant_pb2.Variant, _Mapping]] = ...) -> None: ...
