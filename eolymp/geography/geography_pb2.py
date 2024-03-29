# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/geography/geography.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.geography import country_pb2 as eolymp_dot_geography_dot_country__pb2
from eolymp.geography import region_pb2 as eolymp_dot_geography_dot_region__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n eolymp/geography/geography.proto\x12\x10\x65olymp.geography\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/geography/country.proto\x1a\x1d\x65olymp/geography/region.proto\x1a!eolymp/wellknown/expression.proto\"*\n\x14\x44\x65scribeCountryInput\x12\x12\n\ncountry_id\x18\x01 \x01(\t\"C\n\x15\x44\x65scribeCountryOutput\x12*\n\x07\x63ountry\x18\x01 \x01(\x0b\x32\x19.eolymp.geography.Country\"\xe7\x01\n\x12ListCountriesInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12<\n\x07\x66ilters\x18( \x01(\x0b\x32+.eolymp.geography.ListCountriesInput.Filter\x1au\n\x06\x46ilter\x12\r\n\x05query\x18\x01 \x01(\t\x12*\n\x02id\x18\x02 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x30\n\x04name\x18\x03 \x03(\x0b\x32\".eolymp.wellknown.ExpressionString\"N\n\x13ListCountriesOutput\x12(\n\x05items\x18\x01 \x03(\x0b\x32\x19.eolymp.geography.Country\x12\r\n\x05total\x18\x02 \x01(\x05\"(\n\x13\x44\x65scribeRegionInput\x12\x11\n\tregion_id\x18\x01 \x01(\t\"@\n\x14\x44\x65scribeRegionOutput\x12(\n\x06region\x18\x01 \x01(\x0b\x32\x18.eolymp.geography.Region\"\xac\x02\n\x10ListRegionsInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12:\n\x07\x66ilters\x18( \x01(\x0b\x32).eolymp.geography.ListRegionsInput.Filter\x12\x12\n\ncountry_id\x18\x01 \x01(\t\x1a\xa9\x01\n\x06\x46ilter\x12\r\n\x05query\x18\x01 \x01(\t\x12*\n\x02id\x18\x02 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x32\n\ncountry_id\x18\x03 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x30\n\x04name\x18\x04 \x03(\x0b\x32\".eolymp.wellknown.ExpressionString\"K\n\x11ListRegionsOutput\x12\'\n\x05items\x18\x01 \x03(\x0b\x32\x18.eolymp.geography.Region\x12\r\n\x05total\x18\x02 \x01(\x05\x32\xfd\x05\n\tGeography\x12\x9d\x01\n\x0f\x44\x65scribeCountry\x12&.eolymp.geography.DescribeCountryInput\x1a\'.eolymp.geography.DescribeCountryOutput\"9\xea\xe2\n\x0c\xf5\xe2\n\x00\x00HB\xf8\xe2\n\xf4\x03\x82\xd3\xe4\x93\x02#\x12!/geography/countries/{country_id}\x12\x8a\x01\n\rListCountries\x12$.eolymp.geography.ListCountriesInput\x1a%.eolymp.geography.ListCountriesOutput\",\xea\xe2\n\x0c\xf5\xe2\n\x00\x00HB\xf8\xe2\n\xf4\x03\x82\xd3\xe4\x93\x02\x16\x12\x14/geography/countries\x12\x97\x01\n\x0e\x44\x65scribeRegion\x12%.eolymp.geography.DescribeRegionInput\x1a&.eolymp.geography.DescribeRegionOutput\"6\xea\xe2\n\x0c\xf5\xe2\n\x00\x00HB\xf8\xe2\n\xf4\x03\x82\xd3\xe4\x93\x02 \x12\x1e/geography/regions/{region_id}\x12\x82\x01\n\x0bListRegions\x12\".eolymp.geography.ListRegionsInput\x1a#.eolymp.geography.ListRegionsOutput\"*\xea\xe2\n\x0c\xf5\xe2\n\x00\x00HB\xf8\xe2\n\xf4\x03\x82\xd3\xe4\x93\x02\x14\x12\x12/geography/regions\x12\xa3\x01\n\x15\x44\x65precatedListRegions\x12\".eolymp.geography.ListRegionsInput\x1a#.eolymp.geography.ListRegionsOutput\"A\xea\xe2\n\x0c\xf5\xe2\n\x00\x00HB\xf8\xe2\n\xf4\x03\x82\xd3\xe4\x93\x02+\x12)/geography/countries/{country_id}/regionsB5Z3github.com/eolymp/go-sdk/eolymp/geography;geographyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.geography.geography_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/eolymp/go-sdk/eolymp/geography;geography'
  _GEOGRAPHY.methods_by_name['DescribeCountry']._options = None
  _GEOGRAPHY.methods_by_name['DescribeCountry']._serialized_options = b'\352\342\n\014\365\342\n\000\000HB\370\342\n\364\003\202\323\344\223\002#\022!/geography/countries/{country_id}'
  _GEOGRAPHY.methods_by_name['ListCountries']._options = None
  _GEOGRAPHY.methods_by_name['ListCountries']._serialized_options = b'\352\342\n\014\365\342\n\000\000HB\370\342\n\364\003\202\323\344\223\002\026\022\024/geography/countries'
  _GEOGRAPHY.methods_by_name['DescribeRegion']._options = None
  _GEOGRAPHY.methods_by_name['DescribeRegion']._serialized_options = b'\352\342\n\014\365\342\n\000\000HB\370\342\n\364\003\202\323\344\223\002 \022\036/geography/regions/{region_id}'
  _GEOGRAPHY.methods_by_name['ListRegions']._options = None
  _GEOGRAPHY.methods_by_name['ListRegions']._serialized_options = b'\352\342\n\014\365\342\n\000\000HB\370\342\n\364\003\202\323\344\223\002\024\022\022/geography/regions'
  _GEOGRAPHY.methods_by_name['DeprecatedListRegions']._options = None
  _GEOGRAPHY.methods_by_name['DeprecatedListRegions']._serialized_options = b'\352\342\n\014\365\342\n\000\000HB\370\342\n\364\003\202\323\344\223\002+\022)/geography/countries/{country_id}/regions'
  _DESCRIBECOUNTRYINPUT._serialized_start=219
  _DESCRIBECOUNTRYINPUT._serialized_end=261
  _DESCRIBECOUNTRYOUTPUT._serialized_start=263
  _DESCRIBECOUNTRYOUTPUT._serialized_end=330
  _LISTCOUNTRIESINPUT._serialized_start=333
  _LISTCOUNTRIESINPUT._serialized_end=564
  _LISTCOUNTRIESINPUT_FILTER._serialized_start=447
  _LISTCOUNTRIESINPUT_FILTER._serialized_end=564
  _LISTCOUNTRIESOUTPUT._serialized_start=566
  _LISTCOUNTRIESOUTPUT._serialized_end=644
  _DESCRIBEREGIONINPUT._serialized_start=646
  _DESCRIBEREGIONINPUT._serialized_end=686
  _DESCRIBEREGIONOUTPUT._serialized_start=688
  _DESCRIBEREGIONOUTPUT._serialized_end=752
  _LISTREGIONSINPUT._serialized_start=755
  _LISTREGIONSINPUT._serialized_end=1055
  _LISTREGIONSINPUT_FILTER._serialized_start=886
  _LISTREGIONSINPUT_FILTER._serialized_end=1055
  _LISTREGIONSOUTPUT._serialized_start=1057
  _LISTREGIONSOUTPUT._serialized_end=1132
  _GEOGRAPHY._serialized_start=1135
  _GEOGRAPHY._serialized_end=1900
# @@protoc_insertion_point(module_scope)
