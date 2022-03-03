# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cafe.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncafe.proto\x12\x04\x63\x61\x66\x65\" \n\rClientRequest\x12\x0f\n\x07product\x18\x01 \x01(\t\"\x1a\n\x07Weekday\x12\x0f\n\x07weekday\x18\x01 \x01(\x05\"\x9e\x01\n\x0bProductInfo\x12\x0f\n\x07product\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\x12\x0f\n\x07\x66lavors\x18\x03 \x01(\t\x12\x34\n\x0c\x61vailability\x18\x04 \x01(\x0e\x32\x1e.cafe.ProductInfo.Availability\"(\n\x0c\x41vailability\x12\n\n\x06\x41lways\x10\x00\x12\x0c\n\x08Weekends\x10\x01\"6\n\x0cSpecialDrink\x12\x0f\n\x07product\x18\x01 \x01(\t\x12\x15\n\rspecial_price\x18\x02 \x01(\x02\"\x1d\n\tHoursInfo\x12\x10\n\x08opens_at\x18\x01 \x01(\t2s\n\x04Menu\x12\x33\n\x07Pricing\x12\x13.cafe.ClientRequest\x1a\x11.cafe.ProductInfo\"\x00\x12\x36\n\x0fSpecialOfTheDay\x12\r.cafe.Weekday\x1a\x12.cafe.SpecialDrink\"\x00\x32<\n\x08\x42usiness\x12\x30\n\x0cOpeningHours\x12\r.cafe.Weekday\x1a\x0f.cafe.HoursInfo\"\x00\x42*\n\x15io.grpc.examples.cafeB\tCafeProtoP\x01\xa2\x02\x03HLWb\x06proto3')



_CLIENTREQUEST = DESCRIPTOR.message_types_by_name['ClientRequest']
_WEEKDAY = DESCRIPTOR.message_types_by_name['Weekday']
_PRODUCTINFO = DESCRIPTOR.message_types_by_name['ProductInfo']
_SPECIALDRINK = DESCRIPTOR.message_types_by_name['SpecialDrink']
_HOURSINFO = DESCRIPTOR.message_types_by_name['HoursInfo']
_PRODUCTINFO_AVAILABILITY = _PRODUCTINFO.enum_types_by_name['Availability']
ClientRequest = _reflection.GeneratedProtocolMessageType('ClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTREQUEST,
  '__module__' : 'cafe_pb2'
  # @@protoc_insertion_point(class_scope:cafe.ClientRequest)
  })
_sym_db.RegisterMessage(ClientRequest)

Weekday = _reflection.GeneratedProtocolMessageType('Weekday', (_message.Message,), {
  'DESCRIPTOR' : _WEEKDAY,
  '__module__' : 'cafe_pb2'
  # @@protoc_insertion_point(class_scope:cafe.Weekday)
  })
_sym_db.RegisterMessage(Weekday)

ProductInfo = _reflection.GeneratedProtocolMessageType('ProductInfo', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCTINFO,
  '__module__' : 'cafe_pb2'
  # @@protoc_insertion_point(class_scope:cafe.ProductInfo)
  })
_sym_db.RegisterMessage(ProductInfo)

SpecialDrink = _reflection.GeneratedProtocolMessageType('SpecialDrink', (_message.Message,), {
  'DESCRIPTOR' : _SPECIALDRINK,
  '__module__' : 'cafe_pb2'
  # @@protoc_insertion_point(class_scope:cafe.SpecialDrink)
  })
_sym_db.RegisterMessage(SpecialDrink)

HoursInfo = _reflection.GeneratedProtocolMessageType('HoursInfo', (_message.Message,), {
  'DESCRIPTOR' : _HOURSINFO,
  '__module__' : 'cafe_pb2'
  # @@protoc_insertion_point(class_scope:cafe.HoursInfo)
  })
_sym_db.RegisterMessage(HoursInfo)

_MENU = DESCRIPTOR.services_by_name['Menu']
_BUSINESS = DESCRIPTOR.services_by_name['Business']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025io.grpc.examples.cafeB\tCafeProtoP\001\242\002\003HLW'
  _CLIENTREQUEST._serialized_start=20
  _CLIENTREQUEST._serialized_end=52
  _WEEKDAY._serialized_start=54
  _WEEKDAY._serialized_end=80
  _PRODUCTINFO._serialized_start=83
  _PRODUCTINFO._serialized_end=241
  _PRODUCTINFO_AVAILABILITY._serialized_start=201
  _PRODUCTINFO_AVAILABILITY._serialized_end=241
  _SPECIALDRINK._serialized_start=243
  _SPECIALDRINK._serialized_end=297
  _HOURSINFO._serialized_start=299
  _HOURSINFO._serialized_end=328
  _MENU._serialized_start=330
  _MENU._serialized_end=445
  _BUSINESS._serialized_start=447
  _BUSINESS._serialized_end=507
# @@protoc_insertion_point(module_scope)
