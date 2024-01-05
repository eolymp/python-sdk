from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Quota(_message.Message):
    __slots__ = ["active_contests_per_space", "attributes_per_space", "contests_per_space", "courses_per_space", "members_per_space", "participants_per_contest", "permissions_per_space", "problems_per_contest", "problems_per_space", "scoreboards_per_space"]
    ACTIVE_CONTESTS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    CONTESTS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    COURSES_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_PER_CONTEST_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_PER_CONTEST_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARDS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    active_contests_per_space: int
    attributes_per_space: int
    contests_per_space: int
    courses_per_space: int
    members_per_space: int
    participants_per_contest: int
    permissions_per_space: int
    problems_per_contest: int
    problems_per_space: int
    scoreboards_per_space: int
    def __init__(self, problems_per_space: _Optional[int] = ..., members_per_space: _Optional[int] = ..., contests_per_space: _Optional[int] = ..., active_contests_per_space: _Optional[int] = ..., scoreboards_per_space: _Optional[int] = ..., permissions_per_space: _Optional[int] = ..., attributes_per_space: _Optional[int] = ..., courses_per_space: _Optional[int] = ..., problems_per_contest: _Optional[int] = ..., participants_per_contest: _Optional[int] = ...) -> None: ...
