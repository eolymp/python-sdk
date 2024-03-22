from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import activity_pb2 as _activity_pb2
from eolymp.judge import announcement_pb2 as _announcement_pb2
from eolymp.judge import contest_pb2 as _contest_pb2
from eolymp.judge import participant_pb2 as _participant_pb2
from eolymp.judge import problem_pb2 as _problem_pb2
from eolymp.judge import result_pb2 as _result_pb2
from eolymp.judge import score_pb2 as _score_pb2
from eolymp.judge import submission_pb2 as _submission_pb2
from eolymp.judge import template_pb2 as _template_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant: _participant_pb2.Participant
    def __init__(self, contest_id: _Optional[str] = ..., participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class AddParticipantOutput(_message.Message):
    __slots__ = ["participant_id"]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    participant_id: str
    def __init__(self, participant_id: _Optional[str] = ...) -> None: ...

class CloseContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class CloseContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ConfigureAppearanceInput(_message.Message):
    __slots__ = ["appearance", "contest_id"]
    APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    appearance: _contest_pb2.Contest.Appearance
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., appearance: _Optional[_Union[_contest_pb2.Contest.Appearance, _Mapping]] = ...) -> None: ...

class ConfigureAppearanceOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ConfigureRuntimeInput(_message.Message):
    __slots__ = ["contest_id", "runtime"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    runtime: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, contest_id: _Optional[str] = ..., runtime: _Optional[_Iterable[str]] = ...) -> None: ...

class ConfigureRuntimeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateAnnouncementInput(_message.Message):
    __slots__ = ["announcement", "contest_id"]
    ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    announcement: _announcement_pb2.Announcement
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., announcement: _Optional[_Union[_announcement_pb2.Announcement, _Mapping]] = ...) -> None: ...

class CreateAnnouncementOutput(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CreateContestInput(_message.Message):
    __slots__ = ["contest"]
    CONTEST_FIELD_NUMBER: _ClassVar[int]
    contest: _contest_pb2.Contest
    def __init__(self, contest: _Optional[_Union[_contest_pb2.Contest, _Mapping]] = ...) -> None: ...

class CreateContestOutput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class CreateSubmissionInput(_message.Message):
    __slots__ = ["contest_id", "lang", "problem_id", "source"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    lang: str
    problem_id: str
    source: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class CreateSubmissionOutput(_message.Message):
    __slots__ = ["submission_id"]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    def __init__(self, submission_id: _Optional[str] = ...) -> None: ...

class DeleteAnnouncementInput(_message.Message):
    __slots__ = ["announcement_id", "contest_id"]
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    announcement_id: str
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., announcement_id: _Optional[str] = ...) -> None: ...

class DeleteAnnouncementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DeleteContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteProblemInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class DeleteProblemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteSubmissionInput(_message.Message):
    __slots__ = ["contest_id", "submission_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    submission_id: str
    def __init__(self, contest_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class DeleteSubmissionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeAnnouncementInput(_message.Message):
    __slots__ = ["announcement_id", "contest_id", "extra"]
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    announcement_id: str
    contest_id: str
    extra: _containers.RepeatedScalarFieldContainer[_announcement_pb2.Announcement.Extra]
    def __init__(self, contest_id: _Optional[str] = ..., announcement_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_announcement_pb2.Announcement.Extra, str]]] = ...) -> None: ...

class DescribeAnnouncementOutput(_message.Message):
    __slots__ = ["announcement"]
    ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    announcement: _announcement_pb2.Announcement
    def __init__(self, announcement: _Optional[_Union[_announcement_pb2.Announcement, _Mapping]] = ...) -> None: ...

class DescribeAnnouncementStatusInput(_message.Message):
    __slots__ = ["announcement_id", "contest_id"]
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    announcement_id: str
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., announcement_id: _Optional[str] = ...) -> None: ...

class DescribeAnnouncementStatusOutput(_message.Message):
    __slots__ = ["is_read"]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    is_read: bool
    def __init__(self, is_read: bool = ...) -> None: ...

class DescribeAppearanceInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DescribeAppearanceOutput(_message.Message):
    __slots__ = ["appearance"]
    APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    appearance: _contest_pb2.Contest.Appearance
    def __init__(self, appearance: _Optional[_Union[_contest_pb2.Contest.Appearance, _Mapping]] = ...) -> None: ...

class DescribeCodeTemplateInput(_message.Message):
    __slots__ = ["contest_id", "problem_id", "template_ern", "template_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ERN_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    template_ern: str
    template_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., template_id: _Optional[str] = ..., template_ern: _Optional[str] = ...) -> None: ...

class DescribeCodeTemplateOutput(_message.Message):
    __slots__ = ["template"]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...

class DescribeContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DescribeContestOutput(_message.Message):
    __slots__ = ["contest"]
    CONTEST_FIELD_NUMBER: _ClassVar[int]
    contest: _contest_pb2.Contest
    def __init__(self, contest: _Optional[_Union[_contest_pb2.Contest, _Mapping]] = ...) -> None: ...

class DescribeContestUsageInput(_message.Message):
    __slots__ = ["period_end", "period_start"]
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    period_end: _timestamp_pb2.Timestamp
    period_start: _timestamp_pb2.Timestamp
    def __init__(self, period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DescribeContestUsageOutput(_message.Message):
    __slots__ = ["active_contests", "monthly_contests", "total_contests"]
    ACTIVE_CONTESTS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_CONTESTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CONTESTS_FIELD_NUMBER: _ClassVar[int]
    active_contests: int
    monthly_contests: int
    total_contests: int
    def __init__(self, total_contests: _Optional[int] = ..., active_contests: _Optional[int] = ..., monthly_contests: _Optional[int] = ...) -> None: ...

class DescribeParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class DescribeParticipantOutput(_message.Message):
    __slots__ = ["participant"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    participant: _participant_pb2.Participant
    def __init__(self, participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class DescribeProblemInput(_message.Message):
    __slots__ = ["contest_id", "problem_ern", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ERN_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_ern: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., problem_ern: _Optional[str] = ...) -> None: ...

class DescribeProblemOutput(_message.Message):
    __slots__ = ["problem"]
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    problem: _problem_pb2.Problem
    def __init__(self, problem: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ...) -> None: ...

class DescribeRuntimeInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DescribeRuntimeOutput(_message.Message):
    __slots__ = ["runtime"]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    runtime: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, runtime: _Optional[_Iterable[str]] = ...) -> None: ...

class DescribeScoreInput(_message.Message):
    __slots__ = ["contest_id", "mode", "participant_id", "time_offset"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    mode: _score_pb2.Score.FetchingMode
    participant_id: str
    time_offset: int
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., mode: _Optional[_Union[_score_pb2.Score.FetchingMode, str]] = ..., time_offset: _Optional[int] = ...) -> None: ...

class DescribeScoreOutput(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _score_pb2.Score
    def __init__(self, score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class DescribeSubmissionInput(_message.Message):
    __slots__ = ["contest_id", "extra", "submission_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    extra: _containers.RepeatedScalarFieldContainer[_submission_pb2.Submission.Extra]
    submission_id: str
    def __init__(self, contest_id: _Optional[str] = ..., submission_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_submission_pb2.Submission.Extra, str]]] = ...) -> None: ...

class DescribeSubmissionOutput(_message.Message):
    __slots__ = ["submission"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...

class DisableParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class DisableParticipantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EnableParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class EnableParticipantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EnterPasscodeInput(_message.Message):
    __slots__ = ["contest_id", "passcode"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    passcode: str
    def __init__(self, contest_id: _Optional[str] = ..., passcode: _Optional[str] = ...) -> None: ...

class EnterPasscodeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExportScoreInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class ExportScoreOutput(_message.Message):
    __slots__ = ["scores"]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    scores: _containers.RepeatedCompositeFieldContainer[_score_pb2.Score]
    def __init__(self, scores: _Optional[_Iterable[_Union[_score_pb2.Score, _Mapping]]] = ...) -> None: ...

class FreezeContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class FreezeContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ImportProblemInput(_message.Message):
    __slots__ = ["contest_id", "import_id", "index", "score_by_best_testset", "submit_limit"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    IMPORT_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SCORE_BY_BEST_TESTSET_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    import_id: str
    index: int
    score_by_best_testset: bool
    submit_limit: int
    def __init__(self, contest_id: _Optional[str] = ..., import_id: _Optional[str] = ..., index: _Optional[int] = ..., submit_limit: _Optional[int] = ..., score_by_best_testset: bool = ...) -> None: ...

class ImportProblemOutput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ImportScoreInput(_message.Message):
    __slots__ = ["contest_id", "participant_id", "scores"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    scores: _containers.RepeatedCompositeFieldContainer[_score_pb2.Score]
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., scores: _Optional[_Iterable[_Union[_score_pb2.Score, _Mapping]]] = ...) -> None: ...

class ImportScoreOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectParticipantInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class IntrospectParticipantOutput(_message.Message):
    __slots__ = ["participant"]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    participant: _participant_pb2.Participant
    def __init__(self, participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class IntrospectScoreInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class IntrospectScoreOutput(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _score_pb2.Score
    def __init__(self, score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class JoinContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class JoinContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListActivitiesInput(_message.Message):
    __slots__ = ["contest_id", "offset", "size"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    offset: int
    size: int
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListActivitiesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_activity_pb2.Activity]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_activity_pb2.Activity, _Mapping]]] = ...) -> None: ...

class ListAnnouncementsInput(_message.Message):
    __slots__ = ["contest_id", "extra", "filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "is_read"]
        ID_FIELD_NUMBER: _ClassVar[int]
        IS_READ_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        is_read: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., is_read: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    extra: _containers.RepeatedScalarFieldContainer[_announcement_pb2.Announcement.Extra]
    filters: ListAnnouncementsInput.Filter
    offset: int
    size: int
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListAnnouncementsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_announcement_pb2.Announcement.Extra, str]]] = ...) -> None: ...

class ListAnnouncementsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_announcement_pb2.Announcement]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_announcement_pb2.Announcement, _Mapping]]] = ...) -> None: ...

class ListAttachmentsInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class ListAttachmentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2.Problem.Attachment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2.Problem.Attachment, _Mapping]]] = ...) -> None: ...

class ListContestsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["city", "country", "difficulty", "ends_at", "featured", "format", "id", "name", "public", "query", "region", "scale", "series", "starts_at", "status", "visibility", "year"]
        CITY_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
        ENDS_AT_FIELD_NUMBER: _ClassVar[int]
        FEATURED_FIELD_NUMBER: _ClassVar[int]
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        SCALE_FIELD_NUMBER: _ClassVar[int]
        SERIES_FIELD_NUMBER: _ClassVar[int]
        STARTS_AT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        YEAR_FIELD_NUMBER: _ClassVar[int]
        city: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        country: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        difficulty: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        ends_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        featured: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        format: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        public: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        query: str
        region: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        scale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        series: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        starts_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        visibility: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        year: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., starts_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., ends_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., public: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., visibility: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., format: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., featured: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., year: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., scale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., series: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., difficulty: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., country: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., region: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., city: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListContestsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListContestsInput.Filter, _Mapping]] = ...) -> None: ...

class ListContestsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_contest_pb2.Contest]
    total: int
    def __init__(self, items: _Optional[_Iterable[_Union[_contest_pb2.Contest, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class ListExamplesInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class ListExamplesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2.Problem.Test]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2.Problem.Test, _Mapping]]] = ...) -> None: ...

class ListParticipantsInput(_message.Message):
    __slots__ = ["contest_id", "filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["complete_at", "id", "member_id", "name", "penalty", "score", "started_at", "status"]
        COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        complete_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        penalty: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        score: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        started_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., score: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., penalty: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., started_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., complete_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ...) -> None: ...
    COMPLETE_AT: ListParticipantsInput.Sortable
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PENALTY: ListParticipantsInput.Sortable
    RANK: ListParticipantsInput.Sortable
    SCORE: ListParticipantsInput.Sortable
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT: ListParticipantsInput.Sortable
    contest_id: str
    filters: ListParticipantsInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListParticipantsInput.Sortable
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListParticipantsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListParticipantsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListParticipantsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_participant_pb2.Participant]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_participant_pb2.Participant, _Mapping]]] = ...) -> None: ...

class ListProblemsInput(_message.Message):
    __slots__ = ["contest_id", "offset", "size"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    offset: int
    size: int
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListProblemsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2.Problem]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2.Problem, _Mapping]]] = ...) -> None: ...

class ListResultInput(_message.Message):
    __slots__ = ["contest_id", "mode", "offset", "size", "time_offset"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    mode: _score_pb2.Score.FetchingMode
    offset: int
    size: int
    time_offset: int
    def __init__(self, contest_id: _Optional[str] = ..., mode: _Optional[_Union[_score_pb2.Score.FetchingMode, str]] = ..., time_offset: _Optional[int] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListResultOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_result_pb2.Result]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_result_pb2.Result, _Mapping]]] = ...) -> None: ...

class ListStatementsInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class ListStatementsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2.Problem.Statement]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2.Problem.Statement, _Mapping]]] = ...) -> None: ...

class ListSubmissionsInput(_message.Message):
    __slots__ = ["contest_id", "extra", "filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "lang", "participant_id", "percentage", "problem_id", "score", "signature", "status", "submitted_at"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LANG_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        lang: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        participant_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        percentage: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        problem_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        score: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        signature: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        submitted_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., participant_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., problem_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., lang: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., score: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., percentage: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., submitted_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., signature: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    extra: _containers.RepeatedScalarFieldContainer[_submission_pb2.Submission.Extra]
    filters: ListSubmissionsInput.Filter
    offset: int
    size: int
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSubmissionsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_submission_pb2.Submission.Extra, str]]] = ...) -> None: ...

class ListSubmissionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_submission_pb2.Submission]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_submission_pb2.Submission, _Mapping]]] = ...) -> None: ...

class LookupCodeTemplateInput(_message.Message):
    __slots__ = ["contest_id", "problem_ern", "problem_id", "runtime"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ERN_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_ern: str
    problem_id: str
    runtime: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., problem_ern: _Optional[str] = ..., runtime: _Optional[str] = ...) -> None: ...

class LookupCodeTemplateOutput(_message.Message):
    __slots__ = ["template"]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...

class LookupContestInput(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class LookupContestOutput(_message.Message):
    __slots__ = ["appearance", "contest"]
    APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    CONTEST_FIELD_NUMBER: _ClassVar[int]
    appearance: _contest_pb2.Contest.Appearance
    contest: _contest_pb2.Contest
    def __init__(self, contest: _Optional[_Union[_contest_pb2.Contest, _Mapping]] = ..., appearance: _Optional[_Union[_contest_pb2.Contest.Appearance, _Mapping]] = ...) -> None: ...

class OpenContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class OpenContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ReadAnnouncementInput(_message.Message):
    __slots__ = ["announcement_id", "contest_id"]
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    announcement_id: str
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., announcement_id: _Optional[str] = ...) -> None: ...

class ReadAnnouncementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RebuildScoreInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class RebuildScoreOutput(_message.Message):
    __slots__ = ["activity_id"]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    def __init__(self, activity_id: _Optional[str] = ...) -> None: ...

class RemoveParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class RemoveParticipantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemovePasscodeInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class RemovePasscodeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ResetPasscodeInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class ResetPasscodeOutput(_message.Message):
    __slots__ = ["passcode"]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    passcode: str
    def __init__(self, passcode: _Optional[str] = ...) -> None: ...

class RestoreSubmissionInput(_message.Message):
    __slots__ = ["contest_id", "submission_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    submission_id: str
    def __init__(self, contest_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class RestoreSubmissionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ResumeContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class ResumeContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RetestProblemInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class RetestProblemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RetestSubmissionInput(_message.Message):
    __slots__ = ["contest_id", "submission_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    submission_id: str
    def __init__(self, contest_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class RetestSubmissionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetPasscodeInput(_message.Message):
    __slots__ = ["contest_id", "participant_id", "passcode"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    passcode: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., passcode: _Optional[str] = ...) -> None: ...

class SetPasscodeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StartContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class StartContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SuspendContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class SuspendContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SyncProblemInput(_message.Message):
    __slots__ = ["contest_id", "problem_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class SyncProblemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAnnouncementInput(_message.Message):
    __slots__ = ["announcement", "announcement_id", "contest_id"]
    ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    announcement: _announcement_pb2.Announcement
    announcement_id: str
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., announcement_id: _Optional[str] = ..., announcement: _Optional[_Union[_announcement_pb2.Announcement, _Mapping]] = ...) -> None: ...

class UpdateAnnouncementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateContestInput(_message.Message):
    __slots__ = ["contest", "contest_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateContestInput.Patch
    APPEARANCE: UpdateContestInput.Patch
    CONTEST_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN: UpdateContestInput.Patch
    DURATION: UpdateContestInput.Patch
    ENDS_AT: UpdateContestInput.Patch
    ENVIRONMENT: UpdateContestInput.Patch
    FEATURED_UNTIL: UpdateContestInput.Patch
    FORMAT: UpdateContestInput.Patch
    JOIN_UNOFFICIALLY: UpdateContestInput.Patch
    NAME: UpdateContestInput.Patch
    PARTICIPATION_MODE: UpdateContestInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD: UpdateContestInput.Patch
    STARTS_AT: UpdateContestInput.Patch
    TAXONOMY: UpdateContestInput.Patch
    UPSOLVE: UpdateContestInput.Patch
    VISIBILITY: UpdateContestInput.Patch
    contest: _contest_pb2.Contest
    contest_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateContestInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateContestInput.Patch, str]]] = ..., contest_id: _Optional[str] = ..., contest: _Optional[_Union[_contest_pb2.Contest, _Mapping]] = ...) -> None: ...

class UpdateContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateParticipantInput(_message.Message):
    __slots__ = ["contest_id", "participant", "participant_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: UpdateParticipantInput.Patch
    ALL: UpdateParticipantInput.Patch
    BONUS_TIME: UpdateParticipantInput.Patch
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    MEDAL: UpdateParticipantInput.Patch
    NAME: UpdateParticipantInput.Patch
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    PASSCODE: UpdateParticipantInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL: UpdateParticipantInput.Patch
    contest_id: str
    participant: _participant_pb2.Participant
    participant_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateParticipantInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateParticipantInput.Patch, str]]] = ..., contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class UpdateParticipantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateProblemInput(_message.Message):
    __slots__ = ["contest_id", "index", "problem_id", "score_by_best_testset", "submit_limit"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_BY_BEST_TESTSET_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    index: int
    problem_id: str
    score_by_best_testset: bool
    submit_limit: int
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., index: _Optional[int] = ..., submit_limit: _Optional[int] = ..., score_by_best_testset: bool = ...) -> None: ...

class UpdateProblemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VerifyPasscodeInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class VerifyPasscodeOutput(_message.Message):
    __slots__ = ["required", "valid"]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    VALID_FIELD_NUMBER: _ClassVar[int]
    required: bool
    valid: bool
    def __init__(self, required: bool = ..., valid: bool = ...) -> None: ...

class WatchSubmissionInput(_message.Message):
    __slots__ = ["contest_id", "extra", "submission_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    extra: _containers.RepeatedScalarFieldContainer[_submission_pb2.Submission.Extra]
    submission_id: str
    def __init__(self, contest_id: _Optional[str] = ..., submission_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_submission_pb2.Submission.Extra, str]]] = ...) -> None: ...

class WatchSubmissionOutput(_message.Message):
    __slots__ = ["submission"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...
