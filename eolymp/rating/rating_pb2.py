# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/rating/rating.proto
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
    'eolymp/rating/rating.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x65olymp/rating/rating.proto\x12\reolymp.rating\x1a\x1fgoogle/protobuf/timestamp.proto\"\x88\x01\n\x06Rating\x12\n\n\x02id\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tmember_id\x18\x03 \x01(\t\x12\x12\n\ncontest_id\x18\x04 \x01(\t\x12\r\n\x05value\x18\n \x01(\r\x12\r\n\x05level\x18\x0b \x01(\rB/Z-github.com/eolymp/go-sdk/eolymp/rating;ratingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.rating.rating_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/eolymp/go-sdk/eolymp/rating;rating'
  _globals['_RATING']._serialized_start=79
  _globals['_RATING']._serialized_end=215
# @@protoc_insertion_point(module_scope)
