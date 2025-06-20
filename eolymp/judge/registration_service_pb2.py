# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/judge/registration_service.proto
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
    'eolymp/judge/registration_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.community import attribute_pb2 as eolymp_dot_community_dot_attribute__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'eolymp/judge/registration_service.proto\x12\x0c\x65olymp.judge\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a eolymp/community/attribute.proto\"/\n\x19\x44\x65scribeRegistrationInput\x12\x12\n\ncontest_id\x18\x01 \x01(\t\"\x80\x01\n\x1a\x44\x65scribeRegistrationOutput\x12/\n\nattributes\x18\x14 \x03(\x0b\x32\x1b.eolymp.community.Attribute\x12\x31\n\x06values\x18\x15 \x03(\x0b\x32!.eolymp.community.Attribute.Value\"`\n\x17SubmitRegistrationInput\x12\x12\n\ncontest_id\x18\x01 \x01(\t\x12\x31\n\x06values\x18\x14 \x03(\x0b\x32!.eolymp.community.Attribute.Value\"\x1a\n\x18SubmitRegistrationOutput2\xf5\x02\n\x13RegistrationService\x12\xb0\x01\n\x14\x44\x65scribeRegistration\x12\'.eolymp.judge.DescribeRegistrationInput\x1a(.eolymp.judge.DescribeRegistrationOutput\"E\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\n\x82\xe3\n\x1d\x8a\xe3\n\x19judge:contest:participate\x82\xd3\xe4\x93\x02\x0f\x12\r/registration\x12\xaa\x01\n\x12SubmitRegistration\x12%.eolymp.judge.SubmitRegistrationInput\x1a&.eolymp.judge.SubmitRegistrationOutput\"E\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x03\x82\xe3\n\x1d\x8a\xe3\n\x19judge:contest:participate\x82\xd3\xe4\x93\x02\x0f\"\r/registrationB-Z+github.com/eolymp/go-sdk/eolymp/judge;judgeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.judge.registration_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/judge;judge'
  _globals['_REGISTRATIONSERVICE'].methods_by_name['DescribeRegistration']._loaded_options = None
  _globals['_REGISTRATIONSERVICE'].methods_by_name['DescribeRegistration']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\n\202\343\n\035\212\343\n\031judge:contest:participate\202\323\344\223\002\017\022\r/registration'
  _globals['_REGISTRATIONSERVICE'].methods_by_name['SubmitRegistration']._loaded_options = None
  _globals['_REGISTRATIONSERVICE'].methods_by_name['SubmitRegistration']._serialized_options = b'\352\342\n\013\365\342\n\000\000\200?\370\342\n\003\202\343\n\035\212\343\n\031judge:contest:participate\202\323\344\223\002\017\"\r/registration'
  _globals['_DESCRIBEREGISTRATIONINPUT']._serialized_start=190
  _globals['_DESCRIBEREGISTRATIONINPUT']._serialized_end=237
  _globals['_DESCRIBEREGISTRATIONOUTPUT']._serialized_start=240
  _globals['_DESCRIBEREGISTRATIONOUTPUT']._serialized_end=368
  _globals['_SUBMITREGISTRATIONINPUT']._serialized_start=370
  _globals['_SUBMITREGISTRATIONINPUT']._serialized_end=466
  _globals['_SUBMITREGISTRATIONOUTPUT']._serialized_start=468
  _globals['_SUBMITREGISTRATIONOUTPUT']._serialized_end=494
  _globals['_REGISTRATIONSERVICE']._serialized_start=497
  _globals['_REGISTRATIONSERVICE']._serialized_end=870
# @@protoc_insertion_point(module_scope)
