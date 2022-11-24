from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.harmony import agreement_pb2 as _agreement_pb2
from eolymp.harmony import consent_pb2 as _consent_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FollowShortcutInput(_message.Message):
    __slots__ = ["shortcut_id", "status"]
    SHORTCUT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    shortcut_id: str
    status: _consent_pb2.Consent.Status
    def __init__(self, shortcut_id: _Optional[str] = ..., status: _Optional[_Union[_consent_pb2.Consent.Status, str]] = ...) -> None: ...

class FollowShortcutOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetConsentInput(_message.Message):
    __slots__ = ["agreement_id"]
    AGREEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    agreement_id: str
    def __init__(self, agreement_id: _Optional[str] = ...) -> None: ...

class GetConsentOutput(_message.Message):
    __slots__ = ["consent"]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    consent: _consent_pb2.Consent
    def __init__(self, consent: _Optional[_Union[_consent_pb2.Consent, _Mapping]] = ...) -> None: ...

class ListAgreementsInput(_message.Message):
    __slots__ = ["preferred_locales"]
    PREFERRED_LOCALES_FIELD_NUMBER: _ClassVar[int]
    preferred_locales: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, preferred_locales: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAgreementsOutput(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_agreement_pb2.Agreement]
    def __init__(self, items: _Optional[_Iterable[_Union[_agreement_pb2.Agreement, _Mapping]]] = ...) -> None: ...

class SetConsentInput(_message.Message):
    __slots__ = ["agreement_id", "status"]
    AGREEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    agreement_id: str
    status: _consent_pb2.Consent.Status
    def __init__(self, agreement_id: _Optional[str] = ..., status: _Optional[_Union[_consent_pb2.Consent.Status, str]] = ...) -> None: ...

class SetConsentOutput(_message.Message):
    __slots__ = ["consent"]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    consent: _consent_pb2.Consent
    def __init__(self, consent: _Optional[_Union[_consent_pb2.Consent, _Mapping]] = ...) -> None: ...
