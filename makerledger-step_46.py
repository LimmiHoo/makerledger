# === Stage 46: Add a schema version field and migration helper ===
# Project: MakerLedger
"""Schema versioning and migration helper for MakerLedger."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Callable

LOG = logging.getLogger(__name__)


class SchemaMigrator:
    """Track schema versions in JSON files and apply incremental upgrades.

    Each file stores a top-level ``"schema_version": int`` key.  The migrator
    records the current version, compares it against any registered migrations,
    applies them in order, and writes back the updated payload to disk.

    Usage::

        Migrator(Path("project.json")).register(version=1, fn=lambda d: d) \
            .register(version=2, fn=lambda d: {**d, "notes": ""}) \
            .migrate()
    """

    def __init__(self, path: Path):
        self.path = path
        self._version: int | None = None
        self._migrations: list[tuple[int, Callable]] = []
        self._payload: dict[str, Any] = {}

    @property
    def version(self) -> int | None:
        return self._version

    @staticmethod
    def load(path: Path) -> SchemaMigrator:
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            payload = {"schema_version": 0}
        else:
            with path.open("r") as fh:
                payload = json.load(fh)
        migrator = SchemaMigrator(path)
        migrator._version = int(payload.get("schema_version", 0))
        migrator._payload = {k: v for k, v in payload.items() if k != "schema_version"}
        return migrator

    def register(self, version: int, fn: Callable[[dict], dict]) -> "SchemaMigrator":
        self._migrations.append((version, fn))
        return self

    def migrate(self) -> SchemaMigrator:
        for target_ver, fn in sorted(self._migrations):
            if self._version < target_ver:
                LOG.info("Applying migration to v%d", target_ver)
                self._payload = fn(self._payload)
                self._version = target_ver
        return self

    def save(self) -> None:
        data = {"schema_version": self._version, **self._payload}
        with self.path.open("w") as fh:
            json.dump(data, fh, indent=2, sort_keys=True)
