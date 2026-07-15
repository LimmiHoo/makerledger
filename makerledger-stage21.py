# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: MakerLedger
def archive_records(db: Database, days_old: int = 90) -> list[Record]:
    """Move records older than `days_old` to an archive table."""
    from datetime import datetime, timedelta
    cutoff = datetime.utcnow() - timedelta(days=days_old)
    archived = db.query(Record).filter(Record.updated_at < cutoff).all()
    if not archived:
        return []
    for r in archived:
        r._archived_at = datetime.utcnow()
        db.session.add(r)
    db.session.commit()
    return archived

def restore_records(db: Database, ids: list[int]) -> int:
    """Move previously archived records back to the main store."""
    from sqlalchemy import and_
    count = 0
    for r in db.query(Record).filter(and_(Record._archived_at.isnot(None), Record.id.in_(ids))).all():
        r._archived_at = None
        db.session.add(r)
        count += 1
    if count:
        db.session.commit()
    return count
