# -*- coding: utf-8 -*-
"""Wrapper حول datetime/schedule لتبسيط حساب «الثواني الكونية»."""
from datetime import datetime, timedelta
from .config import COSMIC_SECOND

def sleep_cosmic(multiplier: int = 1) -> None:
    """Pause the thread for N cosmic-seconds (scaled)."""
    from time import sleep
    sleep(COSMIC_SECOND.total_seconds() * multiplier)

def now() -> datetime:
    """الوقت الحالي (مجرّد)."""
    return datetime.utcnow()
