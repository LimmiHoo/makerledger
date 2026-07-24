# === Stage 58: Add bulk update behavior for selected records ===
# Project: MakerLedger
def bulk_update_records(self, updates):
    """Update multiple records by their identifiers in a single batch operation."""
    if not isinstance(updates, list) or len(updates) == 0:
        raise ValueError("bulk_update_records requires a non-empty list of record updates")

    for update_data in updates:
        rec_id = update_data.get("record_id", None)
        fields_to_set = {k: v for k, v in update_data.items() if k != "record_id"}
        if not rec_id or not fields_to_set:
            raise ValueError(f"Invalid update entry: missing record_id or no fields to set")

    updated_records = []
    for update_data in updates:
        rec_id = update_data["record_id"]
        new_fields = {k: v for k, v in update_data.items() if k != "record_id"}
        existing_record = self._find_record(rec_id)
        if not existing_record:
            raise KeyError(f"Record with id '{rec_id}' does not exist")

        merged = dict(existing_record)
        merged.update(new_fields)
        updated_records.append(merged)

    return updated_records
