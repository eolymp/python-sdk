from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import activity_pb2 as _activity_pb2
from eolymp.judge import contest_pb2 as _contest_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloseContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class CloseContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CopyContestInput(_message.Message):
    __slots__ = ["contest_id", "copy_name", "copy_scope", "copy_visibility"]
    class Scope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: CopyContestInput.Scope
    CONFIGURATION: CopyContestInput.Scope
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    COPY_NAME_FIELD_NUMBER: _ClassVar[int]
    COPY_SCOPE_FIELD_NUMBER: _ClassVar[int]
    COPY_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS: CopyContestInput.Scope
    PERMISSIONS: CopyContestInput.Scope
    PROBLEMS: CopyContestInput.Scope
    contest_id: str
    copy_name: str
    copy_scope: _containers.RepeatedScalarFieldContainer[CopyContestInput.Scope]
    copy_visibility: _contest_pb2.Contest.Visibility
    def __init__(self, contest_id: _Optional[str] = ..., copy_scope: _Optional[_Iterable[_Union[CopyContestInput.Scope, str]]] = ..., copy_name: _Optional[str] = ..., copy_visibility: _Optional[_Union[_contest_pb2.Contest.Visibility, str]] = ...) -> None: ...

class CopyContestOutput(_message.Message):
    __slots__ = ["copy_contest_id"]
    COPY_CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    copy_contest_id: str
    def __init__(self, copy_contest_id: _Optional[str] = ...) -> None: ...

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

class DeleteContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DeleteContestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

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

class FreezeContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class FreezeContestOutput(_message.Message):
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

class OpenContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class OpenContestOutput(_message.Message):
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

class SuspendContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class SuspendContestOutput(_message.Message):
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
    DURATION: UpdateContestInput.Patch
    ENDS_AT: UpdateContestInput.Patch
    ENVIRONMENT: UpdateContestInput.Patch
    FEATURED_UNTIL: UpdateContestInput.Patch
    FORMAT: UpdateContestInput.Patch
    JOIN_UNOFFICIALLY: UpdateContestInput.Patch
    KEY: UpdateContestInput.Patch
    LOGO_URL: UpdateContestInput.Patch
    NAME: UpdateContestInput.Patch
    PARTICIPANT_COUNT_HIDDEN: UpdateContestInput.Patch
    PARTICIPATION_MODE: UpdateContestInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_COUNT_HIDDEN: UpdateContestInput.Patch
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

class WatchContestInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class WatchContestOutput(_message.Message):
    __slots__ = ["contest"]
    CONTEST_FIELD_NUMBER: _ClassVar[int]
    contest: _contest_pb2.Contest
    def __init__(self, contest: _Optional[_Union[_contest_pb2.Contest, _Mapping]] = ...) -> None: ...
