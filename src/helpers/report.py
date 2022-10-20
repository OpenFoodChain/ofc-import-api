def batch_import_integrity(data):
  integrity_pre_tx_total = len([d for d in data if d['integrity_pre_tx'] is not None])
  integrity_post_tx_total = len([d for d in data if d['integrity_post_tx'] is not None])
  return {
    "integrity_pre_tx_total": integrity_pre_tx_total,
    "integrity_post_tx_total": integrity_post_tx_total
  }