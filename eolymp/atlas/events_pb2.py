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


from eolymp.atlas import scoring_score_pb2 as eolymp_dot_atlas_dot_scoring__score__pb2
from eolymp.atlas import submission_pb2 as eolymp_dot_atlas_dot_submission__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x65olymp/atlas/events.proto\x12\x0c\x65olymp.atlas\x1a eolymp/atlas/scoring_score.proto\x1a\x1d\x65olymp/atlas/submission.proto\">\n\x17PermissionsDeletedEvent\x12\x12\n\nproblem_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\"W\n\x17SubmissionCompleteEvent\x12,\n\nsubmission\x18\x01 \x01(\x0b\x32\x18.eolymp.atlas.Submission\x12\x0e\n\x06update\x18\x02 \x01(\x08\"7\n\x11ScoreUpdatedEvent\x12\"\n\x05score\x18\x01 \x01(\x0b\x32\x13.eolymp.atlas.ScoreB-Z+github.com/eolymp/go-sdk/eolymp/atlas;atlasb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.atlas.events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/atlas;atlas'
  _PERMISSIONSDELETEDEVENT._serialized_start=108
  _PERMISSIONSDELETEDEVENT._serialized_end=170
  _SUBMISSIONCOMPLETEEVENT._serialized_start=172
  _SUBMISSIONCOMPLETEEVENT._serialized_end=259
  _SCOREUPDATEDEVENT._serialized_start=261
  _SCOREUPDATEDEVENT._serialized_end=316
# @@protoc_insertion_point(module_scope)
