# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/commerce/price.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x65olymp/commerce/price.proto\x12\x0f\x65olymp.commerce\"\xbd\x01\n\x05Price\x12\n\n\x02id\x18\x01 \x01(\t\x12\x35\n\nrecurrence\x18\x03 \x01(\x0e\x32!.eolymp.commerce.Price.Recurrence\x12\x10\n\x08\x63urrency\x18\x1e \x01(\t\x12\x13\n\x0bunit_amount\x18\x1f \x01(\x05\"J\n\nRecurrence\x12\x16\n\x12UNKNOWN_RECURRENCE\x10\x00\x12\x0b\n\x07ONETIME\x10\x01\x12\x0b\n\x07MONTHLY\x10\x02\x12\n\n\x06YEARLY\x10\x03\x42\x33Z1github.com/eolymp/go-sdk/eolymp/commerce;commerceb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.commerce.price_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/eolymp/go-sdk/eolymp/commerce;commerce'
  _PRICE._serialized_start=49
  _PRICE._serialized_end=238
  _PRICE_RECURRENCE._serialized_start=164
  _PRICE_RECURRENCE._serialized_end=238
# @@protoc_insertion_point(module_scope)
