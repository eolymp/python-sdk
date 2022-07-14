from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorLocalization(_message.Message):
    __slots__ = ["phrase_key", "phrase_params"]
    class PhraseParamsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PHRASE_KEY_FIELD_NUMBER: _ClassVar[int]
    PHRASE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    phrase_key: str
    phrase_params: _containers.ScalarMap[str, str]
    def __init__(self, phrase_key: _Optional[str] = ..., phrase_params: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ErrorReport(_message.Message):
    __slots__ = ["report_id"]
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    report_id: str
    def __init__(self, report_id: _Optional[str] = ...) -> None: ...

class InvalidArgument(_message.Message):
    __slots__ = ["argument_path", "validation"]
    ARGUMENT_PATH_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    argument_path: str
    validation: _containers.RepeatedCompositeFieldContainer[Validation]
    def __init__(self, argument_path: _Optional[str] = ..., validation: _Optional[_Iterable[_Union[Validation, _Mapping]]] = ...) -> None: ...

class QuotaExceeded(_message.Message):
    __slots__ = ["quota", "usage"]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    quota: int
    usage: int
    def __init__(self, quota: _Optional[int] = ..., usage: _Optional[int] = ...) -> None: ...

class Validation(_message.Message):
    __slots__ = ["argument_path", "error_message", "localization"]
    ARGUMENT_PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATION_FIELD_NUMBER: _ClassVar[int]
    argument_path: _containers.RepeatedScalarFieldContainer[str]
    error_message: str
    localization: ErrorLocalization
    def __init__(self, argument_path: _Optional[_Iterable[str]] = ..., error_message: _Optional[str] = ..., localization: _Optional[_Union[ErrorLocalization, _Mapping]] = ...) -> None: ...
