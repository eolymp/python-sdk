# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/wellknown/expression.proto
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
    'eolymp/wellknown/expression.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!eolymp/wellknown/expression.proto\x12\x10\x65olymp.wellknown\x1a\x1fgoogle/protobuf/timestamp.proto\"z\n\x0c\x45xpressionID\x12/\n\x02is\x18\x01 \x01(\x0e\x32#.eolymp.wellknown.ExpressionID.Type\x12\r\n\x05value\x18\x02 \x01(\t\"*\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x45QUAL\x10\x01\x12\r\n\tNOT_EQUAL\x10\x02\"\xca\x01\n\rExpressionInt\x12\x30\n\x02is\x18\x01 \x01(\x0e\x32$.eolymp.wellknown.ExpressionInt.Type\x12\r\n\x05value\x18\x02 \x01(\x05\"x\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x45QUAL\x10\x01\x12\r\n\tNOT_EQUAL\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x16\n\x12GREATER_THAN_EQUAL\x10\x04\x12\r\n\tLESS_THAN\x10\x05\x12\x13\n\x0fLESS_THAN_EQUAL\x10\x06\"\xce\x01\n\x0f\x45xpressionFloat\x12\x32\n\x02is\x18\x01 \x01(\x0e\x32&.eolymp.wellknown.ExpressionFloat.Type\x12\r\n\x05value\x18\x02 \x01(\x02\"x\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x45QUAL\x10\x01\x12\r\n\tNOT_EQUAL\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x16\n\x12GREATER_THAN_EQUAL\x10\x04\x12\r\n\tLESS_THAN\x10\x05\x12\x13\n\x0fLESS_THAN_EQUAL\x10\x06\"\xa0\x01\n\x10\x45xpressionString\x12\x33\n\x02is\x18\x01 \x01(\x0e\x32\'.eolymp.wellknown.ExpressionString.Type\x12\r\n\x05value\x18\x02 \x01(\t\"H\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x45QUAL\x10\x01\x12\r\n\tNOT_EQUAL\x10\x02\x12\x0e\n\nCONTAINING\x10\x03\x12\x0c\n\x08STARTING\x10\x04\"~\n\x0e\x45xpressionEnum\x12\x31\n\x02is\x18\x01 \x01(\x0e\x32%.eolymp.wellknown.ExpressionEnum.Type\x12\r\n\x05value\x18\x02 \x01(\t\"*\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x45QUAL\x10\x01\x12\r\n\tNOT_EQUAL\x10\x02\"o\n\x0e\x45xpressionBool\x12\x31\n\x02is\x18\x01 \x01(\x0e\x32%.eolymp.wellknown.ExpressionBool.Type\x12\r\n\x05value\x18\x02 \x01(\x08\"\x1b\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x45QUAL\x10\x01\"\xf2\x01\n\x13\x45xpressionTimestamp\x12\x36\n\x02is\x18\x01 \x01(\x0e\x32*.eolymp.wellknown.ExpressionTimestamp.Type\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"x\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05\x45QUAL\x10\x01\x12\r\n\tNOT_EQUAL\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x16\n\x12GREATER_THAN_EQUAL\x10\x04\x12\r\n\tLESS_THAN\x10\x05\x12\x13\n\x0fLESS_THAN_EQUAL\x10\x06\x42\x35Z3github.com/eolymp/go-sdk/eolymp/wellknown;wellknownb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.wellknown.expression_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/eolymp/go-sdk/eolymp/wellknown;wellknown'
  _globals['_EXPRESSIONID']._serialized_start=88
  _globals['_EXPRESSIONID']._serialized_end=210
  _globals['_EXPRESSIONID_TYPE']._serialized_start=168
  _globals['_EXPRESSIONID_TYPE']._serialized_end=210
  _globals['_EXPRESSIONINT']._serialized_start=213
  _globals['_EXPRESSIONINT']._serialized_end=415
  _globals['_EXPRESSIONINT_TYPE']._serialized_start=295
  _globals['_EXPRESSIONINT_TYPE']._serialized_end=415
  _globals['_EXPRESSIONFLOAT']._serialized_start=418
  _globals['_EXPRESSIONFLOAT']._serialized_end=624
  _globals['_EXPRESSIONFLOAT_TYPE']._serialized_start=295
  _globals['_EXPRESSIONFLOAT_TYPE']._serialized_end=415
  _globals['_EXPRESSIONSTRING']._serialized_start=627
  _globals['_EXPRESSIONSTRING']._serialized_end=787
  _globals['_EXPRESSIONSTRING_TYPE']._serialized_start=715
  _globals['_EXPRESSIONSTRING_TYPE']._serialized_end=787
  _globals['_EXPRESSIONENUM']._serialized_start=789
  _globals['_EXPRESSIONENUM']._serialized_end=915
  _globals['_EXPRESSIONENUM_TYPE']._serialized_start=168
  _globals['_EXPRESSIONENUM_TYPE']._serialized_end=210
  _globals['_EXPRESSIONBOOL']._serialized_start=917
  _globals['_EXPRESSIONBOOL']._serialized_end=1028
  _globals['_EXPRESSIONBOOL_TYPE']._serialized_start=168
  _globals['_EXPRESSIONBOOL_TYPE']._serialized_end=195
  _globals['_EXPRESSIONTIMESTAMP']._serialized_start=1031
  _globals['_EXPRESSIONTIMESTAMP']._serialized_end=1273
  _globals['_EXPRESSIONTIMESTAMP_TYPE']._serialized_start=295
  _globals['_EXPRESSIONTIMESTAMP_TYPE']._serialized_end=415
# @@protoc_insertion_point(module_scope)
