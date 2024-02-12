from eolymp.ecm import node_pb2 as _node_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entry(_message.Message):
    __slots__ = ["attachments", "attributes", "content", "id", "timestamp", "type"]
    class Attachment(_message.Message):
        __slots__ = ["reference", "rel", "type"]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        REL_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        reference: str
        rel: str
        type: str
        def __init__(self, rel: _Optional[str] = ..., type: _Optional[str] = ..., reference: _Optional[str] = ...) -> None: ...
    class AttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    attachments: _containers.RepeatedCompositeFieldContainer[Entry.Attachment]
    attributes: _containers.ScalarMap[str, str]
    content: _node_pb2.Node
    id: str
    timestamp: _timestamp_pb2.Timestamp
    type: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., attributes: _Optional[_Mapping[str, str]] = ..., attachments: _Optional[_Iterable[_Union[Entry.Attachment, _Mapping]]] = ..., content: _Optional[_Union[_node_pb2.Node, _Mapping]] = ...) -> None: ...
