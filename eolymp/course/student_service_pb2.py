# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/course/student_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.course import student_pb2 as eolymp_dot_course_dot_student__pb2
from eolymp.wellknown import direction_pb2 as eolymp_dot_wellknown_dot_direction__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#eolymp/course/student_service.proto\x12\reolymp.course\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\x1b\x65olymp/course/student.proto\x1a eolymp/wellknown/direction.proto\x1a!eolymp/wellknown/expression.proto\"W\n\x14\x44\x65scribeStudentInput\x12\x11\n\tmember_id\x18\x01 \x01(\t\x12,\n\x05\x65xtra\x18\xe3\x08 \x03(\x0e\x32\x1c.eolymp.course.Student.Extra\"@\n\x15\x44\x65scribeStudentOutput\x12\'\n\x07student\x18\x01 \x01(\x0b\x32\x16.eolymp.course.Student\"\x15\n\x13\x44\x65scribeViewerInput\"?\n\x14\x44\x65scribeViewerOutput\x12\'\n\x07student\x18\x01 \x01(\x0b\x32\x16.eolymp.course.Student\"\x80\x03\n\x11ListStudentsInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x38\n\x07\x66ilters\x18( \x01(\x0b\x32\'.eolymp.course.ListStudentsInput.Filter\x12\x37\n\x04sort\x18\x32 \x01(\x0e\x32).eolymp.course.ListStudentsInput.Sortable\x12*\n\x05order\x18\x33 \x01(\x0e\x32\x1b.eolymp.wellknown.Direction\x12,\n\x05\x65xtra\x18\xe3\x08 \x03(\x0e\x32\x1c.eolymp.course.Student.Extra\x1ag\n\x06\x46ilter\x12*\n\x02id\x18\n \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x31\n\tmember_id\x18\x0b \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\"\x17\n\x08Sortable\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\"J\n\x12ListStudentsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12%\n\x05items\x18\x02 \x03(\x0b\x32\x16.eolymp.course.Student\"&\n\x11WatchStudentInput\x12\x11\n\tmember_id\x18\x02 \x01(\t\"=\n\x12WatchStudentOutput\x12\'\n\x07student\x18\x01 \x01(\x0b\x32\x16.eolymp.course.Student2\xda\x04\n\x0eStudentService\x12\xa4\x01\n\x0f\x44\x65scribeStudent\x12#.eolymp.course.DescribeStudentInput\x1a$.eolymp.course.DescribeStudentOutput\"F\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x17\x12\x15/students/{member_id}\x12\x9b\x01\n\x0e\x44\x65scribeViewer\x12\".eolymp.course.DescribeViewerInput\x1a#.eolymp.course.DescribeViewerOutput\"@\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x11\x12\x0f/viewer/student\x12\x8f\x01\n\x0cListStudents\x12 .eolymp.course.ListStudentsInput\x1a!.eolymp.course.ListStudentsOutput\":\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x0b\x12\t/students\x12q\n\x0cWatchStudent\x12 .eolymp.course.WatchStudentInput\x1a!.eolymp.course.WatchStudentOutput\"\x1a\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read0\x01\x42/Z-github.com/eolymp/go-sdk/eolymp/course;courseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.course.student_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/eolymp/go-sdk/eolymp/course;course'
  _STUDENTSERVICE.methods_by_name['DescribeStudent']._options = None
  _STUDENTSERVICE.methods_by_name['DescribeStudent']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\027\022\025/students/{member_id}'
  _STUDENTSERVICE.methods_by_name['DescribeViewer']._options = None
  _STUDENTSERVICE.methods_by_name['DescribeViewer']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\021\022\017/viewer/student'
  _STUDENTSERVICE.methods_by_name['ListStudents']._options = None
  _STUDENTSERVICE.methods_by_name['ListStudents']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\013\022\t/students'
  _STUDENTSERVICE.methods_by_name['WatchStudent']._options = None
  _STUDENTSERVICE.methods_by_name['WatchStudent']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read'
  _DESCRIBESTUDENTINPUT._serialized_start=251
  _DESCRIBESTUDENTINPUT._serialized_end=338
  _DESCRIBESTUDENTOUTPUT._serialized_start=340
  _DESCRIBESTUDENTOUTPUT._serialized_end=404
  _DESCRIBEVIEWERINPUT._serialized_start=406
  _DESCRIBEVIEWERINPUT._serialized_end=427
  _DESCRIBEVIEWEROUTPUT._serialized_start=429
  _DESCRIBEVIEWEROUTPUT._serialized_end=492
  _LISTSTUDENTSINPUT._serialized_start=495
  _LISTSTUDENTSINPUT._serialized_end=879
  _LISTSTUDENTSINPUT_FILTER._serialized_start=751
  _LISTSTUDENTSINPUT_FILTER._serialized_end=854
  _LISTSTUDENTSINPUT_SORTABLE._serialized_start=856
  _LISTSTUDENTSINPUT_SORTABLE._serialized_end=879
  _LISTSTUDENTSOUTPUT._serialized_start=881
  _LISTSTUDENTSOUTPUT._serialized_end=955
  _WATCHSTUDENTINPUT._serialized_start=957
  _WATCHSTUDENTINPUT._serialized_end=995
  _WATCHSTUDENTOUTPUT._serialized_start=997
  _WATCHSTUDENTOUTPUT._serialized_end=1058
  _STUDENTSERVICE._serialized_start=1061
  _STUDENTSERVICE._serialized_end=1663
# @@protoc_insertion_point(module_scope)
