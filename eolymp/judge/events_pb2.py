# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/judge/events.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'eolymp/judge/events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.judge import participant_pb2 as eolymp_dot_judge_dot_participant__pb2
from eolymp.judge import score_pb2 as eolymp_dot_judge_dot_score__pb2
from eolymp.judge import submission_pb2 as eolymp_dot_judge_dot_submission__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x65olymp/judge/events.proto\x12\x0c\x65olymp.judge\x1a\x1e\x65olymp/judge/participant.proto\x1a\x18\x65olymp/judge/score.proto\x1a\x1d\x65olymp/judge/submission.proto\"\\\n\x18SubmissionCompletedEvent\x12\x12\n\ncontest_id\x18\n \x01(\t\x12,\n\nsubmission\x18\x01 \x01(\x0b\x32\x18.eolymp.judge.Submission\"<\n\x11RebuildScoreEvent\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63tivity_id\x18\x02 \x01(\t\"w\n\x11ScoreChangedEvent\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x16\n\x0eparticipant_id\x18\x02 \x01(\t\x12\x12\n\nunofficial\x18\x04 \x01(\x08\x12\"\n\x05score\x18\x03 \x01(\x0b\x32\x13.eolymp.judge.Score\"Q\n\x12RetestProblemEvent\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x12\n\nproblem_id\x18\x02 \x01(\t\x12\x13\n\x0b\x61\x63tivity_id\x18\x03 \x01(\tB-Z+github.com/eolymp/go-sdk/eolymp/judge;judgeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.judge.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/judge;judge'
  _globals['_SUBMISSIONCOMPLETEDEVENT']._serialized_start=132
  _globals['_SUBMISSIONCOMPLETEDEVENT']._serialized_end=224
  _globals['_REBUILDSCOREEVENT']._serialized_start=226
  _globals['_REBUILDSCOREEVENT']._serialized_end=286
  _globals['_SCORECHANGEDEVENT']._serialized_start=288
  _globals['_SCORECHANGEDEVENT']._serialized_end=407
  _globals['_RETESTPROBLEMEVENT']._serialized_start=409
  _globals['_RETESTPROBLEMEVENT']._serialized_end=490
# @@protoc_insertion_point(module_scope)
