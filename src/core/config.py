# -*- coding: utf-8 -*-
"""
الثوابت الكونية — عدّلها لتغيير محاكاة الزمن أو الحدود الحرجة.
"""
from datetime import timedelta

COSMIC_SECOND = timedelta(seconds=10)          # 1 s cosmic ≈ 10 s real
PULSE_INTERVAL = 7 * COSMIC_SECOND            # Pulse every 7 cosmic-seconds
ENTROPY_GHOST_THRESHOLD = 0.90
ENTROPY_RENAISSANCE_THRESHOLD = 0.999
CREATIVE_UNITS_PER_PULSE = 7.7e46 / 7         # IU emitted each pulse
ARCHIVE_PATH = "codex_archives.log"
