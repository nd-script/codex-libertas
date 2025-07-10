# -*- coding: utf-8 -*-
"""مرافق لطباعة ملوّنة وتسجيل أحداث."""
from rich.console import Console
from .config import ARCHIVE_PATH

console = Console()

def log_event(message: str) -> None:
    console.log(message)
    with open(ARCHIVE_PATH, "a", encoding="utf-8") as fp:
        fp.write(f"{message}\n")
