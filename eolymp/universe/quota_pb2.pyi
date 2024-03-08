from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Quota(_message.Message):
    __slots__ = ["active_contests_per_space", "allow_discussions", "attributes_per_space", "code_templates_per_problem", "contest_upsolve_mode", "contests_per_space", "courses_per_space", "customer_support_reply_time", "dedicated_user_database", "editorial_per_problem", "ghost_participants", "max_contest_duration", "members_per_space", "monthly_contests_per_space", "monthly_evaluations_by_seat", "participants_per_contest", "permissions_per_space", "plagiarism_analysis", "priority_evaluation_queue", "problems_per_contest", "problems_per_space", "scoreboards_per_space", "single_sing_on", "solutions_per_problem", "statement_per_problem", "team_contests", "tests_per_problem", "testset_per_problem", "unofficial_participants"]
    ACTIVE_CONTESTS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DISCUSSIONS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    CODE_TEMPLATES_PER_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    CONTESTS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    CONTEST_UPSOLVE_MODE_FIELD_NUMBER: _ClassVar[int]
    COURSES_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_SUPPORT_REPLY_TIME_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_USER_DATABASE_FIELD_NUMBER: _ClassVar[int]
    EDITORIAL_PER_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    GHOST_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONTEST_DURATION_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_CONTESTS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_EVALUATIONS_BY_SEAT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_PER_CONTEST_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    PLAGIARISM_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_EVALUATION_QUEUE_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_PER_CONTEST_FIELD_NUMBER: _ClassVar[int]
    PROBLEMS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARDS_PER_SPACE_FIELD_NUMBER: _ClassVar[int]
    SINGLE_SING_ON_FIELD_NUMBER: _ClassVar[int]
    SOLUTIONS_PER_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_PER_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    TEAM_CONTESTS_FIELD_NUMBER: _ClassVar[int]
    TESTSET_PER_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    TESTS_PER_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    active_contests_per_space: int
    allow_discussions: bool
    attributes_per_space: int
    code_templates_per_problem: int
    contest_upsolve_mode: bool
    contests_per_space: int
    courses_per_space: int
    customer_support_reply_time: int
    dedicated_user_database: bool
    editorial_per_problem: int
    ghost_participants: bool
    max_contest_duration: int
    members_per_space: int
    monthly_contests_per_space: int
    monthly_evaluations_by_seat: int
    participants_per_contest: int
    permissions_per_space: int
    plagiarism_analysis: bool
    priority_evaluation_queue: bool
    problems_per_contest: int
    problems_per_space: int
    scoreboards_per_space: int
    single_sing_on: bool
    solutions_per_problem: int
    statement_per_problem: int
    team_contests: bool
    tests_per_problem: int
    testset_per_problem: int
    unofficial_participants: bool
    def __init__(self, permissions_per_space: _Optional[int] = ..., single_sing_on: bool = ..., dedicated_user_database: bool = ..., attributes_per_space: _Optional[int] = ..., customer_support_reply_time: _Optional[int] = ..., allow_discussions: bool = ..., monthly_evaluations_by_seat: _Optional[int] = ..., priority_evaluation_queue: bool = ..., plagiarism_analysis: bool = ..., members_per_space: _Optional[int] = ..., scoreboards_per_space: _Optional[int] = ..., courses_per_space: _Optional[int] = ..., problems_per_space: _Optional[int] = ..., tests_per_problem: _Optional[int] = ..., testset_per_problem: _Optional[int] = ..., statement_per_problem: _Optional[int] = ..., editorial_per_problem: _Optional[int] = ..., solutions_per_problem: _Optional[int] = ..., code_templates_per_problem: _Optional[int] = ..., contests_per_space: _Optional[int] = ..., active_contests_per_space: _Optional[int] = ..., monthly_contests_per_space: _Optional[int] = ..., problems_per_contest: _Optional[int] = ..., participants_per_contest: _Optional[int] = ..., contest_upsolve_mode: bool = ..., max_contest_duration: _Optional[int] = ..., team_contests: bool = ..., ghost_participants: bool = ..., unofficial_participants: bool = ...) -> None: ...
