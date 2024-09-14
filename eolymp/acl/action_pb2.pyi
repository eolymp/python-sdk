from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

BILLING_READ: Action
BILLING_WRITE: Action
CONTENT_READ: Action
CONTENT_WRITE: Action
CONTEST_READ: Action
CONTEST_WRITE: Action
COURSE_ASSIGN: Action
COURSE_READ: Action
COURSE_WRITE: Action
DESCRIPTOR: _descriptor.FileDescriptor
MEMBER_READ: Action
MEMBER_WRITE: Action
POLICY_READ: Action
POLICY_WRITE: Action
POST_READ: Action
POST_WRITE: Action
PROBLEM_READ: Action
PROBLEM_TESTING: Action
PROBLEM_WRITE: Action
SCOREBOARD_READ: Action
SCOREBOARD_WRITE: Action
SPACE_DELETE: Action
SPACE_READ: Action
SPACE_WRITE: Action
TICKET_READ: Action
TICKET_WRITE: Action
UNKNOWN_ACTION: Action

class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
