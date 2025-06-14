from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Certification(_message.Message):
    __slots__ = ("enabled", "affiliation", "signers")
    class Signer(_message.Message):
        __slots__ = ("name", "title")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        name: str
        title: str
        def __init__(self, name: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    AFFILIATION_FIELD_NUMBER: _ClassVar[int]
    SIGNERS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    affiliation: str
    signers: _containers.RepeatedCompositeFieldContainer[Certification.Signer]
    def __init__(self, enabled: bool = ..., affiliation: _Optional[str] = ..., signers: _Optional[_Iterable[_Union[Certification.Signer, _Mapping]]] = ...) -> None: ...
