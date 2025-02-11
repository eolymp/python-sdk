from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.runtime import runtime_pb2 as _runtime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Editor(_message.Message):
    __slots__ = ("state", "features", "runtimes")
    class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_FEATURE: _ClassVar[Editor.Feature]
        PRINT_CODE: _ClassVar[Editor.Feature]
    UNKNOWN_FEATURE: Editor.Feature
    PRINT_CODE: Editor.Feature
    class State(_message.Message):
        __slots__ = ("runtime", "source_code", "input_data")
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
        INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
        runtime: str
        source_code: str
        input_data: str
        def __init__(self, runtime: _Optional[str] = ..., source_code: _Optional[str] = ..., input_data: _Optional[str] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    RUNTIMES_FIELD_NUMBER: _ClassVar[int]
    state: Editor.State
    features: _containers.RepeatedScalarFieldContainer[Editor.Feature]
    runtimes: _containers.RepeatedCompositeFieldContainer[_runtime_pb2.Runtime]
    def __init__(self, state: _Optional[_Union[Editor.State, _Mapping]] = ..., features: _Optional[_Iterable[_Union[Editor.Feature, str]]] = ..., runtimes: _Optional[_Iterable[_Union[_runtime_pb2.Runtime, _Mapping]]] = ...) -> None: ...

class DescribeEditorInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeEditorOutput(_message.Message):
    __slots__ = ("editor",)
    EDITOR_FIELD_NUMBER: _ClassVar[int]
    editor: Editor
    def __init__(self, editor: _Optional[_Union[Editor, _Mapping]] = ...) -> None: ...

class DescribeEditorStateInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeEditorStateOutput(_message.Message):
    __slots__ = ("runtime", "source_code", "input_data", "features")
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    runtime: str
    source_code: str
    input_data: str
    features: _containers.RepeatedScalarFieldContainer[Editor.Feature]
    def __init__(self, runtime: _Optional[str] = ..., source_code: _Optional[str] = ..., input_data: _Optional[str] = ..., features: _Optional[_Iterable[_Union[Editor.Feature, str]]] = ...) -> None: ...

class UpdateEditorStateInput(_message.Message):
    __slots__ = ("runtime", "source_code", "input_data")
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
    runtime: str
    source_code: str
    input_data: str
    def __init__(self, runtime: _Optional[str] = ..., source_code: _Optional[str] = ..., input_data: _Optional[str] = ...) -> None: ...

class UpdateEditorStateOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PrintEditorCodeInput(_message.Message):
    __slots__ = ("runtime", "source_code")
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    runtime: str
    source_code: str
    def __init__(self, runtime: _Optional[str] = ..., source_code: _Optional[str] = ...) -> None: ...

class PrintEditorCodeOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
