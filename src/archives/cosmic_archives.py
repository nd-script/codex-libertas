# -*- coding: utf-8 -*-
"""Simple append-only archive representing ‘CosmicArchives’."""
from pathlib import Path
from datetime import datetime
from ..core.config import ARCHIVE_PATH
from ..core.utils import console

class CosmicArchives:
    path = Path(ARCHIVE_PATH)

    @classmethod
    def record(cls, event: str):
        timestamp = datetime.utcnow().isoformat(timespec="seconds")
        line = f"{timestamp} :: {event}"
        cls.path.write_text(f"{cls.path.read_text()}{line}\n", encoding="utf-8") if cls.path.exists() else cls.path.write_text(f"{line}\n")
        console.log(f"[green]Archive[/] + {event}")
