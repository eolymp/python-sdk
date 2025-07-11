# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/judge/submission_service.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'eolymp/judge/submission_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.judge import submission_pb2 as eolymp_dot_judge_dot_submission__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%eolymp/judge/submission_service.proto\x12\x0c\x65olymp.judge\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\x1d\x65olymp/judge/submission.proto\x1a!eolymp/wellknown/expression.proto\"]\n\x15\x43reateSubmissionInput\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x12\n\nproblem_id\x18\x02 \x01(\t\x12\x0c\n\x04lang\x18\x03 \x01(\t\x12\x0e\n\x06source\x18\x04 \x01(\t\"/\n\x16\x43reateSubmissionOutput\x12\x15\n\rsubmission_id\x18\x01 \x01(\t\"\xa3\x05\n\x14ListSubmissionsInput\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\r\n\x05\x61\x66ter\x18\x0c \x01(\t\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12:\n\x07\x66ilters\x18( \x01(\x0b\x32).eolymp.judge.ListSubmissionsInput.Filter\x12.\n\x05\x65xtra\x18\xe3\x08 \x03(\x0e\x32\x1e.eolymp.judge.Submission.Extra\x1a\xdd\x03\n\x06\x46ilter\x12*\n\x02id\x18\x01 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x36\n\x0eparticipant_id\x18\x02 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x32\n\nproblem_id\x18\x03 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x30\n\x06status\x18\x04 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x12.\n\x04lang\x18\x05 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x12\x30\n\x05score\x18\x06 \x03(\x0b\x32!.eolymp.wellknown.ExpressionFloat\x12\x35\n\npercentage\x18\x07 \x03(\x0b\x32!.eolymp.wellknown.ExpressionFloat\x12;\n\x0csubmitted_at\x18\x08 \x03(\x0b\x32%.eolymp.wellknown.ExpressionTimestamp\x12\x33\n\tsignature\x18\t \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\"i\n\x15ListSubmissionsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12\'\n\x05items\x18\x02 \x03(\x0b\x32\x18.eolymp.judge.Submission\x12\x18\n\x10next_page_cursor\x18\x03 \x01(\t\"t\n\x17\x44\x65scribeSubmissionInput\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x15\n\rsubmission_id\x18\x02 \x01(\t\x12.\n\x05\x65xtra\x18\xe3\x08 \x03(\x0e\x32\x1e.eolymp.judge.Submission.Extra\"H\n\x18\x44\x65scribeSubmissionOutput\x12,\n\nsubmission\x18\x01 \x01(\x0b\x32\x18.eolymp.judge.Submission\"A\n\x14PrintSubmissionInput\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x15\n\rsubmission_id\x18\x02 \x01(\t\"\x17\n\x15PrintSubmissionOutput\"q\n\x14WatchSubmissionInput\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x15\n\rsubmission_id\x18\x02 \x01(\t\x12.\n\x05\x65xtra\x18\xe3\x08 \x03(\x0e\x32\x1e.eolymp.judge.Submission.Extra\"E\n\x15WatchSubmissionOutput\x12,\n\nsubmission\x18\x01 \x01(\x0b\x32\x18.eolymp.judge.Submission\"B\n\x15RetestSubmissionInput\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x15\n\rsubmission_id\x18\x02 \x01(\t\"\x18\n\x16RetestSubmissionOutput\"B\n\x15\x44\x65leteSubmissionInput\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x15\n\rsubmission_id\x18\x02 \x01(\t\"\x18\n\x16\x44\x65leteSubmissionOutput\"C\n\x16RestoreSubmissionInput\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x15\n\rsubmission_id\x18\x02 \x01(\t\"\x19\n\x17RestoreSubmissionOutput\"<\n\x12RetestProblemInput\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x12\n\nproblem_id\x18\x02 \x01(\t\"\x15\n\x13RetestProblemOutput\"/\n\x16\x41nalyzeSubmissionInput\x12\x15\n\rsubmission_id\x18\n \x01(\t\"\x19\n\x17\x41nalyzeSubmissionOutput2\xd1\r\n\x11SubmissionService\x12\xb9\x01\n\x10\x43reateSubmission\x12#.eolymp.judge.CreateSubmissionInput\x1a$.eolymp.judge.CreateSubmissionOutput\"Z\xea\xe2\n\x0b\xf5\xe2\n\n\xd7#>\xf8\xe2\n\n\x82\xe3\n\x1d\x8a\xe3\n\x19judge:contest:participate\x82\xd3\xe4\x93\x02$\"\"/problems/{problem_id}/submissions\x12\x99\x01\n\x0fListSubmissions\x12\".eolymp.judge.ListSubmissionsInput\x1a#.eolymp.judge.ListSubmissionsOutput\"=\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xe3\n\x16\x8a\xe3\n\x12judge:contest:read\x82\xd3\xe4\x93\x02\x0e\x12\x0c/submissions\x12\xb2\x01\n\x12\x44\x65scribeSubmission\x12%.eolymp.judge.DescribeSubmissionInput\x1a&.eolymp.judge.DescribeSubmissionOutput\"M\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xe3\n\x16\x8a\xe3\n\x12judge:contest:read\x82\xd3\xe4\x93\x02\x1e\x12\x1c/submissions/{submission_id}\x12\xaf\x01\n\x0fPrintSubmission\x12\".eolymp.judge.PrintSubmissionInput\x1a#.eolymp.judge.PrintSubmissionOutput\"S\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x02\x82\xe3\n\x16\x8a\xe3\n\x12judge:contest:read\x82\xd3\xe4\x93\x02$\"\"/submissions/{submission_id}/print\x12x\n\x0fWatchSubmission\x12\".eolymp.judge.WatchSubmissionInput\x1a#.eolymp.judge.WatchSubmissionOutput\"\x1a\x82\xe3\n\x16\x8a\xe3\n\x12judge:contest:read0\x01\x12\xb4\x01\n\x10RetestSubmission\x12#.eolymp.judge.RetestSubmissionInput\x1a$.eolymp.judge.RetestSubmissionOutput\"U\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\n2\x82\xe3\n\x17\x8a\xe3\n\x13judge:contest:write\x82\xd3\xe4\x93\x02%\"#/submissions/{submission_id}/retest\x12\xad\x01\n\x10\x44\x65leteSubmission\x12#.eolymp.judge.DeleteSubmissionInput\x1a$.eolymp.judge.DeleteSubmissionOutput\"N\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\n2\x82\xe3\n\x17\x8a\xe3\n\x13judge:contest:write\x82\xd3\xe4\x93\x02\x1e*\x1c/submissions/{submission_id}\x12\xb8\x01\n\x11RestoreSubmission\x12$.eolymp.judge.RestoreSubmissionInput\x1a%.eolymp.judge.RestoreSubmissionOutput\"V\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\n2\x82\xe3\n\x17\x8a\xe3\n\x13judge:contest:write\x82\xd3\xe4\x93\x02&\"$/submissions/{submission_id}/restore\x12\xa5\x01\n\rRetestProblem\x12 .eolymp.judge.RetestProblemInput\x1a!.eolymp.judge.RetestProblemOutput\"O\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xe3\n\x17\x8a\xe3\n\x13judge:contest:write\x82\xd3\xe4\x93\x02\x1f\x12\x1d/problems/{problem_id}/retest\x12\xb8\x01\n\x11\x41nalyzeSubmission\x12$.eolymp.judge.AnalyzeSubmissionInput\x1a%.eolymp.judge.AnalyzeSubmissionOutput\"V\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\n2\x82\xe3\n\x17\x8a\xe3\n\x13judge:contest:write\x82\xd3\xe4\x93\x02&\"$/submissions/{submission_id}/analyzeB-Z+github.com/eolymp/go-sdk/eolymp/judge;judgeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.judge.submission_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/judge;judge'
  _globals['_SUBMISSIONSERVICE'].methods_by_name['CreateSubmission']._loaded_options = None
  _globals['_SUBMISSIONSERVICE'].methods_by_name['CreateSubmission']._serialized_options = b'\352\342\n\013\365\342\n\n\327#>\370\342\n\n\202\343\n\035\212\343\n\031judge:contest:participate\202\323\344\223\002$\"\"/problems/{problem_id}/submissions'
  _globals['_SUBMISSIONSERVICE'].methods_by_name['ListSubmissions']._loaded_options = None
  _globals['_SUBMISSIONSERVICE'].methods_by_name['ListSubmissions']._serialized_options = b'\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\343\n\026\212\343\n\022judge:contest:read\202\323\344\223\002\016\022\014/submissions'
  _globals['_SUBMISSIONSERVICE'].methods_by_name['DescribeSubmission']._loaded_options = None
  _globals['_SUBMISSIONSERVICE'].methods_by_name['DescribeSubmission']._serialized_options = b'\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\343\n\026\212\343\n\022judge:contest:read\202\323\344\223\002\036\022\034/submissions/{submission_id}'
  _globals['_SUBMISSIONSERVICE'].methods_by_name['PrintSubmission']._loaded_options = None
  _globals['_SUBMISSIONSERVICE'].methods_by_name['PrintSubmission']._serialized_options = b'\352\342\n\013\365\342\n\000\000\200?\370\342\n\002\202\343\n\026\212\343\n\022judge:contest:read\202\323\344\223\002$\"\"/submissions/{submission_id}/print'
  _globals['_SUBMISSIONSERVICE'].methods_by_name['WatchSubmission']._loaded_options = None
  _globals['_SUBMISSIONSERVICE'].methods_by_name['WatchSubmission']._serialized_options = b'\202\343\n\026\212\343\n\022judge:contest:read'
  _globals['_SUBMISSIONSERVICE'].methods_by_name['RetestSubmission']._loaded_options = None
  _globals['_SUBMISSIONSERVICE'].methods_by_name['RetestSubmission']._serialized_options = b'\352\342\n\013\365\342\n\000\000 A\370\342\n2\202\343\n\027\212\343\n\023judge:contest:write\202\323\344\223\002%\"#/submissions/{submission_id}/retest'
  _globals['_SUBMISSIONSERVICE'].methods_by_name['DeleteSubmission']._loaded_options = None
  _globals['_SUBMISSIONSERVICE'].methods_by_name['DeleteSubmission']._serialized_options = b'\352\342\n\013\365\342\n\000\000 A\370\342\n2\202\343\n\027\212\343\n\023judge:contest:write\202\323\344\223\002\036*\034/submissions/{submission_id}'
  _globals['_SUBMISSIONSERVICE'].methods_by_name['RestoreSubmission']._loaded_options = None
  _globals['_SUBMISSIONSERVICE'].methods_by_name['RestoreSubmission']._serialized_options = b'\352\342\n\013\365\342\n\000\000 A\370\342\n2\202\343\n\027\212\343\n\023judge:contest:write\202\323\344\223\002&\"$/submissions/{submission_id}/restore'
  _globals['_SUBMISSIONSERVICE'].methods_by_name['RetestProblem']._loaded_options = None
  _globals['_SUBMISSIONSERVICE'].methods_by_name['RetestProblem']._serialized_options = b'\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\343\n\027\212\343\n\023judge:contest:write\202\323\344\223\002\037\022\035/problems/{problem_id}/retest'
  _globals['_SUBMISSIONSERVICE'].methods_by_name['AnalyzeSubmission']._loaded_options = None
  _globals['_SUBMISSIONSERVICE'].methods_by_name['AnalyzeSubmission']._serialized_options = b'\352\342\n\013\365\342\n\000\000 A\370\342\n2\202\343\n\027\212\343\n\023judge:contest:write\202\323\344\223\002&\"$/submissions/{submission_id}/analyze'
  _globals['_CREATESUBMISSIONINPUT']._serialized_start=220
  _globals['_CREATESUBMISSIONINPUT']._serialized_end=313
  _globals['_CREATESUBMISSIONOUTPUT']._serialized_start=315
  _globals['_CREATESUBMISSIONOUTPUT']._serialized_end=362
  _globals['_LISTSUBMISSIONSINPUT']._serialized_start=365
  _globals['_LISTSUBMISSIONSINPUT']._serialized_end=1040
  _globals['_LISTSUBMISSIONSINPUT_FILTER']._serialized_start=563
  _globals['_LISTSUBMISSIONSINPUT_FILTER']._serialized_end=1040
  _globals['_LISTSUBMISSIONSOUTPUT']._serialized_start=1042
  _globals['_LISTSUBMISSIONSOUTPUT']._serialized_end=1147
  _globals['_DESCRIBESUBMISSIONINPUT']._serialized_start=1149
  _globals['_DESCRIBESUBMISSIONINPUT']._serialized_end=1265
  _globals['_DESCRIBESUBMISSIONOUTPUT']._serialized_start=1267
  _globals['_DESCRIBESUBMISSIONOUTPUT']._serialized_end=1339
  _globals['_PRINTSUBMISSIONINPUT']._serialized_start=1341
  _globals['_PRINTSUBMISSIONINPUT']._serialized_end=1406
  _globals['_PRINTSUBMISSIONOUTPUT']._serialized_start=1408
  _globals['_PRINTSUBMISSIONOUTPUT']._serialized_end=1431
  _globals['_WATCHSUBMISSIONINPUT']._serialized_start=1433
  _globals['_WATCHSUBMISSIONINPUT']._serialized_end=1546
  _globals['_WATCHSUBMISSIONOUTPUT']._serialized_start=1548
  _globals['_WATCHSUBMISSIONOUTPUT']._serialized_end=1617
  _globals['_RETESTSUBMISSIONINPUT']._serialized_start=1619
  _globals['_RETESTSUBMISSIONINPUT']._serialized_end=1685
  _globals['_RETESTSUBMISSIONOUTPUT']._serialized_start=1687
  _globals['_RETESTSUBMISSIONOUTPUT']._serialized_end=1711
  _globals['_DELETESUBMISSIONINPUT']._serialized_start=1713
  _globals['_DELETESUBMISSIONINPUT']._serialized_end=1779
  _globals['_DELETESUBMISSIONOUTPUT']._serialized_start=1781
  _globals['_DELETESUBMISSIONOUTPUT']._serialized_end=1805
  _globals['_RESTORESUBMISSIONINPUT']._serialized_start=1807
  _globals['_RESTORESUBMISSIONINPUT']._serialized_end=1874
  _globals['_RESTORESUBMISSIONOUTPUT']._serialized_start=1876
  _globals['_RESTORESUBMISSIONOUTPUT']._serialized_end=1901
  _globals['_RETESTPROBLEMINPUT']._serialized_start=1903
  _globals['_RETESTPROBLEMINPUT']._serialized_end=1963
  _globals['_RETESTPROBLEMOUTPUT']._serialized_start=1965
  _globals['_RETESTPROBLEMOUTPUT']._serialized_end=1986
  _globals['_ANALYZESUBMISSIONINPUT']._serialized_start=1988
  _globals['_ANALYZESUBMISSIONINPUT']._serialized_end=2035
  _globals['_ANALYZESUBMISSIONOUTPUT']._serialized_start=2037
  _globals['_ANALYZESUBMISSIONOUTPUT']._serialized_end=2062
  _globals['_SUBMISSIONSERVICE']._serialized_start=2065
  _globals['_SUBMISSIONSERVICE']._serialized_end=3810
# @@protoc_insertion_point(module_scope)
