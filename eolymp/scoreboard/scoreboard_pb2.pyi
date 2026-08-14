from eolymp.community import attribute_pb2 as _attribute_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Scoreboard(_message.Message):
    __slots__ = ("id", "slug", "name", "best_of", "modes", "contests", "attributes")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_MODE: _ClassVar[Scoreboard.Mode]
        MAIN: _ClassVar[Scoreboard.Mode]
        FROZEN: _ClassVar[Scoreboard.Mode]
        UPSOLVE: _ClassVar[Scoreboard.Mode]
    UNKNOWN_MODE: Scoreboard.Mode
    MAIN: Scoreboard.Mode
    FROZEN: Scoreboard.Mode
    UPSOLVE: Scoreboard.Mode
    class Contest(_message.Message):
        __slots__ = ("contest_id", "index", "name", "image_url", "problems")
        CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        PROBLEMS_FIELD_NUMBER: _ClassVar[int]
        contest_id: str
        index: int
        name: str
        image_url: str
        problems: _containers.RepeatedCompositeFieldContainer[Scoreboard.Problem]
        def __init__(self, contest_id: _Optional[str] = ..., index: _Optional[int] = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., problems: _Optional[_Iterable[_Union[Scoreboard.Problem, _Mapping]]] = ...) -> None: ...
    class Problem(_message.Message):
        __slots__ = ("problem_id", "index", "title")
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        problem_id: str
        index: int
        title: str
        def __init__(self, problem_id: _Optional[str] = ..., index: _Optional[int] = ..., title: _Optional[str] = ...) -> None: ...
    class Attribute(_message.Message):
        __slots__ = ("attribute_key", "index", "label", "type")
        ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        attribute_key: str
        index: int
        label: str
        type: _attribute_pb2.Attribute.Type
        def __init__(self, attribute_key: _Optional[str] = ..., index: _Optional[int] = ..., label: _Optional[str] = ..., type: _Optional[_Union[_attribute_pb2.Attribute.Type, str]] = ...) -> None: ...
    class Patch(_message.Message):
        __slots__ = ("slug", "name", "best_of")
        SLUG_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        BEST_OF_FIELD_NUMBER: _ClassVar[int]
        slug: str
        name: str
        best_of: int
        def __init__(self, slug: _Optional[str] = ..., name: _Optional[str] = ..., best_of: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BEST_OF_FIELD_NUMBER: _ClassVar[int]
    MODES_FIELD_NUMBER: _ClassVar[int]
    CONTESTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    slug: str
    name: str
    best_of: int
    modes: _containers.RepeatedScalarFieldContainer[Scoreboard.Mode]
    contests: _containers.RepeatedCompositeFieldContainer[Scoreboard.Contest]
    attributes: _containers.RepeatedCompositeFieldContainer[Scoreboard.Attribute]
    def __init__(self, id: _Optional[str] = ..., slug: _Optional[str] = ..., name: _Optional[str] = ..., best_of: _Optional[int] = ..., modes: _Optional[_Iterable[_Union[Scoreboard.Mode, str]]] = ..., contests: _Optional[_Iterable[_Union[Scoreboard.Contest, _Mapping]]] = ..., attributes: _Optional[_Iterable[_Union[Scoreboard.Attribute, _Mapping]]] = ...) -> None: ...

class Row(_message.Message):
    __slots__ = ("member_id", "display_name", "index", "rank", "rank_length", "rank_all", "rank_all_length", "score", "penalty", "unofficial", "disqualified", "contests", "attributes")
    class ProblemScore(_message.Message):
        __slots__ = ("problem_id", "score", "penalty", "percentage", "attempts", "time", "pending", "changed", "first_to_solve")
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        PENDING_FIELD_NUMBER: _ClassVar[int]
        CHANGED_FIELD_NUMBER: _ClassVar[int]
        FIRST_TO_SOLVE_FIELD_NUMBER: _ClassVar[int]
        problem_id: str
        score: float
        penalty: float
        percentage: float
        attempts: int
        time: int
        pending: int
        changed: bool
        first_to_solve: bool
        def __init__(self, problem_id: _Optional[str] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., percentage: _Optional[float] = ..., attempts: _Optional[int] = ..., time: _Optional[int] = ..., pending: _Optional[int] = ..., changed: _Optional[bool] = ..., first_to_solve: _Optional[bool] = ...) -> None: ...
    class ContestScore(_message.Message):
        __slots__ = ("contest_id", "score", "penalty", "counted", "frozen", "problems")
        CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        COUNTED_FIELD_NUMBER: _ClassVar[int]
        FROZEN_FIELD_NUMBER: _ClassVar[int]
        PROBLEMS_FIELD_NUMBER: _ClassVar[int]
        contest_id: str
        score: float
        penalty: float
        counted: bool
        frozen: bool
        problems: _containers.RepeatedCompositeFieldContainer[Row.ProblemScore]
        def __init__(self, contest_id: _Optional[str] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., counted: _Optional[bool] = ..., frozen: _Optional[bool] = ..., problems: _Optional[_Iterable[_Union[Row.ProblemScore, _Mapping]]] = ...) -> None: ...
    class AttributeValue(_message.Message):
        __slots__ = ("attribute_key", "string", "number")
        ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
        STRING_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        attribute_key: str
        string: str
        number: int
        def __init__(self, attribute_key: _Optional[str] = ..., string: _Optional[str] = ..., number: _Optional[int] = ...) -> None: ...
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    RANK_LENGTH_FIELD_NUMBER: _ClassVar[int]
    RANK_ALL_FIELD_NUMBER: _ClassVar[int]
    RANK_ALL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    PENALTY_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
    CONTESTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    display_name: str
    index: int
    rank: int
    rank_length: int
    rank_all: int
    rank_all_length: int
    score: float
    penalty: float
    unofficial: bool
    disqualified: bool
    contests: _containers.RepeatedCompositeFieldContainer[Row.ContestScore]
    attributes: _containers.RepeatedCompositeFieldContainer[Row.AttributeValue]
    def __init__(self, member_id: _Optional[str] = ..., display_name: _Optional[str] = ..., index: _Optional[int] = ..., rank: _Optional[int] = ..., rank_length: _Optional[int] = ..., rank_all: _Optional[int] = ..., rank_all_length: _Optional[int] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., unofficial: _Optional[bool] = ..., disqualified: _Optional[bool] = ..., contests: _Optional[_Iterable[_Union[Row.ContestScore, _Mapping]]] = ..., attributes: _Optional[_Iterable[_Union[Row.AttributeValue, _Mapping]]] = ...) -> None: ...
