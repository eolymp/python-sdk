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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n eolymp/geography/geography.proto\x12\x10\x65olymp.geography\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/geography/country.proto\"*\n\x14\x44\x65scribeCountryInput\x12\x12\n\ncountry_id\x18\x01 \x01(\t\"C\n\x15\x44\x65scribeCountryOutput\x12*\n\x07\x63ountry\x18\x01 \x01(\x0b\x32\x19.eolymp.geography.Country\"\x14\n\x12ListCountriesInput\"N\n\x13ListCountriesOutput\x12(\n\x05items\x18\x01 \x03(\x0b\x32\x19.eolymp.geography.Country\x12\r\n\x05total\x18\x02 \x01(\x05\x32\xb8\x02\n\tGeography\x12\x9d\x01\n\x0f\x44\x65scribeCountry\x12&.eolymp.geography.DescribeCountryInput\x1a\'.eolymp.geography.DescribeCountryOutput\"9\xea\xe2\n\x0c\xf5\xe2\n\x00\x00HB\xf8\xe2\n\xf4\x03\x82\xd3\xe4\x93\x02#\x12!/geography/countries/{country_id}\x12\x8a\x01\n\rListCountries\x12$.eolymp.geography.ListCountriesInput\x1a%.eolymp.geography.ListCountriesOutput\",\xea\xe2\n\x0c\xf5\xe2\n\x00\x00HB\xf8\xe2\n\xf4\x03\x82\xd3\xe4\x93\x02\x16\x12\x14/geography/countriesB5Z3github.com/eolymp/go-sdk/eolymp/geography;geographyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.geography.geography_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/eolymp/go-sdk/eolymp/geography;geography'
  _GEOGRAPHY.methods_by_name['DescribeCountry']._options = None
  _GEOGRAPHY.methods_by_name['DescribeCountry']._serialized_options = b'\352\342\n\014\365\342\n\000\000HB\370\342\n\364\003\202\323\344\223\002#\022!/geography/countries/{country_id}'
  _GEOGRAPHY.methods_by_name['ListCountries']._options = None
  _GEOGRAPHY.methods_by_name['ListCountries']._serialized_options = b'\352\342\n\014\365\342\n\000\000HB\370\342\n\364\003\202\323\344\223\002\026\022\024/geography/countries'
  _DESCRIBECOUNTRYINPUT._serialized_start=153
  _DESCRIBECOUNTRYINPUT._serialized_end=195
  _DESCRIBECOUNTRYOUTPUT._serialized_start=197
  _DESCRIBECOUNTRYOUTPUT._serialized_end=264
  _LISTCOUNTRIESINPUT._serialized_start=266
  _LISTCOUNTRIESINPUT._serialized_end=286
  _LISTCOUNTRIESOUTPUT._serialized_start=288
  _LISTCOUNTRIESOUTPUT._serialized_end=366
  _GEOGRAPHY._serialized_start=369
  _GEOGRAPHY._serialized_end=681
# @@protoc_insertion_point(module_scope)
