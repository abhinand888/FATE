# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature-selection-meta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66\x65\x61ture-selection-meta.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\xda\x06\n\x14\x46\x65\x61tureSelectionMeta\x12\x16\n\x0e\x66ilter_methods\x18\x01 \x03(\t\x12\x0c\n\x04\x63ols\x18\x03 \x03(\t\x12L\n\x0bunique_meta\x18\x04 \x01(\x0b\x32\x37.com.webank.ai.fate.core.mlmodel.buffer.UniqueValueMeta\x12S\n\riv_value_meta\x18\x05 \x01(\x0b\x32<.com.webank.ai.fate.core.mlmodel.buffer.IVValueSelectionMeta\x12]\n\x12iv_percentile_meta\x18\x06 \x01(\x0b\x32\x41.com.webank.ai.fate.core.mlmodel.buffer.IVPercentileSelectionMeta\x12]\n\x11variance_coe_meta\x18\x07 \x01(\x0b\x32\x42.com.webank.ai.fate.core.mlmodel.buffer.VarianceOfCoeSelectionMeta\x12V\n\x0coutlier_meta\x18\x08 \x01(\x0b\x32@.com.webank.ai.fate.core.mlmodel.buffer.OutlierColsSelectionMeta\x12Q\n\rmanually_meta\x18\t \x01(\x0b\x32:.com.webank.ai.fate.core.mlmodel.buffer.ManuallyFilterMeta\x12\x10\n\x08need_run\x18\n \x01(\x08\x12`\n\x15pencentage_value_meta\x18\x0b \x01(\x0b\x32\x41.com.webank.ai.fate.core.mlmodel.buffer.PercentageValueFilterMeta\x12R\n\riv_top_k_meta\x18\x0c \x01(\x0b\x32;.com.webank.ai.fate.core.mlmodel.buffer.IVTopKSelectionMeta\x12H\n\x0c\x66ilter_metas\x18\r \x03(\x0b\x32\x32.com.webank.ai.fate.core.mlmodel.buffer.FilterMeta\"\x8c\x01\n\nFilterMeta\x12\x0f\n\x07metrics\x18\x01 \x01(\t\x12\x13\n\x0b\x66ilter_type\x18\x02 \x01(\t\x12\x11\n\ttake_high\x18\x03 \x01(\x08\x12\x11\n\tthreshold\x18\x04 \x01(\x01\x12\x18\n\x10select_federated\x18\x05 \x01(\x08\x12\x18\n\x10\x66ilter_out_names\x18\x06 \x01(\t\"\x1e\n\x0fUniqueValueMeta\x12\x0b\n\x03\x65ps\x18\x01 \x01(\x01\"C\n\x14IVValueSelectionMeta\x12\x17\n\x0fvalue_threshold\x18\x01 \x01(\x01\x12\x12\n\nlocal_only\x18\x02 \x01(\x08\"M\n\x19IVPercentileSelectionMeta\x12\x1c\n\x14percentile_threshold\x18\x01 \x01(\x01\x12\x12\n\nlocal_only\x18\x02 \x01(\x08\"4\n\x13IVTopKSelectionMeta\x12\t\n\x01k\x18\x01 \x01(\x03\x12\x12\n\nlocal_only\x18\x02 \x01(\x08\"5\n\x1aVarianceOfCoeSelectionMeta\x12\x17\n\x0fvalue_threshold\x18\x01 \x01(\x01\"G\n\x18OutlierColsSelectionMeta\x12\x12\n\npercentile\x18\x01 \x01(\x01\x12\x17\n\x0fupper_threshold\x18\x02 \x01(\x01\".\n\x12ManuallyFilterMeta\x12\x18\n\x10\x66ilter_out_names\x18\x01 \x03(\t\".\n\x19PercentageValueFilterMeta\x12\x11\n\tupper_pct\x18\x01 \x01(\x01\x42\x1b\x42\x19\x46\x65\x61tureSelectionMetaProtob\x06proto3')



_FEATURESELECTIONMETA = DESCRIPTOR.message_types_by_name['FeatureSelectionMeta']
_FILTERMETA = DESCRIPTOR.message_types_by_name['FilterMeta']
_UNIQUEVALUEMETA = DESCRIPTOR.message_types_by_name['UniqueValueMeta']
_IVVALUESELECTIONMETA = DESCRIPTOR.message_types_by_name['IVValueSelectionMeta']
_IVPERCENTILESELECTIONMETA = DESCRIPTOR.message_types_by_name['IVPercentileSelectionMeta']
_IVTOPKSELECTIONMETA = DESCRIPTOR.message_types_by_name['IVTopKSelectionMeta']
_VARIANCEOFCOESELECTIONMETA = DESCRIPTOR.message_types_by_name['VarianceOfCoeSelectionMeta']
_OUTLIERCOLSSELECTIONMETA = DESCRIPTOR.message_types_by_name['OutlierColsSelectionMeta']
_MANUALLYFILTERMETA = DESCRIPTOR.message_types_by_name['ManuallyFilterMeta']
_PERCENTAGEVALUEFILTERMETA = DESCRIPTOR.message_types_by_name['PercentageValueFilterMeta']
FeatureSelectionMeta = _reflection.GeneratedProtocolMessageType('FeatureSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _FEATURESELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureSelectionMeta)
  })
_sym_db.RegisterMessage(FeatureSelectionMeta)

FilterMeta = _reflection.GeneratedProtocolMessageType('FilterMeta', (_message.Message,), {
  'DESCRIPTOR' : _FILTERMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FilterMeta)
  })
_sym_db.RegisterMessage(FilterMeta)

UniqueValueMeta = _reflection.GeneratedProtocolMessageType('UniqueValueMeta', (_message.Message,), {
  'DESCRIPTOR' : _UNIQUEVALUEMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.UniqueValueMeta)
  })
_sym_db.RegisterMessage(UniqueValueMeta)

IVValueSelectionMeta = _reflection.GeneratedProtocolMessageType('IVValueSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _IVVALUESELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.IVValueSelectionMeta)
  })
_sym_db.RegisterMessage(IVValueSelectionMeta)

IVPercentileSelectionMeta = _reflection.GeneratedProtocolMessageType('IVPercentileSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _IVPERCENTILESELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.IVPercentileSelectionMeta)
  })
_sym_db.RegisterMessage(IVPercentileSelectionMeta)

IVTopKSelectionMeta = _reflection.GeneratedProtocolMessageType('IVTopKSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _IVTOPKSELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.IVTopKSelectionMeta)
  })
_sym_db.RegisterMessage(IVTopKSelectionMeta)

VarianceOfCoeSelectionMeta = _reflection.GeneratedProtocolMessageType('VarianceOfCoeSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _VARIANCEOFCOESELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.VarianceOfCoeSelectionMeta)
  })
_sym_db.RegisterMessage(VarianceOfCoeSelectionMeta)

OutlierColsSelectionMeta = _reflection.GeneratedProtocolMessageType('OutlierColsSelectionMeta', (_message.Message,), {
  'DESCRIPTOR' : _OUTLIERCOLSSELECTIONMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.OutlierColsSelectionMeta)
  })
_sym_db.RegisterMessage(OutlierColsSelectionMeta)

ManuallyFilterMeta = _reflection.GeneratedProtocolMessageType('ManuallyFilterMeta', (_message.Message,), {
  'DESCRIPTOR' : _MANUALLYFILTERMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.ManuallyFilterMeta)
  })
_sym_db.RegisterMessage(ManuallyFilterMeta)

PercentageValueFilterMeta = _reflection.GeneratedProtocolMessageType('PercentageValueFilterMeta', (_message.Message,), {
  'DESCRIPTOR' : _PERCENTAGEVALUEFILTERMETA,
  '__module__' : 'feature_selection_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.PercentageValueFilterMeta)
  })
_sym_db.RegisterMessage(PercentageValueFilterMeta)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\031FeatureSelectionMetaProto'
  _FEATURESELECTIONMETA._serialized_start=73
  _FEATURESELECTIONMETA._serialized_end=931
  _FILTERMETA._serialized_start=934
  _FILTERMETA._serialized_end=1074
  _UNIQUEVALUEMETA._serialized_start=1076
  _UNIQUEVALUEMETA._serialized_end=1106
  _IVVALUESELECTIONMETA._serialized_start=1108
  _IVVALUESELECTIONMETA._serialized_end=1175
  _IVPERCENTILESELECTIONMETA._serialized_start=1177
  _IVPERCENTILESELECTIONMETA._serialized_end=1254
  _IVTOPKSELECTIONMETA._serialized_start=1256
  _IVTOPKSELECTIONMETA._serialized_end=1308
  _VARIANCEOFCOESELECTIONMETA._serialized_start=1310
  _VARIANCEOFCOESELECTIONMETA._serialized_end=1363
  _OUTLIERCOLSSELECTIONMETA._serialized_start=1365
  _OUTLIERCOLSSELECTIONMETA._serialized_end=1436
  _MANUALLYFILTERMETA._serialized_start=1438
  _MANUALLYFILTERMETA._serialized_end=1484
  _PERCENTAGEVALUEFILTERMETA._serialized_start=1486
  _PERCENTAGEVALUEFILTERMETA._serialized_end=1532
# @@protoc_insertion_point(module_scope)