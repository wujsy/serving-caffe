# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: obj_detector.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='obj_detector.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_pb=_b('\n\x12obj_detector.proto\x12\x12tensorflow.serving\"o\n\tDetection\x12\x0e\n\x06roi_x1\x18\x01 \x01(\x05\x12\x0e\n\x06roi_x2\x18\x02 \x01(\x05\x12\x0e\n\x06roi_y1\x18\x03 \x01(\x05\x12\x0e\n\x06roi_y2\x18\x04 \x01(\x05\x12\x13\n\x0b\x63lass_label\x18\x05 \x01(\t\x12\r\n\x05score\x18\x06 \x01(\x02\"@\n\rDetectRequest\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\x12\x1b\n\x13min_score_threshold\x18\x02 \x01(\x02\"C\n\x0e\x44\x65tectResponse\x12\x31\n\ndetections\x18\x01 \x03(\x0b\x32\x1d.tensorflow.serving.Detection\"\x16\n\x14\x43onfigurationRequest\"0\n\x13\x44\x65tectConfiguration\x12\x19\n\x11input_image_shape\x18\x01 \x03(\x05\x32\xc7\x01\n\rDetectService\x12\x65\n\x10GetConfiguration\x12(.tensorflow.serving.ConfigurationRequest\x1a\'.tensorflow.serving.DetectConfiguration\x12O\n\x06\x44\x65tect\x12!.tensorflow.serving.DetectRequest\x1a\".tensorflow.serving.DetectResponseb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DETECTION = _descriptor.Descriptor(
  name='Detection',
  full_name='tensorflow.serving.Detection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roi_x1', full_name='tensorflow.serving.Detection.roi_x1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roi_x2', full_name='tensorflow.serving.Detection.roi_x2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roi_y1', full_name='tensorflow.serving.Detection.roi_y1', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roi_y2', full_name='tensorflow.serving.Detection.roi_y2', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_label', full_name='tensorflow.serving.Detection.class_label', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='tensorflow.serving.Detection.score', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=153,
)


_DETECTREQUEST = _descriptor.Descriptor(
  name='DetectRequest',
  full_name='tensorflow.serving.DetectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_data', full_name='tensorflow.serving.DetectRequest.image_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_score_threshold', full_name='tensorflow.serving.DetectRequest.min_score_threshold', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=219,
)


_DETECTRESPONSE = _descriptor.Descriptor(
  name='DetectResponse',
  full_name='tensorflow.serving.DetectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='detections', full_name='tensorflow.serving.DetectResponse.detections', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=221,
  serialized_end=288,
)


_CONFIGURATIONREQUEST = _descriptor.Descriptor(
  name='ConfigurationRequest',
  full_name='tensorflow.serving.ConfigurationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=312,
)


_DETECTCONFIGURATION = _descriptor.Descriptor(
  name='DetectConfiguration',
  full_name='tensorflow.serving.DetectConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_image_shape', full_name='tensorflow.serving.DetectConfiguration.input_image_shape', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=362,
)

_DETECTRESPONSE.fields_by_name['detections'].message_type = _DETECTION
DESCRIPTOR.message_types_by_name['Detection'] = _DETECTION
DESCRIPTOR.message_types_by_name['DetectRequest'] = _DETECTREQUEST
DESCRIPTOR.message_types_by_name['DetectResponse'] = _DETECTRESPONSE
DESCRIPTOR.message_types_by_name['ConfigurationRequest'] = _CONFIGURATIONREQUEST
DESCRIPTOR.message_types_by_name['DetectConfiguration'] = _DETECTCONFIGURATION

Detection = _reflection.GeneratedProtocolMessageType('Detection', (_message.Message,), dict(
  DESCRIPTOR = _DETECTION,
  __module__ = 'obj_detector_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.Detection)
  ))
_sym_db.RegisterMessage(Detection)

DetectRequest = _reflection.GeneratedProtocolMessageType('DetectRequest', (_message.Message,), dict(
  DESCRIPTOR = _DETECTREQUEST,
  __module__ = 'obj_detector_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.DetectRequest)
  ))
_sym_db.RegisterMessage(DetectRequest)

DetectResponse = _reflection.GeneratedProtocolMessageType('DetectResponse', (_message.Message,), dict(
  DESCRIPTOR = _DETECTRESPONSE,
  __module__ = 'obj_detector_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.DetectResponse)
  ))
_sym_db.RegisterMessage(DetectResponse)

ConfigurationRequest = _reflection.GeneratedProtocolMessageType('ConfigurationRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONREQUEST,
  __module__ = 'obj_detector_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.ConfigurationRequest)
  ))
_sym_db.RegisterMessage(ConfigurationRequest)

DetectConfiguration = _reflection.GeneratedProtocolMessageType('DetectConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _DETECTCONFIGURATION,
  __module__ = 'obj_detector_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.DetectConfiguration)
  ))
_sym_db.RegisterMessage(DetectConfiguration)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class DetectServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConfiguration = channel.unary_unary(
        '/tensorflow.serving.DetectService/GetConfiguration',
        request_serializer=ConfigurationRequest.SerializeToString,
        response_deserializer=DetectConfiguration.FromString,
        )
    self.Detect = channel.unary_unary(
        '/tensorflow.serving.DetectService/Detect',
        request_serializer=DetectRequest.SerializeToString,
        response_deserializer=DetectResponse.FromString,
        )


class DetectServiceServicer(object):

  def GetConfiguration(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Detect(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DetectServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConfiguration': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfiguration,
          request_deserializer=ConfigurationRequest.FromString,
          response_serializer=DetectConfiguration.SerializeToString,
      ),
      'Detect': grpc.unary_unary_rpc_method_handler(
          servicer.Detect,
          request_deserializer=DetectRequest.FromString,
          response_serializer=DetectResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tensorflow.serving.DetectService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaDetectServiceServicer(object):
  def GetConfiguration(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Detect(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaDetectServiceStub(object):
  def GetConfiguration(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  GetConfiguration.future = None
  def Detect(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Detect.future = None


def beta_create_DetectService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('tensorflow.serving.DetectService', 'Detect'): DetectRequest.FromString,
    ('tensorflow.serving.DetectService', 'GetConfiguration'): ConfigurationRequest.FromString,
  }
  response_serializers = {
    ('tensorflow.serving.DetectService', 'Detect'): DetectResponse.SerializeToString,
    ('tensorflow.serving.DetectService', 'GetConfiguration'): DetectConfiguration.SerializeToString,
  }
  method_implementations = {
    ('tensorflow.serving.DetectService', 'Detect'): face_utilities.unary_unary_inline(servicer.Detect),
    ('tensorflow.serving.DetectService', 'GetConfiguration'): face_utilities.unary_unary_inline(servicer.GetConfiguration),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_DetectService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('tensorflow.serving.DetectService', 'Detect'): DetectRequest.SerializeToString,
    ('tensorflow.serving.DetectService', 'GetConfiguration'): ConfigurationRequest.SerializeToString,
  }
  response_deserializers = {
    ('tensorflow.serving.DetectService', 'Detect'): DetectResponse.FromString,
    ('tensorflow.serving.DetectService', 'GetConfiguration'): DetectConfiguration.FromString,
  }
  cardinalities = {
    'Detect': cardinality.Cardinality.UNARY_UNARY,
    'GetConfiguration': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'tensorflow.serving.DetectService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
