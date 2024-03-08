from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.discussion import configuration_pb2 as _configuration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeDiscussionConfigInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeDiscussionConfigOutput(_message.Message):
    __slots__ = ["config"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _configuration_pb2.Configuration
    def __init__(self, config: _Optional[_Union[_configuration_pb2.Configuration, _Mapping]] = ...) -> None: ...

class UpdateDiscussionConfigInput(_message.Message):
    __slots__ = ["config"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateDiscussionConfigInput.Patch
    COMMENT_MODERATION: UpdateDiscussionConfigInput.Patch
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_CAN_COMMENT_ON_POSTS: UpdateDiscussionConfigInput.Patch
    MEMBERS_CAN_COMMENT_ON_PROBLEMS: UpdateDiscussionConfigInput.Patch
    MEMBERS_CAN_CREATE_POSTS: UpdateDiscussionConfigInput.Patch
    POST_MODERATION: UpdateDiscussionConfigInput.Patch
    config: _configuration_pb2.Configuration
    def __init__(self, config: _Optional[_Union[_configuration_pb2.Configuration, _Mapping]] = ...) -> None: ...

class UpdateDiscussionConfigOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
