from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Configuration(_message.Message):
    __slots__ = ["comment_moderation", "members_can_comment_on_posts", "members_can_comment_on_problems", "members_can_create_posts", "post_moderation"]
    class Moderation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    COMMENT_MODERATION_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_CAN_COMMENT_ON_POSTS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_CAN_COMMENT_ON_PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_CAN_CREATE_POSTS_FIELD_NUMBER: _ClassVar[int]
    NO_MODERATION: Configuration.Moderation
    POST_MODERATION: Configuration.Moderation
    POST_MODERATION_FIELD_NUMBER: _ClassVar[int]
    PRE_MODERATION: Configuration.Moderation
    UNKNOWN_MODERATION: Configuration.Moderation
    comment_moderation: Configuration.Moderation
    members_can_comment_on_posts: bool
    members_can_comment_on_problems: bool
    members_can_create_posts: bool
    post_moderation: Configuration.Moderation
    def __init__(self, members_can_create_posts: bool = ..., members_can_comment_on_posts: bool = ..., members_can_comment_on_problems: bool = ..., post_moderation: _Optional[_Union[Configuration.Moderation, str]] = ..., comment_moderation: _Optional[_Union[Configuration.Moderation, str]] = ...) -> None: ...
