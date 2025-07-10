# -*- coding: utf-8 -*-
"""Produces steady “creative radiation” every cosmic pulse."""
import schedule
from ..core.config import PULSE_INTERVAL, CREATIVE_UNITS_PER_PULSE
from ..core.utils import console, log_event
from ..core.cosmic_time import sleep_cosmic

class ResonanceEngine:
    def __init__(self, amplitude: float = CREATIVE_UNITS_PER_PULSE):
        self.amplitude = amplitude

    def _emit(self):
        console.print(f"[magenta]⟡ Resonance pulse[/] ⇒ {self.amplitude:.2e} IU")
        # في النسخة المتوسعة يمكن إرسال الطاقة إلى وحدات أخرى
        log_event(f"Resonance pulse emitted | {self.amplitude}")

    def start(self):
        schedule.every(PULSE_INTERVAL.total_seconds()).seconds.do(self._emit)
        console.log("[magenta]ResonanceEngine[/] online.")
        while True:
            schedule.run_pending()
            sleep_cosmic(0.5)  # نصف ثانية واقعية بين التكرارات
