# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/course/student.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x65olymp/course/student.proto\x12\reolymp.course\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8b\x03\n\x07Student\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tcourse_id\x18\x02 \x01(\t\x12\x11\n\tmember_id\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12-\n\x06status\x18\x14 \x01(\x0e\x32\x1d.eolymp.course.Student.Status\x12\x12\n\nbonus_time\x18\x1b \x01(\r\x12.\n\nstarted_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nstarted_in\x18\x16 \x01(\r\x12*\n\x06\x65nd_at\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x65nd_in\x18\x18 \x01(\r\x12/\n\x0b\x63omplete_at\x18\x19 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x63omplete_in\x18\x1a \x01(\r\"7\n\x06Status\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05READY\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x43OMPLETE\x10\x03\x42/Z-github.com/eolymp/go-sdk/eolymp/course;courseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.course.student_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/eolymp/go-sdk/eolymp/course;course'
  _STUDENT._serialized_start=80
  _STUDENT._serialized_end=475
  _STUDENT_STATUS._serialized_start=420
  _STUDENT_STATUS._serialized_end=475
# @@protoc_insertion_point(module_scope)