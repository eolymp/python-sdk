# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/community/tier_service.proto
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
from eolymp.commerce import price_pb2 as eolymp_dot_commerce_dot_price__pb2
from eolymp.community import tier_pb2 as eolymp_dot_community_dot_tier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#eolymp/community/tier_service.proto\x12\x10\x65olymp.community\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\x1b\x65olymp/commerce/price.proto\x1a\x1b\x65olymp/community/tier.proto\"N\n\x0eListTiersInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x0e\n\x06render\x18\x64 \x01(\x08\x12\x0e\n\x06locale\x18\x65 \x01(\t\"G\n\x0fListTiersOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12%\n\x05items\x18\x02 \x03(\x0b\x32\x16.eolymp.community.Tier\"D\n\x11\x44\x65scribeTierInput\x12\x0f\n\x07tier_id\x18\x01 \x01(\t\x12\x0e\n\x06render\x18\x64 \x01(\x08\x12\x0e\n\x06locale\x18\x65 \x01(\t\":\n\x12\x44\x65scribeTierOutput\x12$\n\x04tier\x18\x01 \x01(\x0b\x32\x16.eolymp.community.Tier\"8\n\x13ListTierPricesInput\x12\x0f\n\x07tier_id\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\"=\n\x14ListTierPricesOutput\x12%\n\x05items\x18\x01 \x03(\x0b\x32\x16.eolymp.commerce.Price2\xcc\x03\n\x0bTierService\x12\x9d\x01\n\x0c\x44\x65scribeTier\x12#.eolymp.community.DescribeTierInput\x1a$.eolymp.community.DescribeTierOutput\"B\x82\xe3\n\x17\x8a\xe3\n\x13\x63ommunity:tier:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n2\x82\xd3\xe4\x93\x02\x12\x12\x10/tiers/{tier_id}\x12\x8a\x01\n\tListTiers\x12 .eolymp.community.ListTiersInput\x1a!.eolymp.community.ListTiersOutput\"8\x82\xe3\n\x17\x8a\xe3\n\x13\x63ommunity:tier:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x08\x12\x06/tiers\x12\x8f\x01\n\x0eListTierPrices\x12%.eolymp.community.ListTierPricesInput\x1a&.eolymp.community.ListTierPricesOutput\".\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x19\x12\x17/tiers/{tier_id}/pricesB5Z3github.com/eolymp/go-sdk/eolymp/community;communityb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.community.tier_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/eolymp/go-sdk/eolymp/community;community'
  _TIERSERVICE.methods_by_name['DescribeTier']._options = None
  _TIERSERVICE.methods_by_name['DescribeTier']._serialized_options = b'\202\343\n\027\212\343\n\023community:tier:read\352\342\n\013\365\342\n\000\000\240@\370\342\n2\202\323\344\223\002\022\022\020/tiers/{tier_id}'
  _TIERSERVICE.methods_by_name['ListTiers']._options = None
  _TIERSERVICE.methods_by_name['ListTiers']._serialized_options = b'\202\343\n\027\212\343\n\023community:tier:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\010\022\006/tiers'
  _TIERSERVICE.methods_by_name['ListTierPrices']._options = None
  _TIERSERVICE.methods_by_name['ListTierPrices']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\031\022\027/tiers/{tier_id}/prices'
  _LISTTIERSINPUT._serialized_start=214
  _LISTTIERSINPUT._serialized_end=292
  _LISTTIERSOUTPUT._serialized_start=294
  _LISTTIERSOUTPUT._serialized_end=365
  _DESCRIBETIERINPUT._serialized_start=367
  _DESCRIBETIERINPUT._serialized_end=435
  _DESCRIBETIEROUTPUT._serialized_start=437
  _DESCRIBETIEROUTPUT._serialized_end=495
  _LISTTIERPRICESINPUT._serialized_start=497
  _LISTTIERPRICESINPUT._serialized_end=553
  _LISTTIERPRICESOUTPUT._serialized_start=555
  _LISTTIERPRICESOUTPUT._serialized_end=616
  _TIERSERVICE._serialized_start=619
  _TIERSERVICE._serialized_end=1079
# @@protoc_insertion_point(module_scope)