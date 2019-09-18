# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fxwatcher.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fxwatcher.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0f\x66xwatcher.proto\x12\x02pb\"0\n\x07Request\x12\r\n\x05input\x18\x01 \x01(\x0c\x12\x16\n\x04info\x18\x02 \x01(\x0b\x32\x08.pb.Info\"\x17\n\x05Reply\x12\x0e\n\x06Output\x18\x01 \x01(\t\"{\n\x04Info\x12\x14\n\x0c\x46unctionName\x18\x01 \x01(\t\x12\x0f\n\x07Timeout\x18\x02 \x01(\t\x12\x0f\n\x07Runtime\x18\x03 \x01(\t\x12\x1d\n\x06Limits\x18\x04 \x01(\x0b\x32\r.pb.Resources\x12\x1c\n\x07Trigger\x18\x05 \x01(\x0b\x32\x0b.pb.Trigger\"4\n\x07Trigger\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\r\n\x05Topic\x18\x02 \x01(\t\x12\x0c\n\x04Time\x18\x03 \x01(\t\"5\n\tResources\x12\x0e\n\x06Memory\x18\x01 \x01(\t\x12\x0b\n\x03\x43PU\x18\x02 \x01(\t\x12\x0b\n\x03GPU\x18\x03 \x01(\t2-\n\tFxWatcher\x12 \n\x04\x43\x61ll\x12\x0b.pb.Request\x1a\t.pb.Reply\"\x00\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='pb.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='pb.Request.input', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='pb.Request.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=71,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='pb.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Output', full_name='pb.Reply.Output', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=96,
)


_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='pb.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FunctionName', full_name='pb.Info.FunctionName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Timeout', full_name='pb.Info.Timeout', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Runtime', full_name='pb.Info.Runtime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Limits', full_name='pb.Info.Limits', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Trigger', full_name='pb.Info.Trigger', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=221,
)


_TRIGGER = _descriptor.Descriptor(
  name='Trigger',
  full_name='pb.Trigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='pb.Trigger.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Topic', full_name='pb.Trigger.Topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Time', full_name='pb.Trigger.Time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=275,
)


_RESOURCES = _descriptor.Descriptor(
  name='Resources',
  full_name='pb.Resources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Memory', full_name='pb.Resources.Memory', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CPU', full_name='pb.Resources.CPU', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='GPU', full_name='pb.Resources.GPU', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=330,
)

_REQUEST.fields_by_name['info'].message_type = _INFO
_INFO.fields_by_name['Limits'].message_type = _RESOURCES
_INFO.fields_by_name['Trigger'].message_type = _TRIGGER
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
DESCRIPTOR.message_types_by_name['Info'] = _INFO
DESCRIPTOR.message_types_by_name['Trigger'] = _TRIGGER
DESCRIPTOR.message_types_by_name['Resources'] = _RESOURCES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'fxwatcher_pb2'
  # @@protoc_insertion_point(class_scope:pb.Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'fxwatcher_pb2'
  # @@protoc_insertion_point(class_scope:pb.Reply)
  })
_sym_db.RegisterMessage(Reply)

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), {
  'DESCRIPTOR' : _INFO,
  '__module__' : 'fxwatcher_pb2'
  # @@protoc_insertion_point(class_scope:pb.Info)
  })
_sym_db.RegisterMessage(Info)

Trigger = _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGER,
  '__module__' : 'fxwatcher_pb2'
  # @@protoc_insertion_point(class_scope:pb.Trigger)
  })
_sym_db.RegisterMessage(Trigger)

Resources = _reflection.GeneratedProtocolMessageType('Resources', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCES,
  '__module__' : 'fxwatcher_pb2'
  # @@protoc_insertion_point(class_scope:pb.Resources)
  })
_sym_db.RegisterMessage(Resources)



_FXWATCHER = _descriptor.ServiceDescriptor(
  name='FxWatcher',
  full_name='pb.FxWatcher',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=332,
  serialized_end=377,
  methods=[
  _descriptor.MethodDescriptor(
    name='Call',
    full_name='pb.FxWatcher.Call',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_REPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FXWATCHER)

DESCRIPTOR.services_by_name['FxWatcher'] = _FXWATCHER

# @@protoc_insertion_point(module_scope)