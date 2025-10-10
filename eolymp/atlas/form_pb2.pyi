from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Form(_message.Message):
    __slots__ = ("fields",)
    class Field(_message.Message):
        __slots__ = ("name", "label", "type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_TYPE: _ClassVar[Form.Field.Type]
            CODE: _ClassVar[Form.Field.Type]
            FILE: _ClassVar[Form.Field.Type]
        UNKNOWN_TYPE: Form.Field.Type
        CODE: Form.Field.Type
        FILE: Form.Field.Type
        NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        label: str
        type: Form.Field.Type
        def __init__(self, name: _Optional[str] = ..., label: _Optional[str] = ..., type: _Optional[_Union[Form.Field.Type, str]] = ...) -> None: ...
    class Value(_message.Message):
        __slots__ = ("name", "code", "file")
        class Code(_message.Message):
            __slots__ = ("runtime", "source_url")
            RUNTIME_FIELD_NUMBER: _ClassVar[int]
            SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
            runtime: str
            source_url: str
            def __init__(self, runtime: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...
        class File(_message.Message):
            __slots__ = ("filename", "data_url")
            FILENAME_FIELD_NUMBER: _ClassVar[int]
            DATA_URL_FIELD_NUMBER: _ClassVar[int]
            filename: str
            data_url: str
            def __init__(self, filename: _Optional[str] = ..., data_url: _Optional[str] = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        FILE_FIELD_NUMBER: _ClassVar[int]
        name: str
        code: Form.Value.Code
        file: Form.Value.File
        def __init__(self, name: _Optional[str] = ..., code: _Optional[_Union[Form.Value.Code, _Mapping]] = ..., file: _Optional[_Union[Form.Value.File, _Mapping]] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[Form.Field]
    def __init__(self, fields: _Optional[_Iterable[_Union[Form.Field, _Mapping]]] = ...) -> None: ...
