from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Problem(_message.Message):
    __slots__ = ("schema", "type", "topics", "difficulty", "constraints", "statements", "editorials", "attachments", "templates", "checker", "interactor", "validator", "scripts", "solutions", "testsets", "questions")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TYPE: _ClassVar[Problem.Type]
        PROGRAM: _ClassVar[Problem.Type]
        FUNCTION: _ClassVar[Problem.Type]
        OUTPUT: _ClassVar[Problem.Type]
        SQL: _ClassVar[Problem.Type]
        ML: _ClassVar[Problem.Type]
        QUIZ: _ClassVar[Problem.Type]
        INTERACTIVE: _ClassVar[Problem.Type]
        COMMUNICATION: _ClassVar[Problem.Type]
        WIDGET: _ClassVar[Problem.Type]
    UNKNOWN_TYPE: Problem.Type
    PROGRAM: Problem.Type
    FUNCTION: Problem.Type
    OUTPUT: Problem.Type
    SQL: Problem.Type
    ML: Problem.Type
    QUIZ: Problem.Type
    INTERACTIVE: Problem.Type
    COMMUNICATION: Problem.Type
    WIDGET: Problem.Type
    class Constraints(_message.Message):
        __slots__ = ("time_limit", "cpu_limit", "memory_limit", "run_count", "interactive_followup", "instance_limit", "interactor_time_limit")
        TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
        INTERACTIVE_FOLLOWUP_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_LIMIT_FIELD_NUMBER: _ClassVar[int]
        INTERACTOR_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        time_limit: int
        cpu_limit: int
        memory_limit: int
        run_count: int
        interactive_followup: bool
        instance_limit: int
        interactor_time_limit: int
        def __init__(self, time_limit: _Optional[int] = ..., cpu_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., run_count: _Optional[int] = ..., interactive_followup: _Optional[bool] = ..., instance_limit: _Optional[int] = ..., interactor_time_limit: _Optional[int] = ...) -> None: ...
    class File(_message.Message):
        __slots__ = ("path", "url")
        PATH_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        path: str
        url: str
        def __init__(self, path: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    class Statement(_message.Message):
        __slots__ = ("locale", "title", "content", "author", "source", "download_url", "draft", "automatic")
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        AUTHOR_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
        DRAFT_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        locale: str
        title: str
        content: _content_pb2.Content
        author: str
        source: str
        download_url: str
        draft: bool
        automatic: bool
        def __init__(self, locale: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., author: _Optional[str] = ..., source: _Optional[str] = ..., download_url: _Optional[str] = ..., draft: _Optional[bool] = ..., automatic: _Optional[bool] = ...) -> None: ...
    class Editorial(_message.Message):
        __slots__ = ("locale", "content", "download_url", "draft", "automatic")
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
        DRAFT_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        locale: str
        content: _content_pb2.Content
        download_url: str
        draft: bool
        automatic: bool
        def __init__(self, locale: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., download_url: _Optional[str] = ..., draft: _Optional[bool] = ..., automatic: _Optional[bool] = ...) -> None: ...
    class Attachment(_message.Message):
        __slots__ = ("name", "url", "content")
        NAME_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        name: str
        url: str
        content: str
        def __init__(self, name: _Optional[str] = ..., url: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
    class Template(_message.Message):
        __slots__ = ("runtime", "source", "header", "footer", "files")
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        HEADER_FIELD_NUMBER: _ClassVar[int]
        FOOTER_FIELD_NUMBER: _ClassVar[int]
        FILES_FIELD_NUMBER: _ClassVar[int]
        runtime: str
        source: str
        header: str
        footer: str
        files: _containers.RepeatedCompositeFieldContainer[Problem.File]
        def __init__(self, runtime: _Optional[str] = ..., source: _Optional[str] = ..., header: _Optional[str] = ..., footer: _Optional[str] = ..., files: _Optional[_Iterable[_Union[Problem.File, _Mapping]]] = ...) -> None: ...
    class Checker(_message.Message):
        __slots__ = ("tokens", "lines", "program", "query_results")
        class Tokens(_message.Message):
            __slots__ = ("precision", "case_sensitive")
            PRECISION_FIELD_NUMBER: _ClassVar[int]
            CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
            precision: int
            case_sensitive: bool
            def __init__(self, precision: _Optional[int] = ..., case_sensitive: _Optional[bool] = ...) -> None: ...
        class Lines(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Program(_message.Message):
            __slots__ = ("mode", "runtime", "source", "files")
            class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UNKNOWN_MODE: _ClassVar[Problem.Checker.Program.Mode]
                EOLYMP: _ClassVar[Problem.Checker.Program.Mode]
                TESTLIB: _ClassVar[Problem.Checker.Program.Mode]
                CMS: _ClassVar[Problem.Checker.Program.Mode]
                KATTIS: _ClassVar[Problem.Checker.Program.Mode]
            UNKNOWN_MODE: Problem.Checker.Program.Mode
            EOLYMP: Problem.Checker.Program.Mode
            TESTLIB: Problem.Checker.Program.Mode
            CMS: Problem.Checker.Program.Mode
            KATTIS: Problem.Checker.Program.Mode
            MODE_FIELD_NUMBER: _ClassVar[int]
            RUNTIME_FIELD_NUMBER: _ClassVar[int]
            SOURCE_FIELD_NUMBER: _ClassVar[int]
            FILES_FIELD_NUMBER: _ClassVar[int]
            mode: Problem.Checker.Program.Mode
            runtime: str
            source: str
            files: _containers.RepeatedCompositeFieldContainer[Problem.File]
            def __init__(self, mode: _Optional[_Union[Problem.Checker.Program.Mode, str]] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[Problem.File, _Mapping]]] = ...) -> None: ...
        class QueryResults(_message.Message):
            __slots__ = ("order_sensitive",)
            ORDER_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
            order_sensitive: bool
            def __init__(self, order_sensitive: _Optional[bool] = ...) -> None: ...
        TOKENS_FIELD_NUMBER: _ClassVar[int]
        LINES_FIELD_NUMBER: _ClassVar[int]
        PROGRAM_FIELD_NUMBER: _ClassVar[int]
        QUERY_RESULTS_FIELD_NUMBER: _ClassVar[int]
        tokens: Problem.Checker.Tokens
        lines: Problem.Checker.Lines
        program: Problem.Checker.Program
        query_results: Problem.Checker.QueryResults
        def __init__(self, tokens: _Optional[_Union[Problem.Checker.Tokens, _Mapping]] = ..., lines: _Optional[_Union[Problem.Checker.Lines, _Mapping]] = ..., program: _Optional[_Union[Problem.Checker.Program, _Mapping]] = ..., query_results: _Optional[_Union[Problem.Checker.QueryResults, _Mapping]] = ...) -> None: ...
    class Interactor(_message.Message):
        __slots__ = ("runtime", "source", "files")
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        FILES_FIELD_NUMBER: _ClassVar[int]
        runtime: str
        source: str
        files: _containers.RepeatedCompositeFieldContainer[Problem.File]
        def __init__(self, runtime: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[Problem.File, _Mapping]]] = ...) -> None: ...
    class Validator(_message.Message):
        __slots__ = ("runtime", "source", "files")
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        FILES_FIELD_NUMBER: _ClassVar[int]
        runtime: str
        source: str
        files: _containers.RepeatedCompositeFieldContainer[Problem.File]
        def __init__(self, runtime: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[Problem.File, _Mapping]]] = ...) -> None: ...
    class Script(_message.Message):
        __slots__ = ("name", "runtime", "source", "files")
        NAME_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        FILES_FIELD_NUMBER: _ClassVar[int]
        name: str
        runtime: str
        source: str
        files: _containers.RepeatedCompositeFieldContainer[Problem.File]
        def __init__(self, name: _Optional[str] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[Problem.File, _Mapping]]] = ...) -> None: ...
    class Solution(_message.Message):
        __slots__ = ("name", "outcome", "runtime", "source")
        class Outcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_OUTCOME: _ClassVar[Problem.Solution.Outcome]
            CORRECT: _ClassVar[Problem.Solution.Outcome]
            INCORRECT: _ClassVar[Problem.Solution.Outcome]
            WRONG_ANSWER: _ClassVar[Problem.Solution.Outcome]
            TIMEOUT: _ClassVar[Problem.Solution.Outcome]
            OVERFLOW: _ClassVar[Problem.Solution.Outcome]
            TIMEOUT_OR_ACCEPTED: _ClassVar[Problem.Solution.Outcome]
            OVERFLOW_OR_ACCEPTED: _ClassVar[Problem.Solution.Outcome]
            DONT_RUN: _ClassVar[Problem.Solution.Outcome]
            FAILURE: _ClassVar[Problem.Solution.Outcome]
        UNKNOWN_OUTCOME: Problem.Solution.Outcome
        CORRECT: Problem.Solution.Outcome
        INCORRECT: Problem.Solution.Outcome
        WRONG_ANSWER: Problem.Solution.Outcome
        TIMEOUT: Problem.Solution.Outcome
        OVERFLOW: Problem.Solution.Outcome
        TIMEOUT_OR_ACCEPTED: Problem.Solution.Outcome
        OVERFLOW_OR_ACCEPTED: Problem.Solution.Outcome
        DONT_RUN: Problem.Solution.Outcome
        FAILURE: Problem.Solution.Outcome
        NAME_FIELD_NUMBER: _ClassVar[int]
        OUTCOME_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        name: str
        outcome: Problem.Solution.Outcome
        runtime: str
        source: str
        def __init__(self, name: _Optional[str] = ..., outcome: _Optional[_Union[Problem.Solution.Outcome, str]] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...
    class Testset(_message.Message):
        __slots__ = ("index", "time_limit", "cpu_limit", "memory_limit", "file_size_limit", "scoring", "feedback", "dependencies", "dependency", "tests")
        class Scoring(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_SCORING: _ClassVar[Problem.Testset.Scoring]
            EACH: _ClassVar[Problem.Testset.Scoring]
            ALL: _ClassVar[Problem.Testset.Scoring]
            WORST: _ClassVar[Problem.Testset.Scoring]
            BEST: _ClassVar[Problem.Testset.Scoring]
            NO_SCORE: _ClassVar[Problem.Testset.Scoring]
        UNKNOWN_SCORING: Problem.Testset.Scoring
        EACH: Problem.Testset.Scoring
        ALL: Problem.Testset.Scoring
        WORST: Problem.Testset.Scoring
        BEST: Problem.Testset.Scoring
        NO_SCORE: Problem.Testset.Scoring
        class Feedback(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FEEDBACK: _ClassVar[Problem.Testset.Feedback]
            ICPC: _ClassVar[Problem.Testset.Feedback]
            ICPC_EXPANDED: _ClassVar[Problem.Testset.Feedback]
            COMPLETE: _ClassVar[Problem.Testset.Feedback]
        UNKNOWN_FEEDBACK: Problem.Testset.Feedback
        ICPC: Problem.Testset.Feedback
        ICPC_EXPANDED: Problem.Testset.Feedback
        COMPLETE: Problem.Testset.Feedback
        class Dependency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_DEPENDENCY: _ClassVar[Problem.Testset.Dependency]
            FULLY_ACCEPTED: _ClassVar[Problem.Testset.Dependency]
            FIRST_POINT: _ClassVar[Problem.Testset.Dependency]
        UNKNOWN_DEPENDENCY: Problem.Testset.Dependency
        FULLY_ACCEPTED: Problem.Testset.Dependency
        FIRST_POINT: Problem.Testset.Dependency
        class Test(_message.Message):
            __slots__ = ("index", "example", "inactive", "score", "input_url", "input_content", "input_generator", "answer_url", "answer_content", "answer_generator", "example_input_url", "example_input_content", "example_answer_url", "example_answer_content", "generated_input_url", "generated_answer_url")
            class Generator(_message.Message):
                __slots__ = ("script", "arguments")
                SCRIPT_FIELD_NUMBER: _ClassVar[int]
                ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
                script: str
                arguments: _containers.RepeatedScalarFieldContainer[str]
                def __init__(self, script: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ...) -> None: ...
            INDEX_FIELD_NUMBER: _ClassVar[int]
            EXAMPLE_FIELD_NUMBER: _ClassVar[int]
            INACTIVE_FIELD_NUMBER: _ClassVar[int]
            SCORE_FIELD_NUMBER: _ClassVar[int]
            INPUT_URL_FIELD_NUMBER: _ClassVar[int]
            INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
            INPUT_GENERATOR_FIELD_NUMBER: _ClassVar[int]
            ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
            ANSWER_CONTENT_FIELD_NUMBER: _ClassVar[int]
            ANSWER_GENERATOR_FIELD_NUMBER: _ClassVar[int]
            EXAMPLE_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
            EXAMPLE_INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
            EXAMPLE_ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
            EXAMPLE_ANSWER_CONTENT_FIELD_NUMBER: _ClassVar[int]
            GENERATED_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
            GENERATED_ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
            index: int
            example: bool
            inactive: bool
            score: float
            input_url: str
            input_content: str
            input_generator: Problem.Testset.Test.Generator
            answer_url: str
            answer_content: str
            answer_generator: Problem.Testset.Test.Generator
            example_input_url: str
            example_input_content: str
            example_answer_url: str
            example_answer_content: str
            generated_input_url: str
            generated_answer_url: str
            def __init__(self, index: _Optional[int] = ..., example: _Optional[bool] = ..., inactive: _Optional[bool] = ..., score: _Optional[float] = ..., input_url: _Optional[str] = ..., input_content: _Optional[str] = ..., input_generator: _Optional[_Union[Problem.Testset.Test.Generator, _Mapping]] = ..., answer_url: _Optional[str] = ..., answer_content: _Optional[str] = ..., answer_generator: _Optional[_Union[Problem.Testset.Test.Generator, _Mapping]] = ..., example_input_url: _Optional[str] = ..., example_input_content: _Optional[str] = ..., example_answer_url: _Optional[str] = ..., example_answer_content: _Optional[str] = ..., generated_input_url: _Optional[str] = ..., generated_answer_url: _Optional[str] = ...) -> None: ...
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
        SCORING_FIELD_NUMBER: _ClassVar[int]
        FEEDBACK_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
        TESTS_FIELD_NUMBER: _ClassVar[int]
        index: int
        time_limit: int
        cpu_limit: int
        memory_limit: int
        file_size_limit: int
        scoring: Problem.Testset.Scoring
        feedback: Problem.Testset.Feedback
        dependencies: _containers.RepeatedScalarFieldContainer[int]
        dependency: Problem.Testset.Dependency
        tests: _containers.RepeatedCompositeFieldContainer[Problem.Testset.Test]
        def __init__(self, index: _Optional[int] = ..., time_limit: _Optional[int] = ..., cpu_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., file_size_limit: _Optional[int] = ..., scoring: _Optional[_Union[Problem.Testset.Scoring, str]] = ..., feedback: _Optional[_Union[Problem.Testset.Feedback, str]] = ..., dependencies: _Optional[_Iterable[int]] = ..., dependency: _Optional[_Union[Problem.Testset.Dependency, str]] = ..., tests: _Optional[_Iterable[_Union[Problem.Testset.Test, _Mapping]]] = ...) -> None: ...
    class Question(_message.Message):
        __slots__ = ("index", "type", "content", "score", "multiple", "options", "answers")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_TYPE: _ClassVar[Problem.Question.Type]
            CHOICE: _ClassVar[Problem.Question.Type]
            TEXT: _ClassVar[Problem.Question.Type]
        UNKNOWN_TYPE: Problem.Question.Type
        CHOICE: Problem.Question.Type
        TEXT: Problem.Question.Type
        class Option(_message.Message):
            __slots__ = ("index", "content", "correct")
            INDEX_FIELD_NUMBER: _ClassVar[int]
            CONTENT_FIELD_NUMBER: _ClassVar[int]
            CORRECT_FIELD_NUMBER: _ClassVar[int]
            index: int
            content: _content_pb2.Content
            correct: bool
            def __init__(self, index: _Optional[int] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., correct: _Optional[bool] = ...) -> None: ...
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        MULTIPLE_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        ANSWERS_FIELD_NUMBER: _ClassVar[int]
        index: int
        type: Problem.Question.Type
        content: _content_pb2.Content
        score: float
        multiple: bool
        options: _containers.RepeatedCompositeFieldContainer[Problem.Question.Option]
        answers: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, index: _Optional[int] = ..., type: _Optional[_Union[Problem.Question.Type, str]] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., score: _Optional[float] = ..., multiple: _Optional[bool] = ..., options: _Optional[_Iterable[_Union[Problem.Question.Option, _Mapping]]] = ..., answers: _Optional[_Iterable[str]] = ...) -> None: ...
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    EDITORIALS_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    CHECKER_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    SOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    TESTSETS_FIELD_NUMBER: _ClassVar[int]
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    schema: str
    type: Problem.Type
    topics: _containers.RepeatedScalarFieldContainer[str]
    difficulty: int
    constraints: Problem.Constraints
    statements: _containers.RepeatedCompositeFieldContainer[Problem.Statement]
    editorials: _containers.RepeatedCompositeFieldContainer[Problem.Editorial]
    attachments: _containers.RepeatedCompositeFieldContainer[Problem.Attachment]
    templates: _containers.RepeatedCompositeFieldContainer[Problem.Template]
    checker: Problem.Checker
    interactor: Problem.Interactor
    validator: Problem.Validator
    scripts: _containers.RepeatedCompositeFieldContainer[Problem.Script]
    solutions: _containers.RepeatedCompositeFieldContainer[Problem.Solution]
    testsets: _containers.RepeatedCompositeFieldContainer[Problem.Testset]
    questions: _containers.RepeatedCompositeFieldContainer[Problem.Question]
    def __init__(self, schema: _Optional[str] = ..., type: _Optional[_Union[Problem.Type, str]] = ..., topics: _Optional[_Iterable[str]] = ..., difficulty: _Optional[int] = ..., constraints: _Optional[_Union[Problem.Constraints, _Mapping]] = ..., statements: _Optional[_Iterable[_Union[Problem.Statement, _Mapping]]] = ..., editorials: _Optional[_Iterable[_Union[Problem.Editorial, _Mapping]]] = ..., attachments: _Optional[_Iterable[_Union[Problem.Attachment, _Mapping]]] = ..., templates: _Optional[_Iterable[_Union[Problem.Template, _Mapping]]] = ..., checker: _Optional[_Union[Problem.Checker, _Mapping]] = ..., interactor: _Optional[_Union[Problem.Interactor, _Mapping]] = ..., validator: _Optional[_Union[Problem.Validator, _Mapping]] = ..., scripts: _Optional[_Iterable[_Union[Problem.Script, _Mapping]]] = ..., solutions: _Optional[_Iterable[_Union[Problem.Solution, _Mapping]]] = ..., testsets: _Optional[_Iterable[_Union[Problem.Testset, _Mapping]]] = ..., questions: _Optional[_Iterable[_Union[Problem.Question, _Mapping]]] = ...) -> None: ...
