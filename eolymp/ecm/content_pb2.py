# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/ecm/content.proto
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
    'eolymp/ecm/content.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.ecm import node_pb2 as eolymp_dot_ecm_dot_node__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x65olymp/ecm/content.proto\x12\neolymp.ecm\x1a\x15\x65olymp/ecm/node.proto\"\x8a\x01\n\x07\x43ontent\x12\x0e\n\x04html\x18\x01 \x01(\tH\x00\x12\x0f\n\x05latex\x18\x02 \x01(\tH\x00\x12\x12\n\x08markdown\x18\x03 \x01(\tH\x00\x12\x1f\n\x03\x65\x63m\x18\x04 \x01(\x0b\x32\x10.eolymp.ecm.NodeH\x00\x12 \n\x06render\x18\x63 \x01(\x0b\x32\x10.eolymp.ecm.NodeB\x07\n\x05valueB)Z\'github.com/eolymp/go-sdk/eolymp/ecm;ecmb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.ecm.content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/eolymp/go-sdk/eolymp/ecm;ecm'
  _globals['_CONTENT']._serialized_start=64
  _globals['_CONTENT']._serialized_end=202
# @@protoc_insertion_point(module_scope)
