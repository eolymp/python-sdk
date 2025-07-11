# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/worker/worker_service.proto
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
    'eolymp/worker/worker_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2
from eolymp.worker import worker_job_pb2 as eolymp_dot_worker_dot_worker__job__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"eolymp/worker/worker_service.proto\x12\reolymp.worker\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a!eolymp/wellknown/expression.proto\x1a\x1e\x65olymp/worker/worker_job.proto\"2\n\x0fJobTriggerEvent\x12\x1f\n\x03job\x18\x01 \x01(\x0b\x32\x12.eolymp.worker.Job\"\x88\x01\n\x0e\x43reateJobInput\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x39\n\x06inputs\x18\x02 \x03(\x0b\x32).eolymp.worker.CreateJobInput.InputsEntry\x1a-\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"!\n\x0f\x43reateJobOutput\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"\"\n\x10\x44\x65scribeJobInput\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"4\n\x11\x44\x65scribeJobOutput\x12\x1f\n\x03job\x18\x01 \x01(\x0b\x32\x12.eolymp.worker.Job\"\xfc\x01\n\rListJobsInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x34\n\x07\x66ilters\x18( \x01(\x0b\x32#.eolymp.worker.ListJobsInput.Filter\x1a\x96\x01\n\x06\x46ilter\x12*\n\x02id\x18\x01 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12.\n\x04type\x18\x02 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x12\x30\n\x06status\x18\x03 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\"B\n\x0eListJobsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12!\n\x05items\x18\x02 \x03(\x0b\x32\x12.eolymp.worker.Job2\xec\x02\n\rWorkerService\x12L\n\tCreateJob\x12\x1d.eolymp.worker.CreateJobInput\x1a\x1e.eolymp.worker.CreateJobOutput\"\x00\x12\x8e\x01\n\x0b\x44\x65scribeJob\x12\x1f.eolymp.worker.DescribeJobInput\x1a .eolymp.worker.DescribeJobOutput\"<\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xe3\n\x13\x8a\xe3\n\x0fworker:job:read\x82\xd3\xe4\x93\x02\x10\x12\x0e/jobs/{job_id}\x12|\n\x08ListJobs\x12\x1c.eolymp.worker.ListJobsInput\x1a\x1d.eolymp.worker.ListJobsOutput\"3\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xe3\n\x13\x8a\xe3\n\x0fworker:job:read\x82\xd3\xe4\x93\x02\x07\x12\x05/jobsB/Z-github.com/eolymp/go-sdk/eolymp/worker;workerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.worker.worker_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/eolymp/go-sdk/eolymp/worker;worker'
  _globals['_CREATEJOBINPUT_INPUTSENTRY']._loaded_options = None
  _globals['_CREATEJOBINPUT_INPUTSENTRY']._serialized_options = b'8\001'
  _globals['_WORKERSERVICE'].methods_by_name['DescribeJob']._loaded_options = None
  _globals['_WORKERSERVICE'].methods_by_name['DescribeJob']._serialized_options = b'\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\343\n\023\212\343\n\017worker:job:read\202\323\344\223\002\020\022\016/jobs/{job_id}'
  _globals['_WORKERSERVICE'].methods_by_name['ListJobs']._loaded_options = None
  _globals['_WORKERSERVICE'].methods_by_name['ListJobs']._serialized_options = b'\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\343\n\023\212\343\n\017worker:job:read\202\323\344\223\002\007\022\005/jobs'
  _globals['_JOBTRIGGEREVENT']._serialized_start=219
  _globals['_JOBTRIGGEREVENT']._serialized_end=269
  _globals['_CREATEJOBINPUT']._serialized_start=272
  _globals['_CREATEJOBINPUT']._serialized_end=408
  _globals['_CREATEJOBINPUT_INPUTSENTRY']._serialized_start=363
  _globals['_CREATEJOBINPUT_INPUTSENTRY']._serialized_end=408
  _globals['_CREATEJOBOUTPUT']._serialized_start=410
  _globals['_CREATEJOBOUTPUT']._serialized_end=443
  _globals['_DESCRIBEJOBINPUT']._serialized_start=445
  _globals['_DESCRIBEJOBINPUT']._serialized_end=479
  _globals['_DESCRIBEJOBOUTPUT']._serialized_start=481
  _globals['_DESCRIBEJOBOUTPUT']._serialized_end=533
  _globals['_LISTJOBSINPUT']._serialized_start=536
  _globals['_LISTJOBSINPUT']._serialized_end=788
  _globals['_LISTJOBSINPUT_FILTER']._serialized_start=638
  _globals['_LISTJOBSINPUT_FILTER']._serialized_end=788
  _globals['_LISTJOBSOUTPUT']._serialized_start=790
  _globals['_LISTJOBSOUTPUT']._serialized_end=856
  _globals['_WORKERSERVICE']._serialized_start=859
  _globals['_WORKERSERVICE']._serialized_end=1223
# @@protoc_insertion_point(module_scope)
