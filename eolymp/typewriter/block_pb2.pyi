from eolymp.typewriter import inline_pb2 as _inline_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Block(_message.Message):
    __slots__ = ["code", "embed", "heading", "image", "layout", "list", "math", "paragraph", "table", "widget"]
    class Code(_message.Message):
        __slots__ = ["content", "lang"]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        LANG_FIELD_NUMBER: _ClassVar[int]
        content: str
        lang: str
        def __init__(self, lang: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
    class Embed(_message.Message):
        __slots__ = ["path", "values"]
        class Value(_message.Message):
            __slots__ = ["name", "value"]
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            name: str
            value: str
            def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        PATH_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        path: str
        values: _containers.RepeatedCompositeFieldContainer[Block.Embed.Value]
        def __init__(self, path: _Optional[str] = ..., values: _Optional[_Iterable[_Union[Block.Embed.Value, _Mapping]]] = ...) -> None: ...
    class Heading(_message.Message):
        __slots__ = ["children", "level"]
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        children: _containers.RepeatedCompositeFieldContainer[_inline_pb2.Inline]
        level: int
        def __init__(self, level: _Optional[int] = ..., children: _Optional[_Iterable[_Union[_inline_pb2.Inline, _Mapping]]] = ...) -> None: ...
    class Image(_message.Message):
        __slots__ = ["alt", "height", "src", "title", "width", "zoomable"]
        ALT_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        SRC_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        ZOOMABLE_FIELD_NUMBER: _ClassVar[int]
        alt: str
        height: int
        src: str
        title: str
        width: int
        zoomable: bool
        def __init__(self, src: _Optional[str] = ..., alt: _Optional[str] = ..., title: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., zoomable: bool = ...) -> None: ...
    class Layout(_message.Message):
        __slots__ = ["align_content", "align_items", "children", "direction", "gap", "justify_content", "justify_items", "padding"]
        class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ALIGN_CONTENT_FIELD_NUMBER: _ClassVar[int]
        ALIGN_ITEMS_FIELD_NUMBER: _ClassVar[int]
        CENTER: Block.Layout.Alignment
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        COLUMN: Block.Layout.Direction
        DIRECTION_FIELD_NUMBER: _ClassVar[int]
        END: Block.Layout.Alignment
        GAP_FIELD_NUMBER: _ClassVar[int]
        JUSTIFY_CONTENT_FIELD_NUMBER: _ClassVar[int]
        JUSTIFY_ITEMS_FIELD_NUMBER: _ClassVar[int]
        PADDING_FIELD_NUMBER: _ClassVar[int]
        ROW: Block.Layout.Direction
        START: Block.Layout.Alignment
        align_content: Block.Layout.Alignment
        align_items: Block.Layout.Alignment
        children: _containers.RepeatedCompositeFieldContainer[Container]
        direction: Block.Layout.Direction
        gap: int
        justify_content: Block.Layout.Alignment
        justify_items: Block.Layout.Alignment
        padding: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, direction: _Optional[_Union[Block.Layout.Direction, str]] = ..., align_items: _Optional[_Union[Block.Layout.Alignment, str]] = ..., align_content: _Optional[_Union[Block.Layout.Alignment, str]] = ..., justify_items: _Optional[_Union[Block.Layout.Alignment, str]] = ..., justify_content: _Optional[_Union[Block.Layout.Alignment, str]] = ..., gap: _Optional[int] = ..., padding: _Optional[_Iterable[int]] = ..., children: _Optional[_Iterable[_Union[Container, _Mapping]]] = ...) -> None: ...
    class List(_message.Message):
        __slots__ = ["children", "style"]
        class Style(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class Item(_message.Message):
            __slots__ = ["children"]
            CHILDREN_FIELD_NUMBER: _ClassVar[int]
            children: _containers.RepeatedCompositeFieldContainer[Block]
            def __init__(self, children: _Optional[_Iterable[_Union[Block, _Mapping]]] = ...) -> None: ...
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        ORDERED: Block.List.Style
        STYLE_FIELD_NUMBER: _ClassVar[int]
        UNORDERED: Block.List.Style
        children: _containers.RepeatedCompositeFieldContainer[Block.List.Item]
        style: Block.List.Style
        def __init__(self, style: _Optional[_Union[Block.List.Style, str]] = ..., children: _Optional[_Iterable[_Union[Block.List.Item, _Mapping]]] = ...) -> None: ...
    class Math(_message.Message):
        __slots__ = ["content"]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        content: str
        def __init__(self, content: _Optional[str] = ...) -> None: ...
    class Paragraph(_message.Message):
        __slots__ = ["children"]
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        children: _containers.RepeatedCompositeFieldContainer[_inline_pb2.Inline]
        def __init__(self, children: _Optional[_Iterable[_Union[_inline_pb2.Inline, _Mapping]]] = ...) -> None: ...
    class Table(_message.Message):
        __slots__ = ["children", "header"]
        class Header(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class Cell(_message.Message):
            __slots__ = ["children"]
            CHILDREN_FIELD_NUMBER: _ClassVar[int]
            children: _containers.RepeatedCompositeFieldContainer[Block]
            def __init__(self, children: _Optional[_Iterable[_Union[Block, _Mapping]]] = ...) -> None: ...
        class Row(_message.Message):
            __slots__ = ["children"]
            CHILDREN_FIELD_NUMBER: _ClassVar[int]
            children: _containers.RepeatedCompositeFieldContainer[Block.Table.Cell]
            def __init__(self, children: _Optional[_Iterable[_Union[Block.Table.Cell, _Mapping]]] = ...) -> None: ...
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        HEADER_FIELD_NUMBER: _ClassVar[int]
        HORIZONTAL: Block.Table.Header
        VERTICAL: Block.Table.Header
        children: _containers.RepeatedCompositeFieldContainer[Block.Table.Row]
        header: Block.Table.Header
        def __init__(self, header: _Optional[_Union[Block.Table.Header, str]] = ..., children: _Optional[_Iterable[_Union[Block.Table.Row, _Mapping]]] = ...) -> None: ...
    class Widget(_message.Message):
        __slots__ = ["attributes", "children", "name"]
        class AttributesEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        attributes: _containers.ScalarMap[str, str]
        children: _containers.RepeatedCompositeFieldContainer[Block]
        name: str
        def __init__(self, name: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., children: _Optional[_Iterable[_Union[Block, _Mapping]]] = ...) -> None: ...
    CODE_FIELD_NUMBER: _ClassVar[int]
    EMBED_FIELD_NUMBER: _ClassVar[int]
    HEADING_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    MATH_FIELD_NUMBER: _ClassVar[int]
    PARAGRAPH_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_FIELD_NUMBER: _ClassVar[int]
    code: Block.Code
    embed: Block.Embed
    heading: Block.Heading
    image: Block.Image
    layout: Block.Layout
    list: Block.List
    math: Block.Math
    paragraph: Block.Paragraph
    table: Block.Table
    widget: Block.Widget
    def __init__(self, paragraph: _Optional[_Union[Block.Paragraph, _Mapping]] = ..., layout: _Optional[_Union[Block.Layout, _Mapping]] = ..., code: _Optional[_Union[Block.Code, _Mapping]] = ..., math: _Optional[_Union[Block.Math, _Mapping]] = ..., image: _Optional[_Union[Block.Image, _Mapping]] = ..., heading: _Optional[_Union[Block.Heading, _Mapping]] = ..., list: _Optional[_Union[Block.List, _Mapping]] = ..., embed: _Optional[_Union[Block.Embed, _Mapping]] = ..., table: _Optional[_Union[Block.Table, _Mapping]] = ..., widget: _Optional[_Union[Block.Widget, _Mapping]] = ...) -> None: ...

class Container(_message.Message):
    __slots__ = ["children"]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    children: _containers.RepeatedCompositeFieldContainer[Block]
    def __init__(self, children: _Optional[_Iterable[_Union[Block, _Mapping]]] = ...) -> None: ...
