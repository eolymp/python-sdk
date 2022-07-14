from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Inline(_message.Message):
    __slots__ = ["code", "link", "math", "text", "variable"]
    class Code(_message.Message):
        __slots__ = ["content"]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        content: str
        def __init__(self, content: _Optional[str] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ["children", "url"]
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        children: _containers.RepeatedCompositeFieldContainer[Inline]
        url: str
        def __init__(self, url: _Optional[str] = ..., children: _Optional[_Iterable[_Union[Inline, _Mapping]]] = ...) -> None: ...
    class Math(_message.Message):
        __slots__ = ["content"]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        content: str
        def __init__(self, content: _Optional[str] = ...) -> None: ...
    class Style(_message.Message):
        __slots__ = ["bold", "italic", "strikethrough", "underline"]
        BOLD_FIELD_NUMBER: _ClassVar[int]
        ITALIC_FIELD_NUMBER: _ClassVar[int]
        STRIKETHROUGH_FIELD_NUMBER: _ClassVar[int]
        UNDERLINE_FIELD_NUMBER: _ClassVar[int]
        bold: bool
        italic: bool
        strikethrough: bool
        underline: bool
        def __init__(self, bold: bool = ..., italic: bool = ..., underline: bool = ..., strikethrough: bool = ...) -> None: ...
    class Text(_message.Message):
        __slots__ = ["str", "style"]
        STR_FIELD_NUMBER: _ClassVar[int]
        STYLE_FIELD_NUMBER: _ClassVar[int]
        str: str
        style: Inline.Style
        def __init__(self, str: _Optional[str] = ..., style: _Optional[_Union[Inline.Style, _Mapping]] = ...) -> None: ...
    class Variable(_message.Message):
        __slots__ = ["name", "style"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        STYLE_FIELD_NUMBER: _ClassVar[int]
        name: str
        style: Inline.Style
        def __init__(self, name: _Optional[str] = ..., style: _Optional[_Union[Inline.Style, _Mapping]] = ...) -> None: ...
    CODE_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    MATH_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    code: Inline.Code
    link: Inline.Link
    math: Inline.Math
    text: Inline.Text
    variable: Inline.Variable
    def __init__(self, text: _Optional[_Union[Inline.Text, _Mapping]] = ..., link: _Optional[_Union[Inline.Link, _Mapping]] = ..., math: _Optional[_Union[Inline.Math, _Mapping]] = ..., code: _Optional[_Union[Inline.Code, _Mapping]] = ..., variable: _Optional[_Union[Inline.Variable, _Mapping]] = ...) -> None: ...
