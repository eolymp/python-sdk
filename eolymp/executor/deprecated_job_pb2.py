# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/executor/deprecated_job.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.executor import task_pb2 as eolymp_dot_executor_dot_task__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$eolymp/executor/deprecated_job.proto\x12\x0f\x65olymp.executor\x1a\x1a\x65olymp/executor/task.proto\"\xfa\x0e\n\x03Job\x12\x11\n\treference\x18\x01 \x01(\t\x12\x0e\n\x06origin\x18\x02 \x01(\t\x12\x39\n\rpreconditions\x18\n \x03(\x0b\x32\".eolymp.executor.Task.Precondition\x12*\n\x06\x61\x63tors\x18\x14 \x03(\x0b\x32\x1a.eolymp.executor.Job.Actor\x12+\n\x08scenario\x18( \x03(\x0b\x32\x19.eolymp.executor.Job.Step\x12&\n\x04runs\x18\x1e \x03(\x0b\x32\x18.eolymp.executor.Job.Run\x1a\x88\x03\n\x05\x41\x63tor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07runtime\x18\n \x01(\t\x12\x12\n\nsource_url\x18\x0e \x01(\t\x12\x12\n\nheader_url\x18\x0f \x01(\t\x12\x12\n\nfooter_url\x18\x10 \x01(\t\x12\x30\n\x03\x65nv\x18( \x03(\x0b\x32#.eolymp.executor.Job.Actor.EnvEntry\x12(\n\x05\x66iles\x18) \x03(\x0b\x32\x19.eolymp.executor.Job.File\x12>\n\routput_format\x18# \x01(\x0e\x32\'.eolymp.executor.Job.Actor.OutputFormat\x12)\n\x05mount\x18\x32 \x03(\x0b\x32\x1a.eolymp.executor.Job.Mount\x1a*\n\x08\x45nvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"1\n\x0cOutputFormat\x12\r\n\tEXIT_CODE\x10\x00\x12\x12\n\x0eTESTLIB_OUTPUT\x10\x01\x1a,\n\x05Mount\x12\x12\n\nfrom_actor\x18\x01 \x01(\t\x12\x0f\n\x07to_path\x18\x02 \x01(\t\x1a(\n\x04\x46ile\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x12\n\nsource_url\x18\x03 \x01(\t\x1a\x61\n\x03Run\x12\x11\n\treference\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\r\x12\x0e\n\x06labels\x18\n \x03(\t\x12(\n\x05steps\x18\x14 \x03(\x0b\x32\x19.eolymp.executor.Job.Step\x1a\xcd\x08\n\x04Step\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0f\x65ven_on_failure\x18\x64 \x01(\x08\x12\x17\n\x0fonly_on_failure\x18\x65 \x01(\x08\x12\x30\n\x05write\x18\n \x01(\x0b\x32\x1f.eolymp.executor.Job.Step.WriteH\x00\x12.\n\x04\x63opy\x18\x0b \x01(\x0b\x32\x1e.eolymp.executor.Job.Step.CopyH\x00\x12\x34\n\x07\x65xecute\x18\x0c \x01(\x0b\x32!.eolymp.executor.Job.Step.ExecuteH\x00\x12\x32\n\x06upload\x18\r \x01(\x0b\x32 .eolymp.executor.Job.Step.UploadH\x00\x12\x30\n\x05group\x18\x0e \x01(\x0b\x32\x1f.eolymp.executor.Job.Step.GroupH\x00\x1aX\n\x05Write\x12\x12\n\nsource_url\x18\x05 \x01(\t\x12\x14\n\x0ctarget_actor\x18\x02 \x01(\t\x12\x13\n\x0btarget_path\x18\x03 \x01(\t\x12\x10\n\x08\x66ix_crlf\x18\x04 \x01(\x08\x1a\xa8\x01\n\x06Upload\x12\x14\n\x0csource_actor\x18\x01 \x01(\t\x12\x13\n\x0bsource_path\x18\x02 \x01(\t\x12\x13\n\x0btarget_name\x18\x03 \x01(\t\x12\x12\n\noptionally\x18\x04 \x01(\x08\x12\x0b\n\x03ttl\x18\x05 \x01(\r\x12\x10\n\x08max_size\x18\x06 \x01(\r\x12\x15\n\rmax_data_size\x18\x07 \x01(\r\x12\x14\n\x0c\x66orce_upload\x18\x08 \x01(\x08\x1a\x87\x01\n\x04\x43opy\x12\x14\n\x0csource_actor\x18\x01 \x01(\t\x12\x13\n\x0bsource_path\x18\x02 \x01(\t\x12\x14\n\x0ctarget_actor\x18\x03 \x01(\t\x12\x13\n\x0btarget_path\x18\x04 \x01(\t\x12\x12\n\noptionally\x18\x05 \x01(\x08\x12\x15\n\rremove_source\x18\x06 \x01(\x08\x1a\xae\x02\n\x07\x45xecute\x12\r\n\x05\x61\x63tor\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\x12\x37\n\x03\x65nv\x18\x03 \x03(\x0b\x32*.eolymp.executor.Job.Step.Execute.EnvEntry\x12\r\n\x05stdin\x18\x1e \x01(\t\x12\x0e\n\x06stdout\x18\x1f \x01(\t\x12\x0e\n\x06stderr\x18  \x01(\t\x12\x12\n\nstdin_last\x18! \x01(\x08\x12\x17\n\x0fwall_time_limit\x18\n \x01(\r\x12\x16\n\x0e\x63pu_time_limit\x18\x0b \x01(\r\x12\x14\n\x0cmemory_limit\x18\x0c \x01(\x04\x12\x17\n\x0f\x66ile_size_limit\x18\r \x01(\x04\x1a*\n\x08\x45nvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a=\n\x05Group\x12\x34\n\tprocesses\x18\x01 \x03(\x0b\x32!.eolymp.executor.Job.Step.ExecuteB\x08\n\x06\x61\x63tionB3Z1github.com/eolymp/go-sdk/eolymp/executor;executorb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.executor.deprecated_job_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/eolymp/go-sdk/eolymp/executor;executor'
  _JOB_ACTOR_ENVENTRY._options = None
  _JOB_ACTOR_ENVENTRY._serialized_options = b'8\001'
  _JOB_STEP_EXECUTE_ENVENTRY._options = None
  _JOB_STEP_EXECUTE_ENVENTRY._serialized_options = b'8\001'
  _JOB._serialized_start=86
  _JOB._serialized_end=2000
  _JOB_ACTOR._serialized_start=317
  _JOB_ACTOR._serialized_end=709
  _JOB_ACTOR_ENVENTRY._serialized_start=616
  _JOB_ACTOR_ENVENTRY._serialized_end=658
  _JOB_ACTOR_OUTPUTFORMAT._serialized_start=660
  _JOB_ACTOR_OUTPUTFORMAT._serialized_end=709
  _JOB_MOUNT._serialized_start=711
  _JOB_MOUNT._serialized_end=755
  _JOB_FILE._serialized_start=757
  _JOB_FILE._serialized_end=797
  _JOB_RUN._serialized_start=799
  _JOB_RUN._serialized_end=896
  _JOB_STEP._serialized_start=899
  _JOB_STEP._serialized_end=2000
  _JOB_STEP_WRITE._serialized_start=1225
  _JOB_STEP_WRITE._serialized_end=1313
  _JOB_STEP_UPLOAD._serialized_start=1316
  _JOB_STEP_UPLOAD._serialized_end=1484
  _JOB_STEP_COPY._serialized_start=1487
  _JOB_STEP_COPY._serialized_end=1622
  _JOB_STEP_EXECUTE._serialized_start=1625
  _JOB_STEP_EXECUTE._serialized_end=1927
  _JOB_STEP_EXECUTE_ENVENTRY._serialized_start=616
  _JOB_STEP_EXECUTE_ENVENTRY._serialized_end=658
  _JOB_STEP_GROUP._serialized_start=1929
  _JOB_STEP_GROUP._serialized_end=1990
# @@protoc_insertion_point(module_scope)