from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Configuration(_message.Message):
    __slots__ = ("members_can_create_posts", "members_can_comment_on_posts", "members_can_comment_on_problems", "post_moderation", "comment_moderation")
    class Moderation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_MODERATION: _ClassVar[Configuration.Moderation]
        NO_MODERATION: _ClassVar[Configuration.Moderation]
        PRE_MODERATION: _ClassVar[Configuration.Moderation]
        POST_MODERATION: _ClassVar[Configuration.Moderation]
    UNKNOWN_MODERATION: Configuration.Moderation
    NO_MODERATION: Configuration.Moderation
    PRE_MODERATION: Configuration.Moderation
    POST_MODERATION: Configuration.Moderation
    MEMBERS_CAN_CREATE_POSTS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_CAN_COMMENT_ON_POSTS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_CAN_COMMENT_ON_PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    POST_MODERATION_FIELD_NUMBER: _ClassVar[int]
    COMMENT_MODERATION_FIELD_NUMBER: _ClassVar[int]
    members_can_create_posts: bool
    members_can_comment_on_posts: bool
    members_can_comment_on_problems: bool
    post_moderation: Configuration.Moderation
    comment_moderation: Configuration.Moderation
    def __init__(self, members_can_create_posts: bool = ..., members_can_comment_on_posts: bool = ..., members_can_comment_on_problems: bool = ..., post_moderation: _Optional[_Union[Configuration.Moderation, str]] = ..., comment_moderation: _Optional[_Union[Configuration.Moderation, str]] = ...) -> None: ...
