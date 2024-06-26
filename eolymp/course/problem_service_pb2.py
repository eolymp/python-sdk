# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/course/problem_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.atlas import code_template_pb2 as eolymp_dot_atlas_dot_code__template__pb2
from eolymp.atlas import statement_pb2 as eolymp_dot_atlas_dot_statement__pb2
from eolymp.atlas import submission_pb2 as eolymp_dot_atlas_dot_submission__pb2
from eolymp.atlas import testing_test_pb2 as eolymp_dot_atlas_dot_testing__test__pb2
from eolymp.playground import run_pb2 as eolymp_dot_playground_dot_run__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#eolymp/course/problem_service.proto\x12\reolymp.course\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a eolymp/atlas/code_template.proto\x1a\x1c\x65olymp/atlas/statement.proto\x1a\x1d\x65olymp/atlas/submission.proto\x1a\x1f\x65olymp/atlas/testing_test.proto\x1a\x1b\x65olymp/playground/run.proto\x1a!eolymp/wellknown/expression.proto\"\x15\n\x13ListStatementsInput\"M\n\x14ListStatementsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.eolymp.atlas.Statement\"\x13\n\x11ListExamplesInput\":\n\x12ListExamplesOutput\x12$\n\x08\x65xamples\x18\x02 \x03(\x0b\x32\x12.eolymp.atlas.Test\"L\n\x15\x43reateSubmissionInput\x12\x12\n\nproblem_id\x18\x01 \x01(\t\x12\x0f\n\x07runtime\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\"/\n\x16\x43reateSubmissionOutput\x12\x15\n\rsubmission_id\x18\x01 \x01(\t\"\x97\x04\n\x14ListSubmissionsInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12;\n\x07\x66ilters\x18( \x01(\x0b\x32*.eolymp.course.ListSubmissionsInput.Filter\x1a\xa3\x03\n\x06\x46ilter\x12*\n\x02id\x18\x01 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12/\n\x07user_id\x18\x03 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x31\n\tmember_id\x18\t \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12;\n\x0csubmitted_at\x18\x04 \x03(\x0b\x32%.eolymp.wellknown.ExpressionTimestamp\x12\x31\n\x07runtime\x18\x05 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x12\x30\n\x06status\x18\x06 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x12\x30\n\x05score\x18\x07 \x03(\x0b\x32!.eolymp.wellknown.ExpressionFloat\x12\x35\n\npercentage\x18\x08 \x03(\x0b\x32!.eolymp.wellknown.ExpressionFloat\"O\n\x15ListSubmissionsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12\'\n\x05items\x18\x02 \x03(\x0b\x32\x18.eolymp.atlas.Submission\"D\n\x17\x44\x65scribeSubmissionInput\x12\x12\n\nproblem_id\x18\x01 \x01(\t\x12\x15\n\rsubmission_id\x18\x02 \x01(\t\"H\n\x18\x44\x65scribeSubmissionOutput\x12,\n\nsubmission\x18\x01 \x01(\x0b\x32\x18.eolymp.atlas.Submission\"A\n\x14WatchSubmissionInput\x12\x12\n\nproblem_id\x18\x01 \x01(\t\x12\x15\n\rsubmission_id\x18\x02 \x01(\t\"E\n\x15WatchSubmissionOutput\x12,\n\nsubmission\x18\x01 \x01(\x0b\x32\x18.eolymp.atlas.Submission\"*\n\x17LookupCodeTemplateInput\x12\x0f\n\x07runtime\x18\x01 \x01(\t\"D\n\x18LookupCodeTemplateOutput\x12(\n\x08template\x18\x01 \x01(\x0b\x32\x16.eolymp.atlas.Template\"e\n\x0e\x43reateRunInput\x12\x0f\n\x07runtime\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x64 \x01(\t\x12\x14\n\ninput_data\x18\x65 \x01(\x0cH\x00\x12\x13\n\tinput_ref\x18\x66 \x01(\tH\x00\x42\x07\n\x05input\"!\n\x0f\x43reateRunOutput\x12\x0e\n\x06run_id\x18\x01 \x01(\t\"\"\n\x10\x44\x65scribeRunInput\x12\x0e\n\x06run_id\x18\x01 \x01(\t\"8\n\x11\x44\x65scribeRunOutput\x12#\n\x03run\x18\x01 \x01(\x0b\x32\x16.eolymp.playground.Run\"\x1f\n\rWatchRunInput\x12\x0e\n\x06run_id\x18\x01 \x01(\t\"5\n\x0eWatchRunOutput\x12#\n\x03run\x18\x01 \x01(\x0b\x32\x16.eolymp.playground.Run2\x84\x0c\n\x0eProblemService\x12\x97\x01\n\x0eListStatements\x12\".eolymp.course.ListStatementsInput\x1a#.eolymp.course.ListStatementsOutput\"<\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\r\x12\x0b/statements\x12\x8f\x01\n\x0cListExamples\x12 .eolymp.course.ListExamplesInput\x1a!.eolymp.course.ListExamplesOutput\":\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x0b\x12\t/examples\x12\xa0\x01\n\x10\x43reateSubmission\x12$.eolymp.course.CreateSubmissionInput\x1a%.eolymp.course.CreateSubmissionOutput\"?\x82\xe3\n\x18\x8a\xe3\n\x14\x63ourse:course:submit\xea\xe2\n\x0b\xf5\xe2\n\n\xd7#>\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x0e\"\x0c/submissions\x12\x9b\x01\n\x0fListSubmissions\x12#.eolymp.course.ListSubmissionsInput\x1a$.eolymp.course.ListSubmissionsOutput\"=\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x0e\x12\x0c/submissions\x12\xb4\x01\n\x12\x44\x65scribeSubmission\x12&.eolymp.course.DescribeSubmissionInput\x1a\'.eolymp.course.DescribeSubmissionOutput\"M\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x1e\x12\x1c/submissions/{submission_id}\x12z\n\x0fWatchSubmission\x12#.eolymp.course.WatchSubmissionInput\x1a$.eolymp.course.WatchSubmissionOutput\"\x1a\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read0\x01\x12\xa1\x01\n\x12LookupCodeTemplate\x12&.eolymp.course.LookupCodeTemplateInput\x1a\'.eolymp.course.LookupCodeTemplateOutput\":\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x0b\x12\t/template\x12\x84\x01\n\tCreateRun\x12\x1d.eolymp.course.CreateRunInput\x1a\x1e.eolymp.course.CreateRunOutput\"8\x82\xe3\n\x18\x8a\xe3\n\x14playground:run:write\xea\xe2\n\x0b\xf5\xe2\n\n\xd7#>\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x07\"\x05/runs\x12\x92\x01\n\x0b\x44\x65scribeRun\x12\x1f.eolymp.course.DescribeRunInput\x1a .eolymp.course.DescribeRunOutput\"@\x82\xe3\n\x17\x8a\xe3\n\x13playground:run:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x10\x12\x0e/runs/{run_id}\x12\x91\x01\n\x08WatchRun\x12\x1c.eolymp.course.WatchRunInput\x1a\x1d.eolymp.course.WatchRunOutput\"F\x82\xe3\n\x17\x8a\xe3\n\x13playground:run:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x16\x12\x14/runs/{run_id}/watch0\x01\x42/Z-github.com/eolymp/go-sdk/eolymp/course;courseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.course.problem_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/eolymp/go-sdk/eolymp/course;course'
  _PROBLEMSERVICE.methods_by_name['ListStatements']._options = None
  _PROBLEMSERVICE.methods_by_name['ListStatements']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\r\022\013/statements'
  _PROBLEMSERVICE.methods_by_name['ListExamples']._options = None
  _PROBLEMSERVICE.methods_by_name['ListExamples']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\013\022\t/examples'
  _PROBLEMSERVICE.methods_by_name['CreateSubmission']._options = None
  _PROBLEMSERVICE.methods_by_name['CreateSubmission']._serialized_options = b'\202\343\n\030\212\343\n\024course:course:submit\352\342\n\013\365\342\n\n\327#>\370\342\n\n\202\323\344\223\002\016\"\014/submissions'
  _PROBLEMSERVICE.methods_by_name['ListSubmissions']._options = None
  _PROBLEMSERVICE.methods_by_name['ListSubmissions']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\016\022\014/submissions'
  _PROBLEMSERVICE.methods_by_name['DescribeSubmission']._options = None
  _PROBLEMSERVICE.methods_by_name['DescribeSubmission']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\036\022\034/submissions/{submission_id}'
  _PROBLEMSERVICE.methods_by_name['WatchSubmission']._options = None
  _PROBLEMSERVICE.methods_by_name['WatchSubmission']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read'
  _PROBLEMSERVICE.methods_by_name['LookupCodeTemplate']._options = None
  _PROBLEMSERVICE.methods_by_name['LookupCodeTemplate']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\013\022\t/template'
  _PROBLEMSERVICE.methods_by_name['CreateRun']._options = None
  _PROBLEMSERVICE.methods_by_name['CreateRun']._serialized_options = b'\202\343\n\030\212\343\n\024playground:run:write\352\342\n\013\365\342\n\n\327#>\370\342\n\005\202\323\344\223\002\007\"\005/runs'
  _PROBLEMSERVICE.methods_by_name['DescribeRun']._options = None
  _PROBLEMSERVICE.methods_by_name['DescribeRun']._serialized_options = b'\202\343\n\027\212\343\n\023playground:run:read\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\020\022\016/runs/{run_id}'
  _PROBLEMSERVICE.methods_by_name['WatchRun']._options = None
  _PROBLEMSERVICE.methods_by_name['WatchRun']._serialized_options = b'\202\343\n\027\212\343\n\023playground:run:read\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\026\022\024/runs/{run_id}/watch'
  _LISTSTATEMENTSINPUT._serialized_start=345
  _LISTSTATEMENTSINPUT._serialized_end=366
  _LISTSTATEMENTSOUTPUT._serialized_start=368
  _LISTSTATEMENTSOUTPUT._serialized_end=445
  _LISTEXAMPLESINPUT._serialized_start=447
  _LISTEXAMPLESINPUT._serialized_end=466
  _LISTEXAMPLESOUTPUT._serialized_start=468
  _LISTEXAMPLESOUTPUT._serialized_end=526
  _CREATESUBMISSIONINPUT._serialized_start=528
  _CREATESUBMISSIONINPUT._serialized_end=604
  _CREATESUBMISSIONOUTPUT._serialized_start=606
  _CREATESUBMISSIONOUTPUT._serialized_end=653
  _LISTSUBMISSIONSINPUT._serialized_start=656
  _LISTSUBMISSIONSINPUT._serialized_end=1191
  _LISTSUBMISSIONSINPUT_FILTER._serialized_start=772
  _LISTSUBMISSIONSINPUT_FILTER._serialized_end=1191
  _LISTSUBMISSIONSOUTPUT._serialized_start=1193
  _LISTSUBMISSIONSOUTPUT._serialized_end=1272
  _DESCRIBESUBMISSIONINPUT._serialized_start=1274
  _DESCRIBESUBMISSIONINPUT._serialized_end=1342
  _DESCRIBESUBMISSIONOUTPUT._serialized_start=1344
  _DESCRIBESUBMISSIONOUTPUT._serialized_end=1416
  _WATCHSUBMISSIONINPUT._serialized_start=1418
  _WATCHSUBMISSIONINPUT._serialized_end=1483
  _WATCHSUBMISSIONOUTPUT._serialized_start=1485
  _WATCHSUBMISSIONOUTPUT._serialized_end=1554
  _LOOKUPCODETEMPLATEINPUT._serialized_start=1556
  _LOOKUPCODETEMPLATEINPUT._serialized_end=1598
  _LOOKUPCODETEMPLATEOUTPUT._serialized_start=1600
  _LOOKUPCODETEMPLATEOUTPUT._serialized_end=1668
  _CREATERUNINPUT._serialized_start=1670
  _CREATERUNINPUT._serialized_end=1771
  _CREATERUNOUTPUT._serialized_start=1773
  _CREATERUNOUTPUT._serialized_end=1806
  _DESCRIBERUNINPUT._serialized_start=1808
  _DESCRIBERUNINPUT._serialized_end=1842
  _DESCRIBERUNOUTPUT._serialized_start=1844
  _DESCRIBERUNOUTPUT._serialized_end=1900
  _WATCHRUNINPUT._serialized_start=1902
  _WATCHRUNINPUT._serialized_end=1933
  _WATCHRUNOUTPUT._serialized_start=1935
  _WATCHRUNOUTPUT._serialized_end=1988
  _PROBLEMSERVICE._serialized_start=1991
  _PROBLEMSERVICE._serialized_end=3531
# @@protoc_insertion_point(module_scope)
