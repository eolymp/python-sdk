# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/judge/submission.proto
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
    'eolymp/judge/submission.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.atlas import submission_pb2 as eolymp_dot_atlas_dot_submission__pb2
from eolymp.atlas import testing_feedback_pb2 as eolymp_dot_atlas_dot_testing__feedback__pb2
from eolymp.atlas import testing_scoring_pb2 as eolymp_dot_atlas_dot_testing__scoring__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x65olymp/judge/submission.proto\x12\x0c\x65olymp.judge\x1a\x1d\x65olymp/atlas/submission.proto\x1a#eolymp/atlas/testing_feedback.proto\x1a\"eolymp/atlas/testing_scoring.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa7\n\n\nSubmission\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x07 \x01(\t\x12\x12\n\ncontest_id\x18\x02 \x01(\t\x12\x12\n\nproblem_id\x18\x03 \x01(\t\x12\x16\n\x0eparticipant_id\x18\x04 \x01(\t\x12\x30\n\x0csubmitted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x64\x65leted\x18\x06 \x01(\x08\x12\x0c\n\x04lang\x18\n \x01(\t\x12\x0e\n\x06source\x18\x0b \x01(\t\x12\x12\n\nsource_url\x18n \x01(\t\x12\x11\n\tsignature\x18\x0c \x01(\t\x12/\n\x06status\x18\x14 \x01(\x0e\x32\x1f.eolymp.atlas.Submission.Status\x12\x31\n\x07verdict\x18\x16 \x01(\x0e\x32 .eolymp.atlas.Submission.Verdict\x12\r\n\x05\x65rror\x18\x15 \x01(\t\x12\x11\n\terror_url\x18\x17 \x01(\t\x12\x0c\n\x04\x63ost\x18\x1e \x01(\x02\x12\r\n\x05score\x18\x1f \x01(\x02\x12\x12\n\npercentage\x18  \x01(\x02\x12\x12\n\ntime_usage\x18) \x01(\r\x12\x11\n\tcpu_usage\x18* \x01(\r\x12\x14\n\x0cmemory_usage\x18. \x01(\x04\x12\x16\n\x0eresource_usage\x18/ \x01(\x02\x12\x18\n\x10gen_ai_use_score\x18\x30 \x01(\x02\x12.\n\x06groups\x18\x32 \x03(\x0b\x32\x1e.eolymp.judge.Submission.Group\x12\x0e\n\x06\x63ursor\x18\x64 \x01(\t\x1a\xf9\x01\n\x03Run\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05index\x18\n \x01(\r\x12\x0f\n\x07test_id\x18\x0b \x01(\t\x12\x0c\n\x04\x63ost\x18\x0c \x01(\x02\x12\r\n\x05score\x18\r \x01(\x02\x12\x17\n\x0fwall_time_usage\x18\x02 \x01(\r\x12\x16\n\x0e\x63pu_time_usage\x18\x03 \x01(\r\x12\x14\n\x0cmemory_usage\x18\x04 \x01(\x04\x12/\n\x06status\x18\x14 \x01(\x0e\x32\x1f.eolymp.atlas.Submission.Status\x12\x31\n\x07verdict\x18\x15 \x01(\x0e\x32 .eolymp.atlas.Submission.Verdict\x1a\x9c\x03\n\x05Group\x12\r\n\x05index\x18\x01 \x01(\r\x12\x12\n\ntestset_id\x18\x02 \x01(\t\x12/\n\x06status\x18\n \x01(\x0e\x32\x1f.eolymp.atlas.Submission.Status\x12\x31\n\x07verdict\x18\x0c \x01(\x0e\x32 .eolymp.atlas.Submission.Verdict\x12\x14\n\x0c\x64\x65pendencies\x18\x0b \x03(\r\x12\x0c\n\x04\x63ost\x18\x14 \x01(\x02\x12\r\n\x05score\x18\x15 \x01(\x02\x12/\n\x0cscoring_mode\x18\x16 \x01(\x0e\x32\x19.eolymp.atlas.ScoringMode\x12\x35\n\x0f\x66\x65\x65\x64\x62\x61\x63k_policy\x18\x1e \x01(\x0e\x32\x1c.eolymp.atlas.FeedbackPolicy\x12\x17\n\x0fwall_time_usage\x18) \x01(\r\x12\x16\n\x0e\x63pu_time_usage\x18* \x01(\r\x12\x14\n\x0cmemory_usage\x18. \x01(\x04\x12*\n\x04runs\x18\x64 \x03(\x0b\x32\x1c.eolymp.judge.Submission.Run\"7\n\x05\x45xtra\x12\x0c\n\x08NO_EXTRA\x10\x00\x12\n\n\x06SOURCE\x10\x01\x12\n\n\x06GROUPS\x10\x02\x12\x08\n\x04RUNS\x10\x03\x42-Z+github.com/eolymp/go-sdk/eolymp/judge;judgeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.judge.submission_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/judge;judge'
  _globals['_SUBMISSION']._serialized_start=185
  _globals['_SUBMISSION']._serialized_end=1504
  _globals['_SUBMISSION_RUN']._serialized_start=783
  _globals['_SUBMISSION_RUN']._serialized_end=1032
  _globals['_SUBMISSION_GROUP']._serialized_start=1035
  _globals['_SUBMISSION_GROUP']._serialized_end=1447
  _globals['_SUBMISSION_EXTRA']._serialized_start=1449
  _globals['_SUBMISSION_EXTRA']._serialized_end=1504
# @@protoc_insertion_point(module_scope)
