# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/atlas/snapshot.proto
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
    'eolymp/atlas/snapshot.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.atlas import attachment_pb2 as eolymp_dot_atlas_dot_attachment__pb2
from eolymp.atlas import code_template_pb2 as eolymp_dot_atlas_dot_code__template__pb2
from eolymp.atlas import editorial_pb2 as eolymp_dot_atlas_dot_editorial__pb2
from eolymp.atlas import problem_pb2 as eolymp_dot_atlas_dot_problem__pb2
from eolymp.atlas import script_pb2 as eolymp_dot_atlas_dot_script__pb2
from eolymp.atlas import solution_pb2 as eolymp_dot_atlas_dot_solution__pb2
from eolymp.atlas import statement_pb2 as eolymp_dot_atlas_dot_statement__pb2
from eolymp.atlas import testing_checker_pb2 as eolymp_dot_atlas_dot_testing__checker__pb2
from eolymp.atlas import testing_config_pb2 as eolymp_dot_atlas_dot_testing__config__pb2
from eolymp.atlas import testing_interactor_pb2 as eolymp_dot_atlas_dot_testing__interactor__pb2
from eolymp.atlas import testing_test_pb2 as eolymp_dot_atlas_dot_testing__test__pb2
from eolymp.atlas import testing_testset_pb2 as eolymp_dot_atlas_dot_testing__testset__pb2
from eolymp.atlas import testing_validator_pb2 as eolymp_dot_atlas_dot_testing__validator__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x65olymp/atlas/snapshot.proto\x12\x0c\x65olymp.atlas\x1a\x1d\x65olymp/atlas/attachment.proto\x1a eolymp/atlas/code_template.proto\x1a\x1c\x65olymp/atlas/editorial.proto\x1a\x1a\x65olymp/atlas/problem.proto\x1a\x19\x65olymp/atlas/script.proto\x1a\x1b\x65olymp/atlas/solution.proto\x1a\x1c\x65olymp/atlas/statement.proto\x1a\"eolymp/atlas/testing_checker.proto\x1a!eolymp/atlas/testing_config.proto\x1a%eolymp/atlas/testing_interactor.proto\x1a\x1f\x65olymp/atlas/testing_test.proto\x1a\"eolymp/atlas/testing_testset.proto\x1a$eolymp/atlas/testing_validator.proto\"\xb4\x04\n\x08Snapshot\x12&\n\x07problem\x18\x01 \x01(\x0b\x32\x15.eolymp.atlas.Problem\x12,\n\x07testing\x18\n \x01(\x0b\x32\x1b.eolymp.atlas.TestingConfig\x12&\n\x07\x63hecker\x18\x02 \x01(\x0b\x32\x15.eolymp.atlas.Checker\x12,\n\ninteractor\x18\x03 \x01(\x0b\x32\x18.eolymp.atlas.Interactor\x12*\n\tvalidator\x18\r \x01(\x0b\x32\x17.eolymp.atlas.Validator\x12+\n\nstatements\x18\x04 \x03(\x0b\x32\x17.eolymp.atlas.Statement\x12)\n\ttemplates\x18\x05 \x03(\x0b\x32\x16.eolymp.atlas.Template\x12-\n\x0b\x61ttachments\x18\x06 \x03(\x0b\x32\x18.eolymp.atlas.Attachment\x12\'\n\x08testsets\x18\x07 \x03(\x0b\x32\x15.eolymp.atlas.Testset\x12!\n\x05tests\x18\x08 \x03(\x0b\x32\x12.eolymp.atlas.Test\x12+\n\neditorials\x18\t \x03(\x0b\x32\x17.eolymp.atlas.Editorial\x12)\n\tsolutions\x18\x0b \x03(\x0b\x32\x16.eolymp.atlas.Solution\x12%\n\x07scripts\x18\x0c \x03(\x0b\x32\x14.eolymp.atlas.ScriptB-Z+github.com/eolymp/go-sdk/eolymp/atlas;atlasb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.atlas.snapshot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/atlas;atlas'
  _globals['_SNAPSHOT']._serialized_start=472
  _globals['_SNAPSHOT']._serialized_end=1036
# @@protoc_insertion_point(module_scope)
