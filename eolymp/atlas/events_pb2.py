# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/atlas/events.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.acl import acl_service_pb2 as eolymp_dot_acl_dot_acl__service__pb2
from eolymp.atlas import problem_pb2 as eolymp_dot_atlas_dot_problem__pb2
from eolymp.atlas import scoring_score_pb2 as eolymp_dot_atlas_dot_scoring__score__pb2
from eolymp.atlas import statement_pb2 as eolymp_dot_atlas_dot_statement__pb2
from eolymp.atlas import submission_pb2 as eolymp_dot_atlas_dot_submission__pb2
from eolymp.atlas import suggestion_pb2 as eolymp_dot_atlas_dot_suggestion__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x65olymp/atlas/events.proto\x12\x0c\x65olymp.atlas\x1a\x1c\x65olymp/acl/acl_service.proto\x1a\x1a\x65olymp/atlas/problem.proto\x1a eolymp/atlas/scoring_score.proto\x1a\x1c\x65olymp/atlas/statement.proto\x1a\x1d\x65olymp/atlas/submission.proto\x1a\x1d\x65olymp/atlas/suggestion.proto\"W\n\x17SubmissionCompleteEvent\x12,\n\nsubmission\x18\x01 \x01(\x0b\x32\x18.eolymp.atlas.Submission\x12\x0e\n\x06update\x18\x02 \x01(\x08\"k\n\x16SubmissionChangedEvent\x12(\n\x06\x62\x65\x66ore\x18\x01 \x01(\x0b\x32\x18.eolymp.atlas.Submission\x12\'\n\x05\x61\x66ter\x18\x02 \x01(\x0b\x32\x18.eolymp.atlas.Submission\"7\n\x11ScoreUpdatedEvent\x12\"\n\x05score\x18\x01 \x01(\x0b\x32\x13.eolymp.atlas.Score\"b\n\x13ProblemChangedEvent\x12%\n\x06\x62\x65\x66ore\x18\x01 \x01(\x0b\x32\x15.eolymp.atlas.Problem\x12$\n\x05\x61\x66ter\x18\x02 \x01(\x0b\x32\x15.eolymp.atlas.Problem\"|\n\x15StatementChangedEvent\x12\x12\n\nproblem_id\x18\x01 \x01(\t\x12\'\n\x06\x62\x65\x66ore\x18\x02 \x01(\x0b\x32\x17.eolymp.atlas.Statement\x12&\n\x05\x61\x66ter\x18\x03 \x01(\x0b\x32\x17.eolymp.atlas.Statement\"\\\n\x14\x42ookmarkChangedEvent\x12\x12\n\nproblem_id\x18\x01 \x01(\t\x12\x11\n\tmember_id\x18\x02 \x01(\t\x12\x0e\n\x06\x62\x65\x66ore\x18\x03 \x01(\x08\x12\r\n\x05\x61\x66ter\x18\x04 \x01(\x08\"\x8c\x01\n\x16PermissionChangedEvent\x12\x12\n\nproblem_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12&\n\x06\x62\x65\x66ore\x18\x03 \x01(\x0b\x32\x16.eolymp.acl.Permission\x12%\n\x05\x61\x66ter\x18\x04 \x01(\x0b\x32\x16.eolymp.acl.Permission\"\x7f\n\x16SuggestionChangedEvent\x12\x12\n\nproblem_id\x18\x01 \x01(\t\x12(\n\x06\x62\x65\x66ore\x18\x02 \x01(\x0b\x32\x18.eolymp.atlas.Suggestion\x12\'\n\x05\x61\x66ter\x18\x03 \x01(\x0b\x32\x18.eolymp.atlas.SuggestionB-Z+github.com/eolymp/go-sdk/eolymp/atlas;atlasb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.atlas.events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/atlas;atlas'
  _SUBMISSIONCOMPLETEEVENT._serialized_start=227
  _SUBMISSIONCOMPLETEEVENT._serialized_end=314
  _SUBMISSIONCHANGEDEVENT._serialized_start=316
  _SUBMISSIONCHANGEDEVENT._serialized_end=423
  _SCOREUPDATEDEVENT._serialized_start=425
  _SCOREUPDATEDEVENT._serialized_end=480
  _PROBLEMCHANGEDEVENT._serialized_start=482
  _PROBLEMCHANGEDEVENT._serialized_end=580
  _STATEMENTCHANGEDEVENT._serialized_start=582
  _STATEMENTCHANGEDEVENT._serialized_end=706
  _BOOKMARKCHANGEDEVENT._serialized_start=708
  _BOOKMARKCHANGEDEVENT._serialized_end=800
  _PERMISSIONCHANGEDEVENT._serialized_start=803
  _PERMISSIONCHANGEDEVENT._serialized_end=943
  _SUGGESTIONCHANGEDEVENT._serialized_start=945
  _SUGGESTIONCHANGEDEVENT._serialized_end=1072
# @@protoc_insertion_point(module_scope)
