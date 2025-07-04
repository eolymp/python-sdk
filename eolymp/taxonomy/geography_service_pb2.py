# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/taxonomy/geography_service.proto
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
    'eolymp/taxonomy/geography_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.taxonomy import geography_country_pb2 as eolymp_dot_taxonomy_dot_geography__country__pb2
from eolymp.taxonomy import geography_region_pb2 as eolymp_dot_taxonomy_dot_geography__region__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'eolymp/taxonomy/geography_service.proto\x12\x0f\x65olymp.taxonomy\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\'eolymp/taxonomy/geography_country.proto\x1a&eolymp/taxonomy/geography_region.proto\x1a!eolymp/wellknown/expression.proto\"*\n\x14\x44\x65scribeCountryInput\x12\x12\n\ncountry_id\x18\x01 \x01(\t\"B\n\x15\x44\x65scribeCountryOutput\x12)\n\x07\x63ountry\x18\x01 \x01(\x0b\x32\x18.eolymp.taxonomy.Country\"\xe6\x01\n\x12ListCountriesInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12;\n\x07\x66ilters\x18( \x01(\x0b\x32*.eolymp.taxonomy.ListCountriesInput.Filter\x1au\n\x06\x46ilter\x12\r\n\x05query\x18\x01 \x01(\t\x12*\n\x02id\x18\x02 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x30\n\x04name\x18\x03 \x03(\x0b\x32\".eolymp.wellknown.ExpressionString\"M\n\x13ListCountriesOutput\x12\'\n\x05items\x18\x01 \x03(\x0b\x32\x18.eolymp.taxonomy.Country\x12\r\n\x05total\x18\x02 \x01(\x05\"(\n\x13\x44\x65scribeRegionInput\x12\x11\n\tregion_id\x18\x01 \x01(\t\"?\n\x14\x44\x65scribeRegionOutput\x12\'\n\x06region\x18\x01 \x01(\x0b\x32\x17.eolymp.taxonomy.Region\"\x97\x02\n\x10ListRegionsInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x39\n\x07\x66ilters\x18( \x01(\x0b\x32(.eolymp.taxonomy.ListRegionsInput.Filter\x1a\xa9\x01\n\x06\x46ilter\x12\r\n\x05query\x18\x01 \x01(\t\x12*\n\x02id\x18\x02 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x32\n\ncountry_id\x18\x03 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x30\n\x04name\x18\x04 \x03(\x0b\x32\".eolymp.wellknown.ExpressionString\"J\n\x11ListRegionsOutput\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.eolymp.taxonomy.Region\x12\r\n\x05total\x18\x02 \x01(\x05\x32\xac\x04\n\x10GeographyService\x12~\n\rListCountries\x12#.eolymp.taxonomy.ListCountriesInput\x1a$.eolymp.taxonomy.ListCountriesOutput\"\"\xea\xe2\n\x0c\xf5\xe2\n\x00\x00HB\xf8\xe2\n\xf4\x03\x82\xd3\xe4\x93\x02\x0c\x12\n/countries\x12\x91\x01\n\x0f\x44\x65scribeCountry\x12%.eolymp.taxonomy.DescribeCountryInput\x1a&.eolymp.taxonomy.DescribeCountryOutput\"/\xea\xe2\n\x0c\xf5\xe2\n\x00\x00HB\xf8\xe2\n\xf4\x03\x82\xd3\xe4\x93\x02\x19\x12\x17/countries/{country_id}\x12v\n\x0bListRegions\x12!.eolymp.taxonomy.ListRegionsInput\x1a\".eolymp.taxonomy.ListRegionsOutput\" \xea\xe2\n\x0c\xf5\xe2\n\x00\x00HB\xf8\xe2\n\xf4\x03\x82\xd3\xe4\x93\x02\n\x12\x08/regions\x12\x8b\x01\n\x0e\x44\x65scribeRegion\x12$.eolymp.taxonomy.DescribeRegionInput\x1a%.eolymp.taxonomy.DescribeRegionOutput\",\xea\xe2\n\x0c\xf5\xe2\n\x00\x00HB\xf8\xe2\n\xf4\x03\x82\xd3\xe4\x93\x02\x16\x12\x14/regions/{region_id}B3Z1github.com/eolymp/go-sdk/eolymp/taxonomy;taxonomyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.taxonomy.geography_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/eolymp/go-sdk/eolymp/taxonomy;taxonomy'
  _globals['_GEOGRAPHYSERVICE'].methods_by_name['ListCountries']._loaded_options = None
  _globals['_GEOGRAPHYSERVICE'].methods_by_name['ListCountries']._serialized_options = b'\352\342\n\014\365\342\n\000\000HB\370\342\n\364\003\202\323\344\223\002\014\022\n/countries'
  _globals['_GEOGRAPHYSERVICE'].methods_by_name['DescribeCountry']._loaded_options = None
  _globals['_GEOGRAPHYSERVICE'].methods_by_name['DescribeCountry']._serialized_options = b'\352\342\n\014\365\342\n\000\000HB\370\342\n\364\003\202\323\344\223\002\031\022\027/countries/{country_id}'
  _globals['_GEOGRAPHYSERVICE'].methods_by_name['ListRegions']._loaded_options = None
  _globals['_GEOGRAPHYSERVICE'].methods_by_name['ListRegions']._serialized_options = b'\352\342\n\014\365\342\n\000\000HB\370\342\n\364\003\202\323\344\223\002\n\022\010/regions'
  _globals['_GEOGRAPHYSERVICE'].methods_by_name['DescribeRegion']._loaded_options = None
  _globals['_GEOGRAPHYSERVICE'].methods_by_name['DescribeRegion']._serialized_options = b'\352\342\n\014\365\342\n\000\000HB\370\342\n\364\003\202\323\344\223\002\026\022\024/regions/{region_id}'
  _globals['_DESCRIBECOUNTRYINPUT']._serialized_start=243
  _globals['_DESCRIBECOUNTRYINPUT']._serialized_end=285
  _globals['_DESCRIBECOUNTRYOUTPUT']._serialized_start=287
  _globals['_DESCRIBECOUNTRYOUTPUT']._serialized_end=353
  _globals['_LISTCOUNTRIESINPUT']._serialized_start=356
  _globals['_LISTCOUNTRIESINPUT']._serialized_end=586
  _globals['_LISTCOUNTRIESINPUT_FILTER']._serialized_start=469
  _globals['_LISTCOUNTRIESINPUT_FILTER']._serialized_end=586
  _globals['_LISTCOUNTRIESOUTPUT']._serialized_start=588
  _globals['_LISTCOUNTRIESOUTPUT']._serialized_end=665
  _globals['_DESCRIBEREGIONINPUT']._serialized_start=667
  _globals['_DESCRIBEREGIONINPUT']._serialized_end=707
  _globals['_DESCRIBEREGIONOUTPUT']._serialized_start=709
  _globals['_DESCRIBEREGIONOUTPUT']._serialized_end=772
  _globals['_LISTREGIONSINPUT']._serialized_start=775
  _globals['_LISTREGIONSINPUT']._serialized_end=1054
  _globals['_LISTREGIONSINPUT_FILTER']._serialized_start=885
  _globals['_LISTREGIONSINPUT_FILTER']._serialized_end=1054
  _globals['_LISTREGIONSOUTPUT']._serialized_start=1056
  _globals['_LISTREGIONSOUTPUT']._serialized_end=1130
  _globals['_GEOGRAPHYSERVICE']._serialized_start=1133
  _globals['_GEOGRAPHYSERVICE']._serialized_end=1689
# @@protoc_insertion_point(module_scope)
