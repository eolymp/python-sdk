# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/course/material.proto
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
    'eolymp/course/material.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.ecm import content_pb2 as eolymp_dot_ecm_dot_content__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x65olymp/course/material.proto\x12\reolymp.course\x1a\x18\x65olymp/ecm/content.proto\"\xe2\x05\n\x08Material\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\r\n\x05\x64raft\x18\x03 \x01(\x08\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x11\n\timage_url\x18\x05 \x01(\t\x12\x11\n\tmodule_id\x18\x06 \x01(\t\x12\r\n\x05index\x18\x0b \x01(\r\x12\r\n\x05\x64\x65pth\x18\x0c \x01(\r\x12\x30\n\x07grading\x18\x1e \x01(\x0b\x32\x1f.eolymp.course.Material.Grading\x12\x34\n\x08\x64ocument\x18\x64 \x01(\x0b\x32 .eolymp.course.Material.DocumentH\x00\x12,\n\x04task\x18\x65 \x01(\x0b\x32\x1c.eolymp.course.Material.TaskH\x00\x12\x12\n\npercentage\x18\x14 \x01(\x02\x12\r\n\x05grade\x18\x15 \x01(\r\x12\x32\n\x08progress\x18\x16 \x01(\x0b\x32 .eolymp.course.Material.Progress\x1a\x30\n\x08\x44ocument\x12$\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\x13.eolymp.ecm.Content\x1a\x1a\n\x04Task\x12\x12\n\nproblem_id\x18\x01 \x01(\t\x1a,\n\x07Grading\x12\x11\n\tmax_score\x18\x01 \x01(\r\x12\x0e\n\x06weight\x18\x02 \x01(\x02\x1ao\n\x08Progress\x12\x12\n\npercentage\x18\x14 \x01(\x02\x12\r\n\x05grade\x18\x15 \x01(\r\x12\x17\n\x0fgrade_automatic\x18\x16 \x01(\r\x12\x16\n\x0egrade_override\x18\x17 \x01(\r\x12\x0f\n\x07\x65xcused\x18\x18 \x01(\x08\"w\n\x05\x45xtra\x12\x11\n\rUNKNOWN_EXTRA\x10\x00\x12\x0b\n\x07\x43ONTENT\x10\x01\x12\x11\n\rCONTENT_VALUE\x10\x02\x12\x12\n\x0e\x43ONTENT_RENDER\x10\x03\x12\x0e\n\nPERCENTAGE\x10\x04\x12\t\n\x05GRADE\x10\x05\x12\x0c\n\x08PROGRESS\x10\x06\x42\t\n\x07\x63ontentB/Z-github.com/eolymp/go-sdk/eolymp/course;courseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.course.material_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/eolymp/go-sdk/eolymp/course;course'
  _globals['_MATERIAL']._serialized_start=74
  _globals['_MATERIAL']._serialized_end=812
  _globals['_MATERIAL_DOCUMENT']._serialized_start=445
  _globals['_MATERIAL_DOCUMENT']._serialized_end=493
  _globals['_MATERIAL_TASK']._serialized_start=495
  _globals['_MATERIAL_TASK']._serialized_end=521
  _globals['_MATERIAL_GRADING']._serialized_start=523
  _globals['_MATERIAL_GRADING']._serialized_end=567
  _globals['_MATERIAL_PROGRESS']._serialized_start=569
  _globals['_MATERIAL_PROGRESS']._serialized_end=680
  _globals['_MATERIAL_EXTRA']._serialized_start=682
  _globals['_MATERIAL_EXTRA']._serialized_end=801
# @@protoc_insertion_point(module_scope)
