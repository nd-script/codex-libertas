# -*- coding: utf-8 -*-
"""Measures artistic-entropy and triggers callbacks."""
import random, schedule
from typing import Callable
from ..core.config import PULSE_INTERVAL
from ..core.utils import console, log_event
from ..core.cosmic_time import sleep_cosmic

class EntropyMonitor:
    def __init__(self):
        self.callbacks: list[tuple[float, Callable[[float], None]]] = []

    def on_threshold(self, threshold: float, cb: Callable[[float], None]):
        """Register a callback fired when entropy ≥ threshold."""
        self.callbacks.append((threshold, cb))

    # ----- internal -----
    def _tick(self):
        entropy = random.random()
        console.log(f"[blue]Art-Entropy[/]: {entropy:.3%}")
        log_event(f"entropy={entropy}")
        for th, cb in sorted(self.callbacks, key=lambda x: -x[0]):
            if entropy >= th:
                cb(entropy)
                break

    def start(self):
        schedule.every(PULSE_INTERVAL.total_seconds()).seconds.do(self._tick)
        console.log("[blue]EntropyMonitor[/] active.")
        while True:
            schedule.run_pending()
            sleep_cosmic(0.5)
