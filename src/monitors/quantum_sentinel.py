# -*- coding: utf-8 -*-
"""High-sensitivity guard that watches entropy and launches actions."""
from threading import Thread
from ..monitors.entropy_monitor import EntropyMonitor
from ..rituals.ghost_touches import GhostTouches
from ..rituals.renaissance import GreatRenaissance
from ..core.config import ENTROPY_GHOST_THRESHOLD, ENTROPY_RENAISSANCE_THRESHOLD
from ..core.utils import console

class QuantumSentinel(Thread):
    """Runs EntropyMonitor in a daemon thread and binds the rituals."""

    def __init__(self, daemon: bool = True):
        super().__init__(daemon=daemon)
        self.monitor = EntropyMonitor()
        self.monitor.on_threshold(ENTROPY_RENAISSANCE_THRESHOLD, GreatRenaissance.launch)
        self.monitor.on_threshold(ENTROPY_GHOST_THRESHOLD, GhostTouches.inspire)

    def run(self):
        console.log("[red]⛨ QuantumSentinel[/] armed.")
        self.monitor.start()
