# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/atlas/testing_service.proto
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
from eolymp.atlas import atlas_pb2 as eolymp_dot_atlas_dot_atlas__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"eolymp/atlas/testing_service.proto\x12\x0c\x65olymp.atlas\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\x18\x65olymp/atlas/atlas.proto2\xde\x12\n\x0eTestingService\x12\x93\x01\n\rUpdateChecker\x12!.eolymp.atlas.UpdateVerifierInput\x1a\".eolymp.atlas.UpdateVerifierOutput\";\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\n\xd7#>\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x0b\x1a\t/verifier\x12\x99\x01\n\x0f\x44\x65scribeChecker\x12#.eolymp.atlas.DescribeVerifierInput\x1a$.eolymp.atlas.DescribeVerifierOutput\";\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x0b\x12\t/verifier\x12\x9c\x01\n\x10UpdateInteractor\x12#.eolymp.atlas.UpdateInteractorInput\x1a$.eolymp.atlas.UpdateInteractorOutput\"=\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\n\xd7#>\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\r\x1a\x0b/interactor\x12\xa2\x01\n\x12\x44\x65scribeInteractor\x12%.eolymp.atlas.DescribeInteractorInput\x1a&.eolymp.atlas.DescribeInteractorOutput\"=\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\r\x12\x0b/interactor\x12\x91\x01\n\rCreateTestset\x12 .eolymp.atlas.CreateTestsetInput\x1a!.eolymp.atlas.CreateTestsetOutput\";\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n2\x82\xd3\xe4\x93\x02\x0b\"\t/testsets\x12\x9e\x01\n\rUpdateTestset\x12 .eolymp.atlas.UpdateTestsetInput\x1a!.eolymp.atlas.UpdateTestsetOutput\"H\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n2\x82\xd3\xe4\x93\x02\x18\x1a\x16/testsets/{testset_id}\x12\x9e\x01\n\rDeleteTestset\x12 .eolymp.atlas.DeleteTestsetInput\x1a!.eolymp.atlas.DeleteTestsetOutput\"H\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n2\x82\xd3\xe4\x93\x02\x18*\x16/testsets/{testset_id}\x12\xa4\x01\n\x0f\x44\x65scribeTestset\x12\".eolymp.atlas.DescribeTestsetInput\x1a#.eolymp.atlas.DescribeTestsetOutput\"H\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\n2\x82\xd3\xe4\x93\x02\x18\x12\x16/testsets/{testset_id}\x12\x8e\x01\n\x0cListTestsets\x12\x1f.eolymp.atlas.ListTestsetsInput\x1a .eolymp.atlas.ListTestsetsOutput\";\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\n2\x82\xd3\xe4\x93\x02\x0b\x12\t/testsets\x12\x9c\x01\n\nCreateTest\x12\x1d.eolymp.atlas.CreateTestInput\x1a\x1e.eolymp.atlas.CreateTestOutput\"O\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0c\xf5\xe2\n\x00\x00 A\xf8\xe2\n\xc8\x01\x82\xd3\xe4\x93\x02\x1e\"\x1c/testsets/{testset_id}/tests\x12\xa6\x01\n\nUpdateTest\x12\x1d.eolymp.atlas.UpdateTestInput\x1a\x1e.eolymp.atlas.UpdateTestOutput\"Y\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0c\xf5\xe2\n\x00\x00 A\xf8\xe2\n\xc8\x01\x82\xd3\xe4\x93\x02(\x1a&/testsets/{testset_id}/tests/{test_id}\x12\xa6\x01\n\nDeleteTest\x12\x1d.eolymp.atlas.DeleteTestInput\x1a\x1e.eolymp.atlas.DeleteTestOutput\"Y\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0c\xf5\xe2\n\x00\x00 A\xf8\xe2\n\xc8\x01\x82\xd3\xe4\x93\x02(*&/testsets/{testset_id}/tests/{test_id}\x12\xab\x01\n\x0c\x44\x65scribeTest\x12\x1f.eolymp.atlas.DescribeTestInput\x1a .eolymp.atlas.DescribeTestOutput\"X\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\n2\x82\xd3\xe4\x93\x02(\x12&/testsets/{testset_id}/tests/{test_id}\x12\x98\x01\n\tListTests\x12\x1c.eolymp.atlas.ListTestsInput\x1a\x1d.eolymp.atlas.ListTestsOutput\"N\x82\xe3\n\x17\x8a\xe3\n\x13\x61tlas:problem:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\n2\x82\xd3\xe4\x93\x02\x1e\x12\x1c/testsets/{testset_id}/tests\x12\x8d\x01\n\x0cListExamples\x12\x1f.eolymp.atlas.ListExamplesInput\x1a .eolymp.atlas.ListExamplesOutput\":\x82\xe3\n\x16\x8a\xe3\n\x12\x61tlas:problem:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x0b\x12\t/examplesB-Z+github.com/eolymp/go-sdk/eolymp/atlas;atlasb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.atlas.testing_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/atlas;atlas'
  _TESTINGSERVICE.methods_by_name['UpdateChecker']._options = None
  _TESTINGSERVICE.methods_by_name['UpdateChecker']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\n\327#>\370\342\n\005\202\323\344\223\002\013\032\t/verifier'
  _TESTINGSERVICE.methods_by_name['DescribeChecker']._options = None
  _TESTINGSERVICE.methods_by_name['DescribeChecker']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\013\022\t/verifier'
  _TESTINGSERVICE.methods_by_name['UpdateInteractor']._options = None
  _TESTINGSERVICE.methods_by_name['UpdateInteractor']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\n\327#>\370\342\n\005\202\323\344\223\002\r\032\013/interactor'
  _TESTINGSERVICE.methods_by_name['DescribeInteractor']._options = None
  _TESTINGSERVICE.methods_by_name['DescribeInteractor']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\r\022\013/interactor'
  _TESTINGSERVICE.methods_by_name['CreateTestset']._options = None
  _TESTINGSERVICE.methods_by_name['CreateTestset']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000\240@\370\342\n2\202\323\344\223\002\013\"\t/testsets'
  _TESTINGSERVICE.methods_by_name['UpdateTestset']._options = None
  _TESTINGSERVICE.methods_by_name['UpdateTestset']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000\240@\370\342\n2\202\323\344\223\002\030\032\026/testsets/{testset_id}'
  _TESTINGSERVICE.methods_by_name['DeleteTestset']._options = None
  _TESTINGSERVICE.methods_by_name['DeleteTestset']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000\240@\370\342\n2\202\323\344\223\002\030*\026/testsets/{testset_id}'
  _TESTINGSERVICE.methods_by_name['DescribeTestset']._options = None
  _TESTINGSERVICE.methods_by_name['DescribeTestset']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000 A\370\342\n2\202\323\344\223\002\030\022\026/testsets/{testset_id}'
  _TESTINGSERVICE.methods_by_name['ListTestsets']._options = None
  _TESTINGSERVICE.methods_by_name['ListTestsets']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000 A\370\342\n2\202\323\344\223\002\013\022\t/testsets'
  _TESTINGSERVICE.methods_by_name['CreateTest']._options = None
  _TESTINGSERVICE.methods_by_name['CreateTest']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\014\365\342\n\000\000 A\370\342\n\310\001\202\323\344\223\002\036\"\034/testsets/{testset_id}/tests'
  _TESTINGSERVICE.methods_by_name['UpdateTest']._options = None
  _TESTINGSERVICE.methods_by_name['UpdateTest']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\014\365\342\n\000\000 A\370\342\n\310\001\202\323\344\223\002(\032&/testsets/{testset_id}/tests/{test_id}'
  _TESTINGSERVICE.methods_by_name['DeleteTest']._options = None
  _TESTINGSERVICE.methods_by_name['DeleteTest']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\014\365\342\n\000\000 A\370\342\n\310\001\202\323\344\223\002(*&/testsets/{testset_id}/tests/{test_id}'
  _TESTINGSERVICE.methods_by_name['DescribeTest']._options = None
  _TESTINGSERVICE.methods_by_name['DescribeTest']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000 A\370\342\n2\202\323\344\223\002(\022&/testsets/{testset_id}/tests/{test_id}'
  _TESTINGSERVICE.methods_by_name['ListTests']._options = None
  _TESTINGSERVICE.methods_by_name['ListTests']._serialized_options = b'\202\343\n\027\212\343\n\023atlas:problem:write\352\342\n\013\365\342\n\000\000 A\370\342\n2\202\323\344\223\002\036\022\034/testsets/{testset_id}/tests'
  _TESTINGSERVICE.methods_by_name['ListExamples']._options = None
  _TESTINGSERVICE.methods_by_name['ListExamples']._serialized_options = b'\202\343\n\026\212\343\n\022atlas:problem:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\013\022\t/examples'
  _TESTINGSERVICE._serialized_start=178
  _TESTINGSERVICE._serialized_end=2576
# @@protoc_insertion_point(module_scope)